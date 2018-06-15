def ChangePossibilities(amount, arr):
    permutations = 0
    multiples =[]
    for i in arr:
        if amount % i == 0:
            permutations += 1
            multiples.append(i)
        for j in multiples:
            if i % j == 0 and i != j:
                permutations += 1
        
    return permutations
