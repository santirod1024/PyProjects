import random
import pygame
import time

'''
HIT BOX needs to be fixed, using rectangle hit boxes for circles and triangles
leaderboard is halfway developed but not complete
music could use better mixing
'''

# initialize font and sound
pygame.font.init()
pygame.init()
pygame.mixer.init()


# initializing game window
WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# setting up background
BG = pygame.transform.scale(pygame.image.load("bgg.jpeg"), (WIDTH, HEIGHT))
GOBG = pygame.transform.scale(pygame.image.load("gameoverr.jpeg"), (WIDTH, HEIGHT))
# player dimension and speed
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 8

# Load sound and create empty explosion list
EXPLOSION_SOUND = pygame.mixer.Sound('explosion.wav')
explosions = []
THEME = pygame.mixer.Sound('song.wav')
gameover_song = pygame.mixer.Sound('gameover_song.wav')
highscore_song = pygame.mixer.Sound('highscore_song.mp3')

# obstacle dimension and speed
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 4

hit_count = 0
gameover = False

FONT = pygame.font.SysFont("arial", 25)


def main_screen():
    start = False
    while not start:
        WIN.fill("black")
        welcome_text = FONT.render("WELCOME TO SPACE DODGE", True, "white")
        instruction_text = FONT.render("Press Y to start", True, "white")

        # calculate the x positions for center alignment
        welcome_x = (WIDTH - welcome_text.get_width()) // 2
        instruction_x = (WIDTH - instruction_text.get_width()) // 2

        # y position for vertical spacing
        welcome_y = HEIGHT // 2 - welcome_text.get_height()
        instruction_y = HEIGHT // 2

        # Blit them onto the screen
        WIN.blit(welcome_text, (welcome_x, welcome_y))
        WIN.blit(instruction_text, (instruction_x, instruction_y))

        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    start = True


LEADERBOARD_FILE = 'leaderboard.txt'
MAX_SCORES = 10  # for top 10 scores


def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            scores = [line.strip().split(",") for line in f.readlines()]
            scores = [(name, int(score)) for name, score in scores]
            return scores

    except FileNotFoundError:
        return[]


def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, 'w') as f:
        for name, score in leaderboard:
            f.write(f"{name},{score}\n")


def update_leaderboard(name, score):
    leaderboard = load_leaderboard()
    leaderboard.append((name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)  # assuming higher scores are better
    leaderboard = leaderboard[:MAX_SCORES]  # keep only top scores
    save_leaderboard(leaderboard)


def display_leaderboard():
    leaderboard = load_leaderboard()
    for i, (name, score) in enumerate(leaderboard):
        score_text = FONT.render(f"{i +1}. {name}. {score}", True, "white")
        WIN.blit(score_text, (WIDTH // 4 - score_text.get_width() // 2, HEIGHT / 2))


def get_player_name():
    input_box = pygame.Rect(WIDTH // 4, HEIGHT // 2, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input box
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
    # Draw the text.
    WIN.blit(txt_surface, (input_box.x+5, input_box.y+5))
    # Blit the input box rect.
    pygame.draw.rect(WIN, color, input_box, 2)

    pygame.display.flip()
    clock.tick(30)

def gameover_screen():
    run = True
    while run:
        WIN.blit(GOBG, (0, 0))
        restart_text = FONT.render("Press 'R' to Restart or 'Q' to Quit", True, "white")
        WIN.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT / 2 - 10))
        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # restart the game
                    gameover_song.stop()
                    main()
                if event.key == pygame.K_q:  # quit the game
                    run = False
                    pygame.quit()
            else:
                continue


# function to call the 'player' triangle
def draw_triangle(surface, color, position, size):
    x, y = position
    points = [(x, y - size // 2), (x - size // 2, y + size // 2), (x + size // 2, y + size // 2)]
    pygame.draw.polygon(surface, color, points)


def draw(player1, player2, elapsed_time, stars, hit_count, gameover, explosions):

    WIN.blit(BG, (0, 0))  # window
    pygame.draw.line(WIN, (255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)  # screen divider

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", True, "white")  # time
    WIN.blit(time_text, (10, 10))

    hit_text = FONT.render(str(hit_count) + " hits", True, "white")  # hits
    WIN.blit(hit_text, (25, 40))

    draw_triangle(WIN, "light blue", (player1.x, player1.y), PLAYER_WIDTH)
    draw_triangle(WIN, "light green", (player2.x, player2.y), PLAYER_WIDTH)

    # reiterates through a loop creating a red circle that gets bigger with each iteration until it reaches 50
    for explosion in explosions[:]:  # iterate over a copy of the list
        pygame.draw.circle(WIN, "red", explosion["pos"], explosion["size"])
        explosion["size"] += explosion["rate"]
        if explosion["size"] > 50:  # maximum size of an explosion
            explosions.remove(explosion)

    for star in stars:
        pygame.draw.circle(WIN, "magenta",
        (random.randint(star.x, star.x + star.width), random.randint(star.y, star.y + star.height)), 18)
    pygame.display.update()

    if gameover:
        gameover_text = FONT.render("Game over! Time: " + str(round(elapsed_time)) + "s", True, "white")
        WIN.blit(gameover_text, (WIDTH // 2 - gameover_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()


def main():
    run = True
    gameover = False
    main_screen()

    player1 = pygame.Rect(900, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = pygame.Rect(300, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()

    star_add_increment = 2000
    star_count = 0
    stars = []
    # STAR_RADIUS = 10  # You can adjust this to your liking
    hit_count = [0, 0]
    THEME.play(-1)

    while run and not gameover:

        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if hit_count[0] > 2 or hit_count[1] > 2:
            gameover = True

        elif star_count > star_add_increment:
            for i in range(10):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

                star_add_increment = max(1000, star_add_increment - 25) # higher = harder
                star_count = 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        # player 1 controls
        if keys[pygame.K_LEFT] and player1.x - PLAYER_VEL - player1.width > (WIDTH/2):
            player1.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player1.x + PLAYER_VEL < WIDTH:
            player1.x += PLAYER_VEL
        if keys[pygame.K_UP] and player1.y - PLAYER_VEL > 0:
            player1.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player1.y + PLAYER_VEL + player1.height < HEIGHT:
            player1.y += PLAYER_VEL

        # player 2 controls
        if keys[pygame.K_a] and player2.x - PLAYER_VEL > 0:
            player2.x -= PLAYER_VEL
        if keys[pygame.K_d] and player2.x + PLAYER_VEL + player2.width < (WIDTH/2):
            player2.x += PLAYER_VEL
        if keys[pygame.K_w] and player2.y - PLAYER_VEL > 0:
            player2.y -= PLAYER_VEL
        if keys[pygame.K_s] and player2.y + PLAYER_VEL + player2.height < HEIGHT:
            player2.y += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.colliderect(player1):
                explosion = {"pos": (player1.x, player1.y), "size": 0, "rate": 5}
                explosions.append(explosion)
                EXPLOSION_SOUND.play()
                stars.remove(star)
                hit_count[1] += 1
                break
            elif star.colliderect(player2):
                explosion = {"pos": (player2.x, player2.y), "size": 0, "rate": 5}
                explosions.append(explosion)
                EXPLOSION_SOUND.play()
                stars.remove(star)
                hit_count[0] += 1
                break

        ''' for health in health_bar[:]:
            health.y += STAR_VEL
            if health.y > HEIGHT:
                health
        '''
        draw(player1, player2, elapsed_time, stars, hit_count, gameover, explosions)

    if gameover:
        THEME.stop()
        pygame.time.delay(3000)
        # highscore_song.play()
        # player_name = input("HIGH SCORE! ENTER NAME: ")
        # update_leaderboard(player_name, elapsed_time)
        gameover_song.play()
        gameover_screen()
        display_leaderboard()

    pygame.quit()


if __name__ == "__main__":
    main()
