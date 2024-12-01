import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6852093006:AAFDFDu_AhIQZWGGfsQ73LgL6KuPcM6lf_k")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25662550"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3d2663ae1493ece93fab45f83b659acc")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Ramzy:Ramzy@cluster0.od4yk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
