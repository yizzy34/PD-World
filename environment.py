
class Environment:
    def __init__(self):
        firstLevel = [
            [
                {'type': 'normal', 'reward': -1, 'occupiedBy': 'f'},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'dropoff', 'reward': +14, 'occupiedBy': '', 'blockCount': 0}
            ],
            [
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'pickup', 'reward': +14, 'occupiedBy': '', 'blockCount': 10},
                {'type': 'risky', 'reward': -2, 'occupiedBy': ''}
            ],
            [
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''}
            ]
        ]
        secondLevel = [
            [
                {'type': 'dropoff', 'reward': +14, 'occupiedBy': '', 'blockCount': 0},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''}
            ],
            [
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'risky', 'reward': -2, 'occupiedBy': ''},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''}
            ],
            [
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'pickup', 'reward': +14, 'occupiedBy': '', 'blockCount': 10}
            ]
        ]
        thirdLevel = [
            [
                {'type': 'dropoff', 'reward': +14, 'occupiedBy': '', 'blockCount': 0},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''}
            ],
            [
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'dropoff', 'reward': +14, 'occupiedBy': 'm', 'blockCount': 0}
            ],
            [
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''},
                {'type': 'normal', 'reward': -1, 'occupiedBy': ''}
            ]
        ]
        self.environment = [firstLevel, secondLevel, thirdLevel]

    def move_Agent(self, oldCoordinates, action, agent):
        self.environment[oldCoordinates[0]][oldCoordinates[1]][oldCoordinates[2]]['occupiedBy'] = ''
        newCoordinates = []

        if action == 'up':
            self.environment[oldCoordinates[0] + 1][oldCoordinates[1]][oldCoordinates[2]]['occupiedBy'] = agent
            newCoordinates = [oldCoordinates[0] + 1, oldCoordinates[1], oldCoordinates[2]]
        elif action == 'down':
            self.environment[oldCoordinates[0] - 1][oldCoordinates[1]][oldCoordinates[2]]['occupiedBy'] = agent
            newCoordinates = [oldCoordinates[0] - 1, oldCoordinates[1], oldCoordinates[2]]
        elif action == 'north':
            self.environment[oldCoordinates[0]][oldCoordinates[1] + 1][oldCoordinates[2]]['occupiedBy'] = agent
            newCoordinates = [oldCoordinates[0], oldCoordinates[1] + 1, oldCoordinates[2]]
        elif action == 'south':
            self.environment[oldCoordinates[0]][oldCoordinates[1] - 1][oldCoordinates[2]]['occupiedBy'] = agent
            newCoordinates = [oldCoordinates[0], oldCoordinates[1] - 1, oldCoordinates[2]]
        elif action == 'east':
            self.environment[oldCoordinates[0]][oldCoordinates[1]][oldCoordinates[2] + 1]['occupiedBy'] = agent
            newCoordinates = [oldCoordinates[0], oldCoordinates[1], oldCoordinates[2] + 1]
        elif action == 'west':
            self.environment[oldCoordinates[0]][oldCoordinates[1]][oldCoordinates[2] - 1]['occupiedBy'] = agent
            newCoordinates = [oldCoordinates[0], oldCoordinates[1], oldCoordinates[2] - 1]

        if self.environment[newCoordinates[0]][newCoordinates[1]][newCoordinates[2]]['type'] == 'pickup':
            self.remove_Pickup_Block(newCoordinates)
        elif self.environment[newCoordinates[0]][newCoordinates[1]][newCoordinates[2]]['type'] == 'dropoff':
            self.add_Dropoff_Block(newCoordinates)
        elif self.environment[newCoordinates[0]][newCoordinates[1]][newCoordinates[2]]['type'] == 'normal':
            pass
        elif self.environment[newCoordinates[0]][newCoordinates[1]][newCoordinates[2]]['type'] == 'risky':
            pass

    def remove_Pickup_Block(self, coords):
        if self.environment[coords[0]][coords[1]][coords[2]]['blockCount'] > 0:
            self.environment[coords[0]][coords[1]][coords[2]]['blockCount'] -= 1

    def add_Dropoff_Block(self, coords):
        if self.environment[coords[0]][coords[1]][coords[2]]['blockCount'] < 5:
            self.environment[coords[0]][coords[1]][coords[2]]['blockCount'] += 1


def get_Cell_Types(environment, initial_position, actions):
    cells = {}
    for action in actions:
        match action:
            case 'up':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0] + 1][initial_position[1]][initial_position[2]][
                    'type']
                cells[action]['coords'] = [initial_position[0] + 1, initial_position[1], initial_position[2]]
            case 'down':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0] - 1][initial_position[1]][initial_position[2]][
                    'type']
                cells[action]['coords'] = [initial_position[0] - 1, initial_position[1], initial_position[2]]
            case 'backward':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0]][initial_position[1] + 1][initial_position[2]][
                    'type']
                cells[action]['coords'] = [initial_position[0], initial_position[1] + 1, initial_position[2]]
            case 'forward':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0]][initial_position[1] - 1][initial_position[2]][
                    'type']
                cells[action]['coords'] = [initial_position[0], initial_position[1] - 1, initial_position[2]]
            case 'right':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0]][initial_position[1]][initial_position[2] + 1][
                    'type']
                cells[action]['coords'] = [initial_position[0], initial_position[1], initial_position[2] + 1]
            case 'left':
                cells[action] = {}
                cells[action]['type'] = environment[initial_position[0]][initial_position[1]][initial_position[2] - 1][
                    'type']
                cells[action]['coords'] = [initial_position[0], initial_position[1], initial_position[2] - 1]
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
    return cells
