# hounds_and_hare_env.py

import gym
from gym import spaces
import numpy as np
from hounds_and_hare import HoundsAndHare

class HoundsAndHareEnv(gym.Env):
    def __init__(self):
        super(HoundsAndHareEnv, self).__init__()
        
        # Define action and observation space
        # They must by gym.spaces objects
        # Example when using discrete actions, you have two: move hound and move hare
        self.action_space = spaces.Discrete(3*11+1*11)  # 11 moves for each of the three hounds, and 11 moves for the hare
        self.observation_space = spaces.Box(low=0, high=2, shape=(11,), dtype=np.int32)
        
        # Initialize state
        self.state = None
        
    
    
    def step(self, action):
        # Execute one time step within the environment
        # Your game logic goes here
        
        reward = 0
        done = False
        info = {} # Additional data, not used for training
        
        # Decode action
        if action < 33: # Hound moves
            hound_index = action // 11 # Determine which hound
            target_position = action % 11 # Determine which position
            # Check if the move is valid for the selected hound
            if self.game.is_valid_move(self.game.hounds[hound_index], target_position, 'Hounds'):
                self.game.move_hound(self.game.hounds[hound_index], target_position)
                info['message'] = f"Hound {hound_index} moves to {target_position}"
                
            else: # else handle invalid hound move
                reward = -1 # Penalty for an invalid move
                info['message'] = f"Invalid move by Hound {hound_index} to {target_position}"
                done = True # Optionally end the episode (it will learn faster if it loses if it makes an illegal move?)
        
        else: # Hare moves
            target_position = action - 33
            # Check if the move is valid for the hare
            if self.game.is_valid_move(self.game.hare, target_position, 'Hare'):
                self.game.move_hare(target_position)
                info['message'] = f"Hare moves to {target_position}"
            else: # else handle invalid hare move
                reward = -1 # Penalty for an invalid move
                info['message'] = f"Invalid move by Hare to {target_position}"
                done = True # Optionally end the episode (it will learn faster if it loses if it makes an illegal move?)
        
                    
        # Update the state and check for end game
        self.state = self.game.encode_state()
        game_result, game_reward = self.game.check_win()
        if game_result is not None:
            done = true
            if reward == 0:  # Only update the reward if it hasn't been set by an invalid move
                reward = game_reward
                
        return self.state, reward, done, info
    
    
    def reset(self, seed=None, options=None):
        # Reset the state of the environment to an initial state
        # Initialize your game board here
        super().reset(seed=seed)
        info = {}
        # Reset the game to its intial state
        self.game = HoundsAndHare()
        
        # Reset other state variables
        self.state = np.array(self.game.encode_state()) # Update the state
                                  
        return self.state, info
    
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
    
    
    