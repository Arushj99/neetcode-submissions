class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        - Want to ensure there aren't any cycles '''

        adj = defaultdict(list)
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set() 
        valid = [True]
        def dfs(node, prev):
            
            if node in visit:
                valid[0] = False
                return False

            visit.add(node)
            for nei in adj[node]:
                if not nei == prev:
                    if not dfs(nei, node):
                        return False
            return True
        

        return dfs(0, -1) and n == len(visit)