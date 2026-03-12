## Writeup
### car_simulator.py:
  - I asked Claude to do it for me and then verified the 
  correctness of the plots wrt the problem statement using my knowledge of math.
  - Ensure that Python version 3+ is installed
  - Add the Python executeable to your PATH environment variable
  - Run: `python ./car_simulator.py` 

### sequence.py:
  I began by writing the outputs of `sequence_calculator(N)` to a .txt file.
  Disk writes are slow, so while I was waiting, I did two things:
  
  - Asked Claude to port the Python script to a C executeable and used Zig to compile it.
  - Converted the disk-based-look-up-table-function to an in-memory Python dictionary
    - this yielded a fast result for N=100000

  - I can verify the correctness of the C program's lookup-table,
  `sequence_lookup_table_C.txt`, using the output of the python program:
  `sequence_lookup_table.txt`

  Space Complexity Analysis:
    O(n) because the number of lines in `sequence_lookup_table.txt`
    grows by 1 as N grows by 1

  Time Complexity Analyis:
    - O(1) up to N if we have a lookup table.
    - On the first run:
        = O(n-1) + O(n-2) = 2*O(n) = O(n)
  
  - see: `sequence_performance.png` & `car_simulation_plot.png`