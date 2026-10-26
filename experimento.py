from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score
from datos import cargar_todo

textos, etiquetas = cargar_todo()
textos_estudio, textos_examen, etiquetas_estudio, etiquetas_examen = train_test_split(
    textos, etiquetas, test_size=0.25, random_state=7, stratify=etiquetas
)


def probar(ngramas):
    vectorizador = CountVectorizer(ngram_range=ngramas)
    X_estudio = vectorizador.fit_transform(textos_estudio)
    modelo = MultinomialNB()
    modelo.fit(X_estudio, etiquetas_estudio)

    respuestas = modelo.predict(vectorizador.transform(textos_examen))
    prueba = modelo.predict_proba(vectorizador.transform(
        ["tu codigo de verificacion de google es 482913. no lo compartas con nadie"]
    ))

    print("Configuración:", ngramas)
    print("  Palabras/pares aprendidos:", len(vectorizador.vocabulary_))
    print("  Calificación:", round(accuracy_score(etiquetas_examen, respuestas) * 100, 1), "%")
    print("  Recall phishing:", round(recall_score(etiquetas_examen, respuestas) * 100, 1), "%")
    print("  Precisión phishing:", round(precision_score(etiquetas_examen, respuestas) * 100, 1), "%")
    print("  Mensaje de Google:", round(prueba[0][1] * 100), "% phishing")
    print()


configuraciones = [(1, 1), (1, 2), (1, 3)]
for configuracion in configuraciones:
    probar(configuracion)