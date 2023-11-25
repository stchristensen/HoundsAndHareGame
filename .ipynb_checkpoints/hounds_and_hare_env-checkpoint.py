# hounds_and_hare_env.py

import gym
from gym import spaces
import numpy as np

class HoundsAndHareEnv(gym.Env):
    def __init__(self):
        super(HoundsAndHareEnv, self).__init__()
        
        # Define action and observation space
        # They must by gym.spaces objects
        # Example when using discrete actions, you have two: move hound and move hare
        self.action_space = spaces.Discrete(3*11+1*11)  # 11 moves for each of the three hounds, and 11 moves for the hare
        self.observation_space = spaces.Box(low=0, high=2, shape=(11,), dtype=np.int)
        
        # Initialize state
        self.state = None
    
    def step(self, action):
        # Execute one time step within the environment
        # Your game logic goes here
        
        # Decode action
        if action < 33: # Hound moves
            hound_index = action // 11 # Determine which hound
            target_position = action % 11 # Determine which position
            # Check if the move is valid for the selected hound
            if self.is_valid_move(self.hounds[hound_index], target_position, 'hound'):
                self.move_hound(self.hounds[hound_index], target_position)
            else: # else handle invalid hound move
                reward = -1 # Penalty for an invalid move
                done = True # Optionally end the episode (it will learn faster if it loses if it makes an illegal move?)
        
        else: # Hare moves
            target_position = action - 33
            # Check if the move is valid for the hare
            if self.is_valid_move(selfhare, target_position, 'hare'):
                self.move_hare(hare_move)           
            else: # else handle invalid hare move
                reward = -1 # Penalty for an invalid move
                done = True # Optionally end the episode (it will learn faster if it loses if it makes an illegal move?)
        
                    
        # Update the state and check for end game
        self.state = self.game.encode_state()
        result, reward = self.game.check_win()
        done = result is not None
        
        info = {} # Additional data, not used for training
                    
        return self.state, reward, done, info
    
    def reset(self):
        # Reset the state of the environment to an initial state
        # Initialize your game board here
        
        # Reset the game to its intial state
        self.game = HoundsAndHare()
        
        # Reset other state variables
        self.state = self.game.encode_state() # Update the state
                                  
        return self.state
    
    def render(self, mode='human'):
        # Render the environment to the screen
        # You can use your display_board method here
        if mode == 'human':
            self.game.visualize_board()
        elif mode == 'rgb_array':
            pass                                  
    
    def close(self):
        # Close the environment
        pass
    
    
    