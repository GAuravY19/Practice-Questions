class Solution:
    def BoundaryTraversal(self,matrix, n, m):
        new = []

        for i in range(m):
            new.append(matrix[0][i])

        for i in range(1,n):
            new.append(matrix[i][m-1])

        if n>1:
            for i in range(m-2, -1, -1):
                new.append(matrix[n-1][i])

        if m>1:
            for i in range(n-2, 0, -1):
                new.append(matrix[i][0])

        return new


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0

        matrix = []

        for i in range(n):
            row = []
            for j in range(m):
                row.append(values[k])
                k += 1

            matrix.append(row)

        obj = Solution()
        ans = obj.BoundaryTraversal(matrix, n, m)

        for i in ans:
            print(i, end=" ")
        print()
