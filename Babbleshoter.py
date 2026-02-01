import pygame
import random
import sys
import math

# -----------------------------
# Config
# -----------------------------
WIDTH, HEIGHT = 640, 720
FPS = 60
BUBBLE_RADIUS = 20
COLORS = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255)]

ROWS = 6
COLS = WIDTH // (BUBBLE_RADIUS*2)

# -----------------------------
# Classes
# -----------------------------
class Bubble:
    def __init__(self, grid_x, grid_y, color):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.color = color
        self.radius = BUBBLE_RADIUS
        self.x = grid_x * BUBBLE_RADIUS*2 + BUBBLE_RADIUS
        self.y = grid_y * BUBBLE_RADIUS*2 + BUBBLE_RADIUS
        self.moving = False
        self.dx = 0
        self.dy = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        if self.moving:
            self.x += self.dx
            self.y += self.dy
            # Bounce from walls
            if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
                self.dx *= -1

    def snap_to_grid(self):
        self.grid_x = int(self.x // (BUBBLE_RADIUS*2))
        self.grid_y = int(self.y // (BUBBLE_RADIUS*2))
        self.x = self.grid_x * BUBBLE_RADIUS*2 + BUBBLE_RADIUS
        self.y = self.grid_y * BUBBLE_RADIUS*2 + BUBBLE_RADIUS

# -----------------------------
# Helper functions
# -----------------------------
def create_initial_rows():
    bubbles = []
    for row in range(ROWS):
        for col in range(COLS):
            color = random.choice(COLORS)
            bubbles.append(Bubble(col, row, color))
    return bubbles

def neighbors(bubble, bubbles):
    result = []
    for b in bubbles:
        dist = math.hypot(b.x - bubble.x, b.y - bubble.y)
        if dist <= BUBBLE_RADIUS*2 + 2:
            result.append(b)
    return result

def check_cluster(bubbles, new_bubble):
    cluster = [new_bubble]
    to_check = [new_bubble]
    while to_check:
        current = to_check.pop()
        for b in neighbors(current, bubbles):
            if b.color == new_bubble.color and b not in cluster:
                cluster.append(b)
                to_check.append(b)
    return cluster if len(cluster) >= 3 else []

# -----------------------------
# Main Game
# -----------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubble Shooter - Stand & Next Ball")
    clock = pygame.time.Clock()

    bubbles = create_initial_rows()
    current_bubble = Bubble(COLS//2, ROWS+10, random.choice(COLORS))
    next_bubble = Bubble(COLS//2, ROWS+12, random.choice(COLORS))  # next bubble preview
    score = 0

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not current_bubble.moving:
                mx, my = pygame.mouse.get_pos()
                angle_x = mx - current_bubble.x
                angle_y = my - current_bubble.y
                length = math.hypot(angle_x, angle_y)
                current_bubble.dx = angle_x/length * 8
                current_bubble.dy = angle_y/length * 8
                current_bubble.moving = True

        # Update
        current_bubble.update()

        # Collision check
        if current_bubble.y - current_bubble.radius <= 0:
            current_bubble.moving = False
            current_bubble.snap_to_grid()
            bubbles.append(current_bubble)
            cluster = check_cluster(bubbles, current_bubble)
            if cluster:
                for b in cluster:
                    bubbles.remove(b)
                score += 10 * len(cluster)
            # next bubble becomes current
            current_bubble = next_bubble
            next_bubble = Bubble(COLS//2, ROWS+12, random.choice(COLORS))

        else:
            for b in bubbles:
                dist = math.hypot(b.x - current_bubble.x, b.y - current_bubble.y)
                if dist <= BUBBLE_RADIUS*2:
                    current_bubble.moving = False
                    current_bubble.snap_to_grid()
                    bubbles.append(current_bubble)
                    cluster = check_cluster(bubbles, current_bubble)
                    if cluster:
                        for bub in cluster:
                            bubbles.remove(bub)
                        score += 10 * len(cluster)
                    # next bubble becomes current
                    current_bubble = next_bubble
                    next_bubble = Bubble(COLS//2, ROWS+12, random.choice(COLORS))
                    break

        # Draw
        screen.fill((30,30,30))
        for b in bubbles:
            b.draw(screen)
        current_bubble.draw(screen)
        # Draw next bubble preview above stand
        next_bubble.draw(screen)

        # Draw stand
        pygame.draw.rect(screen, (200,200,200), (WIDTH//2-40, HEIGHT-60, 80, 20))

        font = pygame.font.Font(None, 36)
        text = font.render(f"Coins: {score}", True, (255,255,255))
        screen.blit(text, (20,20))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
