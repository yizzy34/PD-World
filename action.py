def find_possible_actions(state, agent):
    moves = ['up', 'down', 'left', 'right', 'forward', 'backward']
    agent_pos = []
    other_agent_pos = []
    if agent == 'm':
        agent_pos = state.representation['male_position']['coords']
        other_agent_pos = state.representation['female_position']['coords']
    else:
        agent_pos = state.representation['female_position']['coords']
        other_agent_pos = state.representation['male_position']['coords']

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
    moves = ['up', 'down', 'left', 'right', 'forward', 'backward']
    if coords[0] == 0:
        if moves.count('down'):
            moves.remove('down')
    elif coords[0] == 2:
        if moves.count('up'):
            moves.remove('up')
    if coords[1] == 0:
        if moves.count('forward'):
            moves.remove('forward')
    elif coords[1] == 2:
        if moves.count('backward'):
            moves.remove('backward')
    if coords[2] == 0:
        if moves.count('left'):
            moves.remove('left')
    elif coords[2] == 2:
        if moves.count('right'):
            moves.remove('right')
    return moves