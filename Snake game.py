import pygame
import random
 
pygame.init()
# Declaring variables
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128,128,128)
blue = (13,115,183)
red = (255,102,102)
display_width = 700
display_height = 400
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Umayr Snake Game')
clock = pygame.time.Clock()
snake_square = 10
snake_speed = 10
font = pygame.font.SysFont("centurygothic", 20)
score_font = pygame.font.SysFont("centurygothic", 20)

# End of game message
def message(msg, white):
    mesg = font.render(msg, True, white)
    display.blit(mesg, [display_width / 100, display_height / 3])

# Points message
def points(points):
    value = score_font.render("Points: " + str(points), True, white)
    display.blit(value, [0, 0])

# snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, white, [x[0], x[1], snake_block, snake_block])


def gameloop():
    game_over = False
    game_close = False
 
    x1 = display_width / 2
    y1 = display_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    food_width = round(random.randrange(0, display_width - snake_square) / 10.0) * 10.0
    food_length = round(random.randrange(0, display_height - snake_square) / 10.0) * 10.0
 
    while not game_over:
 # When the game is lost
        while game_close == True:
            display.fill(black)
            message("You Lost! Press enter to play again or space to leave the game", white)
            points(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # When the user presses the space key it exits the game
                    if event.key == pygame.K_SPACE:
                        game_over = True
                        game_close = False
                    # When the user presses the enter key it restarts the game
                    if event.key == pygame.K_RETURN:
                        gameloop()
# User controls for the snake in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_square
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_square
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_square
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_square
                    x1_change = 0
 # If the user hits the boundaries the game will end and bring the user to the end screen
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            display.fill(red)
            pygame.display.update()
            clock.tick(snake_speed)
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(black)
# creating food rectangle
        pygame.draw.rect(display, gray, [food_width, food_length, snake_square, snake_square])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

 
        snake(snake_square, snake_List)
        points(Length_of_snake - 1)

        pygame.display.update()
 # when snake meets the food the screen turns blue and the food is relocated adding the score by one and adding onto the snake
        if x1 == food_width and y1 == food_length:
            display.fill(blue)
            food_width = round(random.randrange(0, display_width - snake_square) / 10.0) * 10.0
            food_length = round(random.randrange(0, display_height - snake_square) / 10.0) * 10.0
            Length_of_snake += 1
            pygame.display.update()
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameloop()