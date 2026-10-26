from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from datos import cargar_todo
...
textos, etiquetas = cargar_todo()

textos_estudio, textos_examen, etiquetas_estudio, etiquetas_examen = train_test_split(
    textos, etiquetas, test_size=0.25, random_state=42, stratify=etiquetas
)

print("Mensajes para estudiar:", len(textos_estudio))
print("Mensajes para el examen:", len(textos_examen))

vectorizador = CountVectorizer()
X_estudio = vectorizador.fit_transform(textos_estudio)
modelo = MultinomialNB()
modelo.fit(X_estudio, etiquetas_estudio)

X_examen = vectorizador.transform(textos_examen)
respuestas_ia = modelo.predict(X_examen)

calificacion = accuracy_score(etiquetas_examen, respuestas_ia)
print("Calificación de la IA:", round(calificacion * 100), "%")

for mensaje, correcta, ia in zip(textos_examen, etiquetas_examen, respuestas_ia):
    print(mensaje, "| correcta:", correcta, "| IA:", ia)
    if correcta != ia:
        print("   ❌ FALLÓ")
print(classification_report(etiquetas_examen, respuestas_ia, target_names=["normal", "phishing"]))