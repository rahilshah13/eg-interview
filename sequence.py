import time
import matplotlib.pyplot as plt
import numpy as np
import os

def sequence_calculator_disk(n):
    try:
        with open("sequence_lookup_table.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                line_number, value, _ = line.split()
                if int(line_number) == n:
                    return int(value)
                
    except FileNotFoundError:
        pass

    if n == 0:
        with open("sequence_lookup_table.txt", "w") as file:
            file.write(f"0 0 0.0000\n")
            file.write(f"1 1 0.0000\n")
        return 0
    
    elif n == 1:
        return 1
    
    # n > 1
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = (3 * prev1) - prev2
        prev2, prev1 = prev1, current
        
    return prev1

def generate_lookuptable_disk(N):

    if os.path.exists("sequence_lookup_table.txt"):
        with open("sequence_lookup_table.txt", "r") as file:
            lines = file.readlines()
            current_line_number = int(lines[-1].split()[0]) if lines else 0
    else:
        current_line_number = 0

    with open("sequence_lookup_table.txt", "a") as file:
        for n in range(current_line_number, N + 1):
            print("HERE: ", n)
            start = time.time()
            sequence_value = sequence_calculator_disk(n)
            exe_time_ms = (time.time() - start) * 1000

            file.write(f"{n} {sequence_value} {exe_time_ms:.4f} \n")

sequence_lookup = {0: 0, 1: 1}

def sequence_calculator_memory(n):

    if n in sequence_lookup:
        return sequence_lookup[n]
    
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        current = (3 * prev1) - prev2
        prev2, prev1 = prev1, current
        sequence_lookup[i] = current
        
    return sequence_lookup[n]


def benchmark_sequence(n_max, step=1000):
    n_values = list(range(0, n_max + 1, step))
    times_memory = []
    
    for n in n_values:
        start_time = time.perf_counter()
        sequence_calculator_memory(n)
        end_time = time.perf_counter()
        times_memory.append(end_time - start_time)
    
    return n_values, times_memory


def main():
    N, step = 100000, 1000
    n_values, times_memory = benchmark_sequence(N, step)

    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot actual measurements
    plt.plot(n_values, times_memory, 'b-', label='In-memory Implementation')
    
    # Create O(N) reference line
    # Scale it to intersect with our actual measurements for better visualization
    scale_factor = max(times_memory) / max(n_values)  # Makes O(N) line comparable
    o_n_line = [n * scale_factor for n in n_values]
    plt.plot(n_values, o_n_line, 'r--', label='O(N) Reference')

    plt.xlabel('N')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sequence Calculator Performance')
    plt.legend()
    plt.grid(True)
    plt.savefig('sequence_performance.png')
    plt.show()

if __name__ == "__main__":
    main()