from bs4 import BeautifulSoup
import requests
import json

def get_parionssport_core(url):
    ret = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    for events in list(soup.find_all('div', {'class': 'psel-event'})):
        names = []
        spanname1 = events.find('span', {'class': 'psel-match__label__opponent psel-match__label__opponent--first'})
        spanname2 = events.find('span', {'class': 'psel-match__label__opponent psel-match__label__opponent--second'})
        if spanname1 == None or spanname2 == None:
            continue
        names.append(spanname1.get_text().strip().lower())
        names.append(spanname2.get_text().strip().lower())

        cotes = []
        for spancote in list(events.find_all('span', {'class': 'psel-outcome__data'})):
            cotes.append(spancote.get_text().strip().lower())

        if len(names) > 0 and len(cotes) > 0:
            tmp = []
            tmp.append(names)
            tmp.append(cotes)
            ret.append(tmp)
    return ret

def get_parionssport_football():
    return get_parionssport_core('https://www.enligne.parionssport.fdj.fr/paris-football')
def get_parionssport_baseball():
    return get_parionssport_core('https://www.enligne.parionssport.fdj.fr/paris-baseball')
def get_parionssport_tennis():
    return get_parionssport_core('https://www.enligne.parionssport.fdj.fr/paris-tennis')
def get_parionssport_handball():
    return get_parionssport_core('https://www.enligne.parionssport.fdj.fr/paris-handball')

def get_parionssport(sport):
    if sport == 'football':
        return get_parionssport_football()
    elif sport == 'baseball':
        return get_parionssport_baseball()
    elif sport == 'tennis':
        return get_parionssport_tennis()
    elif sport == 'handball':
        return get_parionssport_handball()
    return []

