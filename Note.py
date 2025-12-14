from GameObject import GameObject

LANE_X = [100, 200, 300, 400]

class Note(GameObject):
    def __init__(self, y, speed, lane):
        x = LANE_X[lane]
        super().__init__(x, y, speed)
        self.__lane = lane
        self.__is_hit = False

    def update(self):
        self.move()

    def hit(self):
        self.__is_hit = True
        return 100

    def get_lane(self):
        return self.__lane

    def get_y(self):
        return self._y


class SpecialNote(Note):
    def hit(self):
        return 200
