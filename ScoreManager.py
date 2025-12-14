class ScoreManager:
    def __init__(self):
        self.__perfect = 0
        self.__good = 0
        self.__miss = 0

    def add_perfect(self):
        self.__perfect += 1

    def add_good(self):
        self.__good += 1

    def add_miss(self):
        self.__miss += 1

    def get_stats(self):
        return self.__perfect, self.__good, self.__miss
