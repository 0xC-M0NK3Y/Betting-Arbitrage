from bs4 import BeautifulSoup
import requests
import json

def get_winamax_core(url):
    ret = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = None
    for jsons in soup.find_all('script'):
        tmp = jsons.encode_contents()
        if tmp.startswith(b'var PRELOADED_STATE = '):
            data = json.loads(tmp[len('var PRELOADED_STATE = '):-1])
            break
    for matches in data['matches']:
        names = []
        if data['matches'][matches]['competitor1Name'] == None or data['matches'][matches]['competitor2Name'] == None:
            continue
        names.append(data['matches'][matches]['competitor1Name'].strip().lower())
        names.append(data['matches'][matches]['competitor2Name'].strip().lower())

        cotes = []

        tmp = data['bets'][str(data['matches'][matches]['mainBetId'])]['outcomes']
        if tmp == None or len(tmp) not in (2,3):
            continue
        cotes = []
        s = False
        for odds in tmp:
            if data['odds'][str(odds)] == None:
                s = True
                break
            cotes.append(data['odds'][str(odds)])

        if s == True:
            continue

        tmp = []
        tmp.append(names)
        tmp.append(cotes)
        ret.append(tmp)

    return ret


def get_winamax_football():
    return get_winamax_core('https://www.winamax.fr/paris-sportifs/sports/1')
def get_winamax_baseball():
    return get_winamax_core('https://www.winamax.fr/paris-sportifs/sports/2')
def get_winamax_tennis():
    return get_winamax_core('https://www.winamax.fr/paris-sportifs/sports/5')
def get_winamax_handball():
    return get_winamax_core('https://www.winamax.fr/paris-sportifs/sports/6')

def get_winamax(sport):
    if sport == 'football':
        return get_winamax_football()
    elif sport == 'baseball':
        return get_winamax_baseball()
    elif sport == 'tennis':
        return get_winamax_tennis()
    elif sport == 'handball':
        return get_winamax_handball()
    return []


