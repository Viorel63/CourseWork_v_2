from utils.scripts import time_correct, five_items


def test_get_transactions():
	pass


def test_sort_transactions():
	pass


def test_five_items():
	assert five_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [1, 2, 3, 4, 5]


def test_time_correct():
	assert time_correct("2019-08-26T10:50:58.294041") == '26-08-2019'


def test_get_from():
	pass


def test_get_to():
	pass


def get_money():
	pass