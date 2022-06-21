import pygame as pg
from arkanoid import ALTO, ANCHO


class Arkanoid:
    def __init__(self) -> None:
        print("Arranca el juego!!")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Arkanoid BZ 11 Versión")
        icon = pg.image.load("resources/images/icon.png")
        pg.display.set_icon(icon)

    def jugar(self):
        """Esto es el bucle principal"""
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.display.fill((99, 99, 99))
            pg.display.flip()


if __name__ == "__main__":
    Arkanoid()
