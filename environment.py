class Environment:
    def __init__(self):
        # Define the environment with 3 levels, each level is a 3x3 grid with different types of cells
        first_level = [
            [
                {'type': 'normal', 'occupied_by': 'f'},
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'dropoff', 'occupied_by': '', 'block_count': 0}
            ],
            [
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'pickup', 'occupied_by': '', 'block_count': 10},
                {'type': 'risky', 'occupied_by': ''}
            ],
            [
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'normal', 'occupied_by': ''}
            ]
        ]
        second_level = [
            [
                {'type': 'dropoff', 'occupied_by': '', 'block_count': 0},
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'normal', 'occupied_by': ''}
            ],
            [
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'risky', 'occupied_by': ''},
                {'type': 'normal', 'occupied_by': ''}
            ],
            [
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'pickup', 'occupied_by': '', 'block_count': 10}
            ]
        ]
        third_level = [
            [
                {'type': 'dropoff', 'occupied_by': '', 'block_count': 0},
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'normal', 'occupied_by': ''}
            ],
            [
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'dropoff', 'occupied_by': 'm', 'block_count': 0}
            ],
            [
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'normal', 'occupied_by': ''},
                {'type': 'normal', 'occupied_by': ''}
            ]
        ]
        self.environment = [first_level, second_level, third_level]

    def move_agent(self, old_coords, action, agent, carrying):
        # Set the cell that the agent is moving from as unoccupied
        self.environment[old_coords[0]][old_coords[1]][old_coords[2]]['occupied_by'] = ''
        new_coords = []
        # Set the new cell that the agent is moving to as occupied by the agent
        match action:
            case 'up':
                self.environment[old_coords[0] + 1][old_coords[1]][old_coords[2]]['occupied_by'] = agent
                new_coords = [old_coords[0] + 1, old_coords[1], old_coords[2]]
            case 'down':
                self.environment[old_coords[0] - 1][old_coords[1]][old_coords[2]]['occupied_by'] = agent
                new_coords = [old_coords[0] - 1, old_coords[1], old_coords[2]]
            case 'backward':
                self.environment[old_coords[0]][old_coords[1] + 1][old_coords[2]]['occupied_by'] = agent
                new_coords = [old_coords[0], old_coords[1] + 1, old_coords[2]]
            case 'forward':
                self.environment[old_coords[0]][old_coords[1] - 1][old_coords[2]]['occupied_by'] = agent
                new_coords = [old_coords[0], old_coords[1] - 1, old_coords[2]]
            case 'right':
                self.environment[old_coords[0]][old_coords[1]][old_coords[2] + 1]['occupied_by'] = agent
                new_coords = [old_coords[0], old_coords[1], old_coords[2] + 1]
            case 'left':
                self.environment[old_coords[0]][old_coords[1]][old_coords[2] - 1]['occupied_by'] = agent
                new_coords = [old_coords[0], old_coords[1], old_coords[2] - 1]
        match self.environment[new_coords[0]][new_coords[1]][new_coords[2]]['type']:
            case 'pickup':
                if carrying == False:
                    return self.remove_pickup_block(new_coords)
            case 'dropoff':
                if carrying:
                    return self.add_dropoff_block(new_coords)
            case 'normal':
                return False
            case 'risky':
                return False

    def remove_pickup_block(self, coords):
        """
        Removes a block from a pickup cell in the environment at the given coordinates.

        Args:
            coords: A list of three integers representing the (x, y, z) coordinates of the cell in the environment.

        Returns:
            A boolean indicating whether a block was successfully removed from the cell.
        """
        if self.environment[coords[0]][coords[1]][coords[2]]['block_count'] > 0:
            self.environment[coords[0]][coords[1]][coords[2]]['block_count'] -= 1
            return True
        return False

    def add_dropoff_block(self, coords):
        """
        Adds a block to a dropoff cell in the environment at the given coordinates.

        Args:
            coords: A list of three integers representing the (x, y, z) coordinates of the cell in the environment.

        Returns:
            A boolean indicating whether a block was successfully added to the cell.
        """
        if self.environment[coords[0]][coords[1]][coords[2]]['block_count'] < 5:
            self.environment[coords[0]][coords[1]][coords[2]]['block_count'] += 1
            return True
        return False


def get_cell_types(environment, initial_position, actions):
    # create an empty dictionary to hold the cell types
    cells = {}
    # loop through each action provided
    for action in actions:
        # determine the type of cell in the direction of the current action
        match action:
            case 'up':
                cells[action] = {}
                # store the cell type and coordinates in the cells dictionary
                cells[action]['type'] = environment[initial_position[0] + 1][initial_position[1]][initial_position[2]]['type']
                cells[action]['coords'] = [initial_position[0] + 1, initial_position[1], initial_position[2]]
            case 'down':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0] - 1][initial_position[1]][initial_position[2]]['type']
                cells[action]['coords'] = [initial_position[0] - 1, initial_position[1], initial_position[2]]
            case 'backward':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0]][initial_position[1] + 1][initial_position[2]]['type']
                cells[action]['coords'] = [initial_position[0], initial_position[1] + 1, initial_position[2]]
            case 'forward':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0]][initial_position[1] - 1][initial_position[2]]['type']
                cells[action]['coords'] = [initial_position[0], initial_position[1] - 1, initial_position[2]]
            case 'right':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0]][initial_position[1]][initial_position[2] + 1]['type']
                cells[action]['coords'] = [initial_position[0], initial_position[1], initial_position[2] + 1]
            case 'left':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0]][initial_position[1]][initial_position[2] - 1]['type']
                cells[action]['coords'] = [initial_position[0], initial_position[1], initial_position[2] - 1]
        # check if the cell is a pickup or dropoff location and if it's empty or full
        coords = cells[action]['coords']
        if cells[action]['type'] == 'pickup':
            if environment[coords[0]][coords[1]][coords[2]]['block_count'] > 0:
                cells[action]['is_empty'] = False
            else:
                cells[action]['is_empty'] = True
        elif cells[action]['type'] == 'dropoff':
            if environment[coords[0]][coords[1]][coords[2]]['block_count'] < 5:
                cells[action]['is_full'] = False
            else:
                cells[action]['is_full'] = True
    # return the dictionary of cell types
    return cells
