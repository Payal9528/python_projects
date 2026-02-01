import pygame
import random
import sys

# -----------------------------
# Config
# -----------------------------
WIDTH, HEIGHT = 800, 500
CELL_SIZE = 20
GRID_COLS = WIDTH // CELL_SIZE
GRID_ROWS = HEIGHT // CELL_SIZE
FPS = 12  # Increase for faster snake

# Colors
BLACK = (15, 15, 15)
WHITE = (240, 240, 240)
GREEN = (60, 200, 85)
RED = (230, 70, 70)
BLUE = (80, 160, 240)
GRAY = (40, 40, 40)
YELLOW = (245, 200, 70)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# -----------------------------
# Helper functions
# -----------------------------
def draw_grid(surface):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRAY, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRAY, (0, y), (WIDTH, y), 1)


def random_empty_cell(snake):
    while True:
        pos = (random.randint(0, GRID_COLS - 1), random.randint(0, GRID_ROWS - 1))
        if pos not in snake:
            return pos


def cell_to_pixels(cell):
    x, y = cell
    return x * CELL_SIZE, y * CELL_SIZE


# -----------------------------
# Game classes
# -----------------------------
class Snake:
    def __init__(self, start_pos, length=3):
        # Snake body as list of cells (head first)
        self.body = [(start_pos[0] - i, start_pos[1]) for i in range(length)]
        self.direction = RIGHT
        self.grow_pending = 0
        self.alive = True

    def set_direction(self, new_dir):
        # Prevent reversing directly into itself
        if (self.direction[0] + new_dir[0] == 0) and (self.direction[1] + new_dir[1] == 0):
            return
        self.direction = new_dir

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self, amount=1):
        self.grow_pending += amount

    def check_collisions(self):
        head = self.body[0]
        x, y = head
        # Wall collision
        if x < 0 or x >= GRID_COLS or y < 0 or y >= GRID_ROWS:
            self.alive = False
            return
        # Self collision (ignore head at index 0)
        if head in self.body[1:]:
            self.alive = False

    def draw(self, surface):
        # Head
        hx, hy = cell_to_pixels(self.body[0])
        pygame.draw.rect(surface, BLUE, (hx, hy, CELL_SIZE, CELL_SIZE), border_radius=4)
        # Body
        for cell in self.body[1:]:
            x, y = cell_to_pixels(cell)
            pygame.draw.rect(surface, GREEN, (x, y, CELL_SIZE, CELL_SIZE), border_radius=4)


class Fruit:
    def __init__(self, snake):
        self.pos = random_empty_cell(snake.body)

    def relocate(self, snake):
        self.pos = random_empty_cell(snake.body)

    def draw(self, surface):
        x, y = cell_to_pixels(self.pos)
        # Draw a little apple-like circle
        pygame.draw.circle(surface, RED, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 2)
        # Leaf
        pygame.draw.circle(surface, YELLOW, (x + CELL_SIZE // 2 + 4, y + 4), 3)


# -----------------------------
# UI helpers
# -----------------------------
def draw_text(surface, text, size, color, center):
    font = pygame.font.Font(None, size)
    label = font.render(text, True, color)
    rect = label.get_rect(center=center)
    surface.blit(label, rect)


def game_over_screen(screen, score):
    screen.fill(BLACK)
    draw_text(screen, "Game Over", 64, WHITE, (WIDTH // 2, HEIGHT // 2 - 40))
    draw_text(screen, f"Score: {score}", 36, WHITE, (WIDTH // 2, HEIGHT // 2 + 10))
    draw_text(screen, "Press R to restart or Esc to quit", 28, WHITE, (WIDTH // 2, HEIGHT // 2 + 50))
    pygame.display.flip()


# -----------------------------
# Main game loop
# -----------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake - Python by Payal")
    clock = pygame.time.Clock()

    # Initial state
    snake = Snake(start_pos=(GRID_COLS // 2, GRID_ROWS // 2), length=3)
    fruit = Fruit(snake)
    score = 0
    running = True
    paused = False

    while running:
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE,):
                    running = False
                elif event.key in (pygame.K_p,):
                    paused = not paused
                elif event.key in (pygame.K_UP, pygame.K_w):
                    snake.set_direction(UP)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    snake.set_direction(DOWN)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    snake.set_direction(LEFT)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    snake.set_direction(RIGHT)
                elif not snake.alive and event.key in (pygame.K_r,):
                    # Restart
                    snake = Snake(start_pos=(GRID_COLS // 2, GRID_ROWS // 2), length=3)
                    fruit = Fruit(snake)
                    score = 0

        if not paused and snake.alive:
            snake.move()
            snake.check_collisions()

            # Eat fruit
            if snake.body[0] == fruit.pos:
                snake.grow(amount=1)
                score += 10
                fruit.relocate(snake)

        # Draw
        screen.fill(BLACK)
        draw_grid(screen)
        fruit.draw(screen)
        snake.draw(screen)
        draw_text(screen, f"Score: {score}", 28, WHITE, (80, 20))

        if paused and snake.alive:
            draw_text(screen, "Paused (P)", 28, WHITE, (WIDTH // 2, 20))

        if not snake.alive:
            game_over_screen(screen, score)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Simple error output to help debugging
        print("Error:", e)
        pygame.quit()
        sys.exit(1)