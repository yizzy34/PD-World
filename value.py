def q_learning_value_function(old_q_val, move_reward, next_q_vals, alpha, gamma):
    """
    Calculates the Q-learning value function for a given state-action pair.

    Parameters:
        old_q_val (float): The current Q-value for the state-action pair.
        move_reward (float): The reward obtained for taking the action in the current state.
        next_q_vals (dict): A dictionary containing the Q-values for the next state.
        alpha (float): The learning rate.
        gamma (float): The discount factor.

    Returns:
        float: The updated Q-value for the state-action pair.
    """
    # Convert next_q_vals dictionary to a list to find the maximum Q-value for the next state
    next_q_vals_list = []
    for i in next_q_vals:
        next_q_vals_list.append(next_q_vals[i])

    # Apply the Q-learning update rule
    return old_q_val + alpha * (move_reward + gamma * max(next_q_vals_list) - old_q_val)


def sarsa_value_function(old_q_val, move_reward, next_q_val, alpha, gamma):
    """
    Calculates the SARSA value function for a given state-action pair.

    Parameters:
        old_q_val (float): The current Q-value for the state-action pair.
        move_reward (float): The reward obtained for taking the action in the current state.
        next_q_val (float): The Q-value for the next state-action pair.
        alpha (float): The learning rate.
        gamma (float): The discount factor.

    Returns:
        float: The updated Q-value for the state-action pair.
    """
    # Apply the SARSA update rule
    return old_q_val + alpha * (move_reward + gamma * next_q_val - old_q_val)
