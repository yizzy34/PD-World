class StateRepresentation:
    def __init__(self):
        pass

    def convert_state(self, environment_state):
        # In this case, we don't need to do any conversion.
        # Simply return the environment_state as it is.
        return environment_state

    def state_to_index(self, state, grid_size_x, grid_size_y, grid_size_z):
        if isinstance(state, int):  # If the state is a single integer, convert it to a tuple
            state = (state,)
        elif isinstance(state, tuple):
            if len(state) == 2:  # If the state is a tuple of two integers, convert it to a tuple of three integers
                state = (state[0], state[1], 1)
            elif len(state) != 3:
                raise ValueError('Invalid state format: {}'.format(state))
        else:
            raise ValueError('Invalid state format: {}'.format(state))

        female_pos, male_pos = state
        state_index = ((female_pos[0] - 1) * grid_size_y + female_pos[1] - 1) * grid_size_x * grid_size_z + \
                      ((male_pos[0] - 1) * grid_size_y + male_pos[1] - 1) * grid_size_z + male_pos[2] - 1
        return state_index
