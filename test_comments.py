from nose.tools import assert_equal

from comments import t_swift, comment_baleeter

def test_t_mat():
	
	obs = t_swift('mat_comment_test')
	exp=['water    \t    1.00   2#i must scream\n', '                              h  11.111        1\n', '                              o  88.889        8 #lol\n']
	assert_equal(obs, exp)

	
