## Writeup
### car_simulator.py:
  - I asked Claude to do it for me and then verified the 
  correctness of the plots wrt the problem statement using my knowledge of math.
  - Ensure that Python version 3+ is installed
  - Add the Python executeable to your PATH environment variable
  - Run: `python ./car_simulator.py` 

<img width="1200" height="500" alt="image" src="https://github.com/user-attachments/assets/7598ccf6-baf8-494f-b42a-05bbcdbb11c8" />

### sequence.py:
  I began by writing the outputs of `sequence_calculator(N)` to a .txt file.
  Disk writes are slow, so while I was waiting, I did two things:
  
  - Asked Claude to port the Python script to a C program and used Zig to compile it (`./Generate-Sequence`).
  - Converted the disk-based-look-up-table-function to an in-memory Python dictionary
    - this yielded a fast result for N=100000

  - I can verify the correctness of the C program's lookup-table,
  `sequence_lookup_table_C.txt`, using the output of the python program:
  `sequence_lookup_table.txt`

  Space Complexity Analysis:
    O(n) because the number of lines in `sequence_lookup_table.txt`
    grows by 1 as N grows by 1

  Time Complexity Analysis:
  - O(1) up to N if we have a lookup table
  
    On the first run: O(n-1) + O(n-2) = 2*O(n) = O(n)

  ``
  
  <img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/d1b03305-120e-42e1-b27d-da0e5883c5f9" />


### Retrospective:
<img width="550" height="187" alt="image" src="https://github.com/user-attachments/assets/46d1e6f0-419d-4026-bbd8-7a98bc8ccc67" />
<img width="405" height="100" alt="image" src="https://github.com/user-attachments/assets/bad09356-d8bb-4cbd-955d-051550881c43" />
