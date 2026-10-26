# PhishGuard

Detector de phishing para mensajes y links. Lo creé para ayudar a los mayores de mi familia a no caer en estafas.

## Qué detecta
- Marcas usadas como subdominio para engañar (`paypal.com.verificar-cuenta.xyz`)
- Typosquatting: letras cambiadas por números o letras parecidas (`paypa1`, `m1crosoft`, `arnazon`)
- Links escritos en mayúsculas para evadir filtros (`NETFLIX.com.pago-pendiente.top`)
- Dominios de otros países (`amazon.com.mx`, `co.uk`)
- Palabras sospechosas en el texto (urgencia, contraseñas, premios)
- Mensajes de phishing aunque no tengan links ("envíenos su clave")
- Mensajes en español e inglés
- Los links peligrosos se muestran desactivados (`hxxp://ejemplo[.]com`) para que no se puedan abrir por accidente

## Cómo funciona
El detector revisa cada mensaje en 3 capas:

1. **Reglas de links:** encuentra los links del mensaje, saca el dominio real y revisa si imita a una marca conocida. Usa una lista de dominios oficiales confiables para evitar falsas alarmas.
2. **Palabras sospechosas:** cuenta cuántas palabras típicas de estafas aparecen en el mensaje.
3. **Inteligencia artificial:** un modelo Naive Bayes (scikit-learn) que lee palabras y pares de palabras (bigramas), entrenado con 7,015 mensajes en español e inglés. En pruebas con mensajes que nunca vio, atrapa entre 90% y 94% del phishing, con una precisión de ~97%.

Con esas 3 capas da uno de estos resultados, y explica por qué:
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

4. Descargar los datasets (ver sección **Datos**) y guardarlos así:
   - `datos/spaphish.csv`
   - `datos/sms_ingles.txt`

5. Ejecutar el detector:
```
python detector.py
```

### Ejemplo
```
Pega el mensaje a revisar: urgente: tu paquete esta retenido, paga aqui http://usps.com-entrega.info
RESULTADO: PELIGROSO
- Link falso: hxxp://usps[.]com-entrega[.]info
- La IA da 99% de probabilidad de phishing
- Palabras sospechosas encontradas: 1
```

### Bot de Telegram
1. Crea un bot con @BotFather y copia el token
2. Crea un archivo `.env` con: `TELEGRAM_TOKEN=tu_token`
3. Ejecuta: `python bot.py`

Luego reenvíale al bot cualquier mensaje sospechoso y te responde con el resultado y las razones.

## Lo que aprendí
Empecé este proyecto sin saber programar. Lo que más me gustó fue ver lo útil que puede ser la IA cuando la usas para ayudar a personas.

- Python desde cero: variables, listas, `if`, `for`, funciones
- Cómo funcionan los ataques de phishing y typosquatting
- Machine learning con scikit-learn: entrenar un modelo y evaluarlo con datos separados
- La diferencia entre falsos positivos y falsos negativos, y por qué en seguridad importa
- Que una IA es tan buena como sus datos
- Limpiar y combinar datasets reales con pandas
- Hacer experimentos: comparé palabras sueltas vs. bigramas y repetí la prueba con otro examen, y descubrí que una mejora que parecía real era suerte
- Manejar secretos (tokens) sin subirlos a GitHub
- Git y GitHub para guardar versiones de mi código

## Limitaciones
- El dataset en inglés es de 2011, así que conoce poco el phishing moderno (por ejemplo, paquetes retenidos)
- La mayoría de los datos en español son correos, no SMS
- El bot solo responde mientras la computadora donde corre esté encendida

## Próximos pasos
- Correr el bot 24/7 en un home lab
- Extensión de navegador
- API
- Validación cruzada para medir mejor la IA

## Datos
- [SpaPhish](https://data.mendeley.com/datasets/hz2d6gz7pc): 1,395 correos en español (CC BY 4.0)
- [SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/): 5,572 SMS en inglés (UCI)
