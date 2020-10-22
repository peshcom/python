#! /usr/bin/env python3

import flask

import sms
import config

app = flask.Flask(
	__name__,
	static_folder='static/',
	template_folder='templates/'
)

@app.route("/")
def login():
	return flask.render_template('login.html', brand="Peshcom")

@app.route("/auth", methods=['GET'])
def auth():
	username = flask.request.args['username']
	print(username)

	# Тут какие то действия, 
	# запросы к БД
	# Подсчет хэша полученного пароля
	# Сверка с паролем в БД
	# Сверка юзернеймов

	# Если проверка успешно, то запоминаем пользователя
	flask.session['username'] = flask.request.args['username']

	# Получение API_KEY

	# Получение номера телефона

	# Если все успешно, переводим пользователя на страницу, где он может отправить смс-ку
	return flask.redirect('/app')

@app.route("/app")
def index():
	# Здесь добавить проверку, а пользователь уже авторизован?
	# Если нет, то перенаправить на страницу авторизации

	# Если все в порядке, то отдаем страницу для отправки смс-ок
	return flask.render_template('index.html', brand="Peshcom", username='Вы зашли как {}'.format(flask.escape(flask.session['username'])))

@app.route("/processing", methods=['GET'])
def processing():
	text = flask.request.args['param']
	__sms = sms.sms_class(config.api, config.phone)
	ret = __sms.send_sms(text.replace(' ', '+'))
	return ret

if __name__ == '__main__':
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(host='0.0.0.0', port=8888, debug=True)