def find_Possible_Actions(state, agent):
    moves_Can_Make = ['up', 'down', 'left', 'right', 'forward', 'backward']
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
        if moves_Can_Make.count('up'):
            moves_Can_Make.remove('up')
    elif agent_pos[0] - other_agent_pos[0] == 1 and (
            agent_pos[1] == other_agent_pos[1] and agent_pos[2] == other_agent_pos[2]):
        if moves_Can_Make.count('down'):
            moves_Can_Make.remove('down')
    elif agent_pos[1] - other_agent_pos[1] == -1 and (
            agent_pos[0] == other_agent_pos[0] and agent_pos[2] == other_agent_pos[2]):
        if moves_Can_Make.count('backward'):
            moves_Can_Make.remove('backward')
    elif agent_pos[1] - other_agent_pos[1] == 1 and (
            agent_pos[0] == other_agent_pos[0] and agent_pos[2] == other_agent_pos[2]):
        if moves_Can_Make.count('forward'):
            moves_Can_Make.remove('forward')
    elif agent_pos[2] - other_agent_pos[2] == -1 and (
            agent_pos[0] == other_agent_pos[0] and agent_pos[1] == other_agent_pos[1]):
        if moves_Can_Make.count('right'):
            moves_Can_Make.remove('right')
    elif agent_pos[2] - other_agent_pos[2] == 1 and (
            agent_pos[0] == other_agent_pos[0] and agent_pos[1] == other_agent_pos[1]):
        if moves_Can_Make.count('left'):
            moves_Can_Make.remove('left')
    if agent_pos[0] == 0:
        if moves_Can_Make.count('down'):
            moves_Can_Make.remove('down')
    elif agent_pos[0] == 2:
        if moves_Can_Make.count('up'):
            moves_Can_Make.remove('up')
    if agent_pos[1] == 0:
        if moves_Can_Make.count('forward'):
            moves_Can_Make.remove('forward')
    elif agent_pos[1] == 2:
        if moves_Can_Make.count('backward'):
            moves_Can_Make.remove('backward')
    if agent_pos[2] == 0:
        if moves_Can_Make.count('left'):
            moves_Can_Make.remove('left')
    elif agent_pos[2] == 2:
        if moves_Can_Make.count('right'):
            moves_Can_Make.remove('right')
    return moves_Can_Make


def find_Next_Position_Possible_Actions(coords):
    moves_Can_Make = ['up', 'down', 'left', 'right', 'forward', 'backward']
    if coords[0] == 0:
        if moves_Can_Make.count('down'):
            moves_Can_Make.remove('down')
    elif coords[0] == 2:
        if moves_Can_Make.count('up'):
            moves_Can_Make.remove('up')
    if coords[1] == 0:
        if moves_Can_Make.count('forward'):
            moves_Can_Make.remove('forward')
    elif coords[1] == 2:
        if moves_Can_Make.count('backward'):
            moves_Can_Make.remove('backward')
    if coords[2] == 0:
        if moves_Can_Make.count('left'):
            moves_Can_Make.remove('left')
    elif coords[2] == 2:
        if moves_Can_Make.count('right'):
            moves_Can_Make.remove('right')
    return moves_Can_Make
