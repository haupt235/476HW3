from nose.tools import assert_equal

from comments import t_swift, comment_baleeter

def test_t_mat():
	
	obs = t_swift('mat_comment_test')
	exp=['water    \t    1.00   2#i must scream\n', '                              h  11.111        1\n', '                              o  88.889        8 #lol\n']
	assert_equal(obs, exp)

def test_t_ele():

	obs = t_swift('ele_comment_test')
	exp=['h       0.100790E+01   1      0.899000E-04   2#it comes\n', '						1      0.999850E+02 #AAA\n', '						2      0.150000E-01\n', '#i wish for death \n']
	assert_equal(obs,exp)

def test_comm_mat():
	
	obs = comment_baleeter('mat_comment_test')
	exp=['water    	    1.00   2', '', '                              h  11.111        1', '', '', '', '', '                              o  88.889        8 ']
	assert_equal(obs, exp)

def test_comm_ele():

	obs = comment_baleeter('ele_comment_test')
	exp=['h       0.100790E+01   1      0.899000E-04   2', '', '						1      0.999850E+02 ', '						2      0.150000E-01', '', '']
	assert_equal(obs, exp)
