from environment import CustomEnvironment
from agent import QLearningAgent
from state import StateRepresentation
from action import ActionSpace
from reward import calculate_reward
from policy import Policy

# Define the parameters for the CustomEnvironment
grid_size_x = 3
grid_size_y = 3
grid_size_z = 3
risky_cells = [...]  # Define the risky cells
male_initial_pos = (1, 1, 1)
female_initial_pos = (2, 2, 2)
pickup_cells = [...]  # Define the pickup cells
dropoff_cells = [...]  # Define the dropoff cells

# Create the CustomEnvironment instance
env = CustomEnvironment(grid_size_x, grid_size_y, grid_size_z, risky_cells, male_initial_pos, female_initial_pos,
                        pickup_cells, dropoff_cells)

# Create the StateRepresentation instance
state_representation = StateRepresentation()

# Create the ActionSpace instance
action_space = ActionSpace()

# Get the number of actions from the action_space instance
n_actions = action_space.get_n_actions()

# Create the QLearningAgent instances for the male and female agents
agent1 = QLearningAgent(env, n_actions=n_actions)
agent2 = QLearningAgent(env, n_actions=n_actions)

# Create instances of the Policy
policy1 = Policy(agent1)
policy2 = Policy(agent2)


def run_experiment(agent1, agent2, n_steps, policy1, policy2):
    for step in range(n_steps):
        # Get the environment states
        current_state1 = agent1.environment.get_state()
        current_state2 = agent2.environment.get_state()

        # Choose actions based on the policies
        action1 = agent1.choose_action(current_state1, policy1)
        action2 = agent2.choose_action(current_state2, policy2)

        # Take the actions and get the next states and rewards
        next_state1, reward1 = agent1.environment.take_action('F', action1)
        next_state2, reward2 = agent2.environment.take_action('M', action2)

        # Calculate the rewards using the calculate_reward function
        reward1 = calculate_reward('F', current_state1, action1)
        reward2 = calculate_reward('M', current_state2, action2)

        # Update the agents with the new information
        agent1.update(current_state1, action1, reward1, next_state1)
        agent2.update(current_state2, action2, reward2, next_state2)

        # Check if the terminal condition has been reached, and if so, break the loop
        # ...


# Set the number of steps and policy types
n_steps = 1000
policy_type1 = 'PEXPLOIT'
policy_type2 = 'PEXPLOIT'

# Run the experiments
run_experiment(agent1, agent2, n_steps, policy1, policy2)
