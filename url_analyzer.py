from urllib.parse import urlparse

url = input("pega el link a revisar: ").lower()

url_con_l = url.replace("1", "l").replace("4", "a").replace("0", "o").replace("3", "e").replace("5", "s").replace("7", "t").replace("8", "b").replace("rn", "m").replace("vv", "w").replace("cl", "d")
url_con_i = url.replace("1", "i").replace("4", "a").replace("0", "o").replace("3", "e").replace("5", "s").replace("7", "t").replace("8", "b").replace("rn", "m").replace("vv", "w").replace("cl", "d")

sufijos_dobles = ["com.mx", "co.uk", "com.br", "com.ec", "com.ar", "com.co"]
partes = urlparse(url)

print("Esquema:", partes.scheme)
print("Dominio:", partes.netloc)
print("Ruta:", partes.path)
partes_dominio = partes.netloc.split(".") 
print("Partes:", partes_dominio)
terminacion = partes_dominio[-2] + "." + partes_dominio[-1]
if terminacion in sufijos_dobles:
    dominio_real = partes_dominio[-3] + "." + partes_dominio[-2] + "." + partes_dominio[-1]
else:
    dominio_real = partes_dominio[-2] + "." + partes_dominio[-1]
print("dominio_real:", dominio_real)
    
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

es_phishing = False 
for marca in marcas:
    aparece_marca = marca in url_con_l or marca in url_con_i
    no_es_oficial  = dominio_real != marca + ".com"
    no_es_confiable = dominio_real not in dominios_confiables
    
    if aparece_marca and no_es_oficial and no_es_confiable:
        print("ALERTA: este link se hace pasar por", marca)
        es_phishing = True
        
if es_phishing: 
    print("RESULTADO: PELIGROSO")
else: 
    print("RESULTADO: Parece seguro")
      
def normalizar(url_con_l):
    print(normalizar("PAYPA1"))
    print(normalizar("G00GLE")) 
    print(normalizar("ARNAZON")) 
         
            