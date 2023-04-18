import numpy as np
import random


class CustomEnvironment:
    def __init__(self, grid_size_x, grid_size_y, grid_size_z, risky_cells, male_initial_pos, female_initial_pos,
                 pickup_cells, dropoff_cells):
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.grid_size_z = grid_size_z
        self.risky_cells = risky_cells
        self.male_initial_pos = male_initial_pos
        self.female_initial_pos = female_initial_pos
        self.pickup_cells = pickup_cells
        self.dropoff_cells = dropoff_cells
        self.male_pos = male_initial_pos
        self.female_pos = female_initial_pos
        self.state = (female_initial_pos, male_initial_pos)

        self.pickup_status = {cell: 10 for cell in pickup_cells}
        self.dropoff_status = {cell: 0 for cell in dropoff_cells}

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.female_pos, self.male_pos = state

    def take_action(self, agent, action):
        # Determine the current position and next position based on the action
        current_pos = self.male_pos if agent == 'M' else self.female_pos
        next_pos = self.calculate_next_position(current_pos, action)

        # Check for collisions
        if next_pos == self.male_pos or next_pos == self.female_pos:
            return self.state, -1  # Penalize for collision

        # Update the position of the agent
        if agent == 'M':
            self.male_pos = next_pos
        else:
            self.female_pos = next_pos

        self.state = (self.female_pos, self.male_pos)

        # Calculate the reward
        reward = 0
        if next_pos in self.risky_cells:
            reward = -2  # Risky cells return 2 times more negative reward than normal cells
        # Add other reward calculations based on your problem requirements

        return self.state, reward

    def calculate_next_position(self, current_pos, action):
        x, y, z = current_pos
        if action == 0:  # North
            y = max(y - 1, 1)
        elif action == 1:  # South
            y = min(y + 1, self.grid_size_y)
        elif action == 2:  # East
            x = min(x + 1, self.grid_size_x)
        elif action == 3:  # West
            x = max(x - 1, 1)
        elif action == 4:  # Up
            z = min(z + 1, self.grid_size_z)
        elif action == 5:  # Down
            z = max(z - 1, 1)
        # Add logic for Pickup and Dropoff actions (6 and 7) if needed

        return x, y, z


class QLearningAgent:
    def __init__(self, environment, alpha=0.3, gamma=0.5, n_actions=8, epsilon=0.1):
        self.environment = environment
        self.alpha = alpha
        self.gamma = gamma
        self.n_actions = n_actions
        self.q_table = {}
        self.epsilon = epsilon

    def get_q(self, state, action):
        if (state, action) not in self.q_table:
            self.q_table[(state, action)] = 0
        return self.q_table[(state, action)]

    def update_q(self, state, action, value):
        self.q_table[(state, action)] = value

    def choose_action(self, state, policy):
        if policy == 'PRANDOM':
            return random.randint(0, self.n_actions - 1)
        elif policy == 'PGREEDY' or policy == 'PEXPLOIT':
            q_values = [self.get_q(state, a) for a in range(self.n_actions)]
            best_action = np.argmax(q_values)
            if policy == 'PGREEDY' or random.random() < self.epsilon:
                return best_action
            else:
                return random.randint(0, self.n_actions - 1)

    def learn(self, state, action, reward, next_state, next_action):
        q_value = self.get_q(state, action)
        next_q_value = self.get_q(next_state, next_action)
        value = q_value + self.alpha * (reward + self.gamma * next_q_value - q_value)
        self.update_q(state, action, value)


def run_experiment(agent1, agent2, n_steps, policy1, policy2):
    for step in range(n_steps):
        current_state1 = agent1.environment.get_state()
        current_state2 = agent2.environment.get_state()
        action1 = agent1.choose_action(current_state1, policy1)
        action2 = agent2.choose_action(current_state2, policy2)

        next_state1, reward1 = agent1.environment.take_action('F', action1)
        next_state2, reward2 = agent2.environment.take_action('M', action2)

        if step >= 500:
            next_action1 = agent1.choose_action(next_state1, policy1)
            next_action2 = agent2.choose_action(next_state2, policy2)

            agent1.learn(current_state1, action1, reward1, next_state1, next_action1)
            agent2.learn(current_state2, action2, reward2, next_state2, next_action2)

            # Add print statements to display progress
            if step % 100 == 0:  # Print every 100 steps
                print(f"Step: {step}")
                print(f"Agent F: State: {current_state1}, Reward: {reward1}")
                print(f"Agent M: State: {current_state2}, Reward: {reward2}")
                print()


# Define the parameters for the CustomEnvironment
grid_size_x = 4
grid_size_y = 4
grid_size_z = 4
risky_cells = [(2, 2, 2), (3, 2, 1)]
male_initial_pos = (3, 2, 3)
female_initial_pos = (1, 1, 1)
pickup_cells = [(2, 2, 1), (3, 3, 2)]
dropoff_cells = [(1, 1, 2), (1, 1, 3), (3, 1, 1), (3, 2, 3)]

# Create the CustomEnvironment instance
environment = CustomEnvironment(grid_size_x, grid_size_y, grid_size_z, risky_cells, male_initial_pos,
                                female_initial_pos, pickup_cells, dropoff_cells)

# Create the QLearningAgent instances for the male and female agents
agent1 = QLearningAgent(environment)
agent2 = QLearningAgent(environment)

# Run the experiments
n_steps = 10000
run_experiment(agent1, agent2, n_steps, 'PRANDOM', 'PRANDOM')
run_experiment(agent1, agent2, n_steps, 'PGREEDY', 'PGREEDY')
run_experiment(agent1, agent2, n_steps, 'PEXPLOIT', 'PEXPLOIT')
