from environment import CustomEnvironment
from agent import QLearningAgent
from state import StateRepresentation
from action import ActionSpace
from reward import calculate_reward
from policy import Policy
from model import Model
from evaluation import evaluate_agent

# Define the parameters for the CustomEnvironment
grid_size_x = 3
grid_size_y = 3
grid_size_z = 3
risky_cells = [(2, 2, 2), (3, 2, 1)]  # Define the risky cells
male_initial_pos = (3, 2, 3)
female_initial_pos = (1, 1, 1)
pickup_cells = [(2, 2, 1), (3, 3, 2)]  # Define the pickup cells
dropoff_cells = [(1, 1, 2), (1, 1, 3), (3, 1, 1), (3, 2, 3)]  # Define the dropoff cells

# Create the CustomEnvironment instance
env = CustomEnvironment(grid_size_x, grid_size_y, grid_size_z, risky_cells, male_initial_pos, female_initial_pos,
                        pickup_cells, dropoff_cells)

# Create the Model instance
model = Model(env)

# Create the StateRepresentation instance
state_representation = StateRepresentation()

# Create the ActionSpace instance
action_space = ActionSpace()

# Get the number of actions from the action_space instance
n_actions = action_space.get_n_actions()

# Create the QLearningAgent instances for the male and female agents
agent1 = QLearningAgent(env, state_representation, n_actions=n_actions, alpha=0.3, gamma=0.5)
agent2 = QLearningAgent(env, state_representation, n_actions=n_actions, alpha=0.3, gamma=0.5)

# Create the Policy instances for the male and female agents
policy1 = Policy(agent1, 'PRANDOM')
policy2 = Policy(agent2, 'PRANDOM')


def run_experiment(agent1, agent2, n_steps, policy1, policy2):
    for step in range(n_steps):
        # Get the environment states
        current_state1 = agent1.environment.get_state()
        current_state2 = agent2.environment.get_state()

        # Choose actions based on the policies
        action1 = policy1.choose_action('F', current_state1)
        action2 = policy2.choose_action('M', current_state2)

        # Take the actions and get the next states
        next_state1, _ = agent1.environment.take_action('F', action1)
        next_state2, _ = agent2.environment.take_action('M', action2)

        # Calculate the rewards using the calculate_reward function
        reward1 = calculate_reward(agent1, current_state1, action1)
        reward2 = calculate_reward(agent2, current_state2, action2)

        # Update the agents with the new information
        agent1.update(current_state1, action1, reward1, next_state1)
        agent2.update(current_state2, action2, reward2, next_state2)


# Experiment 1: Running the traditional Q-learning algorithm for 10000 steps
n_steps = 10000

# Experiment 1a: PRANDOM for 500 steps
policy1.set_policy_type('PRANDOM')
policy2.set_policy_type('PRANDOM')
run_experiment(agent1, agent2, 500, policy1, policy2)

# Experiment 1b: PRANDOM for 9500 more steps
run_experiment(agent1, agent2, 9500, policy1, policy2)

# Experiment 1c: PGREEDY for 9500 more steps
policy1.set_policy_type('PGREEDY')
policy2.set_policy_type('PGREEDY')
run_experiment(agent1, agent2, 9500, policy1, policy2)

# Experiment 1d: PEXPLOIT for 9500 more steps
policy1.set_policy_type('PEXPLOIT')
policy2.set_policy_type('PEXPLOIT')
run_experiment(agent1, agent2, 9500, policy1, policy2)

# Evaluation
num_evaluation_episodes = 100
average_reward1, success_rate1 = evaluate_agent(agent1, env, num_evaluation_episodes)
average_reward2, success_rate2 = evaluate_agent(agent2, env, num_evaluation_episodes)

print(f"Agent 1: Average Reward = {average_reward1}, Success Rate = {success_rate1}")
print(f"Agent 2: Average Reward = {average_reward2}, Success Rate = {success_rate2}")

# Print the final Q-table for agent1 (experiment 1c)
print("Final Q-table for agent 1 (experiment 1c):")
print(agent1.q_table)
