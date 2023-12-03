import pygame   #importing the pygame module
import sys      # built in python module that provides various functions.

pygame.init()   #intializing the module

screen_width = 1260
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))   #displaying the main window.
pygame.display.set_caption('shortest path game')

font = pygame.font.Font(None, 36)   #Setting the font and its size.

clock = pygame.time.Clock()   #Clock to control the time of the game. Mainly used for the tick function to control fps.

gray = (127, 127, 127)  #some random color codes for use.
red = (255, 0, 0)
green = (0, 255, 0)
orange = (255, 97, 3)
yellow = (205, 205, 0)

conversion = 0.1  # the conversion factor according to which the output will be displayed. 1 pixel is equal to 0.1 metre.

textForPath1 = 'PATH 1'    #Texts for use.
textForPath2 = 'PATH 2'
textForPath3 = 'PATH 3'
start_text = 'red box = start point.'
end_text = 'green box = end point.'
button_text = 'play'

start = pygame.Rect(650, 550, 50, 50)    #the start (red) box.
end = pygame.Rect(650, 0, 50, 50)        #the end (green) box.

path_1 = [              #coordinates for the 1st path.
    pygame.Rect(650, 490, 50, 60),
    pygame.Rect(460, 440, 240, 50),
    pygame.Rect(460, 250, 50, 190),
    pygame.Rect(510, 250, 260, 50),
    pygame.Rect(720, 300, 50, 100),
    pygame.Rect(720, 400, 370, 50),
    pygame.Rect(1090, 220, 50, 230),
    pygame.Rect(410, 170, 730, 50),
    pygame.Rect(410, 110, 50, 60),
    pygame.Rect(460, 110, 240, 50),
    pygame.Rect(650, 50, 50, 60)
]

path_2 = [            #coordinates of the 2nd path.
    pygame.Rect(230, 550, 420, 50),
    pygame.Rect(180, 410, 50, 190),
    pygame.Rect(230, 410, 150, 50),
    pygame.Rect(380, 190, 50, 270),
    pygame.Rect(430, 190, 110, 50),
    pygame.Rect(540, 190, 50, 190),
    pygame.Rect(140, 330, 400, 50),
    pygame.Rect(140, 180, 50, 150),
    pygame.Rect(140, 130, 250, 50),
    pygame.Rect(390, 0, 50, 180),
    pygame.Rect(440, 0, 210, 50)
]

path_3 = [           #coordinates for the 3rd path.
    pygame.Rect(700, 550, 290, 50),
    pygame.Rect(990, 390, 50, 210),
    pygame.Rect(840, 390, 150, 50),
    pygame.Rect(840, 190, 50, 200),
    pygame.Rect(750, 190, 90, 50),
    pygame.Rect(700, 190, 50, 100),
    pygame.Rect(700, 290, 500, 50),
    pygame.Rect(1150, 100, 50, 190),
    pygame.Rect(1100, 100, 50, 50),
    pygame.Rect(1050, 100, 50, 140),
    pygame.Rect(1000, 190, 50, 50),
    pygame.Rect(950, 50, 50, 190),
    pygame.Rect(700, 0, 300, 50)
    ]
def distanceOfPaths(rectangles, index=0, count=0):     #A recursive function that will be used for calculating the distance of the paths based
    if index < len(rectangles):                        #on the length and width of the rectangles of each path.
        width, height = rectangles[index].size         #rectangles are the coordinates and dimensions of each of the rectangle from the path
        if width > height:                             #given as input. 
            count += width                             #the index is to keep track for how many rectangles counted. 
        else:                                          #count is storing the dimensions of the rectangles.
            count += height
        return distanceOfPaths(rectangles, index + 1, count)
    else:
        return count

distance_path1_pixels = distanceOfPaths(path_1)
distance_path1_metres = distance_path1_pixels * conversion        #converting the pixel values to metres using the coversion factor.

distance_path2_pixels = distanceOfPaths(path_2)
distance_path2_metres = distance_path2_pixels * conversion        #converting the pixel values to metres using the coversion factor.

distance_path3_pixels = distanceOfPaths(path_3)
distance_path3_metres = distance_path3_pixels * conversion        #converting the pixel values to metres using the coversion factor.

# Dictionary to store information about each path
paths = {
    'path_1': {
        'rectangles': path_1,
        'color': gray,
        'distance_pixels': distance_path1_pixels,
        'distance_metre': distance_path1_metres
    },
    'path_2': {
        'rectangles': path_2,
        'color': orange,
        'distance_pixels': distance_path2_pixels,
        'distance_metre': distance_path2_metres
    },
    'path_3': {
        'rectangles': path_3,
        'color': yellow,
        'distance_pixels': distance_path3_pixels,
        'distance_metre': distance_path3_metres
    }
}

def text_related():                                                          #A function to store all the text related information.
    text_surface1 = font.render(textForPath1, True, (0, 0, 0))
    screen.blit(text_surface1, (500, 455))
    text_surface2 = font.render(textForPath2, True, (0, 0, 0))               #render is used to create  surface object from the text
    screen.blit(text_surface2, (500, 568))                                   #because pygame doues not allow text to be displayed on the screen
    text_surface3 = font.render(textForPath3, True, (0, 0, 0))               #directly. It has to be blit on the screen.
    screen.blit(text_surface3, (800, 568))
    start_text_surface = font.render(start_text, True, (0, 0, 0))            #font.render(text, antialias, color, background)
    screen.blit(start_text_surface, (20, 40))
    end_text_surface = font.render(end_text, True, (0, 0, 0))
    screen.blit(end_text_surface, (20, 80))


def draw_button():                                                         #function that draws the play button. 
    pygame.draw.rect(screen, (0, 0, 255), button_rect)
    button_surface = font.render(button_text, True, (255, 255, 255))
    screen.blit(button_surface, (1150, 510))

button_rect = pygame.Rect(1140, 503, 68, 50)

# Initialize box position and path index
box_x, box_y = 650, 550
box_path_index = None

while True:
    clock.tick(60)
    screen.fill((255, 255, 255))

    for k, v in paths.items():                                 #accessing key value pairs (tuples) from the paths dictionary.
        for rect in v['rectangles']:                           #iterating throught the rectangle coordinates in the dictionary.
            pygame.draw.rect(screen, v['color'], rect)

    pygame.draw.rect(screen, red, start)
    pygame.draw.rect(screen, green, end)

    text_related()
    draw_button()

    mouse_x, mouse_y = pygame.mouse.get_pos()               #storing x,y positions of mouse in a tuple.
    mouse_click = pygame.mouse.get_pressed()                #constantly updating the value of the variable. It is either 0 (not pressed) or 1.

    #checking if the mouse position is the same as the coordinates of the button and whether the button is getting pressed (having value 1) or not.
    if button_rect.collidepoint(mouse_x, mouse_y) and mouse_click[0] == 1:
        box_path_index = int(input("\nGuess the shortest paths among the three.\nEnter the path number (1, 2, or 3): ")) - 1

    if box_path_index is not None:
        target_path_name = list(paths.keys())[box_path_index]
        target_info = paths[target_path_name]
        target_rects = target_info['rectangles']
        target_rect = target_rects[0]

        # Move towards the target position
        if box_x < target_rect.x:
            box_x += 1
        elif box_x > target_rect.x:
            box_x -= 1
        elif box_y < target_rect.y:
            box_y += 1
        elif box_y > target_rect.y:
            box_y -= 1

        # Check if the box has reached the target position
        if (box_x, box_y) == (target_rect.x, target_rect.y):
            target_rects.pop(0)

            if not target_rects:
                distances = [path['distance_metre'] for path in paths.values()]
                shortest_path_name = min(paths, key=lambda k: paths[k]['distance_metre'])
                print('The chosen path was ' + str(target_path_name) + '.')
                if target_path_name == shortest_path_name:
                    print('This was the shortest path.')
                else:
                    print('This was not the shortest path. The shortest path is ' + str(shortest_path_name) + '.')
                for k, v in paths.items():
                    print(str(k) + ' is ' + str(round(v["distance_metre"], 1)) + ' metres or ' + str(round(v["distance_metre"] * 0.01, 1)) + ' kilometres.')
                box_path_index = None

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
