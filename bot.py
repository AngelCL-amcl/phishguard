import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from detector import revisar_mensaje

# Leer el token del archivo secreto .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")


# Cuando alguien escribe /start
async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola! Soy PhishGuard. Reenvíame un mensaje sospechoso y te digo si es peligroso."
    )


# Cuando alguien manda cualquier mensaje de texto
async def revisar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    resultado, razones = revisar_mensaje(texto)

    respuesta = "RESULTADO: " + resultado
    if razones:
        respuesta = respuesta + "\n\nPor qué:"
        for razon in razones:
            respuesta = respuesta + "\n- " + razon

    await update.message.reply_text(respuesta)


# Encender el bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", inicio))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, revisar))

print("Bot funcionando... (Ctrl + C para detenerlo)")
app.run_polling()