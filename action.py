import environment


def find_possible_actions(state, agent):
    listofMoves = ['up', 'down', 'left', 'right', 'forward', 'backward']
    agent_pos_key = f'{agent}_position'
    agent_pos = state.representation[agent_pos_key]['coords']
    other_agent_key = 'female_position' if agent == 'm' else 'male_position'
    other_agent_pos = state.representation[other_agent_key]['coords']

    # Remove listofMoves that lead to the other agent's position
    for move in listofMoves[:]:
        new_coords = environment.move_to_new_position(agent_pos, move)
        if new_coords == other_agent_pos:
            listofMoves.remove(move)

    # Remove listofMoves that lead to a wall
    listofMoves = remove_wall_listofMoves(agent_pos, listofMoves)

    return listofMoves


def remove_wall_listofMoves(coords, listofMoves):
    for move in listofMoves[:]:
        new_coords = environment.move_to_new_position(coords, move)
        if not (0 <= new_coords[0] < 3 and 0 <= new_coords[1] < 3 and 0 <= new_coords[2] < 3):
            listofMoves.remove(move)
    return listofMoves


def find_next_position_possible_actions(coords):
    listofMoves = ['up', 'down', 'left', 'right', 'forward', 'backward']
    listofMoves = remove_wall_listofMoves(coords, listofMoves)
    return listofMoves
