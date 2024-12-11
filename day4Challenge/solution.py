with open("./data.txt") as fin:
    lines = fin.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

#generate all directions 
dd = []
for dx in range(-1,2):
    for dy in range(-1,2):
        if dx != 0 or dy != 0:
            dd.append((dx, dy))
#dd = [(-1,-1), (-1,-0), (-1, 1)
#      (0,-1)            (0, 1)
#      (1.-1), (1,0), (1,1)
#                               ]

def has_xmas(i, j, d):
    dx, dy = d
    for k , x in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy

        if not (0<= ii < n and 0<= jj <m):
            return False
        if lines[ii][jj] != x:
            return False
    return True

def count_Xmas(n,m,dd):
    ans = 0
    for i in range(n):
        for j in range(m):
            for d in dd:
                ans += has_xmas(i,j,d)
    return ans

def has_xmas(i, j):
    if not (1 <= i < n - 1 and 1 <= j < m - 1):
        return False
    if lines[i][j] != "A":
        return False

    # Check both diagonals
    diag_1 = f"{lines[i-1][j-1]}{lines[i+1][j+1]}"
    diag_2 = f"{lines[i-1][j+1]}{lines[i+1][j-1]}"

    return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]

ans = 0
for i in range(n):
    for j in range(m):
        ans += has_xmas(i, j)

print(ans)