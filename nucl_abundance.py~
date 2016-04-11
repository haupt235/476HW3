import readthrough as rt
import matmods as mm




def nucl_abundance(key):
	matdict = mm.library_creator('matlib')
	eledict = rt.library_creator('elelib')	
	if key in matdict:
		smol = matdict[key]
		atoms = smol['Mass Fraction']
		wo = []
		atom = []
		rho = []
		mm = []
		N_i = []
		element_data = []
		A = []
		i=0
		while i < len(atoms):			
			wo.append(atoms[i][1])
			atom.append(atoms[i][0])
			element_data = eledict[atom[i]]
			mm  = element_data['Molar Mass']
			rho = element_data['rho']
			isos = element_data['iso']
				while j < len(isos):
					percent_abundance = isos[j][1]
					A = isos[j][0]
				ao=sum(A*percent_abundance)
			N_i = rho[i]*wo[i]*[ao]/mm[i]
			i=i+1
		answer_dict = {'N': element_data, 'A':A, 'N_i': N_i}
		
		
			
			
		
