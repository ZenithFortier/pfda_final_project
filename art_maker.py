import pygame

class Turtle():
    def __init__(self, color, modifier_x = 1, modifier_y = 1, pos=(306, 396), size = 3,):
        self.pos = pos
        self.size = size
        self.color = color
        self.pos_list = [pos]
        self.surface = self.update_surface()
        self.modifier_x = modifier_x
        self.modifier_y = modifier_y
    
    def update(self):
        #TODO: curves
        self.pos = ((self.pos[0] + self.modifier_x), (self.pos[1] + self.modifier_y))
        self.pos_list.append(self.pos)
        return self.pos_list

    
    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class TurtleContainer():
    def __init__(self, screen):
        self.colors = ["Red", "Blue", "Green", "Purple"]
        self.turtles = [Turtle(self.colors[0], 1, 1), 
                        Turtle(self.colors[1], -1, 1), 
                        Turtle(self.colors[2], 1, -1), 
                        Turtle(self.colors[3], -1, -1)]
        self.lists = [[(0,0)], [(0,0)], [(0,0)], [(0,0)]]
        self.screen = screen
    
    def update(self):
        self._update_turtles()

    def _update_turtles(self):
        for idx, turtle in enumerate(self.turtles):
            self.lists[idx] = turtle.update()

    def draw(self, screen):
        for turtle in self.turtles:
            turtle.draw(screen)
        for idx, list in enumerate(self.lists):
            pygame.draw.aalines(screen, self.colors[idx], False, list)
            


def main():
    pygame.init()
    pygame.display.set_caption("trA rorriM")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (612, 792) #72dpi 8.5x11 paper sized
    screen = pygame.display.set_mode(resolution)
    turtles = TurtleContainer(screen)
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
        turtles.update()
        # Render & Display
        white = pygame.Color(255, 255, 255)
        screen.fill(white)
        turtles.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30)
    pygame.quit()



if __name__ == "__main__":
    main()