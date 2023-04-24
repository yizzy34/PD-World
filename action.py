def find_possible_actions(state, agent):
    # Define a list of possible moves
    moves = ['up', 'down', 'left', 'right', 'forward', 'backward']

    # Get the current position of the agent and the other agent
    agent_pos = []
    other_agent_pos = []
    if agent == 'm':
        agent_pos = state.representation['male_position']['coords']
        other_agent_pos = state.representation['female_position']['coords']
    else:
        agent_pos = state.representation['female_position']['coords']
        other_agent_pos = state.representation['male_position']['coords']

    # Check if the agent is adjacent to the other agent, and remove corresponding moves from the list
    if agent_pos[0] - other_agent_pos[0] == -1 and (
            agent_pos[1] == other_agent_pos[1] and agent_pos[2] == other_agent_pos[2]):
        if moves.count('up'):
            moves.remove('up')
    elif agent_pos[0] - other_agent_pos[0] == 1 and (
            agent_pos[1] == other_agent_pos[1] and agent_pos[2] == other_agent_pos[2]):
        if moves.count('down'):
            moves.remove('down')
    elif agent_pos[1] - other_agent_pos[1] == -1 and (
            agent_pos[0] == other_agent_pos[0] and agent_pos[2] == other_agent_pos[2]):
        if moves.count('backward'):
            moves.remove('backward')
    elif agent_pos[1] - other_agent_pos[1] == 1 and (
            agent_pos[0] == other_agent_pos[0] and agent_pos[2] == other_agent_pos[2]):
        if moves.count('forward'):
            moves.remove('forward')
    elif agent_pos[2] - other_agent_pos[2] == -1 and (
            agent_pos[0] == other_agent_pos[0] and agent_pos[1] == other_agent_pos[1]):
        if moves.count('right'):
            moves.remove('right')
    elif agent_pos[2] - other_agent_pos[2] == 1 and (
            agent_pos[0] == other_agent_pos[0] and agent_pos[1] == other_agent_pos[1]):
        if moves.count('left'):
            moves.remove('left')

    # Check if the agent is at the edge of the grid, and remove corresponding moves from the list
    if agent_pos[0] == 0:
        if moves.count('down'):
            moves.remove('down')
    elif agent_pos[0] == 2:
        if moves.count('up'):
            moves.remove('up')
    if agent_pos[1] == 0:
        if moves.count('forward'):
            moves.remove('forward')
    elif agent_pos[1] == 2:
        if moves.count('backward'):
            moves.remove('backward')
    if agent_pos[2] == 0:
        if moves.count('left'):
            moves.remove('left')
    elif agent_pos[2] == 2:
        if moves.count('right'):
            moves.remove('right')
    return moves


def find_next_position_possible_actions(coords):
    # Define a list of all possible moves
    moves = ['up', 'down', 'left', 'right', 'forward', 'backward']

    # If the agent is at the top edge of the 3D space, remove 'down' from the list of possible moves
    if coords[0] == 0:
        if moves.count('down'):  # check if 'down' is in the list
            moves.remove('down')  # remove 'down' from the list

    # If the agent is at the bottom edge of the 3D space, remove 'up' from the list of possible moves
    elif coords[0] == 2:
        if moves.count('up'):  # check if 'up' is in the list
            moves.remove('up')  # remove 'up' from the list

    # If the agent is at the front edge of the 3D space, remove 'forward' from the list of possible moves
    if coords[1] == 0:
        if moves.count('forward'):  # check if 'forward' is in the list
            moves.remove('forward')  # remove 'forward' from the list

    # If the agent is at the back edge of the 3D space, remove 'backward' from the list of possible moves
    elif coords[1] == 2:
        if moves.count('backward'):  # check if 'backward' is in the list
            moves.remove('backward')  # remove 'backward' from the list

    # If the agent is at the left edge of the 3D space, remove 'left' from the list of possible moves
    if coords[2] == 0:
        if moves.count('left'):  # check if 'left' is in the list
            moves.remove('left')  # remove 'left' from the list

    # If the agent is at the right edge of the 3D space, remove 'right' from the list of possible moves
    elif coords[2] == 2:
        if moves.count('right'):  # check if 'right' is in the list
            moves.remove('right')  # remove 'right' from the list

    # Return the list of possible moves after removing any moves that would take the agent outside of the 3D space
    return moves


