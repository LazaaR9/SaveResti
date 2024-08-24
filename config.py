import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7335357897:AAEMKAGJkQKcbnm99_UdhFlK15H1-_uw6mQ")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26303261"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e924187728893dd49765079342ea3d21")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://hackerbaloch07:<db_password>@cluster0.jnffy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
