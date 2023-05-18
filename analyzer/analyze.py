from analyzer.betclic import get_betclic
from analyzer.netbet import get_netbet
from analyzer.winamax import get_winamax
from analyzer.parionssport import get_parionssport

def verif_len_and_parse(cotes):
	lenn = len(cotes[0])
	for i in range(len(cotes)):
		if (len(cotes[i]) != lenn):
			return False
	for i in range(len(cotes)):
		for j in range(len(cotes[i])):
			if isinstance(cotes[i][j], float) == False:
				if isinstance(cotes[i][j], int):
					cotes[i][j] = float(cotes[i][j])
				else:
					cotes[i][j] = float(cotes[i][j].replace(',', '.'))
	return True

def compute(data):
	cotes = []
	for i in range(len(data)):
		cotes.append(data[i][1])
	ret = 0
	if verif_len_and_parse(cotes) == False:
		return -1;
	max = []
	for i in range(len(cotes[0])):
		tmp = 0
		for j in range(len(cotes)):
			if cotes[j][i] > tmp:
				tmp = cotes[j][i]
		max.append(tmp)
	for i in range(len(max)):
		ret = ret + 1 / max[i]
	return ret


def print_site(site, name):
	print(f"{name} : ")
	for i in range(len(site)):
		print(site[i])


def analyze_sport(sport):
	ret = []

	netbet = get_netbet(sport)
	betclic = get_betclic(sport)
	winamax = get_winamax(sport)
	parionssport = get_parionssport(sport)

	sites = []
	sites.append(netbet)
	sites.append(betclic)
	sites.append(winamax)
	sites.append(parionssport)

	names = []
	names.append("netbet")
	names.append("betclic")
	names.append("winamax")
	names.append("parionssport")

	for i in range(len(sites)):
		for j in range(len(sites[i])):
			cmp = []
			cmp_name = []
			cmp_name.append(names[i])
			cmp.append(sites[i][j])
			for k in range(len(sites)):
				if k == i:
					continue
				for l in range(len(sites[k])):
					if sites[i][j][0][0] == sites[k][l][0][0] or sites[i][j][0][1] == sites[k][l][0][1]:
						cmp_name.append(names[k])
						cmp.append(sites[k][l])
			if (len(cmp) > 1):
				result = compute(cmp)
				if result < 0:
					continue
				ret.append(f"Result : {result:.2f} for :\n")
				for u in range(len(cmp)):
					ret.append(f'{cmp_name[u]} : {cmp[u]}\n')
				ret.append('\n')
	return ret


