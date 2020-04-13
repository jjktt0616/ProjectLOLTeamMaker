import discord, asyncio # 디스코드 모듈과, 보조 모듈인 asyncio를 불러옵니다.

token = "토큰" # 아까 메모해 둔 토큰을 입력합니다 직접넣어서 깃허브에올리면 토큰이 
client = discord.Client() # discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언입니다.


@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
    # 봇이 "반갑습니다"를 플레이 하게 됩니다.
    # 눈치 채셨을지 모르곘지만, discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
    await client.change_presence(status=discord.Status.online, activity=discord.Game("반갑습니다 :D"))
    print("I'm Ready!") # I'm Ready! 문구를 출력합니다.
    print(client.user.name) # 봇의 이름을 출력합니다.
    print(client.user.id) # 봇의 Discord 고유 ID를 출력합니다.
    """
    주석처리?
    """
@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
    if message.author.bot: # 채팅을 친 사람이 봇일 경우
        return None # 반응하지 않고 구문을 종료합니다.
    if message.content == "!명령어": # !명령어 라는 채팅을 친다면
    # 메시지 전송이 두가지 방법이 있습니다. 상황에 맞는 구문을 사용하시면 됩니다.
    # 이 구문은 메시지가 보내진 채널에 메시지를 보내는 구문입니다.
        await message.channel.send("회사에서 응답")
    # 이 아래 구문은 메시지를 보낸 사람의 DM으로 메시지를 보냅니다.
    #await message.author.send("응답")
    if message.content == "!식별자":
        userDiscriminator = message.author.discriminator
        discordUserId = str(message.author.id)
        await message.channel.send("당신의 식별자는 " + userDiscriminator + " 입니다.")
        await message.channel.send("당신의 아이디는 " + discordUserId + " 입니다.")
    

client.run(token) # 아까 넣어놓은 토큰 가져다가 봇을 실행하라는 부분입니다. 이 코드 없으면 구문이 아무리 완벽해도 실행되지 않습니다.
