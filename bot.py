import telebot
import aposta
from time import sleep


chave = "6137681069:AAFxyV8lUfQ6rTC0rrnqOtnij9ebgVWT_DM"

bot = telebot.TeleBot(chave)


def verificar(menssagem):
    if menssagem.text == 'start':
        return True

@bot.message_handler(func=verificar)
def responder(menssagem):
    print('iniciou')
    while True:
        times = aposta.coner()

        if len(times) > 0:
            print('entrou')
            for jogo in times:

                liga = jogo[0]
                casa = jogo[1]
                visitante = jogo[2]
                texto = f"""
                liga - {liga}
                {casa} X {visitante}
                ----------------
                Entrada canto limite
                link: https://www.bet365.com/#/IP/B1
                """
                bot.reply_to(menssagem,texto)

        sleep(60)


bot.polling()