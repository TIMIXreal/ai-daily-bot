import random
import requests

# 🔑 ВСТАВЬ СЮДА ТОКЕН БОТА
TOKEN = "8613530703:AAE8HR8AEd27csub2vssa39Q6xJhovceBkA"

# 📢 ТВОЙ КАНАЛ
CHANNEL = "@AIDailyneuro"

# 📄 Читаем посты
with open("posts.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Разделяем посты
posts = content.split("\n\n---\n\n")

# Выбираем случайный пост
post = random.choice(posts)

# Отправка в Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHANNEL,
    "text": post,
    "parse_mode": "HTML"
}

response = requests.post(url, data=data)

print(response.text)
