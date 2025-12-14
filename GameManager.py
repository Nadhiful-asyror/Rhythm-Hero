import pygame
from Note import Note
from Player import Player
from ScoreManager import ScoreManager

KEY_LANE = {
    pygame.K_a: 0,
    pygame.K_s: 1,
    pygame.K_d: 2,
    pygame.K_f: 3
}

HIT_LINE_Y = 650
PERFECT_RANGE = 20
GOOD_RANGE = 50

class GameManager:
    def __init__(self, screen):
        self.__screen = screen
        self.__player = Player()
        self.__score_manager = ScoreManager()
        self.__notes = []
        self.__spawn_timer = 0

    def start_game(self):
        self.__notes.clear()

    def spawn_note(self):
        import random
        lane = random.randint(0, 3)
        self.__notes.append(Note(-50, 5, lane))

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_LANE:
                    self.hit_note(KEY_LANE[event.key])
        return True

    def hit_note(self, lane):
        for note in self.__notes:
            if note.get_lane() == lane:
                distance = abs(note.get_y() - HIT_LINE_Y)

                if distance <= PERFECT_RANGE:
                    self.__player.add_score(300)
                    self.__score_manager.add_perfect()
                elif distance <= GOOD_RANGE:
                    self.__player.add_score(100)
                    self.__score_manager.add_good()
                else:
                    self.__player.reset_combo()
                    self.__score_manager.add_miss()

                self.__notes.remove(note)
                break

    def update_game(self):
        self.__spawn_timer += 1
        if self.__spawn_timer >= 60:
            self.spawn_note()
            self.__spawn_timer = 0

        for note in self.__notes[:]:
            note.update()
            note.draw(self.__screen)

            if note.get_y() > 750:
                self.__notes.remove(note)
                self.__player.reset_combo()
                self.__score_manager.add_miss()

    def draw_ui(self):
        font = pygame.font.SysFont(None, 30)
        score = font.render(f"Score: {self.__player.get_score()}", True, (255,255,255))
        combo = font.render(f"Combo: {self.__player.get_combo()}", True, (255,255,0))
        self.__screen.blit(score, (10, 10))
        self.__screen.blit(combo, (10, 40))

        for x in [100, 200, 300, 400]:
            pygame.draw.line(self.__screen, (100,100,100), (x+30, 0), (x+30, 800))

        pygame.draw.line(self.__screen, (255,0,0), (0, HIT_LINE_Y), (600, HIT_LINE_Y))
