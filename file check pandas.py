import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)     # Visualizza tutto il database

use_cols = ["Directory", "Nome_file", "Peso", "Size_byte", "Last_mod_num"]    # Colonne da importare

name1 = input("1) Inserire nome file: ")
name2 = input("2) Inserire nome file: ")
nome_excel = input("Inserire nome excel: ")

df1 = pd.read_csv("{}.csv".format(name1), usecols=use_cols)
df2 = pd.read_csv("{}.csv".format(name2), usecols=use_cols)

print("df1 len: ", len(df1))
print("df2 len: ", len(df2))

missing1 = df2[~df2.Nome_file.isin(df1.Nome_file)]      # Controlla se i nomi di 1 sono in 2
missing2 = df1[~df1.Nome_file.isin(df2.Nome_file)]      # Controlla se i nomi di 2 sono in 1


if len(missing1) == 0:                                  # Se non ci sono differenze
    print("\nTutti i file di 2 sono in 1")
else:                                                   # Stampa le differenze
    print("\nFile mancanti in 1:\n", missing2)

if len(missing2) == 0:
    print("\nTutti i file di 1 sono in 2")
else:
    print("\nFile mancanti in 2:\n", missing1)

presenti1 = df2[df2.Nome_file.isin(df1.Nome_file)]      # File df1 presenti in df2
print("\nFile presenti in 2:\n", presenti1)
print("\nFile mancanti in 2:\n", missing2)
print(len(presenti1), len(df2))
print(missing2.index)
df1.drop(missing2.index, inplace=True)      # Eliminiamo i file mancanti da df1
df1 = df1.reset_index(drop=True)            # Resettiamo gli indici
print("Banane:\n", df1)

# Definiamo un nuovo dataframe

colonne = ["Directory", "Nome", "Dimensioni", "last1", "last2", "Recente"]
df3 = pd.DataFrame(columns=colonne)
df3["Directory"] = df1["Directory"]
df3["Nome"] = df1["Nome_file"]
df3["Dimensioni"] = df1["Peso"]
df3["last1"] = df1["Last_mod_num"]          # Importiamo le ultime modifiche di df1
df3["last2"] = df2["Last_mod_num"]          # Importiamo le ultime modifiche di df2

df3["Recente"] = np.where(df3["last1"] > df3["last2"], "Sì", " ")  # Controlliamo il file più recente

del df3["last2"]    # Eliminiamo le colonne inutili
del df3["last1"]

df3.to_excel(r"D:\Python\Random shit\USB Check\{}.xlsx".format(nome_excel), index=False, header=True)
print(df3)
