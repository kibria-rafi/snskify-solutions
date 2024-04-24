def can_attack(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            row_diff = abs(queens[i][0] - queens[j][0])
            col_diff = abs(queens[i][1] - queens[j][1])
            if (queens[i][0] == queens[j][0] or 
                queens[i][1] == queens[j][1] or  
                row_diff == col_diff):   
                return "YES"  
    return "NO"  

queens = [tuple(map(int, input().split())) for _ in range(8)]
print(can_attack(queens))
