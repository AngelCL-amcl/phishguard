import pandas as pd

espanol = pd.read_csv("datos/spaphish.csv", sep=",")
print("ESPAÑOL:", espanol.shape)
print(espanol.columns.tolist())
print(espanol["Label"].value_counts())
print(espanol[["subject", "Label"]].head(5))

ingles = pd.read_csv("datos/sms_ingles.txt", sep="\t", header=None, names=["etiqueta", "texto"])
print("INGLÉS:", ingles.shape)
print(ingles.head(5))
print(ingles["etiqueta"].value_counts())