from analyzer.analyzers import ANALYZERS

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

def is_valid(names):
	for i in range(len(names)):
		for j in range(i+1, len(names)):
			if names[i] == names[j]:
				return False
	return True

def analyze_sport(sport):
	ret = []
	results = []
	names = []

	for i in range(len(ANALYZERS)):
		results.append(ANALYZERS[i][1](sport))
		names.append(ANALYZERS[i][0])

	for i in range(len(results)):
		for j in range(len(results[i])):
			cmp = []
			cmp_name = []
			cmp_name.append(names[i])
			cmp.append(results[i][j])
			for k in range(len(results)):
				if k == i:
					continue
				for l in range(len(results[k])):
					if results[i][j][0][0] == results[k][l][0][0] or results[i][j][0][1] == results[k][l][0][1]:
						cmp_name.append(names[k])
						cmp.append(results[k][l])
			if is_valid(cmp_name) and len(cmp) > 1:
				result = compute(cmp)
				if result < 0:
					continue
				ret.append(f"Result : {result:.2f} for :\n")
				for u in range(len(cmp)):
					ret.append(f'{cmp_name[u]} : {cmp[u]}\n')
				ret.append('\n')
	return ret


