class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            print(f"[INFO] {cls.__name__} синглтон был создан : {hex(id(cls._instance))}")

        # Вывод идентификатора экземпляра (для проверки)
        print(f"[INFO] {cls.__name__} синглтон был возвращён : {hex(id(cls._instance))}")

        return cls._instance
