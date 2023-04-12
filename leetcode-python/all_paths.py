def func(graph):
    n = len(graph) - 1
    paths = []
    def dfs(idx, path):
        if idx == n:
            path.append(idx)
            paths.append(path)
            path = path[:-1]
            return
        
        for adj in graph[idx]:
            m = len(path)
            path.append(idx)
            dfs(adj, path)
            path = path[:m]
        return
    
    dfs(0, [])
    return paths

def main():
    graph = [[1,2],[3],[3],[]]
    sol = func(graph)
    print(sol)
    return

if __name__ == "__main__":
    main()