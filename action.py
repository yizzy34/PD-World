# Find the possible actions that an agent can take in a given state
def find_possible_actions(state, agent):
    # List of possible actions
    moves = ['up', 'down', 'left', 'right', 'forward', 'backward']

    # Get the positions of the agent and the other agent
    if agent == 'm':
        agent_pos = state.representation['male_position']['coords']
        other_agent_pos = state.representation['female_position']['coords']
    else:
        agent_pos = state.representation['female_position']['coords']
        other_agent_pos = state.representation['male_position']['coords']

    # Remove any actions that would cause the agent to move into the same position as the other agent
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

    # Remove any actions that would cause the agent to move outside of the grid
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

    # Return the list of possible actions
    return moves


def find_next_position_possible_actions(coords):
    # List of possible actions
    moves = ['up', 'down', 'left', 'right', 'forward', 'backward']
    # Remove any actions that would cause the agent to move outside of the grid
    if coords[0] == 0:
        if moves.count('down'):  # If the agent is at the bottom edge of the grid, it cannot move down
            moves.remove('down')
    elif coords[0] == 2:
        if moves.count('up'):  # If the agent is at the top edge of the grid, it cannot move up
            moves.remove('up')
    if coords[1] == 0:
        if moves.count('forward'):  # If the agent is at the front edge of the grid, it cannot move forward
            moves.remove('forward')
    elif coords[1] == 2:
        if moves.count('backward'):  # If the agent is at the back edge of the grid, it cannot move backward
            moves.remove('backward')
    if coords[2] == 0:
        if moves.count('left'):  # If the agent is at the left edge of the grid, it cannot move left
            moves.remove('left')
    elif coords[2] == 2:
        if moves.count('right'):  # If the agent is at the right edge of the grid, it cannot move right
            moves.remove('right')
    return moves
