#! /usr/bin/env python3

import flask

app = flask.Flask(
	__name__,
	static_folder='static/',
	template_folder='templates/'
)

# С этой страницы начинается знакомство с сайтом. Она откроется первой
@app.route("/")
def index():
	# говорим отрендерь шаблон
	return flask.render_template('index.html', brand="peshcom") # передаю переменню brand. смотри в index.html как ее вставить в html код

# При отправке запроса на URL http://0.0.0.0:8888/test_url/какой_либо_текст_сюда
# переменная text будет содержать "какой_либо_текст_сюда"
# далее с ней можно будет работать
@app.route("/test_url/<text>")
def test_url(text):
	print(text)
	return "Это test_url!!!"

# Или можем передавать с помощью GET запроса
# при отправке запроса на http://127.0.0.1:8888/processing?param=value
@app.route("/processing", methods=['GET'])
def processing():
	# выведет "value"
	print(flask.request.args['param'])
	return "Это processing!!!"


# Запускаем приложение
app.run(host='0.0.0.0', port=8888, debug=True)