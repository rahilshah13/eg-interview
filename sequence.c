// zig cc sequence.c -o Generate-Sequence
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
 * Sequence calculator: S(n) = 3*S(n-1) - S(n-2), with S(0) = 0 and S(1) = 1
 * Space Complexity: O(1) as we only store previous values
 * Time Complexity: O(n) for first calculation, O(1) for cached lookups
 */

long long sequence_calculator(long long n) {
    FILE *file = fopen("sequence_lookup_table_C.txt", "r");
    
    // Try to read from lookup table first
    if (file != NULL) {
        long long line_num, value;
        double exec_time;
        
        while (fscanf(file, "%lld %lld %lf\n", &line_num, &value, &exec_time) == 3) {
            if (line_num == n) {
                fclose(file);
                return value;
            }
        }
        fclose(file);
    }

    // Base cases
    if (n == 0) {
        file = fopen("sequence_lookup_table_C.txt", "w");
        if (file != NULL) {
            fprintf(file, "0 0 0.0000\n");
            fprintf(file, "1 1 0.0000\n");
            fclose(file);
        }
        return 0;
    }
    else if (n == 1) {
        return 1;
    }

    // Calculate sequence
    long long prev2 = 0, prev1 = 1;
    long long current;
    
    for (long long i = 2; i <= n; i++) {
        current = (3 * prev1) - prev2;
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}

void generate_lookuptable(long long N) {
    FILE *file = fopen("sequence_lookup_table_C.txt", "r");
    long long current_line_number = 0;
    
    // Find the last calculated number
    if (file != NULL) {
        long long line_num, value;
        double exec_time;
        
        while (fscanf(file, "%lld %lld %lf\n", &line_num, &value, &exec_time) == 3) {
            current_line_number = line_num;
        }
        fclose(file);
    }

    // Append new calculations
    file = fopen("sequence_lookup_table_C.txt", "a");
    if (file != NULL) {
        for (long long n = current_line_number; n <= N; n++) {
            printf("HERE: %lld\n", n);
            
            clock_t start = clock();
            long long sequence_value = sequence_calculator(n);
            double exe_time_ms = ((double)(clock() - start) * 1000.0) / CLOCKS_PER_SEC;
            
            fprintf(file, "%lld %lld %.4f\n", n, sequence_value, exe_time_ms);
        }
        fclose(file);
    }
}

int main() {
    generate_lookuptable(10000000000LL);
    return 0;
}
