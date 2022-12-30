import discord
from datetime import datetime, timedelta

# 定義
# botのトークン
BOT_TOKEN = "*************************************"
# サーバーID(int型)
SERVER_ID = "000000000000"
# 通知させるチャンネルのID
ALERT_CHANNEL = 00000000000
# 通話参加時のみ付与させるロールのID
ROLE_ID = 00000000
# 通知を除外させたいメンバーID(Rhythmとか)
EXCLUDE_ID = 000000000

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_voice_state_update(member, before, after):
    # 通話チャンネルの状態を監視、入退室がトリガー
    if str(member.guild.id) == SERVER_ID and (str(before.channel) != str(after.channel)):
        #now = datetime.utcnow() + timedelta(hours=9)
        # メッセージを送るチャンネル
        alert_channel = client.get_channel(ALERT_CHANNEL)
        if member.id != EXCLUDE_ID:
            # 通話参加時に付与するロールを取得
            role = member.guild.get_role(ROLE_ID)
            # 入室か退室かを判定
            if before.channel is None:
                if member.nick is None:
                    msg = f'{member.name} が参加しました。'
                    await alert_channel.send(msg, tts=True)
                    await member.add_roles(role)
                else:
                    msg = f'{member.nick} が参加しました。'
                    await alert_channel.send(msg, tts=True)
                    await member.add_roles(role)
            elif after.channel is None:
                if member.nick is None:
                    msg = f'{member.name} が退出しました。'
                    await alert_channel.send(msg, tts=True)
                    await member.remove_roles(role)
                else:
                    msg = f'{member.nick} が退出しました。'
                    await alert_channel.send(msg, tts=True)
                    await member.remove_roles(role)

client.run(BOT_TOKEN)
