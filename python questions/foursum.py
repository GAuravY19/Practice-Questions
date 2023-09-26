class Solution:
    def fourSum(self, arr, k):
        # code here
        sums = []
        arr.sort()
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for n in range(j+1,len(arr)-1):
                    if (arr[i] + arr[j] + arr[n] + arr[n+1]) == k:
                        sums.append(arr[i])
                        sums.append(arr[j])
                        sums.append(arr[n])
                        sums.append(arr[n+1])
                        break

        return sums


n, k = map(int, input().split())
arr = list(map(int, input().split()))
MySol = solution()
sums = MySol.foursum(arr,k)
print(*sums, end=" ")
print("$")
