import telebot
import os
from dotenv import load_dotenv
import requests
from libretranslatepy import LibreTranslateAPI

load_dotenv()
token = os.getenv('AUTH_TOKEN')

bot = telebot.TeleBot(token)  # instanciando
lt = LibreTranslateAPI("https://translate.astian.org/")


def pegar_url():
    conteudo = requests.get('https://dog.ceo/api/breeds/image/random').json()
    imagem_url = conteudo['message']
    return imagem_url


def pegar_fato():
    # conteudo = requests.get('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1').json()
    conteudo = requests.get('https://dog-api.kinduff.com/api/facts?number=1').json()
    fato = conteudo['facts'][0]
    fato_br = lt.translate(fato, 'en', 'pt')
    return fato_br


@bot.message_handler(commands=['auau'])
@bot.message_handler(regexp=r'auau')
def auau(message):
    url = pegar_url()
    bot.send_photo(message.chat.id, url)


@bot.message_handler(commands=['fato'])
@bot.message_handler(regexp=r'fato')
def fato(message):
    fato = pegar_fato()
    bot.send_message(message.chat.id, fato)


@bot.message_handler(commands=['criador', 'creator'])
@bot.message_handler(regexp=r'criador')
def criador(message):
    criador = 'https://github.com/davimassarelli'
    bot.send_message(message.chat.id, criador)


@bot.message_handler(commands=['ola', 'start'])
@bot.message_handler(regexp=r'ola')
def ola(message):
    msg = ''' Olá, como vai você? 
    Para fotos digite "auau"
    Para fatos curiosos digite "fato"'''
    bot.send_message(message.chat.id, msg)


@bot.message_handler(func=lambda m: True)
def repetir(message):
    bot.reply_to(message, message.text)


def main():
    bot.polling()  # buscando mensagens


if __name__ == '__main__':
    main()
