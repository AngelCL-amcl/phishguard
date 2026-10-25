# PhishGuard

Detector de phishing para mensajes y links. Lo creé para ayudar a los mayores de mi familia a no caer en estafas.

## Qué detecta
- Marcas usadas como subdominio para engañar (`paypal.com.verificar-cuenta.xyz`)
- Typosquatting: letras cambiadas por números o letras parecidas (`paypa1`, `m1crosoft`, `arnazon`)
- Links escritos en mayúsculas para evadir filtros (`NETFLIX.com.pago-pendiente.top`)
- Dominios de otros países (`amazon.com.mx`, `co.uk`)
- Palabras sospechosas en el texto (urgencia, contraseñas, premios)
- Mensajes de phishing aunque no tengan links ("envíenos su clave")

## Cómo funciona
El detector revisa cada mensaje en 3 capas:

1. **Reglas de links:** encuentra los links del mensaje, saca el dominio real y revisa si imita a una marca conocida. Usa una lista de dominios oficiales confiables para evitar falsas alarmas.
2. **Palabras sospechosas:** cuenta cuántas palabras típicas de estafas aparecen en el mensaje.
3. **Inteligencia artificial:** un modelo Naive Bayes (scikit-learn) entrenado con ejemplos de mensajes de phishing y normales. Calcula la probabilidad de que el mensaje sea phishing. En una prueba con mensajes que nunca vio, acertó el 80%.

Con esas 3 capas da uno de estos resultados:
- **PELIGROSO**: un link falso o la IA da 70% o más
- **SOSPECHOSO**: la IA da 40% o más, o hay varias palabras sospechosas
- **Parece seguro**: ninguna de las anteriores

## Cómo usarlo

1. Clonar el repositorio:
```
   git clone https://github.com/AngelCL-amcl/phishguard.git
   cd phishguard
```
2. Crear y activar el entorno virtual:
```
   python3 -m venv venv
   source venv/bin/activate
```
3. Instalar las dependencias:
```
   pip install -r requirements.txt
```
4. Ejecutar el detector:
```
   python detector.py
```

### Ejemplo

```
Pega el mensaje a revisar: urgente: tu paquete esta retenido, paga aqui http://usps.com-entrega.info
Revisando: http://usps.com-entrega.info
Dominio real: com-entrega.info
ALERTA: este link se hace pasar por usps
Palabras sospechosas encontradas: 1
Probabilidad de phishing (IA): 98 %
RESULTADO: PELIGROSO
```
## Lo que aprendí
Empecé este proyecto sin saber programar. Lo que más me gustó fue ver lo útil que puede ser la IA cuando la usas para ayudar a personas.

- Python desde cero: variables, listas, `if`, `for`, funciones
- Cómo funcionan los ataques de phishing y typosquatting
- Machine learning con scikit-learn: entrenar un modelo y evaluarlo con datos separados
- La diferencia entre falsos positivos y falsos negativos, y por qué en seguridad importa
- Que una IA es tan buena como sus datos
- Git y GitHub para guardar versiones de mi código

## Próximos pasos
- Agregar más datos. 
- Extensión
- API 
- Coneccion con telegram

## Limitaciones
- La IA se entrenó con solo 40 ejemplos, por eso todavía se equivoca con mensajes normales que usan palabras como "código" o "datos"
- Solo funciona en la terminal por ahora