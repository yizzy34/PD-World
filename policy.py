import random


def p_random(carrying, cells):
    for i in cells:
        if (cells[i]['type'] == "pickup" and carrying == False) or (cells[i]['type'] == "dropoff" and carrying):
            return i
    position = random.randint(0, len(cells) - 1)
    action = (list(cells))[position]
    return action


def p_greedy(carrying, cells, q_vals):
    max_q_val = float('-inf')
    max_actions = []
    for i in cells:
        if (cells[i]['type'] == "pickup" and carrying == False) or (cells[i]['type'] == "dropoff" and carrying):
            return i
    for i in q_vals:
        if (q_vals[i] > max_q_val):
            max_actions.clear()
            max_q_val = q_vals[i]
            max_actions.append(i)
        elif (q_vals[i] == max_q_val):
            max_actions.append(i)
    position = random.randint(0, len(max_actions) - 1)
    action_chosen = max_actions[position]
    return action_chosen


def p_exploit(carrying, cells, q_vals):
    max_q_val = float('-inf')
    max_actions = []
    for i in cells:
        if (cells[i]['type'] == "pickup" and carrying == False) or (cells[i]['type'] == "dropoff" and carrying):
            return i
    for i in q_vals:
        if (q_vals[i] > max_q_val):
            max_actions.clear()
            max_q_val = q_vals[i]
            max_actions.append(i)
        elif (q_vals[i] == max_q_val):
            max_actions.append(i)

    non_max_actions = []
    for i in cells:
        if (max_actions.count(i) == 0):
            non_max_actions.append(i)

    if len(max_actions) == len(q_vals):
        non_max_actions = max_actions
    elif len(non_max_actions) == len(q_vals):
        max_actions = non_max_actions

    actions = [{'list': 'max_actions'}, {'list': 'non_max_actions'}]
    weight = [0.80, 0.20]
    choice_made = random.choices(actions, k=1, weights=weight)
    action_chosen = ''
    if (choice_made[0]['list'] == 'max_actions'):
        position = random.randint(0, len(max_actions) - 1)
        action_chosen = max_actions[position]
    else:
        position = random.randint(0, len(non_max_actions) - 1)
        action_chosen = non_max_actions[position]
    return action_chosen
