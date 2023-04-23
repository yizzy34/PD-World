def q_Learning_Value_Function(old_q_val, move_reward, next_q_vals, alpha, gamma):
    next_q_vals_list = []
    for i in next_q_vals:
        next_q_vals_list.append(next_q_vals[i])
    return old_q_val + alpha * (move_reward + gamma * max(next_q_vals_list) - old_q_val)


def sarsa_Value_Function(old_q_val, move_reward, next_q_val, alpha, gamma):
    return old_q_val + alpha * (move_reward + gamma * next_q_val - old_q_val)
