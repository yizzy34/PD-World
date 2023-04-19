def evaluate_agent(agent, env, num_episodes):
    total_reward = 0
    num_successes = 0

    for episode in range(num_episodes):
        env.reset()  # Reset the environment to the initial state
        state = env.get_state()
        done = False
        episode_reward = 0

        while not done:
            action = agent.choose_action(state, 'PGREEDY')
            next_state, reward, done = env.take_action(agent.gender, action)
            state = next_state
            episode_reward += reward

            if env.is_success(agent.gender):  # You need to implement this function in your CustomEnvironment class
                num_successes += 1

        total_reward += episode_reward

    average_reward = total_reward / num_episodes
    success_rate = num_successes / num_episodes

    return average_reward, success_rate
