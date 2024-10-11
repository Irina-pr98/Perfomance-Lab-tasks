import sys
import math

def dot_position(xc, yc, r, x, y):
    distance = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)
    if distance == r:
        return 0
    elif distance < r:
        return 1
    else:
        return 2
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py <circle_file> <dot_file>")
        sys.exit(1)
        
    circle_file = sys.argv[1]
    dot_file = sys.argv[2]
    
    with open(circle_file, 'r') as file:
        xc, yc = map(float, file.readline().split())
        r = float(file.readline().strip())
        
    with open(dot_file, 'r') as file:
        dot = [list(map(float, line.split())) for line in file.readlines()]
        
    for x, y in dot:
        print(dot_position(xc, yc, r, x, y))