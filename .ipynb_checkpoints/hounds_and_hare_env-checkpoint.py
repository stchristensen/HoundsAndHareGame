import gym
from gym import spaces
import numpy as np

class HoundsAndHareEnv(gym.Env):
    def __init__(self):
        super(HOundsAndHareEnv, self).__init__()
        
        # Define action and observation space
        # They must by gym.spaces objects
        # Example when using discrete actions, you have two: move hound and move hare
        self.action_space = spaces.Discrete(11)
        self.observation_space = spaces.Box(low=0, high=2, shape=(11,), dtype=np.int)
        
        # Initialize state
        self.state = None
    
    def step(self, action):
        # Execute one time step within the environment
        # Your game logic goes here
        
        # Check if the action is for the hare or a hound
        if action in self.game.possible_hare_moves():
            # Move the hare
            self.game.move_hare(action)
        else:
            # Find which hond can make the move and move it
            for move in self.game.possible_hound_moves():
                if move[1] == action:
                    self.game.move_hound(move[0], move[1])
                    break
                    
        # Update the state and check for end game
        self.state = self.game.encode_state()
        result, reward = self.game.check_win()
        done = result is not None
        
        info = {} # Additional data, not used for training
                    
        return self.state, reward, done, info
    
    def reset(self):
        # Reset the state of the environment to an initial satte
        # Initialize your game board here
        return self.state
    
    def render(self, mode='human'):
        # Render the environment to the screen
        # You can use your display_board method here
        pass
    
    def close(self):
        # Close the environment
        pass
    
    
    