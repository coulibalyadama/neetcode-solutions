class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        nodeEdge = {i : [] for i in range(n)}

        for node1, node2 in edges:
            nodeEdge[node1].append(node2)
            nodeEdge[node2].append(node1)

        visited = set()
        
        def dfs(node, par):
            if node in visited:
                return False

            # if nodeEdge[node] == []:
            #     visited.add(node)
            #     print("test")
            #     return True
            
            visited.add(node)

            for nei in nodeEdge[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        res = dfs(0, -1)
        print(nodeEdge)
        print(visited)  
        return res and len(visited) == n
        