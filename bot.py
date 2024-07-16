from config import API_ID, API_HASH, SESSIONS
from pyrogram import Client, idle
import sys

CLIENTS = []

for i,SESSION in enumerate(SESSIONS):
    if SESSION:
        client = Client(
            name=f"SHUKLA{i}",
            session_string=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="SHUKLA.modules"),
        )
        CLIENTS.append(client)


if __name__ == "__main__":

    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("ALL_SANATANI_BOT")
            CLIENT.join_chat("SANATANI_TECH")
            CLIENT.join_chat("II_SANATANI_II")
            print(f"ꜱᴛᴏʀᴍ ꜱᴛᴀʀᴛᴇᴅ ᴀꜱ{i+1}")
            print(f"ʙᴏᴏᴛᴇᴅ/ꜱᴛᴀʀᴛᴇᴅ {CLIENT.me.first_name} 🎉")
        except Exception as e:
            print(e)
            print("ᴇxɪᴛɪɴɢ ᴛʜᴇ ᴘʀᴏɢʀᴀᴍ")
            sys.exit(1)

    print("ꜱᴛᴏʀᴍ ᴜꜱᴇʀ ʙᴏᴛ ɪꜱ ᴅᴇᴘʟᴏʏᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🌩️🥀")
    idle()
