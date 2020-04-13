import discord, asyncio # 디스코드 모듈과, 보조 모듈인 asyncio를 불러옵니다.
import datetime

token = "Njk3NzYxOTgxMzg1NDA4NTgz.XpQk5w.mdDxFN-KJYnvNOZWfUHJ1G3JKVQ" # 아까 메모해 둔 토큰을 입력합니다
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
    
    global timenow # 글로벌함수로 나중에 다른곳에서도 시간을 불러올수있게합니다.
    global timesave # 약속시간용 함수
    global timesaveswitch #약속시간을 한번만 작동하게하는 스위치
    timesave = "0000"
    timesaveswitch = "0"
    

    while True: # 무한반복 함수
        timenow = str(datetime.datetime.now()) # 현재시간을 받아옵니다 예)2020-04-13 11:13:32.520761 초뒤에 마이크로초까지나옴

        if(timesave[0:2] == timenow[11:13]): # 현재시간과 약속시간의 '시' 를 비교
            if(timesave[2:4] == timenow[14:16]): # 현재시간과 약속시간의 '분' 를 비교
                if(timesaveswitch == "1"): # 스위치가 
                    await client.get_channel(697767955127337054).send(timesave + " 해당 약속시간이 되었습니다.")
                    timesaveswitch = "0"
            
        #await client.get_channel(697767955127337054).timesave
        await asyncio.sleep(3) # 중간중간 쉬게해주어서 다른 명령어를 받을수있게함

@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
    global timesave
    global timesaveswitch
    if message.author.bot: # 채팅을 친 사람이 봇일 경우
        return None # 반응하지 않고 구문을 종료합니다.
    if message.content == "!명령어": # !명령어 라는 채팅을 친다면
    # 메시지 전송이 두가지 방법이 있습니다. 상황에 맞는 구문을 사용하시면 됩니다.
    # 이 구문은 메시지가 보내진 채널에 메시지를 보내는 구문입니다.
        await message.channel.send("회사에서 응답")
        await client.get_channel(697767955127337054).send(timesave)
    # 이 아래 구문은 메시지를 보낸 사람의 DM으로 메시지를 보냅니다.
    #await message.author.send("응답")
    # 여기 token에는 토큰을 넣지 않고 그대로 옮겨 쓰시면 됩니다.
    if message.content == "!현재시간":
        await message.channel.send(timenow)

    if message.content.startswith("!약속"):
        
        timesave = message.content[4:]
        timesaveswitch = "1"
        await message.channel.send(timesave)
    

client.run(token) # 아까 넣어놓은 토큰 가져다가 봇을 실행하라는 부분입니다. 이 코드 없으면 구문이 아무리 완벽해도 실행되지 않습니다.
