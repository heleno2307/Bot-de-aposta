import requests
import telebot
import time

def jason():
    url = requests.get("https://api.sportsanalytics.com.br/api/v1/fixtures-svc/fixtures/livescores?include=weatherReport,additionalInfo,league,stats,pressureStats,probabilities&api_key=OjS6sjgyOjtAfk82AzxZKxc78Z4y9FJn")
    ojason = url.json()
    return ojason

def coner():
    ojason = jason()
    tot = 0
    cont = 0
    aux = []
    times = []

    tot = int(ojason['total'])
    minutos = 0

    for jogos in ojason['data']:
        if jogos['stats'] != None:
            minutos = jogos['currentTime']['minute']

            # verifica o tempo
            if minutos >= 36 and minutos < 45 or minutos >= 82 and minutos < 90:

                # tratamento para campo nulo
                if jogos['stats']['possessiontime']['home'] == None:
                    poss = 0

                else:
                    poss = jogos['stats']['possessiontime']['home']

                # verifica o posse de bola
                if poss >= 60:

                    # verifica se o mandante está empatando ou perdendo o jogo
                    if jogos['stats']['goals']['home'] <= jogos['stats']['goals']['away']:

                        # VERIFICANDO CAMPO NULO
                        if jogos['pressureStats'] != None:

                            # VERIFICANDO CAMPO NULO
                            if jogos['pressureStats']['appm1'] != None:

                                # VERIFICANDO ATAQUE PERIGOSO POR MINUTO
                                if jogos['pressureStats']['appm1']['home'] > 1 and jogos['pressureStats']['appm2']['home'] > 1:

                                    aux.append(jogos['league']['name'])
                                    aux.append(jogos['homeTeam']['name'])
                                    aux.append(jogos['awayTeam']['name'])

                                    if jogos['fixtureId'] != None:
                                        aux.append(jogos['fixtureId'])

                                    if jogos['currentTime']['minute'] != None:
                                        aux.append(jogos['currentTime']['minute'])

                                    times.append(aux[:])
                                    aux.clear()
    return times


