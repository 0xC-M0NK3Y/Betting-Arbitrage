from analyzer.betclic import get_betclic
from analyzer.netbet import get_netbet
from analyzer.winamax import get_winamax
from analyzer.parionssport import get_parionssport
from analyzer.rabona import get_rabona

ANALYZERS = [
    ['betclic',     get_betclic],
    ['netbet',      get_netbet],
    ['winamax',     get_winamax],
    ['pariossport', get_parionssport],
	['rabona',      get_rabona]
]
