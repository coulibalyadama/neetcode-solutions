class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()
        res = 0

        def dfs(node, par, comp):
            comp.add(node)

            if len(visited) == n:
                return comp

            for nei in adj[node]:
                if nei == par:
                    continue
                if nei not in comp:
                    dfs(nei, node, comp)
            return comp
        
        for k in range(n):
            if k not in visited:
                visited = visited.union(dfs(k, -1, set()))
                res += 1
                
        return res
            
        