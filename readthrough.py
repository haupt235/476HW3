def element_data(l):
	info= {"Molar Mass": l[1], "Z": l[2], "rho":l[3]}
	return info

def isotope_data(line, l, lines):
	position = lines.index(line)
	iso_number =int(l[4])
	isos = {}
	for i in range(iso_number):
		j= lines[position+1+i].split())
		isos.update({j[0]: j[1:]})
	return isos

def library_creator(data_input): 
	
	file = open(data_input, "r+")

	lines = file.readlines()

	nice = {}

	

	for line in lines:
		l = line.split()
		if line[0].isalpha():

			nice[l[0]] = element_data(l)
			nice[l[0]].update({"iso" : isotope_data(line, l, lines)})

	print(nice)
	return(nice)
