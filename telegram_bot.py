import telebot

bot = telebot.TeleBot('7285132994:AAF_5lboS-l_O5thcaxTDvO_XxlxEPmH1Lc')

#Мій чат з ботом
CHAT_ID = '1037537681'

def send_product_message(product):
    message = (
        f"Новый товар добавлен:\n\n"
        f"Название: {product.name}\n"
        f"Количество: {product.amount}\n"
        f"Описание: {product.description}\n"
        f"Цена: {product.price}\n"
        f"Скидка: {product.discount}%"
    )
    bot.send_message(CHAT_ID, message)


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, f"Your Chat ID is: {message.chat.id}")

# bot.polling()