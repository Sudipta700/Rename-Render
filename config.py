# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27770330")

API_HASH = os.environ.get("API_HASH", "85251c8ab120d81f04b6c16ba876c673")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7421654904:AAGAZXHjrWpmI9DuPH98iLRQCgiejhknRswmongodb+srv://raftaarjrkalamkar:Ytxb4Uvva0difMMa@cluster0.ttrf7tz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Rename_filmsclub04_bot") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://raftaarjrkalamkar:Ytxb4Uvva0difMMa@cluster0.ttrf7tz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5507349138').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
