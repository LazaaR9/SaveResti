import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8000889471:AAHhs6_GiIttptUZNibJ-QGaDKELfDN4Cp0")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22289599"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e8692e47ce07995977be6f336033c2fd")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Ramzy:Ramzy@cluster0.od4yk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
