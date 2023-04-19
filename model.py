class Model:
    def __init__(self, environment):
        self.environment = environment

    def predict(self, state, action):
        next_state, reward = self.environment.simulate_action(state, action)
        terminal = self.environment.is_terminal_state(next_state)
        return next_state, reward, terminal
