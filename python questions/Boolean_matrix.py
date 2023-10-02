

def booleanMatrix(matrix):
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                for k in range(r):
                    matrix[k][j] = 1

                for k in range(c):
                    matrix[r][k] = 1

if __name__ == '__main__':
    t = int(input())
    for  _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)

        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
        print()

