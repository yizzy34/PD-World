import random


def choose_Action_Based_On_Weight(actions, weights):
    chosen_action_list = random.choices(actions, k=1, weights=weights)
    position = random.randint(0, len(chosen_action_list[0]) - 1)
    return chosen_action_list[0][position]


def p_Random(carrying, cells):
    relevant_cells = [i for i in cells if
                      (cells[i]['type'] == "pickup" and not carrying) or (cells[i]['type'] == "dropoff" and carrying)]
    if relevant_cells:
        return random.choice(relevant_cells)

    return random.choice(list(cells))


def p_Exploit(carrying, cells, q_vals):
    relevant_cells = [i for i in cells if
                      (cells[i]['type'] == "pickup" and not carrying) or (cells[i]['type'] == "dropoff" and carrying)]
    if relevant_cells:
        return random.choice(relevant_cells)

    max_q_val = max(q_vals.values())
    max_actions = [i for i in q_vals if q_vals[i] == max_q_val]
    non_max_actions = [i for i in cells if i not in max_actions]

    actions = [max_actions, non_max_actions]
    weights = [0.80, 0.20]

    return choose_Action_Based_On_Weight(actions, weights)


def p_Greedy(carrying, cells, q_vals):
    relevant_cells = [i for i in cells if
                      (cells[i]['type'] == "pickup" and not carrying) or (cells[i]['type'] == "dropoff" and carrying)]
    if relevant_cells:
        return random.choice(relevant_cells)

    max_q_val = max(q_vals.values())
    max_actions = [i for i in q_vals if q_vals[i] == max_q_val]

    return random.choice(max_actions)
