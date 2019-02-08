from telegram.ext import Updater, CommandHandler
import requests
import re
#Bot criado com intuito de testar conhecimentos basicos
#Funcao responsavel por pegar a url da api random.dog
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()#pegando o json
    url = contents['url']#pegando a url da imagem gerada
    return(url)#retornando-a
#funcao responsavel por executar ao comando /bop
def cachorro(bot, update):
    url = get_url()#chama a anterior
    chat_id = update.message.chat_id#passa a atualizar o envio
    bot.send_photo(chat_id=chat_id, photo=url)#envia
#construcao da conexao
def main():
    updater = Updater('711505407:AAHB7bWRoEVKkvv4HmmAZPEuerImyA2iYRo')#token do bot
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('cachorro', cachorro))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
