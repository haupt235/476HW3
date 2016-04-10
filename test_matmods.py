from nose.tools import assert_equal, assert_raises

from matmods import library_creator, mat_data, massfract_data

def test_mass():
    
    obs = mat_data(["lol", 1,2])
    exp = {"Density @STP": 1}
    assert_equal(obs, exp)

def test_massfract():

	obs = massfract_data('lol 4 1', ["lol", '4', '1'], ['lol 4 1', 'kek 5 6', 'lol 9 2'])
	exp = [['kek', '5', '6']]
	assert_equal(obs, exp)

