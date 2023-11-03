import pandas as pd
import os

path = "bases"

arquivos = os.listdir(path)

tabella_consolidada = pd.DataFrame()

for nome_arquivo in arquivos:
    tabela_vendas = pd.read_csv(os.path.join(path, nome_arquivo))
    tabela_vendas["Data de Venda"] = pd.to_datetime("01/01/1900") + pd.to_timedelta(tabela_vendas["Data de Venda"], 
                                                                                    unit="day")
    tabella_consolidada = pd.concat([tabella_consolidada, tabela_vendas])
    

tabella_consolidada = tabella_consolidada.sort_values(by="Data de Venda")
tabella_consolidada = tabella_consolidada.reset_index(drop = True)

tabella_consolidada.to_excel("Vendas.xlsx", index=False)
#print(tabella_consolidada)