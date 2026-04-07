Dashboard criado em Power BI com o objetivo de controlar máquinas com custo de manutenção muito alto em relação ao custo de renovação das mesmas, estipulado em 5%, projeto feito utilizando Python, SQL, e Power BI

<img width="720" height="360" alt="Explicação" src="https://github.com/user-attachments/assets/7139fb27-0234-4671-969b-83435c6190ea" />

Extração com Python do Dólar

Esta parte foi necessária para trazer o valor presente das máquinas, para que pudessemos trabalhar com um valor absoluto considerando a inflação do periodo, o que era importante para máquinas muito antigas. Aproveitando o trabalho já feito para extrair o dólar, à pedido do setor financeiro, posteriormente foram adicionadas outras moedas para auxiliá-los em suas atividades.

Requisições de Compra SAP

Utilizando um script simples foi possível automatizar a coleta de dados das requisições de compra realizadas pela manutenção vindas da operação ME5A.  Após salvar os dados em uma planilha excel, o arquivo é carregado 1 vez no mês(ainda não automatizei esta etapa) para o SQL SERVER, organizei as tabelas para formar o que é conhecido como Star Schema para armazenar os dados de custos de manutenção dos equipamentos conforme a imagem ao lado.

<img width="360" height="720" alt="Requisições SAP" src="https://github.com/user-attachments/assets/21ee0e37-8b28-4937-b695-02f19462a2b8" />

Dashboard Power BI

O indicador final nos permitiu gerar insights importantes para visualizarmos de fomra clara quais máquinas valiam a pena o investimento de serem trocadas ou passar por Retrofit, além de permitir visualizar os principais gastos de cada máquina e os principais fornecedores contratados.


<img width="1440" height="1120" alt="Descrição" src="https://github.com/user-attachments/assets/61251bad-a834-4c6c-9a81-bef74f96b0e3" />


