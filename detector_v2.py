from urllib.parse import urlparse

# ===== BLOQUE 1: LISTAS =====
sufijos_dobles = ["com.mx", "co.uk", "com.br", "com.ec", "com.ar", "com.co"]

marcas = ["paypal", "amazon", "netflix", "google", "apple",
          "microsoft", "facebook", "instagram", "whatsapp",
          "usps", "fedex", "dhl", "chase", "wellsfargo", "bankofamerica", "youtube"]

dominios_confiables = [
    # Microsoft
    "microsoft.com", "microsoftonline.com", "live.com", "office.com",
    "outlook.com", "microsoft365.com", "sharepoint.com", "bing.com", "xbox.com",
    # Google
    "google.com", "gmail.com", "youtube.com", "youtu.be", "googleapis.com",
    # Apple
    "apple.com", "icloud.com",
    # Amazon
    "amazon.com", "amazonaws.com", "amazon.com.mx",
    # Meta
    "facebook.com", "instagram.com", "whatsapp.com", "whatsapp.net", "messenger.com",
    # Pagos y streaming
    "paypal.com", "paypalobjects.com", "netflix.com",
    # Paquetería
    "usps.com", "fedex.com", "dhl.com",
    # Bancos
    "chase.com", "jpmorganchase.com", "wellsfargo.com", "bankofamerica.com",
]


# ===== BLOQUE 2: FUNCIÓN QUE NORMALIZA =====
def normalizar(texto, uno_por):
    resultado = texto.lower().replace("1", uno_por).replace("4", "a").replace("0", "o").replace("3", "e").replace("5", "s").replace("7", "t").replace("8", "b").replace("rn", "m").replace("vv", "w").replace("cl", "d")
    return resultado


# ===== BLOQUE 3: FUNCIÓN QUE ANALIZA UNA URL =====
def analizar_url(url):
    url_con_l = normalizar(url, "l")
    url_con_i = normalizar(url, "i")

    partes = urlparse(url)
    partes_dominio = partes.netloc.split(".")

    terminacion = partes_dominio[-2] + "." + partes_dominio[-1]
    if terminacion in sufijos_dobles:
        dominio_real = partes_dominio[-3] + "." + partes_dominio[-2] + "." + partes_dominio[-1]
    else:
        dominio_real = partes_dominio[-2] + "." + partes_dominio[-1]
    print("Dominio real:", dominio_real)

    es_phishing = False
    for marca in marcas:
        aparece_marca = marca in url_con_l or marca in url_con_i
        no_es_oficial = dominio_real != marca + ".com"
        no_es_confiable = dominio_real not in dominios_confiables

        if aparece_marca and no_es_oficial and no_es_confiable:
            print("ALERTA: este link se hace pasar por", marca)
            es_phishing = True

    return es_phishing

def encontrar_links(mensaje):
    links = []
    palabras = mensaje.split()
    for palabra in palabras:
        if palabra.startswith("http"):
            links.append(palabra)
    return links
    
def analizar_texto(mensaje):
    palabras_sospechosas = ["urgen", "contraseña", "verifica", "suspendida", "ganaste", "gratis", "tarjeta", "codigo", "inmediato", "premio"]      
    puntos = 0
    for palabra_sospechosa in palabras_sospechosas:                   
        if palabra_sospechosa in mensaje:                
            puntos += 1
    return puntos
    
# ===== BLOQUE 4: PROGRAMA PRINCIPAL =====

mensaje = input("Pega el mensaje a revisar: ").lower()

links = encontrar_links(mensaje)
mensaje_peligroso = False
for link in links:
    print("Revisando:", link)
    if analizar_url(link):
        mensaje_peligroso = True
        
puntos = analizar_texto(mensaje)
print("Palabras sospechosas encontradas:", puntos)

if puntos >= 2:
    mensaje_peligroso = True
    
if mensaje_peligroso:
    print("RESULTADO: PELIGROSO")
else:
    print("RESULTADO: Parece seguro")
    