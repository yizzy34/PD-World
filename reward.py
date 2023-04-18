def calculate_reward(agent, current_state, action):
    environment = agent.environment

    # Check if the agent is in a risky cell
    if current_state in environment.risky_cells:
        return -2

    # Check if the agent is in a pickup cell
    if current_state in environment.pickup_cells:
        # You can add more logic here to check the agent's action (e.g., picking up a block)
        # and return a reward accordingly. For simplicity, we'll return a positive reward for being in a pickup cell.
        return 1

    # Check if the agent is in a dropoff cell
    if current_state in environment.dropoff_cells:
        # You can add more logic here to check the agent's action (e.g., dropping off a block)
        # and return a reward accordingly. For simplicity, we'll return a positive reward for being in a dropoff cell.
        return 1

    # Return a small negative reward for all other actions and states
    return -0.1
