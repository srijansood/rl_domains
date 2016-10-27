"""
Represents Gridworld with varying agent representations (as shapes)

"""
from display import display

class params:
    grid_size = [10, 10]
    grid_to_pixel = 8
    img_size = [g * grid_to_pixel for g in grid_size] + [3]
    # shapes = "square" or "circle"
    agent_shape = "square"

class ShapeWorld:

    ACTIONS = ["up", "down", "left", "right"]

    def __init__(self, params):
        self.grid_size = params.grid_size
        self.screen_size = params.img_size
        self.grid_to_pixel = params.grid_to_pixel


def main():
    """
    Test Method - wasd to move.
    """
    fighter = ShapeWorld(params)
    gui = display(fighter.grid_size, fighter.grid_to_pixel)
    gui.draw(fighter)
    # print("New Instance: Agent: ", fighter.agent, "Fire(s): ", fighter.fire, " Water(s): ", fighter.water)
    inp = None
    while (inp != "l"):
        pass
        # inp = raw_input("Input: ")
        # mapping = {"a": 0, "d": 1, "w": 2, "s": 3, "z": 4, "x": 5}
        # if inp in mapping:
        #     fighter.execute_action(mapping[inp])
        #     gui.draw(fighter.disp_arr)
        # elif inp == 'l':
        #     print("Quitting")
        # else:
        #     print("Illegal")
        #     # print("Agent: " , fighter.agent, "Fire: ", fighter.fire , " Water: ", fighter.water, " Has Water: ", fighter.has_water)
    gui.quit()

    # TODO: add -d flag for display mode


if __name__ == "__main__":
    main()