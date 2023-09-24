def is_perfect_number(N):
    if N <= 1:
        return 0  # Numbers less than or equal to 1 are not perfect

    factor_sum = 1  # Start with 1 as 1 is always a factor of any number

    # Calculate the sum of factors excluding the number itself
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            factor_sum += i
            if i != N // i:
                factor_sum += N // i

    return 1 if factor_sum == N else 0
