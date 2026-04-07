import pandas as pd
from datetime import datetime, timedelta

caminho = r"C:\Cotacao_Dolar\Bacen.xlsx"
moedas = ["USD", "EUR", "CHF", "INR", "CNH", "CNY"]

dfs = {}

# --- 1. LER EXCEL ---
print("Lendo arquivo Excel...")
for i, nome in enumerate(moedas):
    # Lê cada aba pelo índice (0, 1, 2...) para garantir que pegue a ordem certa
    dfs[nome] = pd.read_excel(caminho, sheet_name=i, usecols=["data", "valor"])
    dfs[nome]["Datetime"] = pd.to_datetime(dfs[nome]["data"], dayfirst=True)
    
    dfs[nome]["data"] = dfs[nome]["Datetime"].dt.strftime("%d/%m/%Y")

    maior_data = dfs[nome]["Datetime"].max()
    # A próxima busca começa no dia seguinte à última data encontrada
    dfs[f"{nome}_data"] = maior_data + timedelta(days=1)

    print(f"[{nome}] Última data: {maior_data.strftime('%d/%m/%Y')} | Próxima: {dfs[f'{nome}_data'].strftime('%d/%m/%Y')}")

print("-" * 30)

# --- 2. BUSCAR COTAÇÕES E ATUALIZAR ---
for nome in moedas:
    data_atual = dfs[f"{nome}_data"]
    hoje = datetime.today()

    while data_atual <= hoje:
        # FORMATO CRUCIAL: O link do Bacen exige AAAAMMDD
        data_url = data_atual.strftime("%Y%m%d")
        # FORMATO PRINT: Só para você ler no console
        data_exibicao = data_atual.strftime("%d/%m/%Y")
        
        url = f"https://www4.bcb.gov.br/Download/fechamento/{data_url}.csv"

        try:
            # Lendo o CSV diretamente da URL
            df_temp = pd.read_csv(
                url,
                sep=";",
                header=None,
                names=['data_ref', "cod_moeda", "tipo", "sigla", "taxa_compra", "cotação", "par_compra", "par_venda"],
                decimal=","
            )

            # Filtra pela sigla da moeda (USD, EUR, etc)
            linha = df_temp[df_temp["sigla"] == nome]

            if linha.empty:
                raise Exception("Moeda não encontrada no arquivo")

            valor_venda = linha["cotação"].iloc[0]

            # Cria a nova linha para anexar
            nova_linha = pd.DataFrame({
                "data": [data_atual.strftime("%d/%m/%Y")], 
                "valor": [valor_venda],
                "Datetime": [data_atual] 
            })

            # Adiciona ao DataFrame daquela moeda
            dfs[nome] = pd.concat([dfs[nome], nova_linha], ignore_index=True)
            print(f"{nome} OK {data_exibicao} -> {valor_venda}")

        except Exception:
            # Se cair aqui é porque é fim de semana, feriado ou o link ainda não subiu
            print(f"{nome} sem dados em {data_exibicao} (Fim de semana/Feriado)")

        # SEMPRE avança a data, dando erro ou não
        data_atual += timedelta(days=1)

# --- 3. LIMPEZA E SALVAMENTO ---
print("-" * 30)
print("Salvando no Excel...")

with pd.ExcelWriter(caminho, engine="openpyxl", mode="w") as writer:
    for nome in moedas:
        # Remove a coluna auxiliar antes de salvar
        df_final = dfs[nome].drop(columns=["Datetime"], errors="ignore")
        # Garante que não salvamos duplicados por erro de execução
        df_final = df_final.drop_duplicates(subset=['data'], keep='last')
        
        df_final.to_excel(writer, sheet_name=nome, index=False)

print("Tudo pronto! Planilha atualizada.")