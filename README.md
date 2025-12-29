# Dashboard para Análise de Atletas de Jiu Jitsu <br> em Power BI com Web Scraping em Python

#### Douglas Augusto da Silva
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dougaugsilva/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DougAugSilva)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:douglasaugustosilva323@gmail.com)

Neste projeto, foi utilizado o web scraping tradicional do python (sem o uso de web drivers), com a biblioteca BeautifulSoup para a extração de informações de atletas de Jiu Jitsu do site da Federação Internacional de Jiu-Jitsu Brasileiro (IBJJF).
Depois, foi utilizado o Power BI para a criação de um dashboard para análise das informações dos atletas, podendo ser feitas comparações entre as academias, diferenças do desempenho de cada gênero em cada categoria, e os atletas de maior destaque de cada gênero em cada categoria.

## Colunas Utilizadas dos Dados Coletados

- `Academy:` Academia em que o atleta estava afiliado quando competiu.
- `Details:` Link com mais detalhes sobre o atleta
- `Division:` Divisão em que atleta se enquadra com base no peso
- `Gender:` Gênero do atleta (masculino e feminino)
- `Kimono:` Se o atleta usa ou não kimono, neste caso, todos os atletas participam da categoria com Kimono.
- `Name:` Nome do atleta.
- `Photo:` Foto deo atletas (dos que possuem foto).
- `Points:` Pontuação do atleta.
- `Posição:` Posição do atleta no ranking da sua categoria e do seu gênero.
  
**OBS:** Foi realizado um tratamento dos dados no Power Query, e para o uso somente dos dados necessários no dashboard.


![Tela 1 do Dashboard](https://github.com/DougAugSilva/dashboard_analise_atletas_jiujitsu/blob/main/images/fig_tela_1.jpg)
> Tela 1 do Dashboard aberto no Power BI: Comparação entre as diferentes academias.

![Tela 2 do Dashboard](https://github.com/DougAugSilva/dashboard_analise_atletas_jiujitsu/blob/main/images/fig_tela_2.jpg)
> Tela 2 do Dashboard aberto no Power BI: Análise da diferença de desempenho entre os gêneros em diferentes categorias.

![Tela 3 do Dashboard](https://github.com/DougAugSilva/dashboard_analise_atletas_jiujitsu/blob/main/images/fig_tela_3.jpg)
> Tela 3 do Dashboard aberto no Power BI: Comparação entre cada atleta em sua respectiva categoria, separados por gênero.

## Conceitos utilizados

### Coleta dos Dados (Python):

- Controle de versão e criação de ambientes virtuais em Python.
- Web scraping com BeBeautifulSoup.
- Análise de tabelas HTML para web scraping.

### Criação do Dashboard (Power BI):

- Tratamento de dados com Power Query.
- Fórmulas DAX para criação de medidas.
- Criação de medidas e KPI's significativas.

## Funcionamento

Para poder praticar o web scraping em Python e a criação de dashboards em Power BI, resolvi unir tudo em um só projeto, desta vez com BeautifulSoup no lugar de Selenium, dado que os dados das tabelas estão disponiveis diretamente no HTML do site, e não em uma API. Para poder testar este projeto, você pode baixar os dados de amostra e o arquivo .pbix que deixei disponível, nele está o dashboard e basta abrí-lo no Power BI e indicar a pasta de origem como aquela que contém os dados que baixou deste repositório. Porém, é possível testar este dashboard com os dados de ações atualizados segundo o dia em que está lendo isso, basta baixar o script Python e rodar segundo a sua versão (eu utilizei para este projeto a 3.14.2, mas ele deve funcionar para qualquer versão que o BeautifulSoup esteja devidamente atualizado), feito isso ajuste as versões das bibliotecas segundo o arquivo `requirements.txt` que também deixei disponível, e executar o código.

## Análise e Insights

- Podemos perceber que no geral há uma boa distribuição da soma de pontos de cada atleta entre as academias, não havendo uma única academia com uma grande fatia dos pontos, apesar de a academia AOJ ter uma pontuação significativa em cada categoria, e possuindo mais atletas entre os top 3 de do ranking de cdata categoria, em ambos os gêneros (masculino e feminino).

- O gênero masculino tem uma soma de pontos maior que o feminino em praticamente todas as academias, além de possuir uma soma de pontos maior no contexto geral em cada categorias ( a comparação só não é feita no caso da categoria “ultra pesados”, dado que esta só existe para o gênero masculino).

- Já na análise do ranking individual dos atletas de maior pontuação em cada categoria, temos alguns casos onde atletas femininas no topo do ranking possuem pontuação maiores que os atletas masculinos no topo do ranking, como é o caso da categoria de peso “leve”, onde a atleta Janaína maia Possui uma pontuação maior que atleta  Matheus Gabriel, qm que, no momento desta análise, ambos são top 1 dessa categoria.


