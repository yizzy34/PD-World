import random


def p_random(carrying, cells):
    # This function implements a random policy for choosing actions
    # It takes the current state of whether the agent is carrying a block and the available cells as input
    for i in cells:
        if (cells[i]['type'] == "pickup" and carrying == False) or (cells[i]['type'] == "dropoff" and carrying):
            # If there is a pickup cell and the agent is not carrying a block, or if there is a dropoff cell and the agent is carrying a block, return the action corresponding to that cell
            return i
    # Otherwise, choose a random action from the available cells
    position = random.randint(0, len(cells) - 1)
    action = (list(cells))[position]
    return action


def p_greedy(carrying, cells, q_vals):
    # This function implements a greedy policy for choosing actions
    # It takes the current state of whether the agent is carrying a block, the available cells, and the Q-values for each action as input
    max_q_val = float('-inf')
    max_actions = []
    for i in cells:
        if (cells[i]['type'] == "pickup" and carrying == False) or (cells[i]['type'] == "dropoff" and carrying):
            # If there is a pickup cell and the agent is not carrying a block, or if there is a dropoff cell and the agent is carrying a block, add the corresponding action to the list of possible actions
            return i
    for i in q_vals:
        if q_vals[i] > max_q_val:
            # If the Q-value for this action is higher than the current maximum, clear the list of maximum actions and add this action to the list
            max_actions.clear()
            max_q_val = q_vals[i]
            max_actions.append(i)
        elif q_vals[i] == max_q_val:
            # If the Q-value for this action is equal to the current maximum, add this action to the list of maximum actions
            max_actions.append(i)
    # Choose a random action from the list of maximum actions
    position = random.randint(0, len(max_actions) - 1)
    action_chosen = max_actions[position]
    return action_chosen


def p_exploit(carrying, cells, q_vals):
    # Initialize variables to find the maximum Q-value and corresponding actions
    max_q_val = float('-inf')
    max_actions = []

    # If the agent is not carrying a block, look for pickup cells. If the agent is carrying a block, look for dropoff cells.
    for i in cells:
        if (cells[i]['type'] == "pickup" and carrying == False) or (cells[i]['type'] == "dropoff" and carrying):
            return i

    # Find the maximum Q-value among the possible actions
    for i in q_vals:
        if q_vals[i] > max_q_val:
            max_actions.clear()
            max_q_val = q_vals[i]
            max_actions.append(i)
        elif q_vals[i] == max_q_val:
            max_actions.append(i)

    # Find the actions that do not have the maximum Q-value
    non_max_actions = []
    for i in cells:
        if max_actions.count(i) == 0:
            non_max_actions.append(i)

    # If all actions have the same Q-value, consider all actions to be non-maximal.
    # Otherwise, if all non-maximal actions have been pruned, consider all actions to be maximal.
    if len(max_actions) == len(q_vals):
        non_max_actions = max_actions
    elif len(non_max_actions) == len(q_vals):
        max_actions = non_max_actions

    # Choose between the maximal and non-maximal actions based on a random weight
    actions = [{'list': 'max_actions'}, {'list': 'non_max_actions'}]
    weight = [0.80, 0.20]
    choice_made = random.choices(actions, k=1, weights=weight)
    action_chosen = ''

    # Choose an action from the list of maximal or non-maximal actions based on the random weight
    if choice_made[0]['list'] == 'max_actions':
        position = random.randint(0, len(max_actions) - 1)
        action_chosen = max_actions[position]
    else:
        position = random.randint(0, len(non_max_actions) - 1)
        action_chosen = non_max_actions[position]

    return action_chosen

