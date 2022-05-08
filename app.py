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
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        else:
            return Answers.not_heard()
    
    # вступление
    elif stage[0][0] == 2:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        Manager.set_value("StoryStage", 3, user)
        return Answers.intro()
        
    # первый сюжетный выбор    
    elif stage[0][0] == 3:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["первый выбор"]["первый"]:
            print("первый")
            Manager.set_value("StoryStage", 6, user)
            return Answers.roadside_change()
        elif req in Intents.que_ans["первый выбор"]["второй"]:
            print("второй")
            Manager.set_value("StoryStage", 5, user)
            return Answers.deathroad_change()
        else: return Answers.not_heard()
    
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
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["второй выбор"]["второй"]:
            Manager.set_value("StoryStage", 7, user)
            return Answers.roadside_death()
        elif req in Intents.que_ans["второй выбор"]["первый"]:
            Manager.set_value("StoryStage", 9, user)
            return Answers.open_bag_change()
        else: return Answers.not_heard()
    
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
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
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
        else: return Answers.not_heard()
        
    # растираем руки
    elif stage[0][0] == 13:
        Manager.set_value("StoryStage", 14, user)
        return Answers.wrap_hands()
    
    # зажигаем костёр
    elif stage[0][0] == 11:
        Manager.set_value("StoryStage", 12, user)
        return Answers.make_fire()
    
    # бандиты (пробуждение)
    elif stage[0][0] == 14 or stage[0][0] == 12:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["продолжить (повествование)"]:
            Manager.set_value("StoryStage", 16, user)
            return Answers.wake_up()
        else: return Answers.not_heard()
    
    # бандиты (пробуждение)
    elif stage[0][0] == 15:
        Manager.set_value("StoryStage", 16, user)
        return Answers.wake_up()
        
    elif stage[0][0] == 16:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["четвёртый выбор"]["первый"]:
            Manager.set_value("StoryStage", 18, user)
            return Answers.fight()
        elif req in Intents.que_ans["четвёртый выбор"]["второй"]:
            Manager.set_value("StoryStage", 18, user) #############
            return Answers.do_nothing()
        else: return Answers.not_heard()
    
    elif stage[0][0] == 17:
        Manager.set_value("StoryStage", 18, user)
        return Answers.fight()
    
    elif stage[0][0] == 18:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["продолжить (повествование)"]:
            Manager.set_value("StoryStage", 19, user)
            Manager.set_value("Enemies", "100 100", user)           
            return  Answers.fight_status(user)
        else: return Answers.not_heard()
    
    # битва №1 на дороге
    elif stage[0][0] == 19:
        post(Answers.fight_status(user))
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["битва"]["атака мечом"]:
            fights(user, req, "меч")
        else: Answers.not_heard()
    
    # бездействие (выбор с сумкой)
    elif stage[0][0] == 7:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        else: return Answers.not_heard()
    
    # бездействие (дорога)
    elif stage[0][0] == 5:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        else: return Answers.not_heard()
        
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

@app.route("/alice",methods=["POST"])
def new_user(user):
    Manager.create_row(user)
    Manager.set_value("StoryStage", 1, user)
    return Answers.hello()

@app.route("/alice", methods=["POST"])
def fights(user, req, action):
    import random
    player_hp = Manager.get_value("PlayerHp", user)[0][0]
    player_chance = Manager.get_value("Attack_evasion", user)[0][0]
    enemies = Manager.get_value("Enemies", user)[0][0].split(" ")
    num = random.randint(1, 100)
    if action == "меч":
        for i in range(len(enemies)):
            for j in Intents.que_ans["№противника"][i]:
                if j in req:
                    if num <= player_chance:
                        enemies[i] == str(int(enemies[i]) - random.randint(15, 30))
                        print(enemies)
                    
        
    

@app.route("/alice", methods=["POST"])
def post(resp):
    return resp
    

