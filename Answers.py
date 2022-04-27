class Answers:

    """Этот класс хранит в себе все возможные ответы нашего приложения пользователю."""

    @staticmethod  # Этот декоратор делает метод статическим, т.е. его можно вызывать без экземпляра класса.
    def hello():
        """Приветствие."""
        resp = {
            "response": {
                "text": "Приветствую! Это мой новый навык, который позволит вам окунуться "
                        "в мир невероятных фэнтезийных приключений.",
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