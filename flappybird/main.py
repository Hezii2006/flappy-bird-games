
import pygame
from bird import Bird

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH = 400
HEIGHT = 600
GROUND_HEIGHT = 60
GROUND_Y = HEIGHT - GROUND_HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird - Physics Demo")

# Đồng hồ điều khiển FPS và thời gian
clock = pygame.time.Clock()
FPS = 60

# Màu sắc
SKY_BLUE = (135, 206, 235)
GREEN = (100, 200, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 32)

# Tạo chim
bird = Bird(100, 250)

# Trạng thái game
started = False
game_over = False
running = True


def reset_game():
    """Đưa game về trạng thái ban đầu."""
    global bird, started, game_over

    bird = Bird(100, 250)
    started = False
    game_over = False


# Game Loop
while running:

    # Tính thời gian giữa hai khung hình, đơn vị giây
    dt = min(clock.tick(FPS) / 1000.0, 0.05)

    # ---------------------------------
    # 1. XỬ LÝ SỰ KIỆN (INPUT)
    # ---------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Nhấn phím Space
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_SPACE:
                if game_over:
                    reset_game()
                else:
                    started = True
                    bird.flap()

            elif event.key == pygame.K_r and game_over:
                reset_game()

        # Nhấn chuột trái
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if game_over:
                    reset_game()
                else:
                    started = True
                    bird.flap()

    # ---------------------------------
    # 2. CẬP NHẬT TRẠNG THÁI (UPDATE)
    # ---------------------------------
    if started and not game_over:

        # Cập nhật vật lý của chim
        bird.update(dt)

        # Va chạm với trần màn hình
        if bird.y - bird.radius <= 0:
            game_over = True

        # Va chạm với mặt đất
        if bird.y + bird.radius >= GROUND_Y:
            bird.y = GROUND_Y - bird.radius
            game_over = True

    # ---------------------------------
    # 3. VẼ MÀN HÌNH (RENDER)
    # ---------------------------------
    screen.fill(SKY_BLUE)

    # Vẽ mặt đất
    pygame.draw.rect(
        screen,
        GREEN,
        (0, GROUND_Y, WIDTH, GROUND_HEIGHT)
    )

    # Vẽ chim
    bird.draw(screen)

    # Hiển thị hướng dẫn
    if not started and not game_over:
        message = font.render(
            "SPACE / Click to flap",
            True,
            WHITE
        )
        screen.blit(message, (65, 100))

    # Hiển thị trạng thái thua
    if game_over:
        title = font.render("GAME OVER", True, BLACK)
        hint = font.render("SPACE / Click to restart", True, BLACK)

        screen.blit(
            title,
            title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        )
        screen.blit(
            hint,
            hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        )

    # Cập nhật hình ảnh lên màn hình
    pygame.display.flip()

# Đóng Pygame
pygame.quit()
