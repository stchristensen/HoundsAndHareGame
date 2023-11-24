import networkx as nx
import matplotlib.pyplot as plt

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
            1: (1, 0.5),
            2: (2, 0.5),
            3: (3, 0.5),
            4: (1, 0),
            5: (2, 0),
            6: (3, 0),
            7: (1, -0.5),
            8: (2, -0.5),
            9: (3, -0.5),
            10: (4, 0)}
        
        node_colors = ['red' if node == self.hare else 'blue' if node in self.hounds else 'gray' for node in G.nodes()]
        nx.draw(G, pos=positions, with_labels=True, node_color=node_colors, node_size=800, font_size=10)
        plt.show()
        
    def is_valid_move(self, current_position, new_position, player):
        # Check if the new position is in th elist of connected positions
        if new_position in self.board[current_position] and new_position not in self.hounds and new_position != self.hare:
            if player=='hound' and new_position in self.backward_moves.get(current_position, []):
                return False
            return True
        return False
        
    def move_hound(self, hound_position, new_position):
        # Move a hound to a new position
        if self.is_valid_move(hound_position, new_position, 'hound'):
            self.hounds[self.hounds.index(hound_position)] = new_position
            return True
        return False
    
    def move_hare(self, new_position):
        # Move the hare to a new position
        if self.is_valid_move(self.hare, new_position, 'hare'):
            self.hare = new_position
            return True
        return False
    
    def check_win(self):
        #check for a win or a draw
        pass
    
    def play_game(self):
        # Main game loop
        pass