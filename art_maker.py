import pygame

#TODO: recreate turtle logic into class object(s)
#Remaking turtle in pygame will be easier than learning enough tkinter to make surrounding application with default turtle module 

def main():
    pygame.init()
    pygame.display.set_caption("trA rorriM")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (612, 792) #72dpi 8.5x11 paper sized
    screen = pygame.display.set_mode(resolution)
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
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        pygame.display.flip()
        dt = clock.tick(30)
    pygame.quit()



if __name__ == "__main__":
    main()