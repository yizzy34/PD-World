
class CustomEnvironment:
    def __init__(self, grid_size_x, grid_size_y, grid_size_z, risky_cells, male_initial_pos, female_initial_pos,
                 pickup_cells, dropoff_cells):
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.grid_size_z = grid_size_z
        self.risky_cells = set(risky_cells)
        self.male_initial_pos = male_initial_pos
        self.female_initial_pos = female_initial_pos
        self.pickup_cells = {cell: 10 for cell in pickup_cells}  # Initialize pickup cells with 10 blocks
        self.dropoff_cells = {cell: 0 for cell in dropoff_cells}  # Initialize dropoff cells with 0 blocks
        self.dropoff_capacity = 5  # Capacity for dropoff cells
        self.state = (self.female_initial_pos, self.male_initial_pos)  # Initialize the environment state

    def get_n_states(self):
        return self.grid_size_x * self.grid_size_y * self.grid_size_z

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.female_pos, self.male_pos = state

    def take_action(self, agent_type, action):
        # Get the agent's current position
        if agent_type == 'M':
            current_position = self.state[1]  # Get male agent's position from the state
        elif agent_type == 'F':
            current_position = self.state[0]  # Get female agent's position from the state

        # Calculate the new position based on the action
        new_position = self._apply_action(current_position, action)

        # Update the agent's position
        if agent_type == 'M':
            self.state = (self.state[0], new_position)
        elif agent_type == 'F':
            self.state = (new_position, self.state[1])

        # Check if the new_position is a risky cell
        if new_position in self.risky_cells:
            reward = -2  # Return twice the negative reward for any action in risky cells
        # Check if the new_position is a pickup cell
        elif new_position in self.pickup_cells:
            if self.pickup_cells[new_position] > 0:
                self.pickup_cells[new_position] -= 1
                reward = 1  # Reward for picking up a block
            else:
                reward = -1  # Penalty for trying to pick up from an empty cell
        # Check if the new_position is a dropoff cell
        elif new_position in self.dropoff_cells:
            if self.dropoff_cells[new_position] < self.dropoff_capacity:
                self.dropoff_cells[new_position] += 1
                reward = 1  # Reward for dropping off a block
            else:
                reward = -1  # Penalty for trying to drop off at a full cell
        else:
            reward = 0

        # Update the environment state
        self.set_state(self.state)  # Update the state using the modified state

        return new_position, reward

    def is_success(self, agent_type):
        # calculate success criteria based on agent's position and return True or False
        if agent_type == 'F':
            return self.state[0][0] == self.grid_size_x // 2 and self.state[0][1] == self.grid_size_y // 2 and \
                   self.dropoff_cells[(self.grid_size_x // 2, self.grid_size_y // 2, 1)] == self.dropoff_capacity
        elif agent_type == 'M':
            return self.state[1][0] == self.grid_size_x // 2 and self.state[1][1] == self.grid_size_y // 2 and \
                   self.dropoff_cells[(self.grid_size_x // 2, self.grid_size_y // 2, 1)] == self.dropoff_capacity
        else:
            raise ValueError("Invalid agent type specified. Expected 'F' or 'M', got {}".format(agent_type))

    def _apply_action(self, position, action):
        x, y, z = position

        if action == 'U':
            z = min(z + 1, self.grid_size_z)
        elif action == 'D':
            z = max(z - 1, 1)
        elif action == 'F':
            y = min(y + 1, self.grid_size_y)
        elif action == 'B':
            y = max(y - 1, 1)
        elif action == 'L':
            x = max(x - 1, 1)
        elif action == 'R':
            x = min(x + 1, self.grid_size_x)

        return x, y, z
