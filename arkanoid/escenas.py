from curses import KEY_DOWN
import os

import pygame as pg

from . import ANCHO, ALTO, COLOR_FONDO_PORTADA, COLOR_MENSAJE, FPS
from .entidades import Pelota, Raqueta, Ladrillo


class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        """
        Este método debe ser implementado por cada una de las escenas,
        en función de lo que estén esperando hasta la condición de salida.
        """
        pass


class Portada(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

        self.logo = pg.image.load(os.path.join(
            "resources", "images", "arkanoid_name.png"))

        # asignamos la ruta de la fuente a una variable con el metodo os path
        font_file = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(font_file, 40)

    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    print("salimos de portada")
                    salir = True

                if event.type == pg.QUIT:
                    pg.quit()

            self.pantalla.fill(COLOR_FONDO_PORTADA)

            self.pintar_logo()
            self.pintar_texto()

            pg.display.flip()

    def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo)/2
        pos_y = (ALTO / 3)
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_texto(self):
        mensaje = "Pulsa espacio para empezar"
        texto = self.tipografia.render(mensaje, True, COLOR_MENSAJE)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto) / 2  # ANCHO / 2 - ancho_texto / 2
        pos_y = 3/4 * ALTO                 # posición vertical a tres cuartas del alto, abajo
        self.pantalla.blit(texto, (pos_x, pos_y))


class Partida(Escena):
    """
1. Cargar la imagen de fondo en memoria , done
2. creamos una función para "pintar Fondo"
3. Llamar a la función "pintar_fondo" en el bucle principal para que el fondo se pinte
4. 
    """

    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        bg_file = os.path.join("resources", "images", "background.jpg")
        self.fondo = pg.image.load(bg_file)
        self.jugador = Raqueta()
        self.crear_muro()
        self.pelotita = Pelota(midbottom=self.jugador.rect.midtop)

    def bucle_principal(self):
        salir = False
        partida_iniciada = False
        while not salir:
            self.reloj.tick(FPS)
            self.jugador.update()
            self.pelotita.update(self.jugador, partida_iniciada)
            self.pelotita.hay_colision(self.jugador)
            golpeados = pg.sprite.spritecollide(
                self.pelotita, self.ladrillos, True)
            if len(golpeados) > 0:
                self.pelotita.velocidad_y *= -1
                # para los ladrillos golpeados, sumar puntuacion
                # for ladrillo in golpeados:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    partida_iniciada = True

            self.pantalla.fill((0, 0, 66))
            self.pintar_fondo()

            # pintar la raqueta
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            # pintar el muro
            self.ladrillos.draw(self.pantalla)

            # pintar la pelota
            self.pantalla.blit(self.pelotita.image, self.pelotita.rect)

            pg.display.flip()

    def pintar_fondo(self):
        self.pantalla.blit(self.fondo, (0, 0))

    def crear_muro(self):
        num_filas = 5
        num_columnas = 6
        self.ladrillos = pg.sprite.Group()
        self.ladrillos.empty()
        margen_y = 40

        for fila in range(num_filas):
            for columna in range(num_columnas):
                ladrillo = Ladrillo(fila, columna)
                margen_x = (ANCHO - ladrillo.image.get_width()
                            * num_columnas) // 2
                ladrillo.rect.x += margen_x
                ladrillo.rect.y += margen_y
                self.ladrillos.add(ladrillo)


class HallOfFame(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
