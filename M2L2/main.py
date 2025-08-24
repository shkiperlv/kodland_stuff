import telebot
from random import choice
from datetime import datetime, timedelta
from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}! Проблема загрязнения природы на данный момент является одной из самых актуальных в нашем обществе, и я могу тебе объяснить почему.')
    bot.send_message(message.chat.id, 'Используй команду /info чтобы узнать больше о загрязнении')

info_data = [
    {
        "image": "images/bottle.jpg",
        "text": "bottle"
    },
    
    {
        "image": "images/paket.jpg",
        "text": "paket"
    }
    
]

@bot.message_handler(commands=['info'])
def send_info(message):
    item = choice(info_data)

    if item["text"] == "paket":
        today = datetime.now()
        future_date = today + timedelta(days=500*365)
        text = (
            "Полиэтиленовый пакет разлагается сотни лет. Это печальная перспектива – в отличие от бумажной и металлической упаковки, которая сгниет в земле за несколько десятков лет, пакет будет отравлять окружающую среду очень долго."
            f" Пластиковый пакет, выброшенный сегодня, полностью разложится только к {future_date.strftime('%d.%m.%Y')}."
        )
    elif item["text"] == "bottle":
        today = datetime.now()
        future_date = today + timedelta(days=700*365)
        text = (
            "Сегодня производится 380 миллионов тонн пластиковых изделий в год. Отходы, скопившиеся в Тихом океане, по размерам больше площади острова Гренландия. Но и окончательно отказаться от полимера невозможно. Упаковка из него увеличивает срок годности продуктов и сокращает на 75% количество пищевых отходов."
            f" Пластиковая бутылка, выброшенная сегодня, полностью разложится только к {future_date.strftime('%d.%m.%Y')}."
        )
    else:
        text = item["text"]

    with open(item["image"], 'rb') as f:
        bot.send_photo(message.chat.id, f, caption=text)

bot.polling() 