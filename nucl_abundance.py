import readthrough as rt
import matmods as mm

def dicsum(dic):
	sum =0
	for i in dic:
		sum = sum + dic[i]
	return sum



def nucl_abundance(key):
	"""returns A Z and atomic abundance of a key within matdict & kills the rob"""
	matdict = mm.library_creator('matlib')
	eledict = rt.library_creator('elelib')
	answer_dict = {}	
	if key in matdict:
		smol = matdict[key]
		atoms = smol['Mass Fraction']
		answer_dict = {}
		N_i = {}
		N_final = {}
		A={}
		N_total = {}
		for i in atoms:			
			wo = atoms[i][0]
			atom = atoms[i][1]
			element_data = eledict[i]
			molar  = element_data['Molar Mass']
			rho = element_data['rho']
			isos = element_data['iso']
			percent_abundance= 0 
			N_i[i] = {}
			A[i] = {}
			
			for j in isos:
				percent_abundance = isos[j][0]
				A[i].update({j:element_data['Z']})
				N_i[i].update({j:float(rho)*float(wo)/100*float(percent_abundance)/float(molar)})			
			N_total[i] = dicsum(N_i[i])	
		
		io={}
		for l in N_i:
			io[l] = {}
			for m in N_i:
				io[l][m] = N_i[l][m]/N_total[l]
		for n in atoms:
			answer_dict[n] = {}
			for p in A[n]:
				answer_dict[n].update({i+str(j[0]): [A[n][p],j[0],io[n][p]]}) 
		return {key: answer_dict}
