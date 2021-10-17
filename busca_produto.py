import pandas as pd
import os
from carrega_produtos import carregar_produtos
from os.path import exists

file_name_supermarket = "precos_supermarket.csv"
file_name_prix = "precos_prix.csv"
file_name_mundial = "precos_mundial.csv"

if not (
        exists(file_name_supermarket)
        and exists(file_name_prix)
        and exists(file_name_mundial)
    ):
    carregar_produtos()

df_supermarket = pd.read_csv(file_name_supermarket)
df_supermarket["mercado"] = "SuperMarket"

df_prix = pd.read_csv(file_name_prix)
df_prix["mercado"] = "Prix"

df_mundial = pd.read_csv(file_name_mundial)
df_mundial["mercado"] = "Mundial"


df_mercados = df_supermarket.append(df_prix).append(df_mundial)

while True:
    search = input("Digite a sua busca ou [ENTER] para sair: ")
    if not search:
        break
    print(df_mercados[df_mercados.nome.str.contains(search, case=False)])

