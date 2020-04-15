class Info:
    def __init__(self, discriminator, userId):
        self.userDiscriminator = discriminator
        self.discordUserId = userId

def discriminator(message):
    if message.content == "!식별자":
        userDiscriminator = message.author.discriminator
        discordUserId = str(message.author.id)
        Info(userDiscriminator, discordUserId)
        return Info