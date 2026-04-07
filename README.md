Dashboard criado em Power BI com o objetivo de controlar máquinas com custo de manutenção muito alto em relação ao custo de renovação das mesmas, estipulado em 5%, projeto feito utilizando Python, SQL, e Power BI

<img width="1246" height="568" alt="Explicação" src="https://github.com/user-attachments/assets/627170d9-8612-4a23-a25b-60c87b6df385" />

Extração com Python do Dólar

Esta parte foi necessária para trazer o valor presente das máquinas, para que pudessemos trabalhar com um valor absoluto considerando a inflação do periodo, o que era importante para máquinas muito antigas. Aproveitando o trabalho já feito para extrair o dólar, à pedido do setor financeiro, posteriormente foram adicionadas outras moedas para auxiliá-los em suas atividades.

Requisições de Compra SAP

Utilizando um script simples foi possível automatizar a coleta de dados das requisições de compra realizadas pela manutenção vindas da operação ME5A.  Após salvar os dados em uma planilha excel, o arquivo é carregado 1 vez no mês(ainda não automatizei esta etapa) para o SQL SERVER, organizei as tabelas para formar o que é conhecido como Star Schema para armazenar os dados de custos de manutenção dos equipamentos conforme a imagem ao lado.

<img width="360" height="720" alt="Requisições SAP" src="https://github.com/user-attachments/assets/21ee0e37-8b28-4937-b695-02f19462a2b8" />

Dashboard Power BI

O indicador final nos permitiu gerar insights importantes para visualizarmos de forma clara quais máquinas valiam a pena o investimento de serem trocadas ou passar por Retrofit, além de permitir visualizar os principais gastos de cada máquina e os principais fornecedores contratados.

O principal insight foi associar o custo de manutenção ao tempo de uso do equipamento, comprovando a hipótese que o custo de manutenção da máquina aumenta gradualmente conforme os anos, com base nisso, os ativos da fábrica foram distribuidos em 4 quadrantes para tomada de ação.

- Ano de uso < 10 anos e custo de manutenção percentual < 5% (estes ativos são os ideais)  
- Ano de uso < 10 anos e custo de manutenção > 5% (ativos novos que não deveriam ter custo alto; ações como retrofit ou troca de fornecedores podem ser tomadas)  
- Ano de uso > 10 anos e custo de manutenção < 5% (analisar tendência antes de decidir pela troca)  
- Ano de uso > 10 anos e custo de manutenção > 5% (a troca por um equipamento mais novo geralmente é a melhor solução)
  


<img width="1440" height="1120" alt="Descrição" src="https://github.com/user-attachments/assets/61251bad-a834-4c6c-9a81-bef74f96b0e3" />


