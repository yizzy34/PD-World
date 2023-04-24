import environment


class State:
    def __init__(self, world_environment):
        # Initialize the state with the world environment and an empty representation dictionary
        self.world_environment = world_environment
        self.representation = {'male_position': {}, 'female_position': {}, 'male_carrying': False,
                               'female_carrying': False, 'pickup_cell_blocks': {}, 'dropoff_cell_blocks': {}}

        # Set the state representation based on the current environment
        self.set_state_environment()
        self.set_male_position()
        self.set_female_position()
        self.set_pickup_cell_blocks()
        self.set_dropoff_cell_blocks()

    def set_state_environment(self):
        # Set the state environment to be the same as the world environment
        self.environment = self.world_environment.environment

    def set_male_position(self):
        # Find the current position of the male agent in the environment and store it in the state representation
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['occupied_by'] == 'm':
                        self.representation['male_position']['coords'] = [x, y, z]
                        self.representation['male_position']['cell_type'] = self.environment[x][y][z]['type']

    def set_female_position(self):
        # Find the current position of the female agent in the environment and store it in the state representation
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['occupied_by'] == 'f':
                        self.representation['female_position']['coords'] = [x, y, z]
                        self.representation['female_position']['cell_type'] = self.environment[x][y][z]['type']

    def toggle_male_carrying(self):
        # Toggle the male carrying status in the state representation
        self.representation['male_carrying'] = not self.representation['male_carrying']

    def toggle_female_carrying(self):
        # Toggle the female carrying status in the state representation
        self.representation['female_carrying'] = not self.representation['female_carrying']

    def set_pickup_cell_blocks(self):
        # Find all the pickup cell blocks in the environment and store their block counts in the state representation
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['type'] == 'pickup':
                        self.representation['pickup_cell_blocks'][(x, y, z)] = self.environment[x][y][z]['block_count']

    def set_dropoff_cell_blocks(self):
        # Find all the dropoff cell blocks in the environment and store their block counts in the state representation
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['type'] == 'dropoff':
                        self.representation['dropoff_cell_blocks'][(x, y, z)] = self.environment[x][y][z]['block_count']

    def update_environment_and_state(self, old_coords, action, agent, carrying, new_position):
        # Update the environment based on the given action and agent, and store the new state representation
        picked_up_or_dropped_off = self.world_environment.move_agent(old_coords, action, agent, carrying)

        # Update the position of the male or female agent depending on the given agent
        if agent == 'm':
            self.set_male_position()
        else:
            self.set_female_position()

        # If the agent is on a pickup or dropoff cell, update its carrying status accordingly
        if picked_up_or_dropped_off:
            # If the new position is a pickup cell and the agent is not carrying a block, update the pickup cell blocks count
            if new_position == 'pickup' and carrying == False:
                self.set_pickup_cell_blocks()
            # If the new position is a dropoff cell, update the dropoff cell blocks count
            else:
                self.set_dropoff_cell_blocks()

            # Toggle the carrying status of the male or female agent
            if agent == 'm':
                self.toggle_male_carrying()
            else:
                self.toggle_female_carrying()

        # Update the state environment representation with the new environment
        self.set_state_environment()

        # Return a boolean indicating whether a block was picked up or dropped off in the last action
        return picked_up_or_dropped_off

