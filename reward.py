def get_reward(cell):
    # Initialize the reward variable
    reward = 0

    # Use a match statement to determine the reward value based on the type of the cell
    match cell:
        case 'normal':
            # For normal cells, set the reward to -1
            reward = -1
        case 'risky':
            # For risky cells, set the reward to -2
            reward = -2
        case 'pickup':
            # For pickup cells, set the reward to 14
            reward = 14
        case 'dropoff':
            # For dropoff cells, set the reward to 14
            reward = 14

    # Return the calculated reward value
    return reward
