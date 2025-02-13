import os  
import discord
from discord.ext import commands, tasks
from discord import Embed
import requests

# Variables d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))  # Salon où envoyer le message
ROLE_ID = int(os.getenv("DISCORD_ROLE_ID"))  # Rôle à attribuer
EMOJI = "❤️"  # Emoji à surveiller pour la réaction

intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # Lire les messages et réactions

bot = commands.Bot(command_prefix="!!", intents=intents)

# Fonction pour envoyer le message
@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        embed = Embed(
            title="Joyeuse St-Valentin !",
            description="Voici votre petit badge exclusif ! 🎉",
            color=discord.Color.purple()
        )
        embed.set_image(url="https://example.com/image.png")  # Remplace par l'URL de ton image

        # Envoi du message avec l'embed
        message = await channel.send(embed=embed)

        # Ajouter une réaction prédéfinie à ce message
        await message.add_reaction(EMOJI)

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

os.system("sleep infinity")
