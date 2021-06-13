# Panning-and-Zooming-Demo
A very simple demonstration on how some portion of a screen can be panned around, and zoomed in/out. 

# What does it do?
when run, the program renders a 20 (rows) x 20 (columns) grid on a pygame window. The grid can be panned around by pressing the left mouse button and at the same time dragging the mouse. The grid can also be zoomed in / out via either the mouse wheel, or pressing the `-` key (to zoom out) and the `=` key (to zoom in). 

# Modules
`main.py` needs pygame to render the grid in real time, and also handles mouse and keyboard input. The program itself runs at a steady 250
frames per second. 
I also created two more files, namely `constants.py`(to handle pygame constants for the window, and keyboard input, mouse motion, rgb color values, etc) and `grid.py` (which handles the grid, changes the grid variables to support panning and zooming). 

# What the program lacks:
Right now, the basic functionality of panning and zooming works perfectly fine, though the rendering isn't exactly 'great', the grid does not pan around in real time, it moves from a previous mouse position to where you release the mouse. If asked to pan around on mouse motion, a peculiar jittering can be observed. I might fix it in the future.
