from utils.read_json_file import load_data
from utils.scripts import get_transactions, sort_transactions, five_items, time_correct, get_from


def main():
	data = load_data()
	ex_items = get_transactions(data)
	sort_items = sort_transactions(ex_items)
	items = five_items(sort_items)
	for item in items:
		print(time_correct(item['date']), item["description"])
		print(get_from(item), (item))
		print((item))
		print()


if __name__ == '__main__':
	main()
