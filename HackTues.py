import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHTO NE TRUGWA")

def main():

    run = True 
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill((255,255,255))
        pygame.display.update()
    pygame.quit()

if __name__ == "__HackTues__":
    main()