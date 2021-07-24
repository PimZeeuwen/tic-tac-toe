import pygame

pygame.init()

screen_with_9_cels = pygame.display.set_mode([600, 600])
pygame.display.set_caption('Tic Tac Toe')

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)


class Cel:
    def __init__(self, value, x_center, y_center):
        self.value = value
        self.x_center = x_center
        self.y_center = y_center

    def draw_cel(self):
        if self.value == 'X':
            pygame.draw.line(screen_with_9_cels, blue, (self.x_center - 75, self.y_center - 75), (self.x_center + 75, self.y_center + 75), 2)
            pygame.draw.line(screen_with_9_cels, blue, (self.x_center - 75, self.y_center + 75), (self.x_center + 75, self.y_center - 75), 2)
        elif self.value == 'O':
            pygame.draw.circle(screen_with_9_cels, black, (self.x_center, self.y_center), 75, 2)


cel_1 = Cel('', 100, 100)
cel_2 = Cel('', 300, 100)
cel_3 = Cel('', 500, 100)

cel_4 = Cel('', 100, 300)
cel_5 = Cel('', 300, 300)
cel_6 = Cel('', 500, 300)

cel_7 = Cel('', 100, 500)
cel_8 = Cel('', 300, 500)
cel_9 = Cel('', 500, 500)



class Board:
    def __init__(self, cel_1, cel_2, cel_3, cel_4, cel_5, cel_6, cel_7, cel_8, cel_9):
        self.cel_1 = cel_1
        self.cel_2 = cel_2
        self.cel_3 = cel_3

        self.cel_4 = cel_4
        self.cel_5 = cel_5
        self.cel_6 = cel_6

        self.cel_7 = cel_7
        self.cel_8 = cel_8
        self.cel_9 = cel_9

        self.won = False
        self.winner = ''

    def draw_screen(self):
        screen_with_9_cels.fill(white)

        pygame.draw.line(screen_with_9_cels, black, (200, 0), (200, 600), 5)
        pygame.draw.line(screen_with_9_cels, black, (400, 0), (400, 600), 5)

        pygame.draw.line(screen_with_9_cels, black, (0, 200), (600, 200), 5)
        pygame.draw.line(screen_with_9_cels, black, (0, 400), (600, 400), 5)

        self.cel_1.draw_cel()
        self.cel_2.draw_cel()
        self.cel_3.draw_cel()

        self.cel_4.draw_cel()
        self.cel_5.draw_cel()
        self.cel_6.draw_cel()

        self.cel_7.draw_cel()
        self.cel_8.draw_cel()
        self.cel_9.draw_cel()

        pygame.display.flip()

    def check_winner(self):
        if self.cel_1 == self.cel_2 == self.cel_3:
            self.won = True
            self.winner = self.cel_1.value

        if self.cel_4 == self.cel_5 == self.cel_6:
            self.won = True
            self.winner = self.cel_4.value

        if self.cel_7 == self.cel_8 == self.cel_9:
            self.won = True
            self.winner = self.cel_7.value

        if self.cel_1 == self.cel_4 == self.cel_7:
            self.won = True
            self.winner = self.cel_1.value

        if self.cel_2 == self.cel_5 == self.cel_8:
            self.won = True
            self.winner = self.cel_2.value

        if self.cel_3 == self.cel_5 == self.cel_9:
            self.won = True
            self.winner = self.cel_3.value

        if self.cel_1 == self.cel_5 == self.cel_9:
            self.won = True
            self.winner = self.cel_5.value

        if self.cel_3 == self.cel_5 == self.cel_7:
            self.won = True
            self.winner = self.cel_5.value

    def clear_screen(self):
        self.cel_1 = ''
        self.cel_2 = ''
        self.cel_3 = ''

        self.cel_4 = ''
        self.cel_5 = ''
        self.cel_6 = ''

        self.cel_7 = ''
        self.cel_8 = ''
        self.cel_9 = ''

        self.won = False
        self.winner = ''

    def draw_screen_won(self):
        screen_with_9_cels.fill(white)

        pygame.draw.line(screen_with_9_cels, black, (200, 0), (200, 600))
        pygame.draw.line(screen_with_9_cels, black, (400, 0), (400, 600))

        pygame.draw.line(screen_with_9_cels, black, (0, 200), (600, 200))
        pygame.draw.line(screen_with_9_cels, black, (0, 400), (600, 400))

        self.cel_1.value = self.winner
        self.cel_2.value = self.winner
        self.cel_3.value = self.winner

        self.cel_1.draw_cel()
        self.cel_2.draw_cel()
        self.cel_3.draw_cel()

        self.cel_4.value = self.winner
        self.cel_5.value = self.winner
        self.cel_6.value = self.winner

        self.cel_4.draw_cel()
        self.cel_5.draw_cel()
        self.cel_6.draw_cel()

        self.cel_7.value = self.winner
        self.cel_8.value = self.winner
        self.cel_9.value = self.winner

        self.cel_7.draw_cel()
        self.cel_8.draw_cel()
        self.cel_9.draw_cel()

        pygame.display.flip()

        self.clear_screen()

    def check_even(self):
        if self.cel_1 != '':
            if self.cel_2 != '':
                if self.cel_3 != '':
                    if self.cel_4 != '':
                        if self.cel_5 != '':
                            if self.cel_6 != '':
                                if self.cel_7 != '':
                                    if self.cel_8 != '':
                                        if self.cel_9 != '':
                                            self.clear_screen


board = Board(cel_1, cel_2, cel_3, cel_4, cel_5, cel_6, cel_7, cel_8, cel_9)

turn = 'X'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            position = list(position)
            if position[1] < 200:
                if position[0] < 200:
                    board.cel_1.value = turn

                elif 200 < position[0] < 400:
                    board.cel_2.value = turn

                elif 400 < position[0]:
                    board.cel_3.value = turn

            elif 200 < position[1] < 400:
                if position[0] < 200:
                    board.cel_4.value = turn

                elif 200 < position[0] < 400:
                    board.cel_5.value = turn

                elif 400 < position[0]:
                    board.cel_6.value = turn

            elif 400 < position[1]:
                if position[0] < 200:
                    board.cel_7.value = turn

                elif 200 < position[0] < 400:
                    board.cel_8.value = turn

                elif 400 < position[0]:
                    board.cel_9.value = turn

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

            board.check_winner()

            if board.won:
                board.draw_screen_won()

            board.check_even()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.draw_screen()
