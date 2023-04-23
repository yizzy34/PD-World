class Environment:
    def __init__(self):
        self.environment = [
            [
                [{'type': 'normal', 'occupied_by': 'f'}, {'type': 'normal', 'occupied_by': ''}, {'type': 'dropoff', 'occupied_by': '', 'block_count': 0}],
                [{'type': 'normal', 'occupied_by': ''}, {'type': 'pickup', 'occupied_by': '', 'block_count': 10}, {'type': 'risky', 'occupied_by': ''}],
                [{'type': 'normal', 'occupied_by': ''}, {'type': 'normal', 'occupied_by': ''}, {'type': 'normal', 'occupied_by': ''}]
            ],
            [
                [{'type': 'dropoff', 'occupied_by': '', 'block_count': 0}, {'type': 'normal', 'occupied_by': ''}, {'type': 'normal', 'occupied_by': ''}],
                [{'type': 'normal', 'occupied_by': ''}, {'type': 'risky', 'occupied_by': ''}, {'type': 'normal', 'occupied_by': ''}],
                [{'type': 'normal', 'occupied_by': ''}, {'type': 'normal', 'occupied_by': ''}, {'type': 'pickup', 'occupied_by': '', 'block_count': 10}]
            ],
            [
                [{'type': 'dropoff', 'occupied_by': '', 'block_count': 0}, {'type': 'normal', 'occupied_by': ''}, {'type': 'normal', 'occupied_by': ''}],
                [{'type': 'normal', 'occupied_by': ''}, {'type': 'normal', 'occupied_by': ''}, {'type': 'dropoff', 'occupied_by': 'm', 'block_count': 0}],
                [{'type': 'normal', 'occupied_by': ''}, {'type': 'normal', 'occupied_by': ''}, {'type': 'normal', 'occupied_by': ''}]
            ]
        ]

    def move_Agent(self, old_coords, action, agent):
        self.environment[old_coords[0]][old_coords[1]][old_coords[2]]['occupied_by'] = ''
        action_moves = {'up': (1, 0, 0), 'down': (-1, 0, 0), 'forward': (0, 1, 0), 'backward': (0, -1, 0),
                        'right': (0, 0, 1), 'left': (0, 0, -1)}
        move = action_moves[action]
        new_coords = [old_coords[i] + move[i] for i in range(3)]
        self.environment[new_coords[0]][new_coords[1]][new_coords[2]]['occupied_by'] = agent

        cell_type = self.environment[new_coords[0]][new_coords[1]][new_coords[2]]['type']
        if cell_type == 'pickup':
            self.remove_Pickup_Block(new_coords)
        elif cell_type == 'dropoff':
            self.add_Dropoff_Block(new_coords)

    def remove_Pickup_Block(self, coords):
        if self.environment[coords[0]][coords[1]][coords[2]]['block_count'] > 0:
            self.environment[coords[0]][coords[1]][coords[2]]['block_count'] -= 1

    def add_Dropoff_Block(self, coords):
        if self.environment[coords[0]][coords[1]][coords[2]]['block_count'] < 5:
            self.environment[coords[0]][coords[1]][coords[2]]['block_count'] += 1

    def get_Cell_Types(environment, initial_position, actions):
        cells = {}
        action_moves = {'up': (1, 0, 0), 'down': (-1, 0, 0), 'forward': (0, 1, 0), 'backward': (0, -1, 0),
                        'right': (0, 0, 1), 'left': (0, 0, -1)}
        for action in actions:
            move = action_moves[action]
            new_coords = [initial_position[i] + move[i] for i in range(3)]
            cell = environment[new_coords[0]][new_coords[1]][new_coords[2]]
            cells[action] = {}
            cells[action]['type'] = cell['type']
            cells[action]['coords'] = new_coords
            if cell['type'] == 'pickup':
                cells[action]['is_empty'] = cell['block_count'] == 0
            elif cell['type'] == 'dropoff':
                cells[action]['is_full'] = cell['block_count'] >= 5
        return cells
