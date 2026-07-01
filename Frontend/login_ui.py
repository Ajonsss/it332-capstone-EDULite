import pygame
import sys
from Backend.auth.login import login_user, register_user 

# 1. Initialize Pygame
pygame.init()

# Setup Screen (Height reduced to 850 for a tighter fit)
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("8-Bit App - Edulite")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
YELLOW = (255, 255, 0)

# --- Custom Font Loader ---
def load_font(path, size):
    try:
        return pygame.font.Font(path, size)
    except Exception as e:
        print(f"Warning: Could not load font '{path}'. Using default. Error: {e}")
        return pygame.font.Font(None, size)

# Load fonts
font = load_font("Frontend/assets/8bit_font.ttf", 28)
small_font = load_font("Frontend/assets/8bit_font.ttf", 20)
title_font = load_font("Frontend/assets/8bit_font.ttf", 30)

# 2. Asset Loader with Auto-Scaling
def load_img(path, target_size, fallback_color):
    try:
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, target_size)
        return img
    except Exception as e:
        print(f"Failed to load {path} - Error: {e}")
        surf = pygame.Surface(target_size)
        surf.fill(fallback_color)
        return surf

# Load background
try:
    bg_img = pygame.image.load("Frontend/assets/background.png").convert()
    bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
except Exception as e:
    print(f"Failed to load Background - Error: {e}")
    bg_img = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_img.fill((50, 50, 50))

# Defined Target Sizes for UI Elements
INPUT_SIZE = (300, 140)
BTN_SIZE = (350, 250)
LOGO_SIZE = (120, 120) 

# Load UI Elements including the Logo
logo_img = load_img("Frontend/assets/logo.png", LOGO_SIZE, (200, 200, 200))
input_inactive = load_img("Frontend/assets/input_box_inactive.png", INPUT_SIZE, (100, 100, 100))
input_active = load_img("Frontend/assets/input_box_active.png", INPUT_SIZE, (150, 150, 150))
btn_normal = load_img("Frontend/assets/btn_login_normal.png", BTN_SIZE, (0, 100, 200))
btn_hover = load_img("Frontend/assets/btn_login_hover.png", BTN_SIZE, (0, 150, 255))

class InputBox:
    def __init__(self, x, y, is_password=False):
        self.rect = pygame.Rect(x, y, input_inactive.get_width(), input_inactive.get_height())
        self.text = ""
        self.active = False
        self.is_password = is_password

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, surface):
        current_image = input_active if self.active else input_inactive
        surface.blit(current_image, (self.rect.x, self.rect.y))
        
        display_text = "*" * len(self.text) if self.is_password else self.text
        text_surface = font.render(display_text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

class Button:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, btn_normal.get_width(), btn_normal.get_height())

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        current_image = btn_hover if self.rect.collidepoint(mouse_pos) else btn_normal
        surface.blit(current_image, (self.rect.x, self.rect.y))

# 3. Main Dashboard Redirect State
def launch_dashboard():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Draw background in dashboard
        screen.blit(bg_img, (0, 0)) 
        
        # Using the new custom fonts
        title = title_font.render("Navotas Elementary School", True, WHITE)
        subtitle = font.render("Teacher Dashboard - Authentication Successful", True, GREEN)
        
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, 250)))
        screen.blit(subtitle, subtitle.get_rect(center=(SCREEN_WIDTH//2, 300)))
        
        pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    
    input_width = input_inactive.get_width()
    btn_width = btn_normal.get_width()
    
    # TIGHTENED Y POSITIONS:
    # Logo is centered at 100 (bottom edge at 160).
    # Username label will be at 170 (10px gap).
    username_box = InputBox(SCREEN_WIDTH//2 - (input_width//2), 200)
    
    # Username box ends at 340. Password label will be at 350 (10px gap).
    password_box = InputBox(SCREEN_WIDTH//2 - (input_width//2), 300, is_password=True)
    
    # Password box ends at 520. Button starts at 560 (40px gap).
    action_btn = Button(SCREEN_WIDTH//2 - (btn_width//2), 350)
    
    current_mode = "login"
    status_message = ""
    status_color = BLACK

    running = True
    while running:
        toggle_text_str = "Need an account? Click here to Register" if current_mode == "login" else "Already have an account? Click here to Login"
        toggle_surface = small_font.render(toggle_text_str, True, YELLOW)
        
        # Pulled up slightly to sit just under the button
        toggle_rect = toggle_surface.get_rect(center=(SCREEN_WIDTH//2, 600))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            username_box.handle_event(event)
            password_box.handle_event(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action_btn.rect.collidepoint(event.pos):
                    username = username_box.text.strip()
                    password = password_box.text.strip()
                    
                    if not username or not password:
                        status_message = "Please fill out both fields."
                        status_color = RED
                        continue

                    if current_mode == "login":
                        if login_user(username, password): 
                            launch_dashboard() 
                        else: 
                            status_message = "Invalid username or password."
                            status_color = RED
                    
                    elif current_mode == "register":
                        if register_user(username, password):
                            launch_dashboard() 
                        else:
                            status_message = "Registration Failed. Username might exist."
                            status_color = RED

                if toggle_rect.collidepoint(event.pos):
                    current_mode = "register" if current_mode == "login" else "login"
                    status_message = "" 
                    username_box.text = ""
                    password_box.text = ""

        # Drawing Phase
        screen.blit(bg_img, (0, 0))
        
        # Draw the Logo at the top
        logo_rect = logo_img.get_rect(center=(SCREEN_WIDTH//2, 100))
        screen.blit(logo_img, logo_rect)
        
        action_label = font.render("LOGIN" if current_mode == "login" else "REGISTER", True, BLACK)
        
        username_box.draw(screen)
        password_box.draw(screen)
        action_btn.draw(screen)
        
        screen.blit(font.render("Username:", True, WHITE), (username_box.rect.x, username_box.rect.y - 2))
        screen.blit(font.render("Password:", True, WHITE), (password_box.rect.x, password_box.rect.y - 2))
        screen.blit(action_label, action_label.get_rect(center=action_btn.rect.center))
        screen.blit(toggle_surface, toggle_rect)

        # Status message raised up to sit just below the toggle text
        if status_message:
            msg_surface = small_font.render(status_message, True, status_color)
            screen.blit(msg_surface, msg_surface.get_rect(center=(SCREEN_WIDTH//2, 820)))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()