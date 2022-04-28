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
    def new_player():
        resp = {
            "response": {
                "text": "Я вижу, ты у нас новенький. Верно? Чтож, тогда тебе объяснить правила?",
                "buttons": [
                    {
                        "title": "Я уже смешарик!",
                        "hide": True
                    },
                    {
                        "title": "Выкладывай!",
                        "hide": True
                    }
                            ],
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
                        "вам опыт да и банальный здравый смысл.",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp

    @staticmethod
    def new_game():
        resp = {
            "response": {
                "text": "Ааа! Новая игра. С чистого листа. Ну, чтож, продолжим!",
                "end_session": False
            },
            "version": "1.0"
        }
        return resp

    @staticmethod
    def not_heard():
        resp = {
            "response": {
                "text": "Что-что? Я не услышал. Можешь повторить?",
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
                "end_session": True
            },
            "version": "1.0"
        }
        return resp