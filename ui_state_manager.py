import pygame

class GameState:
    """Các trạng thái chính của Game"""
    START = "START"          # Màn hình chờ bắt đầu
    PLAYING = "PLAYING"      # Đang chơi
    GAME_OVER = "GAME_OVER"  # Màn hình kết thúc ván đấu

class UIManager:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        
        # Khởi tạo Trạng thái mặc định khi mở Game
        self.state = GameState.START
        
        # Khởi tạo Font chữ hệ thống
        pygame.font.init()
        self.font_title = pygame.font.SysFont("Arial", 40, bold=True)
        self.font_score = pygame.font.SysFont("Arial", 36, bold=True)
        self.font_sub = pygame.font.SysFont("Arial", 22)

    def set_state(self, new_state):
        """Chuyển đổi trạng thái game"""
        self.state = new_state

    def is_start(self):
        return self.state == GameState.START

    def is_playing(self):
        return self.state == GameState.PLAYING

    def is_game_over(self):
        return self.state == GameState.GAME_OVER

    def draw_start_screen(self, screen):
        """Vẽ giao diện màn hình chờ bắt đầu (START)"""
        # Tiêu đề Game
        title_surface = self.font_title.render("FLAPPY BIRD", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 3))
        screen.blit(title_surface, title_rect)

        # Hướng dẫn bấm phím
        msg_surface = self.font_sub.render("Nhan SPACE de bay!", True, (255, 255, 200))
        msg_rect = msg_surface.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(msg_surface, msg_rect)

    def draw_score(self, screen, score):
        """Vẽ điểm số khi đang chơi (PLAYING)"""
        score_surface = self.font_score.render(str(score), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(self.width // 2, 50))
        
        # Tạo hiệu ứng đổ bóng cho chữ điểm số
        shadow_surface = self.font_score.render(str(score), True, (0, 0, 0))
        shadow_rect = shadow_surface.get_rect(center=(self.width // 2 + 2, 52))
        
        screen.blit(shadow_surface, shadow_rect)
        screen.blit(score_surface, score_rect)

    def draw_game_over_screen(self, screen, final_score, high_score=0):
        """Vẽ bảng kết quả Màn hình Game Over (GAME_OVER)"""
        # Chữ Game Over
        go_surface = self.font_title.render("GAME OVER", True, (230, 50, 50))
        go_rect = go_surface.get_rect(center=(self.width // 2, self.height // 3 - 20))
        screen.blit(go_surface, go_rect)

        # Hiển thị Điểm hiện tại
        score_surface = self.font_sub.render(f"Diem cua ban: {final_score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(self.width // 2, self.height // 2 - 10))
        screen.blit(score_surface, score_rect)

        # Hiển thị Kỷ lục (High Score)
        if high_score > 0:
            hs_surface = self.font_sub.render(f"Ky luc: {high_score}", True, (255, 215, 0))
            hs_rect = hs_surface.get_rect(center=(self.width // 2, self.height // 2 + 25))
            screen.blit(hs_surface, hs_rect)

        # Hướng dẫn chơi lại
        restart_surface = self.font_sub.render("Nhan SPACE de choi lai", True, (200, 200, 200))
        restart_rect = restart_surface.get_rect(center=(self.width // 2, self.height * 2 // 3 + 20))
        screen.blit(restart_surface, restart_rect)

    def render(self, screen, score=0, high_score=0):
        """Hàm Render tổng điều phối giao diện theo đúng trạng thái"""
        if self.state == GameState.START:
            self.draw_start_screen(screen)
        elif self.state == GameState.PLAYING:
            self.draw_score(screen, score)
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over_screen(screen, score, high_score)