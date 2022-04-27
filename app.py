from flask import Flask, request  # дока фласка: https://flask.palletsprojects.com/en/2.1.x/
from Answers import *
from DataBaseManager import Manager

# Создаём экземпляр класса Flask для управления фреймворком.
app = Flask(__name__)

# Возможные ответы пользователя и их синонимы.
questions = {
    "о навыке": ["для чего ты", "кто ты", "что умеешь", "что", "о навыке"]
}


# Отправляем пост-запрос на сервер, с целью отображения контента.
# За это отвечает декоратор
@app.route("/alice", methods=["POST"])
def main_controller():
    req = request.json.get("request", {}).get("command")  # получаем текст, напечатанный пользователем

    # Документацию к запросам и ответам найдёшь на https://yandex.ru/dev/dialogs/alice/doc/
    resp = Answers.empty()
    # Если текст, введённый пользователем, совпадает с вариантом ответа или его синонимами, то присваеваем переменнной
    # с ответом соответствующий json файл.
    if req in questions["о навыке"]:
        resp = Answers.hello()  # Вызываем метод hello(), возвращающий нам ответ-приветствие.
    return resp  # отправляем ответ пользователю


app.run("0.0.0.0", port=5000, debug=True)  # запускаем веб-приложение

