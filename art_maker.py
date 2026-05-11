import pygame


class Turtle():
    def __init__(self, pos=(306, 396), size = 15, color = "Red", modifier_x = 1, modifier_y = 1):
        self.pos = pos
        self.size = size
        self.color = color
        self.pos_list = [pos]
        self.surface = self.update_surface()
        self.modifier_x = modifier_x
        self.modifier_y = modifier_y
    
    def update(self):
        #TODO: update position over time
        self.pos = ((self.pos[0] + self.modifier_x), (self.pos[1] + self.modifier_y))
        self.pos_list.append(self.pos)
        return self.pos_list

    
    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)
        
        

def main():
    pygame.init()
    pygame.display.set_caption("trA rorriM")
    clock = pygame.time.Clock()
    dt = 0
    pos_list = []
    pos_list2 = []
    pos_list3 = []
    pos_list4 = []
    resolution = (612, 792) #72dpi 8.5x11 paper sized
    screen = pygame.display.set_mode(resolution)
    turtle = Turtle((306, 396), 3, "Red", 1, 1)
    turtle2 = Turtle((306, 396), 3, "Blue", -1, 1)
    turtle3 = Turtle((306, 396), 3, "Green", 1, -1)
    turtle4 = Turtle((306, 396), 3, "Purple", -1, -1)
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
        # Render & Display
        white = pygame.Color(255, 255, 255)
        screen.fill(white)
        pos_list = turtle.update()
        pos_list2 = turtle2.update()
        pos_list3 = turtle3.update()
        pos_list4 = turtle4.update()
        turtle.draw(screen)
        turtle2.draw(screen)
        turtle3.draw(screen)
        turtle4.draw(screen)
        pygame.draw.aalines(screen, "Red", False, pos_list)
        pygame.draw.aalines(screen, "Blue", False, pos_list2)
        pygame.draw.aalines(screen, "Green", False, pos_list3)
        pygame.draw.aalines(screen, "Purple", False, pos_list4)
        pygame.display.flip()
        dt = clock.tick(30)
    pygame.quit()



if __name__ == "__main__":
    main()