import pygame
import os

class SoundManager:
    def __init__(self, sound_dir="assets/sounds"):
        # Khởi tạo mixer của Pygame nếu chưa được khởi tạo
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        self.sounds = {}
        self.sound_dir = sound_dir
        
        # Danh sách các file âm thanh cần tải
        sound_files = {
            'flap': 'flap.wav',      # Âm thanh khi bấm Space vỗ cánh
            'score': 'score.wav',    # Âm thanh khi qua ống +1 điểm
            'hit': 'hit.wav',        # Âm thanh khi va chạm vào ống/đất
            'die': 'die.wav'         # Âm thanh khi Game Over
        }

        # Tải từng file âm thanh vào dictionary
        for name, file_name in sound_files.items():
            path = os.path.join(self.sound_dir, file_name)
            if os.path.exists(path):
                self.sounds[name] = pygame.mixer.Sound(path)
            else:
                # Tạo sound giả lập (None) nếu không tìm thấy file để không bị crash game
                print(f"[Cảnh báo] Không tìm thấy file âm thanh: {path}")
                self.sounds[name] = None

    def play_flap(self):
        """Phát âm thanh vỗ cánh."""
        if self.sounds.get('flap'):
            self.sounds['flap'].play()

    def play_score(self):
        """Phát âm thanh cộng điểm."""
        if self.sounds.get('score'):
            self.sounds['score'].play()

    def play_hit(self):
        """Phát âm thanh va chạm."""
        if self.sounds.get('hit'):
            self.sounds['hit'].play()

    def play_die(self):
        """Phát âm thanh rớt/thua."""
        if self.sounds.get('die'):
            self.sounds['die'].play()