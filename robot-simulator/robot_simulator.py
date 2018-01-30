EAST, NORTH, WEST, SOUTH = range(4)
ADVANCES = {EAST: (1, 0), NORTH: (0, 1), WEST: (-1, 0), SOUTH: (0, -1)}


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    def turn_right(self):
        self.bearing = (self.bearing - 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing + 1) % 4

    def advance(self):
        x, y = ADVANCES[self.bearing]
        self.x += x
        self.y += y

    def simulate(self, cmds):
        commands_map = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance,
        }
        for cmd in cmds:
            commands_map[cmd]()

    @property
    def coordinates(self):
        return self.x, self.y
