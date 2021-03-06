class Answers:

    """Этот класс хранит в себе все возможные ответы нашего приложения пользователю."""

    @staticmethod  # Этот декоратор делает метод статическим, т.е. его можно вызывать без экземпляра класса.
    def hello():
        """Приветствие."""
        resp = {
            "response": {
                "text": "Приветствую! Это мой новый навык, который позволит вам окунуться "
                        "в мир невероятных фэнтезийных приключений. Если захочешь продолжить, "
                        "скажи мне.",
                "tts":  "Приветствую! Это мой новый навык, который позволит вам окунуться "
                        "в мир невероятных фэнтезийных приключений. Если захочешь продолжить, "
                        "скажи мне.",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp  # отправляем ответ сервера
    
    @staticmethod
    def help():
        resp = {
            "response": {
                "text": "Вижу,тебе нужна помощь, верно? В управлении навыком нет ничего сложного: говори коротко и "
                        "выкладывай всю суть, чтобы я тебя смог понять. Что насчёт боя, вы должны назвать вид атаки и "
                        "противника, по которому хотите нанести удар. В случае с уклонением и излечением - просто назовите "
                        "действие. Надеюсь, я вам помог.",
                "tts":  "Вижу,тебе нужна помощь, верно? В управлении навыком нет ничего сложного: говори коротко и "
                        "выкладывай всю суть, чтобы я тебя смог понять. Что насчёт боя, вы должны назвать вид атаки и "
                        "противника, по которому хотите нанести удар. В случае с уклонением и излечением - просто назовите "
                        "действие. Надеюсь, я вам помог.",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp  # отправляем ответ сервера

    @staticmethod
    def empty():
        """Пустой ответ."""
        resp = {
            "response": {
                "text": "",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp

    @staticmethod
    def intro():
        resp = {
            "response": {
                "text": "Холодный январь, ветер и снег. По просёлочной дороге, устало склонив голову, идёт закутанная в "
                        "темный плащ фигура странника с мечом на поясе и легкой сумкой за спиной - вы. Который день "
                        "перебирая ноги, полностью погрузившись в свои мысли, она движется в единственном направлении. "
                        "Напрямую в город, именуемый Летрен. Однако, прямо сейчас, когда вьюга неугомонно силится, "
                        "а ноги через раз следуют командам мозга, будет лучше спрятаться и отдохнуть - подсказывают "
                        "вам опыт да и банальный здравый смысл.\n\n"
                        "Итак, что же вы сделаете: сойдёте с дороги или же продолжите путь?",
                "tts": "Холодный январь, ветер и снег. По просёлочной дороге, устало склонив голову, идёт закутанная в "
                        "темный плащ фигура странника с мечом на поясе и легкой сумкой за спиной - вы. Который день "
                        "перебирая ноги, полностью погрузившись в свои мысли, она движется в единственном направлении. "
                        "Напрямую в город, именуемый Л+етрен. Однако, прямо сейчас, когда вьюга неугомонно силится, "
                        "а ноги через раз следуют командам мозга, будет лучше спрятаться и отдохнуть - подсказывают "
                        "вам опыт да и банальный здравый смысл.\n\n"
                        "Итак, что же вы сделаете: сойдёте с дороги или же продолжите путь?",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp

    @staticmethod
    def not_heard():
        import random 
        ans = ["Что-что? Я не услышал. Можешь повторить?", "А? Извини, я отвлёкся. Можешь повторить?", "Я не совсем вас понял. "
                "Может, стоит изъясниться как-то иначе?"]
        answ = random.choice(ans)        
        resp = {
            "response": {
                "text": answ,
                "tts": answ,
                "end_session": False
            },
            "version": "1.0"
        }
        return resp

    @staticmethod
    def bye():
        resp = {
            "response": {
                "text": "До новых встреч!",
                "tts":  "До новых встреч!",
                "end_session": True
            },
            "version": "1.0"
        }
        return resp
        
    @staticmethod
    def about_skill():
        resp = {
            "response": {
                "text": "Правила и прочая фигня",
                "tts": "",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
    
    @staticmethod
    def roadside_change():
        resp = {
            "response": {
                "text": "Приняв сторону здравого смысла, вы неспеша отходите в сторону и аккуратно спускаетесь в кювет, " 
                        "усаживаетесь меж корней толстого дуба и наконец можете спокойно вздохнуть. Да - здесь куда менее холодно, "
                        "чем на открытой дороге, хоть ветер и воет так, что неслышно собственных мыслей. Вам хочется есть, но вы знаете, "
                        "что в вашей сумке еды нет. Вам хочется спать, но спать в такой холод - опасно. Как удачно, что за спиной, в "
                        "багаже, у вас должно быть всё необходимое.\n\n"
                        "Теперь вы можете либо открыть сумку, либо не предпринимать никаких действий.",
                "tts":  "Приняв сторону здравого смысла, вы неспеша отходите в сторону и аккуратно спускаетесь в кювет, " 
                        "усаживаетесь меж корней толстого дуба и наконец можете спокойно вздохнуть. Да - здесь куда менее холодно, "
                        "чем на открытой дороге, хоть ветер и воет так, что неслышно собственных мыслей. Вам хочется есть, но вы знаете, "
                        "что в вашей сумке еды нет. Вам хочется спать, но спать в такой холод - опасно. Как удачно, что за спиной, в "
                        "багаже, у вас должно быть всё необходимое.\n\n"
                        "Теперь вы можете либо открыть сумку, либо не предпринимать никаких действий.",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
    
    @staticmethod
    def deathroad_change():
        import random
        ans = ["Хм-м-м, честно сказать, я ожидал от вас чего-то большего. Может повезёт в следующий раз? Скажите мне, если "
               "хотите повторить попытку.", "Да уж. Не самая лучшая партия... Быть может, вы хотите попробовать ещё раз? Скажите мне, "
               "если захотите начать новую игру.", "Не думал, что всё может кончиться вот так. Думаю, вам следует попробовать снова. "
               "Скажите мне, если захотите попробовать ещё раз."]
        answ = random.choice(ans)
        resp = {
            "response": {
                "text": "Решив остаться на дороге, в какой-то момент, вы понимаете, это - конец. Ноги не послушают уже никаких ваших " 
                        "команд, да и сил на простой поворот - даже тех не осталось. Вы спотыкаетесь, и обжигающе холодный снег терпит удар вашего "
                        "лица, пока белая пелена застилает взор раз и навсегда...\n\n\n\n"+answ,
                "tts":  "Решив остаться на дороге, в какой-то момент, вы понимаете, это - конец. Ноги не послушают уже никаких ваших " 
                        "команд, да и сил на простой поворот - даже тех не осталось. Вы спотыкаетесь, и обжигающе холодный снег терпит удар вашего "
                        "лица, пока белая пелена застилает взор раз и навсегда...\n\n\n\n"+answ,
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
    
    @staticmethod
    def roadside_death():
        import random
        ans = ["Хм-м-м, честно сказать, я ожидал от вас чего-то большего. Может повезёт в следующий раз? Скажите мне, если "
               "хотите повторить попытку.", "Да уж. Не самая лучшая партия... Быть может, вы хотите попробовать ещё раз? Скажите мне, "
               "если захотите начать новую игру.", "Не думал, что всё может кончиться вот так. Думаю, вам следует попробовать снова. "
               "Скажите мне, если захотите попробовать ещё раз."]
        answ = ans.random.choice(ans)
        resp = {
            "response": {
                "text": "Впрочем, к чему это беспокойство? Как может навредить вашему могучему и закалённому странствиями телу "
                        "какая-то замёрзшая вода. Бездействие - тоже действие. И вскоре, белая пелена раз и навсегда застилает "
                        "ваш, уже ни на чём не сфокусированный, взор...\n\n\n\n"+answ,
                "tts": "Впрочем, к чему это беспокойство? Как может навредить вашему могучему и закалённому странствиями телу "
                        "какая-то замёрзшая вода. Бездействие - тоже действие. И вскоре, белая пелена раз и навсегда застилает "
                        "ваш, уже ни на чём не сфокусированный, взор...\n\n\n\n"+answ,
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
        
    @staticmethod
    def open_bag_change():
        resp = {
            "response": {
                "text": "Вы снимаете с плеча мешок, кладёте тот перед собой и заглядывайте внутрь. Внутри - всего навсего небольшой "
                        "кошель с горсткой монет, пара сухих брёвен, кусочек угля, да ткань, обрывок какого-то дорогого и наверняка "
                        "тёплого плаща, найденный вами на дороге не так давно. Вот и все ваши пожитки, к сожалению. А руки, тем временем, " 
                        "мёрзнут.\n\n"
                        "Сейчас вы можете сделать следующее: разжечь костёр, обернуть руки тканью или же ничего не делать.",
                "tts": "Вы снимаете с плеча мешок, кладёте тот перед собой и заглядывайте внутрь. Внутри - всего навсего небольшой "
                        "кошель с горсткой монет, пара сухих брёвен, кусочек угля, да ткань, обрывок какого-то дорогого и наверняка "
                        "тёплого плаща, найденный вами на дороге не так давно. Вот и все ваши пожитки, к сожалению. А руки, тем временем, " 
                        "мёрзнут.\n\n"
                        "Сейчас вы можете сделать следующее: разжечь костёр, обернуть руки тканью или же ничего не делать.",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
    
    @staticmethod
    def make_fire():
        resp = {
            "response": {
                "text": "Скоро, в вашу голову приходит светлая мысль - зажечь огонь. Вы расчищаете от снега небольшое углубление перед "
                        "своими ногами, кладёте туда брёвнышки, взятые из мешка, в центр кладёте кусочек угла, который достали оттуда же, "
                        "и щелчком пальцев зажигаете яркое алое пламя. Тёплое и приятное, так и клонящее вас в спасительный от этой грохочущей вьюги сон.",
                "tts":  "Скоро, в вашу голову приходит светлая мысль - зажечь огонь. Вы расчищаете от снега небольшое углубление перед "
                        "своими ногами, кладёте туда брёвнышки, взятые из мешка, в центр кладёте кусочек угла, который достали оттуда же, "
                        "и щелчком пальцев зажигаете яркое алое пламя. Тёплое и приятное, так и клонящее вас в спасительный от этой грохочущей вьюги сон.",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
        
    @staticmethod
    def wrap_hands():
        resp = {
            "response": {
                "text": "Вы решаете взять в руки кусок плаща. Тёплый и мягкий, он вскоре заставляет вас снова почувствовать собственные пальцы."
                        "Этот факт радует, а приятный на ощупь обрывок качественной шкуры так и клонит в, спасительный от этой грохочущей вьюги, сон.",
                "tts": "Вы решаете взять в руки кусок плаща. Тёплый и мягкий, он вскоре заставляет вас снова почувствовать собственные пальцы."
                        "Этот факт радует, а приятный на ощупь обрывок качественной шкуры так и клонит в спасительный от этой грохочущей вьюги сон.",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
    
    @staticmethod
    def wake_up():
        resp = {
            "response": {
                "text": "Ваше утро началось с... Боли. Удар чем то тяжёлым и твёрдым пришёлся ровно по голове, посылая болезненный электрический импульс"
                        "по телу и ни давая вам даже малейшего мгновения встать на ноги. Вы слышали про бандитов на этих дорогах, но были уверены, что" 
                        "кучи снега надёжно спрячут вас от всяких недоброжелателей. Видимо, нет. В любом случае, вы всё ещё в сознании - слышите как противник" 
                        "обыскивает вашу сумку. Сбережения у вас скудные, впрочем они есть. И вы можете либо встать и защищать их, либо притвориться мёртвым и" 
                        "лишится необходимости проливать кровь.",
                "tts": "Ваше утро началось с... Боли. Удар чем то тяжёлым и твёрдым пришёлся ровно по голове, посылая болезненный электрический импульс"
                        "по телу и ни давая вам даже малейшего мгновения встать на ноги. Вы слышали про бандитов на этих дорогах, но были уверены, что" 
                        "кучи снега надёжно спрячут вас от всяких недоброжелателей. Видимо, нет. В любом случае, вы всё ещё в сознании - слышите как противник" 
                        "обыскивает вашу сумку. Сбережения у вас скудные, впрочем они есть. И вы можете либо встать и защищать их, либо притвориться мёртвым и" 
                        "лишится необходимости проливать кровь.",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
     
    @staticmethod
    def do_nothing():
        resp = {
            "response": {
                "text": "Вы бездействуете, и противник скоро уходит. Поднимаясь на ноги, вы радуетесь тому, что все"
                        "деньги у вас забрали, ну хоть клинок, спрятанный за поясом, вам оставили.",
                "tts": "",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
    
    @staticmethod
    def fight():
        resp = {
            "response": {
                "text": "Вы поднимаетесь на ноги и туту же встречаете ошарашенные взгляды бандитов, направленные на вас." 
                        "Достаёте из-за пояса меч, готовясь карать врага сталью; складываете пальцы в причудливую форму," 
                        "набираясь решимости жечь их магическим огнём. Всего перед вами два мужчины: с дубинкой, которую" 
                        "помнит ваш затылок, и с луком. Изо рта первого вырывается:\n-Какого чёрта?! - и вы начинаете сражение.",
                "tts":  "Вы поднимаетесь на ноги и туту же встречаете ошарашенные взгляды бандитов, направленные на вас." 
                        "Достаёте из-за пояса меч, готовясь карать врага сталью; складываете пальцы в причудливую форму," 
                        "набираясь решимости жечь их магическим огнём. Всего перед вами два мужчины: с дубинкой, которую" 
                        "помнит ваш затылок, и с луком. Изо рта первого вырывается:\n-Какого чёрта?! - и вы начинаете сражение.",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
    
    @staticmethod
    def fight_death():
        resp = {
            "response": {
                "text": "Ситуация складывается не в вашу пользу, и холодная сталь поражает вас в живот. По коже пробегает волна как" 
                        "никогда резких мурашек, на языке проступает металлический привкус. Вы чувствуете холод...",
                "tts": "Ситуация складывается не в вашу пользу, и холодная сталь поражает вас в живот. По коже пробегает волна как" 
                        "никогда резких мурашек, на языке проступает металлический привкус. Вы чувствуете холод...",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp
     
    @staticmethod
    def fight_status(user):
        from DataBaseManager import Manager
        from Intents import Intents
        player_hp = Manager.get_value("PlayerHp", user)[0][0]  # здоровье игрока
        player_chance = Manager.get_value("Attack_evasion", user)[0][0]  # шанс уклонения и атаки 
        enemies = Manager.get_value("Enemies", user)[0][0].split(" ")  # здоровье текущих противников
        medkits = Manager.get_value("Inventory", user)[0][0].split(" ")[1]  # кол-во хилок в инвентаре
        enemies_hp = ", ".join([f"{i+1}. бандит: {enemies[i]} оч. здоровья" for i in range(len(enemies))])  # текущие противники и их здоровье 
        # print(player_hp,  player_chance,  enemies_hp, medkits)
        resp = {
            "response": {
                "text": "⚔ВЫ НАХОДИТЕСЬ В СТАТУСЕ БИТВЫ🛡\n\n\n"
                        f"Противники: {enemies_hp}.\n"
                        f"❤Ваше здоровье❤: {player_hp} очков.\n"
                        f"✔Ваш шанс на уклонение и атаку❌: {player_chance}%.\n"
                        f"💊Кол-во восстанавливающих препаратов💊: {medkits} штук.\n\n\n"
                        "Действия: уклонение, атака мечом, атака магией, лечение.",
                "tts": "",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp