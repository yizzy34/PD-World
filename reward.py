def get_Reward(cell):
    reward = 0
    match cell:
        case 'normal':
            reward = -1
        case 'risky':
            reward = -2
        case 'pickup':
            reward = 14
        case 'dropoff':
            reward = 14
    return reward
