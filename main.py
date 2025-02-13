import os  
import discord
from discord.ext import commands
from discord import app_commands
from discord import Embed
from flask import Flask
import threading
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_web, daemon=True).start()
# Variables d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))  # Salon où envoyer le message
ROLE_ID = int(os.getenv("DISCORD_ROLE_ID"))  # Rôle à attribuer
EMOJI = "❤️"  # Emoji à surveiller pour la réaction

CHANNEL_ID = int(CHANNEL_ID)  # Convertir l'ID du salon en entier

intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # Lire les messages et réactions

bot = commands.Bot(command_prefix="!!", intents=intents)

# Fonction pour envoyer un message via le webhook
def send_webhook_message():
    data = {
        "content": "Joyeuse St-Valentin, voici votre petit badge exclusif ! 🎉",
        "embeds": [{
            "title": "Joyeuse St-Valentin !",
            "description": "Voici votre petit badge exclusif ! 🎉",
            "color": 0x800080,  # Couleur violette
            "image": {"url": "https://example.com/image.png"}  # Remplace par l'URL de ton image
        }]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 200:
        print("Message envoyé via le webhook.")
    else:
        print(f"Erreur lors de l'envoi du message: {response.status_code}")

# Fonction pour envoyer le message via le webhook dans le salon
@bot.event
async def on_ready():
    # Envoyer le message via le webhook
    send_webhook_message()

# Fonction pour attribuer un rôle lorsque l'emoji est réagi
@bot.event
async def on_reaction_add(reaction, user):
    # Vérifier si la réaction est sur le bon message et avec le bon emoji
    if reaction.message.author == bot.user and str(reaction.emoji) == EMOJI:
        role = discord.utils.get(user.guild.roles, id=ROLE_ID)
        if role:
            await user.add_roles(role)
            print(f"{user.name} a reçu le rôle {role.name} !")
# Lancer le bot
bot.run(TOKEN)

if __name__ == "__main__":
    os.system("sleep infinity")
