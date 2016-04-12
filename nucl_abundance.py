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
				A[i].update({'A':j})
				N_i[i].update({i:float(rho)*float(wo)*float(percent_abundance)/float(molar)})			
			N_total = dicsum(N_i[i])	
			for l in N_i:
				N = N_i[l][i]/N_total
				N_final.update({l:N})
				print(N_final)	
			answer_dict.update({i:atom,'A':A}) 
		return {key: answer_dict.update({'N':N_final })}
		
			
			
		
