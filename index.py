import requests

from discord import app_commands, Intents, Client, Interaction

print("\n".join([
    "Hey, thanks for using simpledsccommands v1 by dvl.",
    "Please enter your bot's token below to continue.",
    "",
]))


while True:
    token = input("> ")

    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token}"
    })

    data = r.json()
    if data.get("id", None):
        break

    print("\nSeems like you entered an invalid token. Try again.")


class SomeClient(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)


client = SomeClient(intents=Intents.none())


@client.event
async def on_ready():
    print("\n".join([
        f"Logged in as {client.user} (ID: {client.user.id})",
        "",
        f"Invite your bot via invite link",
        f"https://discord.com/api/oauth2/authorize?client_id=[bot id]&scope=applications.commands%20bot"
    ]))

async def response(interaction: Interaction):
    print(f"> {interaction.user} used the command hello.")
    await interaction.response.send_message("\n".join([
        f"Hello {interaction.user} this is command1"
    ]))

async def response2(interaction: Interaction):
    print(f"> {interaction.user} used the command hellotwo.")
    await interaction.response.send_message("\n".join([
        f"Hello {interaction.user} This bot's source slash command atleast was originially made by dvl#0001. This is open source so feel free to use this too! www.github.com/dvlq/simpledsccommands . **Credits not a must but appreciated**"
    ]))

@client.tree.command()
async def hello(interaction: Interaction):
    """ Says hello or something """
    await response(interaction)


@client.tree.command()
async def credits(interaction: Interaction):
    """ Credits to original dev """
    await response2(interaction)


client.run(token)
