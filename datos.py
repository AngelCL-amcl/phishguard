phishing = [
    "su cuenta fue bloqueada, envienos su clave para desbloquearla",
    "usps: su paquete esta retenido por falta de pago, pague $1.99 hoy o sera devuelto",
    "felicidades! ganaste un iphone 16, responde con tus datos para reclamar tu premio",
    "hola mama, cambie de numero, este es el nuevo. me puedes transferir 300 urgente?",
    "netflix: no pudimos procesar tu pago, actualiza tu tarjeta en 24 horas o se cancelara tu cuenta",
    "alerta de seguridad: detectamos un acceso inusual, confirma tu contraseña de inmediato",
    "te enviamos un codigo de verificacion por error, por favor reenvialo a este numero",
    "el irs le debe un reembolso de $850, ingrese su numero de seguro social para recibirlo",
    "su tarjeta ha sido suspendida temporalmente, llame al 800-555-0199 para reactivarla",
    "oferta de trabajo desde casa, gana $500 diarios sin experiencia, envia tus datos bancarios","estimado cliente, su cuenta sera cerrada hoy si no confirma su identidad",
    "has sido seleccionado para recibir un bono del gobierno, responde si para cobrarlo",
    "amazon: hubo un problema con tu pedido, inicia sesion para evitar la cancelacion",
    "tu apple id fue usado en otro dispositivo, confirma tus datos ahora",
    "dhl: tu envio no pudo ser entregado, paga el costo de reenvio aqui",
    "hola soy tu jefe, necesito que compres tarjetas de regalo y me mandes los codigos",
    "ultimo aviso: tiene una multa de transito pendiente, pague hoy para evitar recargos",
    "su prestamo fue aprobado, solo envie el deposito de garantia para liberarlo",
    "whatsapp caducara tu cuenta, reenvia el codigo de 6 digitos para mantenerla",
    "detectamos un virus en tu telefono, llama a soporte tecnico de inmediato",
]

normales = [
    "hola, nos vemos mañana a las 5 para estudiar",
    "gracias por tu compra! envio gratis en tu proximo pedido con el codigo ahorro10",
    "tu pedido de amazon fue entregado en la puerta principal",
    "recordatorio: tu cita con el dentista es el martes a las 10 am",
    "chase: se realizo un cargo de $45.20 en tu tarjeta terminada en 4821. si no fuiste tu, revisa la app",
    "oye, ya subieron las calificaciones del examen a canvas",
    "tu codigo de verificacion de google es 482913. no lo compartas con nadie",
    "mama dice que vengas a cenar el domingo",
    "netflix: tu plan se renovo correctamente, gracias por seguir con nosotros",
    "la reunion del club se movio al jueves, avisale a los demas", "te mando los datos del proyecto y mi numero nuevo",
    "llamame cuando salgas de clase, mi numero es el mismo",
    "ya pague mi parte de la renta, revisa tu cuenta",
    "mi tarjeta del bus se perdio, me prestas la tuya mañana?",
    "el profe pidio los datos de todos para el viaje de campo",
    "olvide la clave del wifi, me la pasas?",
    "tu pago de la matricula fue recibido, gracias",
    "te llamo en 10 minutos, estoy manejando",
    "puedes verificar si el examen es el lunes o el martes?",
    "mi mama cambio de numero, te lo paso por interno", "hola",
    "hola como estas",
    "hola que tal tu dia",
    "buenos dias, ya desayunaste?",
    "hola, ya llegue a la casa",
    "hola hijo, llamame cuando puedas",
    "buenas noches, que descanses",
    "hola, gracias por la ayuda de ayer",
]

import pandas as pd


def cargar_todo():
    # 1. Tus ejemplos
    textos = phishing + normales
    etiquetas = [1] * len(phishing) + [0] * len(normales)

    # 2. Correos en español
    espanol = pd.read_csv("datos/spaphish.csv")
    espanol = espanol.fillna("")
    texto_es = espanol["subject"] + " " + espanol["body"]
    textos = textos + texto_es.str.lower().tolist()
    etiquetas = etiquetas + espanol["Label"].tolist()

    # 3. SMS en inglés
    ingles = pd.read_csv("datos/sms_ingles.txt", sep="\t", header=None, names=["etiqueta", "texto"])
    textos = textos + ingles["texto"].str.lower().tolist()
    etiquetas = etiquetas + ingles["etiqueta"].map({"spam": 1, "ham": 0}).tolist()

    return textos, etiquetas