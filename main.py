import agent
import environment
import policy
from state import StateRepresentation
from reward import calculate_reward
from policy import choose_action

# Create an instance of StateRepresentation
state_representation = StateRepresentation()

# Get the environment state
environment_state = environment.get_state()

# Convert the environment state using the state_representation instance
converted_state = state_representation.convert_state(environment_state)

# Pass the converted_state to the agent
action = agent.choose_action(converted_state, policy)

# In the run_experiment function, replace the reward1 and reward2 calculation with the following lines:
reward1 = calculate_reward(environment.agent1, current_state1, action1)
reward2 = calculate_reward(environment.agent2, current_state2, action2)

# In the QLearningAgent class, replace the choose_action method with the following line:
def choose_action(self, state, policy):
    return choose_action(self, state, policy)

# The rest of your code remains unchanged.

