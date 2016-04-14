import readthrough as rt
import matmods as mm
import pdb 

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
	pdb.set_trace()	
	if key in matdict:
		smol = matdict[key]
		atoms = smol['Mass Fraction']
		answer_dict = {}
		N_i = {}
		N_final = {}
		A={}
		N_total = {}
		isos = []
		for i in atoms.keys():			
			wo = atoms[i][0]
			atom = atoms[i][1]
			element_data = eledict[i]
			molar  = element_data['Molar Mass']
			rho = element_data['rho']
			isos = element_data['iso']
			percent_abundance= 0 
			N_i[i] = {}
			A[i] = {}
			
			for j in isos.keys():
				percent_abundance = isos[j][0]
				A[i].update({j:element_data['Z']})
				N_i[i].update({j:float(rho)*float(wo)/100*float(percent_abundance)/float(molar)})			
			N_total[i] = dicsum(N_i[i])	
		
		io={}
		for i in N_i:
			io[i] = {}
			for j in N_i[i]:
				io[i][j] = N_i[i][j]/N_total[i]
		for i in atoms:
			answer_dict[i] = {}
			for j in A[i]:
				answer_dict[i].update({j: [A[i][j],j,io[i][j]]}) 
		return {key: answer_dict}
