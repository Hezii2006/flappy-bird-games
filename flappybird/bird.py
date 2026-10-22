
import pygame
import math


class Bird:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

        # Vật lý chuyển động
        self.velocity_y = 0.0
        self.gravity = 1200.0
        self.flap_strength = -380.0
        self.max_fall_speed = 600.0

        # Kích thước chim
        self.radius = 18

        # Thời gian hoạt ảnh vỗ cánh
        self.wing_time = 0.0

    def flap(self):
        self.velocity_y = self.flap_strength

    def update(self, dt):
        self.velocity_y += self.gravity * dt
        self.velocity_y = min(self.velocity_y, self.max_fall_speed)
        self.y += self.velocity_y * dt

        # Cập nhật hoạt ảnh cánh
        self.wing_time += dt * 15

    def draw(self, screen):
        x = int(self.x)
        y = int(self.y)

        # Góc nghiêng theo hướng chuyển động
        angle = max(-25, min(65, self.velocity_y * 0.07))

        # Tạo bề mặt để vẽ chim rồi xoay
        bird_surface = pygame.Surface((70, 60), pygame.SRCALPHA)
        cx, cy = 32, 30

        # Bóng nhẹ bên dưới thân
        pygame.draw.ellipse(
            bird_surface, (190, 135, 35, 70),
            (12, 23, 43, 27)
        )

        # Đuôi chim
        pygame.draw.polygon(
            bird_surface, (245, 155, 30),
            [(12, 29), (2, 23), (5, 34)]
        )

        # Cánh chim chuyển động lên xuống
        wing_y = math.sin(self.wing_time) * 5

        pygame.draw.ellipse(
            bird_surface, (210, 125, 25),
            (15, 29 + wing_y, 27, 17)
        )
        pygame.draw.ellipse(
            bird_surface, (255, 185, 45),
            (16, 27 + wing_y, 25, 15)
        )
        pygame.draw.ellipse(
            bird_surface, (255, 218, 100),
            (19, 29 + wing_y, 17, 7)
        )

        # Thân chim
        pygame.draw.ellipse(
            bird_surface, (220, 135, 20),
            (10, 13, 43, 36)
        )
        pygame.draw.ellipse(
            bird_surface, (255, 205, 40),
            (10, 10, 42, 36)
        )

        # Bụng màu kem
        pygame.draw.ellipse(
            bird_surface, (255, 240, 180),
            (21, 27, 25, 17)
        )

        # Má hồng
        pygame.draw.circle(
            bird_surface, (255, 135, 130),
            (42, 30), 5
        )

        # Mắt trắng
        pygame.draw.ellipse(
            bird_surface, (255, 255, 255),
            (35, 15, 14, 17)
        )

        # Con ngươi
        pygame.draw.circle(
            bird_surface, (45, 45, 55),
            (44, 23), 4
        )
        pygame.draw.circle(
            bird_surface, (255, 255, 255),
            (45, 21), 1
        )

        # Mỏ màu cam
        pygame.draw.polygon(
            bird_surface, (255, 115, 25),
            [(48, 29), (65, 33), (49, 37)]
        )
        pygame.draw.line(
            bird_surface, (190, 75, 15),
            (50, 33), (62, 33), 1
        )

        # Viền thân để hình ảnh rõ nét
        pygame.draw.ellipse(
            bird_surface, (175, 100, 20),
            (10, 10, 42, 36), 2
        )

        # Xoay chim theo vận tốc
        rotated = pygame.transform.rotate(bird_surface, -angle)
        rect = rotated.get_rect(center=(x, y))

        screen.blit(rotated, rect)
