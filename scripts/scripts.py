def get_transactions(data):
	"""Читает json файл."""
	items = [item for item in data if item.get('state') == "EXECUTED"]
	return items


def sort_transactions(ex_items):
	"""Создает список успешных транзакций."""
	ex_items.sort(key=lambda x: x.get('date'), reverse=True)
	return ex_items


def five_items(sort_items):
	"""Оставляет пять транзакций в списке."""
	items = sort_items[:5]
	return items


def time_correct(date):
	"""Переделывает дату."""
	new_date = date.split('T')
	return new_date[0][-2:] + new_date[0][-6:-2] + new_date[0][-10:-6]


def get_from(item):
	"""Кодирует счет отправителя."""
	if item["description"] != "Открытие вклада":
		card = item['from'].split()
		if item['from'].count(' ') > 1:
			return card[0] + card[1] + ' ' + card[2][-16:-12] + ' ' + card[2][-12:-10] + '** ****' + ' ' + card[2][-4:]
		return card[0] + ' ' + card[1][-16:-12] + ' ' + card[1][-12:-10] + '** ****' + ' ' + card[1][-4:]
	return ''