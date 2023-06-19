# Import necessary libraries
from copy import deepcopy

# Rubik's Cube class
class RubiksCube:
    def __init__(self):
        # Initialize the cube state
        self.state = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
                      ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                      ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                      ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                      ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                      ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]
    
    # Function to rotate a face clockwise
    def rotate_face_clockwise(self, face):
        face[0][0], face[2][0], face[2][2], face[0][2] = face[2][0], face[2][2], face[0][2], face[0][0]
        face[0][1], face[1][0], face[2][1], face[1][2] = face[1][0], face[2][1], face[1][2], face[0][1]
    
    # Function to rotate a face counter-clockwise
    def rotate_face_counter_clockwise(self, face):
        face[0][0], face[0][2], face[2][2], face[2][0] = face[0][2], face[2][2], face[2][0], face[0][0]
        face[0][1], face[1][2], face[2][1], face[1][0] = face[1][2], face[2][1], face[1][0], face[0][1]
    
    # Function to rotate the whole cube
    def rotate_cube(self, direction):
        if direction == 'U':
            self.rotate_face_clockwise(self.state[0])
            temp = deepcopy(self.state[1][0])
            self.state[1][0] = deepcopy(self.state[3][0])
            self.state[3][0] = deepcopy(self.state[2][0])
            self.state[2][0] = deepcopy(self.state[4][0])
            self.state[4][0] = deepcopy(temp)
        elif direction == 'U\'':
            self.rotate_face_counter_clockwise(self.state[0])
            temp = deepcopy(self.state[1][0])
            self.state[1][0] = deepcopy(self.state[4][0])
            self.state[4][0] = deepcopy(self.state[2][0])
            self.state[2][0] = deepcopy(self.state[3][0])
            self.state[3][0] = deepcopy(temp)
        # Implement rotation for other directions (F, F', B, B', L, L', R, R', D, D')
        # ...
    
    # Function to print the cube state
    def print_cube(self):
        for face in self.state:
            for row in face:
                print(row, end=' ')
            print()
    
    # Function to play the Rubik's Cube
    def play(self):
        while True:
            self.print_cube()
            move = input("Enter move (U, U', F, F', B, B', L, L', R, R', D, D'): ")
            self.rotate_cube(move)

# Create a Rubik's Cube instance
cube = RubiksCube()

# Play the Rubik's Cube
cube.play()
