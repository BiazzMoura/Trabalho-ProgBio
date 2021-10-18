#Foi importado o modulo pandas para a manipulação e analise dos dados dos arquivos criados
import pandas as pd

import os
# Foi importado do arquivo de "Crawler" a função carrega_produtos
from carrega_produtos import carregar_produtos
from os.path import exists

file_name_supermarket = "precos_supermarket.csv"
file_name_prix = "precos_prix.csv"
file_name_mundial = "precos_mundial.csv"
#utilizando um if junto com o exists do pacote os.path caso não exista nenhum desses arquivos, cria-los( para evitar problemas na duplicidade)
if not (
        exists(file_name_supermarket)
        and exists(file_name_prix)
        and exists(file_name_mundial)
    ):
    carregar_produtos()
#Criando um data frame para cada mercado e adicionando uma coluna com os nomes dos respectivos mercados para uma facil identificação
df_supermarket = pd.read_csv(file_name_supermarket)
df_supermarket["mercado"] = "SuperMarket"

df_prix = pd.read_csv(file_name_prix)
df_prix["mercado"] = "Prix"

df_mundial = pd.read_csv(file_name_mundial)
df_mundial["mercado"] = "Mundial"

#Criando um data frame geral de todos os mercados para uma melhor listagem dos produtos procurados
df_mercados = df_supermarket.append(df_prix).append(df_mundial)
#Criando um input para a busca com a palavra chave desejada e um output com todos os produtos e preços nos determinados mercados onde foram encontrados
while True:
    search = input("Digite a sua busca ou [ENTER] para sair: ")
    if not search:
        break
    print(df_mercados[df_mercados.nome.str.contains(search, case=False)])

