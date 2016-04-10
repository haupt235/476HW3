def element_data(l):
	info= {"Molar Mass": l[1], "Z": l[2], "rho":l[3]}
	return info

def isotope_data(line, l, lines):
	position = lines.index(line)
	iso_number =int(l[4])
	isos = []
	for i in range(iso_number):
		isos.append(lines[position+1+i].split())
	return isos
	
