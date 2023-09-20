def max_subsequence_sum(seq):
    # Base Case: If the sequence has only one number, return that number
    if len(seq) == 1:
        return seq[0]
    
    mid = len(seq) // 2
    left_seq = seq[:mid]
    right_seq = seq[mid:]

    # Recursively find the maximum subsequence sum for left and right subsequences
    left_max = max_subsequence_sum(left_seq)
    right_max = max_subsequence_sum(right_seq)

    # Find the maximum sum crossing the midpoint
    left_bound_sum = float('-inf')
    summ = 0
    for i in range(mid-1, -1, -1):
        summ += seq[i]
        left_bound_sum = max(left_bound_sum, summ)

    right_bound_sum = float('-inf')
    summ = 0
    for i in range(mid, len(seq)):
        summ += seq[i]
        right_bound_sum = max(right_bound_sum, summ)

    cross_max = left_bound_sum + right_bound_sum

    # Return the maximum of the three
    return max(left_max, right_max, cross_max)

# Read the sequence from the file
with open('10.txt', 'r') as file:
    seq_str = file.read().strip("{}")
    seq = list(map(int, seq_str.split(',')))

print(max_subsequence_sum(seq))
