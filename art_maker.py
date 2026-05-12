import pygame
import math as m

dictionary = {
    "A": 13,
    "B": 26,
    "C": 39,
    "D": 52,
    "E": 65,
    "F": 78,
    "G": 91,
    "H": 104,
    "I": 117,
    "J": 130,
    "K": 143,
    "L": 156,
    "M": 169,
    "N": 182,
    "O": 195,
    "P": 208,
    "Q": 221,
    "R": 234,
    "S": 247,
    "T": 260,
    "U": 273,
    "V": 286,
    "W": 299,
    "X": 312,
    "Y": 325,
    "Z": 338,
}

class Turtle():
    def __init__(self, color, angle, mirror_x=False, mirror_y=False, pos=(306, 396), size = 3,):
        self.pos = pos
        self.size = size
        self.color = color
        self.pos_list = [pos]
        self.surface = self.update_surface()
        self.angle = angle
        self.mirror_x = mirror_x
        self.mirror_y = mirror_y


    
    def update(self, angle):
        if self.mirror_x == True and self.mirror_y == False:
            self.pos = ((self.pos[0] + m.cos(m.radians(-1*angle))), (self.pos[1] + m.sin(m.radians(angle))))
        elif self.mirror_x == False and self.mirror_y == True:
            self.pos = ((self.pos[0] + m.cos(m.radians(angle))), (self.pos[1] + m.sin(m.radians(-1*angle))))
        elif self.mirror_x == True and self.mirror_y == True:
            self.pos = ((self.pos[0] + m.cos(m.radians(-1*angle))), (self.pos[1] + m.sin(m.radians(-1*angle))))
        else:
            self.pos = ((self.pos[0] + m.cos(m.radians(angle))), (self.pos[1] + m.sin(m.radians(angle))))
        self.pos_list.append(self.pos)
        return self.pos_list

    
    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class TurtleContainer():
    def __init__(self, screen, colors, letters):
        self.colors = colors
        self.turtles = [Turtle(self.colors[0], letters[0]), 
                        Turtle(self.colors[1], letters[0], mirror_x=True), 
                        Turtle(self.colors[2], letters[0], mirror_y=True), 
                        Turtle(self.colors[3], letters[0], mirror_x=True, mirror_y=True)]
        self.lists = [[(0,0)], [(0,0)], [(0,0)], [(0,0)]]
        self.screen = screen
        self.letters = letters
    
    def update(self, gt, counter):
        length = len(self.letters)
        runtime = length * 120
        steps = list(range(120, runtime, 120))
        try:
            if gt > steps[counter]:
                counter += 1
        except IndexError:
            pass
        self._update_turtles(self.letters[counter])
        return counter

    def _update_turtles(self, angle):
        for idx, turtle in enumerate(self.turtles):
            self.lists[idx] = turtle.update(angle)

    def draw(self, screen):
        for turtle in self.turtles:
            turtle.draw(screen)
        for idx, list in enumerate(self.lists):
            pygame.draw.aalines(screen, self.colors[idx], False, list)

            
def color_checker(in_color):
    list = []
    colors = in_color.replace(",", " ").split()
    for color in colors:
        while True:
            try:
                valid_color = pygame.Color(color)
                list.append(valid_color)
            except ValueError:
                print(f"Sorry, we couldn't find color: {color}. Please try that color again.")
                color = input().lower()
                continue
            break
    if len(list) > 4:
        list = list[:4]
    elif len(list) < 4:
        list.append(list[0])
        list.append(list[1])
        list.append(list[2])
        list.append(list[3])
        list = list[:4]
    return list

def word_handler(word):
    list = []
    for letter in word:
        if letter in dictionary:
            list.append(dictionary[letter])
    return list


def main():
    word = input("What word(s) should we draw?").upper().strip()
    letters = word_handler(word)
    colors = input("What color(s) would you like?").lower()
    color_list = color_checker(colors)
    pygame.init()
    pygame.display.set_caption("trA rorriM")
    clock = pygame.time.Clock()
    dt = 0
    gt = 0
    counter = 0
    resolution = (612, 792) #72dpi 8.5x11 paper sized
    screen = pygame.display.set_mode(resolution)
    turtles = TurtleContainer(screen, color_list, letters)
    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
        #Game logic
        counter = turtles.update(gt, counter)
        gt += 1
        # Render & Display
        white = pygame.Color(255, 255, 255)
        screen.fill(white)
        turtles.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30)
    pygame.quit()



if __name__ == "__main__":
    main()