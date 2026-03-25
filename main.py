import pyglet
from pyglet.window import key
from planet import *
from spaceship import *
from pyglet.graphics import Batch
class Window(pyglet.window.Window):
    def __init__(self, width, height, name):
        super().__init__(width, height, name, resizable=True)
        self.width = width
        self.height = height
        self.G =100
        self.batch = Batch()
        self.planet = Planet(self.width//2, self.height//2, 100, 100, color=(255, 76, 148), batch=self.batch)
        self.a1 = Spaceship(self.width//3, 400, 0, 2, 1, 10, visible=True, color=(50, 225, 30), batch=self.batch)
        self.spaceships = [self.a1]
        self.startMousex = 0
        self.startMousey = 0
        self.deltax = 0
        self.deltay = 0
    def on_draw(self):
        self.clear()
        self.planet.draw()
        for ship in self.spaceships:
            ship.draw()
    def on_mouse_press(self, x, y, button, modifiers):
        self.startMousex = x
        self.startMousey = y
    def on_mouse_release(self, x, y, button, modifiers):
        self.deltax = self.startMousex - x
        self.deltay = y - self.startMousey
        self.add_obj(self.deltax, self.deltay)
    def add_obj(self, deltax, deltay):
        self.spaceships.append(Spaceship(self.startMousex, self.startMousey, deltax//2, deltay//2, 10, 10, visible=True, color=(255,45, 175)))
    def update(self, dt):
        for ship in self.spaceships:
            ship.move(self, other=self.planet)

if __name__ == "__main__":
    screen = Window(800, 1000, "3 body program")
    pyglet.clock.schedule_interval(screen.update, 1/60.0)
    pyglet.app.run()
