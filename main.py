import requests
import os  
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

# Récupération des variables d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))
ROLE_ID = int(os.getenv("DISCORD_ROLE_ID"))

# Intents et configuration du bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!!")

# Envoi d'un message via le webhook
def send_webhook_message(user):
    data = {
        "content": f"Bienvenue {user.mention} ! Tu as reçu un rôle 🎉"
    }
    requests.post(WEBHOOK_URL, json=data)

# Attribution automatique du rôle
@bot.event
async def on_member_join(member):
    role = member.guild.get_role(ROLE_ID)
    if role:
        await member.add_roles(role)
        send_webhook_message(member)

# Lancer le bot
bot.run(TOKEN)
