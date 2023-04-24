import random


# Choose an action randomly
def p_random(carrying, cells):
    # Check if there are any pickup or dropoff actions that the agent can take
    for i in cells:
        if (cells[i]['type'] == "pickup" and carrying == False) or (cells[i]['type'] == "dropoff" and carrying):
            return i
    # If there are no pickup or dropoff actions that the agent can take, choose a random action
    position = random.randint(0, len(cells) - 1)
    action = (list(cells))[position]
    return action


# Choose an action greedily (with some probability of exploration)
def p_greedy(carrying, cells, q_vals):
    max_q_val = float('-inf')
    max_actions = []
    # Check if there are any pickup or dropoff actions that the agent can take
    for i in cells:
        if (cells[i]['type'] == "pickup" and carrying == False) or (cells[i]['type'] == "dropoff" and carrying):
            return i
    # Find the action(s) with the highest Q-value
    for i in q_vals:
        if (q_vals[i] > max_q_val):
            max_actions.clear()
            max_q_val = q_vals[i]
            max_actions.append(i)
        elif (q_vals[i] == max_q_val):
            max_actions.append(i)
    # If there is only one action with the highest Q-value, choose it
    if len(max_actions) == 1:
        action_chosen = max_actions[0]
    # If there are multiple actions with the highest Q-value, choose one randomly
    else:
        position = random.randint(0, len(max_actions) - 1)
        action_chosen = max_actions[position]
    return action_chosen


# Choose an action based on the highest Q-value with some probability of choosing a non-maximal action
def p_exploit(carrying, cells, q_vals):
    max_q_val = float('-inf')
    max_actions = []
    # Check if there are any pickup or dropoff actions that the agent can take
    for i in cells:
        if (cells[i]['type'] == "pickup" and carrying == False) or (cells[i]['type'] == "dropoff" and carrying):
            return i
    # Find the action(s) with the highest Q-value and all non-maximal actions
    for i in q_vals:
        if q_vals[i] > max_q_val:
            max_actions.clear()
            max_q_val = q_vals[i]
            max_actions.append(i)
        elif q_vals[i] == max_q_val:
            max_actions.append(i)
    non_max_actions = []
    for i in cells:
        if max_actions.count(i) == 0:
            non_max_actions.append(i)
    # If all actions have the same Q-value, choose from all actions with some probability
    if len(max_actions) == len(q_vals):
        non_max_actions = max_actions
    # If there are no non-maximal actions, choose from all maximal actions
    elif len(non_max_actions) == len(q_vals):
        max_actions = non_max_actions
    # Choose between maximal and non-maximal actions with some probability
    actions = [{'list': 'max_actions'}, {'list': 'non_max_actions'}]
    weight = [0.80, 0.20]
    choice_made = random.choices(actions, k=1, weights=weight)
    action_chosen = ''
    # Choose an action from the chosen list of actions
    # If a maximal action was chosen, choose one randomly from the list of maximal actions
    if choice_made[0]['list'] == 'max_actions':
        position = random.randint(0, len(max_actions) - 1)
        action_chosen = max_actions[position]
    # If a non-maximal action was chosen, choose one randomly from the list of non-maximal actions
    else:
        position = random.randint(0, len(non_max_actions) - 1)
        action_chosen = non_max_actions[position]
    return action_chosen
