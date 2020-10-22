#! /usr/bin/env python3

import sqlite3

# Превращает sql запросы в словарь, вместо дефолтного списка
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Удобная обертка для выполнения sql запросов
def sql_request(sql):
	rezult = []

	conn = sqlite3.connect('db.sqlite')
	conn.row_factory = dict_factory

	cursor = conn.cursor()

	cursor.execute(sql)
	for i in cursor.fetchall():
		rezult.append(i)
	conn.commit()
	conn.close()
	return rezult

if __name__ == '__main__':
	a = sql_request("SELECT * FROM data")
	print(a)
	# [
	# {
	#	'username': 'test_user', 
	#	'sha256_password': '10a6e6cc8311a3e2bcc09bf6c199adecd5dd59408c343e926b129c4914f3cb01', 
	#	'API_KEY': 'example_api_key', 
	#	'phone': '74564565454'
	# }
	# ]

	# Проходимся по каждой записи
	for row in a:
		# Выводим интересующие нас поля
		print(row['username']) # test_user
		print(row['sha256_password']) # 10a6e6cc8311a3e2bcc09bf6c199adecd5dd59408c343e926b129c4914f3cb01
		# и тд

