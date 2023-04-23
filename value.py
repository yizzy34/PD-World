def q_Learning_Value_Function(old_q_val, move_reward, next_q_vals, alpha, gamma):
    max_next_q_val = max(next_q_vals.values())
    return old_q_val + alpha * (move_reward + gamma * max_next_q_val - old_q_val)


def sarsa_Value_Function(old_q_val, move_reward, next_q_val, alpha, gamma):
    return old_q_val + alpha * (move_reward + gamma * next_q_val - old_q_val)
