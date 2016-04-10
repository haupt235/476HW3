from nose.tools import assert_equal, assert_raises

from readthrough import library_creator, element_data, isotope_data

def test_ele():
    
    obs = element_data(["lol", 1,2,3,4])
    exp = {"Molar Mass": 1, "Z": 2, "rho":3}
    assert_equal(obs, exp)

def test_iso():

	obs = isotope_data('lol 4 3 2 1', ["lol", '4', '3','2', '1'], ['lol 4 3 2 1', 'kek 5 6 7 8', 'lol 9 1 2 3'])
	exp = [['kek', '5', '6', '7', '8']]
	assert_equal(obs, exp)

def test_lib():
	
	obs = library_creator("filefortest")
	exp = {'lol': { 'iso' : [['5', '1'], ['6', '2'], ['7', '3'], ['8', '4']], 'rho' : '3',  'Molar Mass' : '1', 'Z' : '2'}}
	assert_equal(obs,exp)
