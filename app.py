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

    # проверка присутствия юзера в бд и проверка на его возвращение
    if not Manager.get_value("UserId", user):
        return new_user(user)
    elif stage[0][0] == 0:
        Manager.set_value("StoryStage", 1, user)
        return Answers.hello()
    elif Manager.get_value("IsComeBack", user)[0][0] == 1:
        Manager.set_value("StoryStage", Intents.changes[stage[0][0]], user)
        Manager.set_value("IsComeBack", 0, user)
        return Answers.hello()

    # "начальный экран"
    if stage[0][0] == 1:
        if req in Intents.que_ans["продолжить"]:
            Manager.set_value("StoryStage", 3, user)
            return Answers.intro()
        elif req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        else:
            return Answers.not_heard()

    # вступление
    elif stage[0][0] == 2:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        Manager.set_value("StoryStage", 3, user)
        return Answers.intro()

    # первый сюжетный выбор    
    elif stage[0][0] == 3:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["первый выбор"]["первый"]:
            Manager.set_value("StoryStage", 6, user)
            return Answers.roadside_change()
        elif req in Intents.que_ans["первый выбор"]["второй"]:
            Manager.set_value("StoryStage", 5, user)
            return Answers.deathroad_change()
        else:
            return Answers.not_heard()

    # вторая сцена
    elif stage[0][0] == 4:
        Manager.set_value("StoryStage", 6, user)
        return Answers.roadside_change()

        # второй сюжетный выбор
    elif stage[0][0] == 6:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["второй выбор"]["второй"]:
            Manager.set_value("StoryStage", 7, user)
            return Answers.roadside_death()
        elif req in Intents.que_ans["второй выбор"]["первый"]:
            Manager.set_value("StoryStage", 9, user)
            return Answers.open_bag_change()
        else:
            return Answers.not_heard()

    # открытие сумки
    elif stage[0][0] == 8:
        Manager.set_value("StoryStage", 9, user)
        return Answers.open_bag_change()

    # третий сюжетный выбор (костёр)
    elif stage[0][0] == 9:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["третий выбор"]["первый"]:
            Manager.set_value("StoryStage", 12, user)
            return Answers.make_fire()
        elif req in Intents.que_ans["третий выбор"]["второй"]:
            Manager.set_value("StoryStage", 14, user)
            return Answers.wrap_hands()
        elif req in Intents.que_ans["третий выбор"]["третий"]:
            Manager.set_value("StoryStage", 7, user)
            return Answers.roadside_death()
        else:
            return Answers.not_heard()

    # зажигаем костёр
    elif stage[0][0] == 11:
        Manager.set_value("StoryStage", 12, user)
        return Answers.make_fire()

    # оборачиваем руки
    elif stage[0][0] == 13:
        Manager.set_value("StoryStage", 14, user)
        return Answers.wrap_hands()

    # Затрещина. Начало 2 главы
    elif stage[0][0] == 14 or stage[0][0] == 12:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["продолжить (повествование)"]:
            Manager.set_value("StoryStage", 16, user)
            return Answers.wake_up()

    elif stage[0][0] == 15:
        Manager.set_value("StoryStage", 16, user)
        return Answers.wake_up()

    elif stage[0][0] == 16:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["пробуждение"]["драка"]:
            Manager.set_value("StoryStage", 17, user)
            return Answers.empty()

    elif stage[0][0] == 17:
        return


    # бездействие (выбор с сумкой)
    elif stage[0][0] == 7:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        else:
            return Answers.not_heard()

    # бездействие (дорога)
    elif stage[0][0] == 5:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        else:
            return Answers.not_heard()

    return Answers.empty()


@app.route("/alice", methods=["POST"])
def bye(user):
    Manager.set_value("IsComeBack", 1, user)
    return Answers.bye()


@app.route("/alice", methods=["POST"])
def new_game(user):
    Manager.set_default(user)
    Manager.create_row(user)
    Manager.set_value("StoryStage", 3, user)
    return Answers.intro()


@app.route("/alice", methods=["POST"])
def new_user(user):
    Manager.create_row(user)
    Manager.set_value("StoryStage", 1, user)
    return Answers.hello()
