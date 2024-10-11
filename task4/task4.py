import sys

def min_moves(numbers):
    numbers.sort()
    median = numbers[len(numbers) // 2]
    moves = sum(abs(number - median) for number in numbers)
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py <numbers_file>")
        sys.exit(1)
        
    numbers_file = sys.argv[1]
    
    with open(numbers_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        
    print(min_moves(numbers))