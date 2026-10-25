from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from datos import phishing, normales
print("Ejemplos de phishing:", len(phishing))
print("Ejemplos normales:", len(normales))

textos = phishing + normales
etiquetas = [1] * len(phishing) + [0] * len(normales)

vectorizador = CountVectorizer()
X = vectorizador.fit_transform(textos)

modelo = MultinomialNB()
modelo.fit(X, etiquetas)

while True: 
    mensaje = input("Mensaje a revisar: ").lower()
    if mensaje == "salir":
        break    
    prediccion = modelo.predict(vectorizador.transform([mensaje]))
    probabilidad = modelo.predict_proba(vectorizador.transform([mensaje]))
    print("Probabilidad de phishing:", round(probabilidad[0][1] * 100), "%")
    if prediccion[0] == 1:
        print("IA dice: PHISHING")
    else: 
        print("IA dice: normal")