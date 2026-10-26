from datos import cargar_todo

textos, etiquetas = cargar_todo()
print("Total de ejemplos:", len(textos))
print("Phishing/spam:", etiquetas.count(1))
print("Normales:", etiquetas.count(0))