import locale
from datetime import datetime
from classes import CoinGeckoApi, TelegramBot
from time import sleep

id_moeda = input('Informe a ID da moeda a ser rastreada: ')
valor_minimo = int(input('Qual o valor mínimo para inicar o rastreio: '))
valor_maximo = int(input('Qual o valor máximo para inicar o rastreio: '))

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

api = CoinGeckoApi(url_base='https://api.coingecko.com/api/v3')

bot = TelegramBot(token='seutokengeradonobotfather', chat_id='seuchatid')

while True:
    if api.ping():
        print('API on-line!')
        sleep(2)
        preco, atualizado_em = api.consulta_preco(id_moeda=id_moeda)
        print('Consulta realizada com sucesso!')
        sleep(2)
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = None

        if preco < valor_minimo:
            mensagem = f'*Cotação do Ethereum*:\n\t' \
                       f'*Preço*: R$ {preco}\n\t' \
                       f'*Horário*: {data_hora}\n\t' \
                       f'*Motivo*: Valor menor que o mínimo!'

        elif preco > valor_maximo:
            mensagem = f'*Cotação do Ethereum*:\n\t' \
                       f'*Preço*: R$ {preco}\n\t' \
                       f'*Horário*: {data_hora}\n\t' \
                       f'*Motivo*: Valor maior que o máximo!'

        if mensagem:
            bot.envia_mensagem(texto_markdown=mensagem)
    else:
        print('Servidor off-line, tente novamente mais tarde! ')

    sleep(1800)
