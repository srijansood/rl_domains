"""
Represents Gridworld with varying agent representations (as shapes)

"""
import pygame
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class params:
    grid_size = [10, 10]
    grid_to_pixel = 8
    img_size = [g * grid_to_pixel for g in grid_size] + [3]
    # shapes = "square" or "circle"
    agent_shape = "square"
    color = (255, 0, 0)

class ShapeWorld:

    ACTIONS = ["up", "down", "left", "right"]

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
        done = False

        # Set the HEIGHT and WIDTH of the screen (for pygame)
        WINDOW_SIZE = [255, 255]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        # Set title of screen
        pygame.display.set_caption("Shape-World")

        # Loop until the user clicks the close button.
        self.done = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # Initialize agent
        self.x = 0
        self.y = 0
        self.shape = params.agent_shape
        self.color = params.color

        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True

            # Set the screen background
            self.screen.fill(BLACK)

            # Draw the grid
            for row in range(10):
                for column in range(10):
                    color = WHITE
            self.draw_agent()

            # Limit to 60 frames per second
            self.clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

    def draw_agent(self):
        if self.shape == "circle":
            pygame.draw.circle(self.screen, self.color, [(self.margin + self.width) * self.x + self.margin,
                                               (self.margin + self.height) * self.y + self.margin], 10)
        else:
            pygame.draw.rect(self.screen,
                             self.color,
                             [(self.margin + self.width) * self.x + self.margin,
                              (self.margin + self.height) * self.y + self.margin,
                              self.width,
                              self.height])

    # def draw(self, screen_arr):
    #     # Set the screen background
    #     self.screen.fill(display.BLACK)
    #
    #     print(screen_arr)
    #
    #     # Draw the grid
    #     for row in range(self.grid_size[0]):
    #         for column in range(self.grid_size[1]):
    #             color = display.WHITE
    #
    #             pygame.draw.rect(self.screen,
    #                              color,
    #                              [(display.MARGIN + self.WIDTH) * column + display.MARGIN,
    #                               (display.MARGIN + self.HEIGHT) * row + display.MARGIN,
    #                               self.WIDTH,
    #                               self.HEIGHT])
    #
    #     # Limit to 60 frames per second
    #     self.clock.tick(60)
    #
    #     # Go ahead and update the screen with what we've drawn.
    #     pygame.display.flip()

    def quit(self):
        pygame.quit()


def main():
    """
    Test Method - wasd to move.
    """
    dom = ShapeWorld(params)
    # gui = display(fighter.grid_size, fighter.grid_to_pixel)
    # gui.draw(fighter)
    # # print("New Instance: Agent: ", fighter.agent, "Fire(s): ", fighter.fire, " Water(s): ", fighter.water)
    # inp = None
    # while (inp != "l"):
    #     pass
    #     # inp = raw_input("Input: ")
    #     # mapping = {"a": 0, "d": 1, "w": 2, "s": 3, "z": 4, "x": 5}
    #     # if inp in mapping:
    #     #     fighter.execute_action(mapping[inp])
    #     #     gui.draw(fighter.disp_arr)
    #     # elif inp == 'l':
    #     #     print("Quitting")
    #     # else:
    #     #     print("Illegal")
    #     #     # print("Agent: " , fighter.agent, "Fire: ", fighter.fire , " Water: ", fighter.water, " Has Water: ", fighter.has_water)
    # gui.quit()

    # TODO: add -d flag for display mode


if __name__ == "__main__":
    main()