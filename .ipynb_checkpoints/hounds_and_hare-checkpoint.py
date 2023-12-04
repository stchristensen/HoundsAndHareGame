# hounds_and_hare.py

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class HoundsAndHare:
    def __init__(self):
        # Initialize the board, hounds, and hare
        self.board = {
            0: [1, 4, 7],
            1: [0, 2, 4, 5],
            2: [1, 3, 5],
            3: [2, 5, 6, 10],
            4: [0, 1, 5, 7],
            5: [1, 2, 3, 4, 6, 7, 8, 9],
            6: [3, 5, 9, 10],
            7: [0, 4, 5, 8],
            8: [5, 7, 9],
            9: [5, 6, 8, 10],
            10: [3, 6, 9]
        }
        
        self.backward_moves = {
            1: [0],
            2: [1],
            3: [2, 5],
            4: [0],
            5: [1, 4, 7],
            6: [5],
            7: [0],
            8: [7],
            9: [5, 8],
            10: [3, 6, 9]
        }
        
        self.hounds = [0, 1, 7]
        self.hare = 10
        self.move_count = 0 # Initialize move counter
        self.current_player = "Hounds"
        
    
    def display_board(self):
        # Displays the current state of the board
        
        # Loop through each position
        for pos in range(11):
            if pos in self.hounds:
                print('H', end=' ') # 'H' represents a hound
            elif pos == self.hare:
                print('R', end=' ') # 'R' represents a hare
            else:
                print('.', end=' ') # '.' represents an empty position
            
            # Print a newline every 3 positions to create rows
            if pos in [3, 6, 10]:
                print()
                
                
    def visualize_board(self):
        plt.figure(figsize=(4,2))  # (width, height) in inches
        G = nx.Graph()
        
        # Add nodes
        for pos in self.board:
            G.add_node(pos, style='filled', fillcolor='white')
            
        # Add edges based on your board connections
        for pos, connections in self.board.items():
            for con in connections:
                G.add_edge(pos, con)
        
        positions = {
            0: (0, 0), 
            1: (1, 1),
            2: (2, 1),
            3: (3, 1),
            4: (1, 0),
            5: (2, 0),
            6: (3, 0),
            7: (1, -1),
            8: (2, -1),
            9: (3, -1),
            10: (4, 0)}
        
        node_colors = ['red' if node == self.hare else 'blue' if node in self.hounds else 'gray' for node in G.nodes()]
        nx.draw(G, pos=positions, with_labels=True, node_color=node_colors, node_size=800, font_size=10)
        
        plt.show()
        
    def is_valid_move(self, current_position, new_position, player):
        # Check if the new position is in the list of connected positions
        if player != self.current_player:  
            return False  # not valid if wrong player
        elif new_position in self.board[current_position] and new_position not in self.hounds and new_position != self.hare:
            if player=='Hounds' and new_position in self.backward_moves.get(current_position, []):
                return False  # Backwards hound move
            return True  # valid move
        return False
        
    def move_hound(self, hound_position, new_position):
        # Move a hound to a new position
        if self.is_valid_move(hound_position, new_position, 'Hounds'):
            self.hounds[self.hounds.index(hound_position)] = new_position
            self.move_count += 1
            self.current_player = "Hare"
            return True
        return False
    
    def move_hare(self, new_position):
        # Move the hare to a new position
        if self.is_valid_move(self.hare, new_position, 'Hare'):
            self.hare = new_position
            self.move_count += 1
            self.current_player = "Hounds"
            return True
        return False
    
    def check_win(self):
        #check for a win or a draw
        # Check if the hare is trapped
        if not any(self.is_valid_move(self.hare, pos, 'Hare') for pos in self.board[self.hare]):
            return 'Hounds', 1
        
        # If hare gets to position 0, that's a win for hare
        if self.hare in [0]:
            return 'Hare', 1
        
        if self.move_count >= 30:
            return 'Draw', 0.5
        return None, 0
    
    def encode_state(self):
        # Create a vector with a default value for empty positions
        state_vector = [0]*11
        
        # Mark postions occupied by hounds
        for hound_pos in self.hounds:
            state_vector[hound_pos] = 1
            
        # Makr the position occupied by the hare
        state_vector[self.hare] = 2
        
        return np.array(state_vector)
    
    def possible_hare_moves(self):
        current_position = self.hare
        return [(self.hare, pos) for pos in self.board[current_position] if pos not in self.hounds]
    
    def possible_hound_moves(self):
        possible_moves = []
        for hound in self.hounds:
            for new_position in self.board[hound]:
                # Check if the move is valid (not backward and not occupied)
                if self.is_valid_move(hound, new_position, 'Hounds'):
                    possible_moves.append((hound, new_position))
        return possible_moves
    
    
    
    def play_game(self):
        # Main game loop
        turn = 'Hounds' # Hounds start the game
        while True:
            if turn == 'Hounds':
                # Implement logic to choose and make a hound move
                
                turn = 'Hare'
            else:
                # Implement logic to choose and make a hare move
                
                turn = 'Hounds'
                
            result = self.check_win()
            if result is not None:
                print(f"Game Over: {result}")
                break
            
            if self.move_count >= 30:
                print("Game Over: Draw")
                break
                
                
                
                
                
                
                
                
                