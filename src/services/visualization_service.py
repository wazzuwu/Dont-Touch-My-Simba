import pygame

from paths import ASSETS_DIR, MENU_DIR
from src.config import Config
from src.utils.tools import sine


class VisualizationService:
    @staticmethod
    def get_right_hand_image():
        return pygame.image.load(ASSETS_DIR / "right_hand.png").convert_alpha()

    @staticmethod
    def get_left_hand_image():
        return pygame.image.load(ASSETS_DIR / "left_hand.png").convert_alpha()

    @staticmethod
    def get_player_image():
        return pygame.image.load(MENU_DIR/ "t1.png").convert_alpha()

    @staticmethod
    def get_dotted_line():
        return pygame.image.load(ASSETS_DIR / "dotted_line.png").convert_alpha()

    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSETS_DIR / "bg.png").convert_alpha()

    @staticmethod
    def get_santa_hand():
        return pygame.image.load(MENU_DIR / "t2.png").convert_alpha()

    @staticmethod
    def get_score_backing():
        return pygame.image.load(ASSETS_DIR / "scoreboard.png").convert_alpha()

    @staticmethod
    def get_press_key_image():
        return pygame.image.load(MENU_DIR / "press_any_key.png").convert_alpha()

    @staticmethod
    def get_title_image():
        return pygame.image.load(MENU_DIR / "title1.png").convert_alpha()

    @staticmethod
    def get_holding_gift_image():
        return pygame.image.load(MENU_DIR / "trial1.png").convert_alpha()

    @staticmethod
    def get_main_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 40)

    @staticmethod
    def get_credit_font_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 12)

    @staticmethod
    def get_score_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 26)

    @staticmethod
    def load_main_game_displays():
        pygame.display.set_caption("Don't Touch My Simba")
        gift = VisualizationService.get_player_image()
        pygame.display.set_icon(gift)

    @staticmethod
    def draw_background_with_scroll(screen, scroll):
        background = VisualizationService.get_background_image()
        screen.blit(background, (0, scroll))

    @staticmethod
    def draw_author_credits(screen):
        credit_font = VisualizationService.get_credit_font_font()
        author_credits = credit_font.render("Github.com/wazzuwu", True, (0, 0, 0))
        credits_rect = author_credits.get_rect(center=(Config.WIDTH // 2, 620))
        screen.blit(author_credits, credits_rect)

    @staticmethod
    def draw_best_score(screen, max_score):
        score_font = VisualizationService.get_score_font()
        best_score = score_font.render(f"Best: {max_score}", True, (0, 0, 0))
        best_score_rect = best_score.get_rect(center=(Config.WIDTH // 2, 220))
        screen.blit(best_score, best_score_rect)

    @staticmethod
    def draw_title(screen):
        y = sine(200.0, 1280, 10.0, 100)
        
        title = VisualizationService.get_title_image()
        screen.blit(title, (0, y-120))
        gift_y = sine(150.0, 640, 10.0, 200)  # Adjust values for smoother effect
        holding_gift = VisualizationService.get_holding_gift_image()
        screen.blit(holding_gift, (0, gift_y)) 

    @staticmethod
    def draw_press_key(screen, press_y):
        press_key = VisualizationService.get_press_key_image()
        screen.blit(press_key, (0, press_y))

    @staticmethod
    def draw_main_menu(screen, max_score, press_y):
        VisualizationService.draw_author_credits(screen)
        VisualizationService.draw_best_score(screen, max_score)
        VisualizationService.draw_title(screen)
        VisualizationService.draw_press_key(screen, press_y)
