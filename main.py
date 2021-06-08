import pygame, constants, grid

def update_fps(clock):
    pygame.display.set_caption('Panning and Zooming example! FPS: %d' % int(clock.get_fps())) # i dont like f-strings

window = pygame.display.set_mode((constants.nScreenWidth, constants.nScreenHeight))

clock = pygame.time.Clock()
    
ctrlPressed = False;
scale = 1 # scale of the grid rendered on the window
gridX, gridY = 0, 0 # initial position of grid, this changes when panning

grid = grid.Grid(window, [0, 0], constants.WHITE, 20, 1)

oldMouseX, oldMouseY, newMouseX, newMouseY = 0, 0, 0, 0
mouseDown = False

while (1):
    for event in pygame.event.get():
        if event.type == constants.window_exit_event:
            pygame.quit()

        if event.type == constants.keydown and event.key == constants.ctrl_key:
            ctrlPressed = True

        if event.type == constants.wheel and ctrlPressed == True:
            if event.y == 1:
                # wheel up
                grid.zoom_in()

            elif event.y == -1:
                # wheel down
                grid.zoom_out()

        # for panning:
        if event.type == constants.mouse_button_down:
            oldMouseX, oldMouseY = pygame.mouse.get_pos()
            mouseDown = True

        if event.type == constants.mouse_motion and mouseDown:
            newMouseX, newMouseY = pygame.mouse.get_pos()

        if event.type == constants.mouse_button_up:
            newMouseX, newMouseY = pygame.mouse.get_pos()

            mouseDown = False
            
            offSetX = abs(oldMouseX - grid.pos_x)
            offSetY = abs(oldMouseY - grid.pos_y)

            grid.panOnMouseMotion([offSetX, offSetY], [newMouseX, newMouseY])

        # zooming in/out without a mouse wheel
        key = pygame.key.get_pressed()
        
        if key[constants.minus_key]: grid.zoom_out()
        if key[constants.equals_to]: grid.zoom_in()

    update_fps(clock) # no hassle of rendering fps as text, simply display fps alongside the window title.

    window.fill(constants.BLACK)
    grid.draw(20, 20)

    clock.tick(constants.nFramesPerSecond) # regulate frames
    pygame.display.flip() # update window with every iteration, pygame.display.update() does the same
