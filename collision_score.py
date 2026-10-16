import pygame

class CollisionAndScoreManager:
    def __init__(self, screen_height, ground_y):
        self.score = 0
        self.screen_height = screen_height
        self.ground_y = ground_y  # Tọa độ Y của mặt đất

    def reset_score(self):
        """Reset lại điểm số khi bắt đầu màn chơi mới."""
        self.score = 0

    def check_collision(self, bird, pipes):
        """
        Kiểm tra va chạm giữa chim và các đối tượng (ống, mặt đất, trần).
        Trả về True nếu có va chạm (Game Over), ngược lại trả về False.
        """
        bird_rect = bird.get_rect()

        # 1. Va chạm với mặt đất hoặc bay quá trần màn hình
        if bird_rect.top <= 0 or bird_rect.bottom >= self.ground_y:
            return True

        # 2. Va chạm với danh sách các ống (ống trên và ống dưới)
        for pipe in pipes:
            # pipe.top_rect và pipe.bottom_rect là khung hình chữ nhật của 2 ống
            if bird_rect.colliderect(pipe.top_rect) or bird_rect.colliderect(pipe.bottom_rect):
                return True

        return False

    def update_score(self, bird, pipes, sound_manager=None):
        """
        Kiểm tra xem chim đã vượt qua ống chưa để cộng điểm.
        Dùng cờ 'passed' để đảm bảo mỗi ống chỉ cộng 1 điểm duy nhất.
        """
        bird_rect = bird.get_rect()

        for pipe in pipes:
            # Nếu chim đã vượt qua mép phải của ống và ống chưa được tính điểm
            if bird_rect.left > pipe.x + pipe.width and not pipe.passed:
                pipe.passed = True
                self.score += 1
                
                # Phát âm thanh cộng điểm nếu truyền sound_manager vào
                if sound_manager:
                    sound_manager.play_score()
                
                return True  # Vừa ghi nhận thêm điểm
        return False