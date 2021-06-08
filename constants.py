import pygame

# window constants
nScreenWidth, nScreenHeight = 1000, 700
nFramesPerSecond = 240

# color constants
WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)

# key constants
ctrl_key = 1073742048
keydown = pygame.KEYDOWN
keyup = pygame.KEYUP
equals_to = pygame.K_EQUALS
minus_key = pygame.K_MINUS

# event constants
mouse_motion = pygame.MOUSEMOTION
wheel = pygame.MOUSEWHEEL
mouse_button_down = pygame.MOUSEBUTTONDOWN
mouse_button_up = pygame.MOUSEBUTTONUP

# functions
exit_window = lambda: pygame.quit()
window_exit_event = pygame.QUIT
