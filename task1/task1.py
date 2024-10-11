import sys

def circular_array_path(n, m):
    array = list(range(1, n + 1))
    path = []
    index = 0
    visited_indices = set()
    
    while True:
        path.append(array[index])
        visited_indices.add(index)
        index = (index + m - 1) % n
        if index in visited_indices:
            break
    return path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task1.py <n> <m>")
        sys.exit(1)
        
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    result_path = circular_array_path(n, m)
    print("".join(map(str, result_path)))