"""
Represents Gridworld with varying agent representations (as shapes)

"""
import pygame
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ACTIONS = ["up", "down", "left", "right"]


class params:
    grid_size = [10, 10]
    grid_to_pixel = 8
    img_size = [g * grid_to_pixel for g in grid_size] + [3]
    # shapes = "square" or "circle"
    agent_shape = "circle"
    color = (255, 0, 0)


class ShapeWorld:

    def __init__(self, params):
        self.grid_size = params.grid_size
        self.screen_size = params.img_size
        self.ratio = params.grid_to_pixel

        # Cell Propertiess
        self.margin = 0
        self.width = (self.screen_size[0] / self.grid_size[0]) - self.margin - (self.margin / self.grid_size[0])
        self.height = (self.screen_size[1] / self.grid_size[1]) - self.margin - (self.margin / self.grid_size[1])

        # Initialize grid
        self.grid = []
        for r in range(self.grid_size[0]):
            self.grid.append([])
            for c in range(self.grid_size[1]):
                self.grid[r].append(0)

        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen (for pygame)
        WINDOW_SIZE = self.screen_size[0:2]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        # Set title of screen
        pygame.display.set_caption("Shape-World")
        self.screen.fill(BLACK)

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        self.clock.tick(60) # 60fps

        # Initialize agent
        self.x = 0
        self.y = 0
        self.shape = params.agent_shape
        self.color = params.color
        self.draw_agent()
        self.steps = 0

        pygame.display.flip()

    def draw_agent(self):
        if self.shape == "circle":
            rad = self.ratio/2
            pygame.draw.circle(self.screen, self.color, [(self.margin + self.width) * self.y + self.margin + rad,
                                               (self.margin + self.height) * self.x + self.margin + rad], rad)
        else:
            pygame.draw.rect(self.screen,
                             self.color,
                             [(self.margin + self.width) * self.y + self.margin,
                              (self.margin + self.height) * self.x + self.margin,
                              self.width,
                              self.height])

    def grab_screen(self):
        return pygame.surfarray.array3d(self.screen)

    def frame_step(self, input_actions):
        """
        :param input_actions: One-hot encoding of actions (eg. up = [1, 0, 0, 0])
        :return: (next_state, reward)
        """
        self.steps += 1
        self.screen.fill(BLACK)

        if input_actions[0] == 1: # up
            if self.y > 0:
                self.y -= 1
        elif input_actions[1] == 1: # down
            if self.y < self.grid_size[1] - 1:
                self.y += 1
        elif input_actions[2] == 1: # left
            if self.x > 0:
                self.x -= 1
        elif input_actions[3] == 1: # right
            if self.x < self.grid_size[0] - 1:
                self.x += 1
        self.draw_agent()

        return self.grab_screen(), 0

    def quit(self):
        pygame.quit()

def main():
    """
    For Testing
    """
    test = False
    if test:
        domain = ShapeWorld(params)
        res = domain.grab_screen()

        from PIL import Image
        Image.fromarray(res).show()

        up = [1, 0, 0, 0]
        down = [0, 1, 0, 0]
        left = [0, 0, 1, 0]
        right = [0, 0, 0, 1]

        test_seq = [up, down, down, left, right, right, down, left, up, right]
        for action in test_seq:
            _ = raw_input("Press to move {}".format(action))
            res, _ = domain.frame_step(action)
            print(domain.x, domain.y)
            Image.fromarray(res).show()

        domain.quit()

if __name__ == "__main__":
    main()