import pygame
from arkanoid import ALTO, ANCHO

class Arkanoid:
    def __init__(self) -> None:
        print("Arranca el juego!!")
        pygame.init()
        self.display = pygame.display.set_mode((ANCHO, ALTO))
    
    def jugar(self):
        """Esto es el bucle principal"""
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir = True
            self.display.fill((99, 99, 99))
            pygame.display.flip()


if __name__ == "__main__":
    Arkanoid()