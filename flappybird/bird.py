
import pygame


class Bird:
    def __init__(self, x, y):
        # Vị trí ban đầu của chim
        self.x = float(x)
        self.y = float(y)

        # Vận tốc theo chiều dọc
        self.velocity_y = 0.0

        # Thông số vật lý
        self.gravity = 1200.0
        self.flap_strength = -380.0
        self.max_fall_speed = 600.0

        # Kích thước chim (bản demo dùng hình tròn)
        self.radius = 15

    def flap(self):
        """Tạo vận tốc hướng lên khi người chơi nhấn nút."""
        self.velocity_y = self.flap_strength

    def update(self, dt):
        """Cập nhật vận tốc và vị trí theo thời gian."""

        # 1. Trọng lực làm thay đổi vận tốc
        self.velocity_y += self.gravity * dt

        # 2. Giới hạn vận tốc rơi
        self.velocity_y = min(
            self.velocity_y,
            self.max_fall_speed
        )

        # 3. Cập nhật vị trí theo vận tốc
        self.y += self.velocity_y * dt

    def draw(self, screen):
        """Vẽ chim lên màn hình."""
        pygame.draw.circle(
            screen,
            (255, 220, 0),
            (int(self.x), int(self.y)),
            self.radius
        )

        # Mắt chim
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.x + 5), int(self.y - 5)),
            4
        )

        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (int(self.x + 6), int(self.y - 5)),
            2
        )
