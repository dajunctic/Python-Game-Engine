import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import *


class GraphicsEngine:
    def __init__(self, win_size=(1280, 720)):
        pg.init()

        self.WIN_SIZE = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        pg.display.set_caption("Unity Python")

        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

        self.clock = pg.time.Clock()
        self.time = 0

        self.camera = Camera(self)
        self.scene = Cube(self)


    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18, 1))

        self.scene.render()
        # swap buffer
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.render()
            self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
