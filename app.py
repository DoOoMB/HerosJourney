from flask import Flask, request  # дока фласка: https://flask.palletsprojects.com/en/2.1.x/
from Answers import *
from DataBaseManager import Manager
from Intents import Intents

# Создаём экземпляр класса Flask для управления фреймворком.
app = Flask(__name__)


# Отправляем пост-запрос на сервер, с целью отображения контента.
# За это отвечает декоратор
@app.route("/alice", methods=["POST"])
def main_controller():

    req = request.json.get("request", {}).get("command")  # получаем текст, напечатанный пользователем
    user = request.json.get("session", {}).get("user", {}).get("user_id")
    stage = Manager.get_value("StoryStage", user)
    if not Manager.get_value("UserId", user):
        Manager.create_row(user)
        Manager.set_value("StoryStage", 1, user)
        return Answers.hello()
    elif stage[0][0] == 0:
        Manager.set_value("StoryStage", 1, user)
        return Answers.hello()
    elif Manager.get_value("IsComeBack", user)[0][0] == 1:
        if stage[0][0] in Intents.changes:
            Manager.set_value("StoryStage", stage[0][0] - 1, user)
        Manager.set_value("IsComeBack", 0, user)
        return Answers.hello()

    if stage[0][0] == 1:
        if req in Intents.que_ans["продолжить"]:
            Manager.set_value("StoryStage", 3, user)
            return Answers.intro()
        elif req in Intents.que_ans["выход"]:
            Manager.set_value("IsComeBack", 1, user)
            return Answers.bye()
        elif req in Intents.que_ans["о навыке"]:
            return Answers.hello()
        else:
            return Answers.not_heard()

    if stage[0][0] == 2:
        if req in Intents.que_ans["выход"]:
            Manager.set_value("IsComeBack", 1, user)
            return Answers.bye()
        elif req in Intents.que_ans["о навыке"]:
            return Answers.hello()
        Manager.set_value("StoryStage", 3, user)
        return Answers.intro()

    if req in Intents.que_ans["выход"]:
        Manager.set_value("IsComeBack", 1, user)
        return Answers.bye()

    return Answers.empty()


