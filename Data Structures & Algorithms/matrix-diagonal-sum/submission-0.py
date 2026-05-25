class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        prim_diag = 0
        sec_diag = 0
        n = len(mat)
        total = 0
        for i in range(n):
            prim_diag += mat[i][i]
            sec_diag += mat[i][n-1-i]

        total += prim_diag + sec_diag
        if n%2 == 1:
            total -= mat[n//2][n//2]

        return total