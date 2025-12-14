class Player:
    def __init__(self):
        self.__score = 0
        self.__combo = 0

    def add_score(self, value):
        self.__score += value
        self.__combo += 1

    def reset_combo(self):
        self.__combo = 0

    def get_score(self):
        return self.__score

    def get_combo(self):
        return self.__combo
