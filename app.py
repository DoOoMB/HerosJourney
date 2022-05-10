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
            Manager.set_value("StoryStage", 6, user)
            return Answers.roadside_change()
        elif req in Intents.que_ans["первый выбор"]["второй"]:
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
            Manager.set_value("StoryStage", 23, user) #############
            inventory = Manager.get_value("Inventory", user)[0][0].split(" ")
            inventory[0] = "0"
            inventory[2] = "0"
            Manager.set_value("Inventory", " ".join(inventory), user)
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
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["битва"]["статус"]:
            return Answers.fight_status(user)
        elif req in Intents.que_ans["битва"]["уклонение"]:
            return fights(user, req, "уклонение")
        elif req in Intents.que_ans["битва"]["лечение"]:
            return fights(user, req, "лечение")
        elif req in Intents.que_ans["битва"]["атака магией"]:
             return fights(user, req, "атака магией")
        else: 
            for i in Intents.que_ans["битва"]["атака мечом"]:
                if i in req:
                    return fights(user, req, "меч")
            
            return Answers.not_heard()
    
    elif stage[0][0] == 20:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        else: Answers.not_heard()
       
    # первая победа в бою (продолжить)
    elif stage[0][0] == 22:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["продолжить (повествование)"]:
            Manager.set_value("StoryStage", 24, user)
            return Answers.next_dialog()
        else: Answers.not_heard()
     
    # первая победа в бою
    elif stage[0][0] == 21: 
        Manager.set_value("StoryStage", 22, user)
        return Answers.first_victory()
    
    # рассказ о королеве
    elif stage[0][0] == 23:
        Manager.set_value("StoryStage", 24, user)
        return Answers.next_dialog()
    
    elif stage[0][0] == 24:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["продолжить (повествование)"]:
            Manager.set_value("StoryStage", 26, user)
            return Answers.fork()
        else: Answers.not_heard()
    
    elif stage[0][0] == 25:
        Manager.set_value("StoryStage", 26, user)
        return Answers.fork()
    
    elif stage[0][0] == 26:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["развилка"]["к домам"]:
            if Manager.get_value("IsMenace", user)[0][0] == 0:
                Manager.set_value("StoryStage", 28, user)
                return Answers.houses_first()
            else: return Answers.houses_menace_true()
        elif req in Intents.que_ans["развилка"]["в таверну"]:          
            Manager.set_value("StoryStage", 30, user)
            return ###
        elif req in Intents.que_ans["развилка"]["в церковь"]:
            Manager.set_value("StoryStage", 32, user)
            return ###
        else: Answers.not_heard()
    
    elif stage[0][0] == 27:
        Manager.set_value("StoryStage", 28, user)
        return Answers.houses_first()
    elif stage[0][0] == 29:
        Manager.set_value("StoryStage", 30, user)
        return ###
    elif stage[0][0] == 31:
        Manager.set_value("StoryStage", 32, user)
        return ###
    
    elif stage[0][0] == 28:
        if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        elif req in Intents.que_ans["дома"]["угроза"]:
            Manager.set_value("StoryStage", 25, user)
            return Answers.houses_menace(user)
        elif req in Intents.que_ans["дома"]["правда"]:
            Manager.set_value("StoryStage", 34, user)
            return Answers.houses_truth()
        else: Answers.not_heard
    
    elif stage[0][0] == 33:
        Manager.set_value("StoryStage", 34, user)
        return Answers.houses_truth()
     
    elif stage[0][0] == 34:
         if req in Intents.que_ans["выход"]:
            return bye(user)
        elif req in Intents.que_ans["о навыке"]:
            return Answers.about_skill()
        elif req in Intents.que_ans["помощь"]:
            return Answers.help()
        elif req in Intents.que_ans["новая игра"]:
            return new_game(user)
        else: 
            Manager.set_value("StoryStage", 36, user)
            return Answers.houses_truth_answer() ######
                     
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
    medkits = Manager.get_value("Inventory", user)[0][0].split(" ")[1]
    player_chance = Manager.get_value("Attack_evasion", user)[0][0]
    enemies = Manager.get_value("Enemies", user)[0][0].split(" ")
    enemy_damage = Manager.get_value("EnemyDamage", user)[0][0].split(" ")
    num = random.randint(1, 100)
    if action == "меч":
        if player_hp <= 0:
            Manager.set_value("StoryStage", 20, user)
            return Answers.fight_death()
        else:
            res = 0 
            for i in enemies:
                if int(i) <= 0: res += 1
            if res == len(enemies):
                Manager.set_value("StoryStage", 22, user)
                reset_fight(user)
                return Answers.first_victory()
        for i in range(len(enemies)):
            for j in Intents.que_ans["битва"]["№противника"][i+1]:
                print(j, req)
                if j in req:
                    if num <= player_chance:
                        damage = random.randint(15, 30)
                        if int(enemies[i]) >= 0:
                            enemies[i] = str(int(enemies[i]) - damage)                           
                        else: 
                            enemies[i] = "0"
                        Manager.set_value("Enemies", " ".join(enemies), user)
                        return Answers.success_attack(damage)                       
                    else:
                        damage = random.randint(int(enemy_damage[0]), int(enemy_damage[1]))
                        Manager.set_value("PlayerHp", player_hp - damage, user)                        
                        return Answers.player_damage(damage)
    elif action == "уклонение":
        if player_hp <= 0:
            Manager.set_value("StoryStage", 20, user)
            return Answers.fight_death()
        else:
            res = 0 
            for i in enemies:
                if int(i) <= 0: res += 1
            if res == len(enemies):
                Manager.set_value("StoryStage", 22, user)
                reset_fight(user)
                return Answers.first_victory()
        if num <= player_chance:
            return Answers.success_attack(damage)           
        else:
            damage = random.randint(int(enemy_damage[0]), int(enemy_damage[1]))
            Manager.set_value("PlayerHp", player_hp - damage, user)                        
            return Answers.player_damage(damage)
    elif action == "атака магией":
        if player_hp <= 0:
            Manager.set_value("StoryStage", 20, user)
            return Answers.fight_death()
        else:
            res = 0 
            for i in enemies:
                if int(i) <= 0: res += 1
            if res == len(enemies):
                Manager.set_value("StoryStage", 22, user)
                reset_fight(user)
                return Answers.first_victory()
        if num <= player_chance:
            damage_killer = random.randint(2, 5)
            new_damage = int(enemy_damage[1])-damage_killer 
            if new_damage >= 10:                         
                Manager.set_value("EnemyDamage", f"10 {new_damage}", user)
                return Answers.success_magical_attack(damage_killer)
            else: Manager.set_value("EnemyDamage", f"10 10", user)
            return Answers.success_magical_attack(int(enemy_damage[1])-10)                   
        else:                       
            damage = random.randint(int(enemy_damage[0]), int(enemy_damage[1]))
            Manager.set_value("PlayerHp", player_hp - damage, user)                        
            return Answers.player_damage(damage)

    if action == "лечение" and int(medkits) > 0:
        if (player_hp + 50) > 100:
            Manager.set_value("PlayerHp", 100, user)
        else: Manager.set_value("PlayerHp", player_hp+50, user)
    else: return Answers.haveNot_medkits()    
  
    
    
            
                
        
        
        
    return Answers.not_heard()
        
    

@app.route("/alice", methods=["POST"])
def post(resp):
    print("post")
    return resp
    
def reset_fight(user):
    Manager.set_value("Enemies", "", user)
    Manager.set_value("PlayerHp", 100, user)
    Manager.set_value("EnemyDamage", "10 20", user)
