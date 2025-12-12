from telethon.sync import TelegramClient
import pandas as pd

# Вставьте свои данные с my.telegram.org
API_ID = 123456  # ваш API_ID
API_HASH = 'your_api_hash'

def get_posts(channel_username, limit=50):
    client = TelegramClient('session', API_ID, API_HASH)
    client.start()

    channel_entity = client.get_entity(channel_username)
    posts = []
    for message in client.iter_messages(channel_entity, limit=limit):
        posts.append({
            'id': message.id,
            'date': message.date,
            'text': message.message or "",
            'views': message.views or 0
        })

    df = pd.DataFrame(posts)
    client.disconnect()
    return df
