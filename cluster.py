
def find_cluster(matrix):
    cluster = []
    row = len(matrix)
    cols = len(matrix[0])
    visited = [[False]*cols for _ in range(row)]
    def dfs(r,c,val,pro):
        if r < 0 or c < 0 or r >= row or c >= cols:
            return
        if visited[r][c] or matrix[r][c] != val:
            return
        visited[r][c] = True
        pro.append((r,c))
        dfs(r+1,c,val,pro)
        dfs(r,c+1,val,pro)
        dfs(r-1,c,val,pro)
        dfs(r,c-1,val,pro)

    for r in range(row):
        for c in range(cols):
            pro = []
            if not visited[r][c]:
                val = matrix[r][c]
                dfs(r,c,val,pro)
                cluster.append((val,pro))
    return cluster





if __name__ == '__main__':
    matrix = [[1,1,0,3],
              [1,2,1,3],
              [1,1,2,3]]
    print(find_cluster(matrix))
