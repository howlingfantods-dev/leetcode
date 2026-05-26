class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        adj = defaultdict(set)
                
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)

        min_edge_count = inf
        for _ , val in adj.items():
            min_edge_count = min(min_edge_count, len(val))
            
        corners = []
        for key, val in adj.items():
            if len(val) == min_edge_count:
                corners.append(key)
                     
        layer = [corners.pop()]
        foo = -1
        while foo == -1:
            prev = layer[-1]
            nei = [el for el in adj[prev] if el != prev]
            sm = len(adj[nei[0]])
            node = nei[0]
            for ne in nei: 
                if len(adj[ne]) < sm:
                    sm = len(adj[ne]) 
                    node = ne
            adj[node].remove(prev)
            adj[prev].remove(node)
            layer.append(node)
            if node in corners:
                foo = 2
        
        answer = [layer]
        m = len(layer)
        num_rows = (n // len(layer))
        for r in range(1, num_rows):
            layer = []
            for c in range(m):
                top = answer[r-1][c]
                assert len(adj[top]) == 1
                curr = list(adj[top])[0]
                layer.append(curr)
                adj[curr].remove(top)
                adj[top].remove(curr)
                if c - 1 >= 0:
                    a = layer[c - 1]
                    b = layer[c]
                    adj[a].remove(b)
                    adj[b].remove(a)
            answer.append(layer)
        
        return answer
            
         
         
"""
how do we know
1. create an adjecency list
2. find the nodes that have the least adjacency nodes
2.5. find minimum length
2.75 set of corner/ends 
3. Start with 1 of them since the result can be rotated?
4. then create the first row by selecting a child node with the
   less nodes left
5. how tf do you expand further, row by row? use the index above?
   and then choose the one with the least nodes left??
   - one issue is verifying a node has a common edges. 4 was confusing
   - i think we only need to use the row above because there would be
     only one node left but we need to update the list, maybe use a set?
     so we can keep track of the length of nodes left connected
     
    n =4 
    
[0,0,0,0,0,0,0,0,0,0]

[1,2,3,4,5,6]
[7,8,9,1,2,3]
[1,2,3,4,5,6]
     
[1,2,3]
Example 3:
visited[1,0,5,7,4]
0: [~1,4,~5]
1: [~0,7]
2: [3,4,5]
3: [2,6]
4: [0,2,6,7]
5: [~0,2]
6: [3,4,8]
7: [~1,4,8]
8: [6,7]
find the corners first or ends first
{1,3,5,8}
1 -> 0 -> 5 [1,0,5]
^.   ^
7    4.   2
^
"""

"""c++
class Solution {
public:
    vector<vector<int>> constructGridLayout(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for(const auto &v : edges)
        {
            adj[v[0]].push_back(v[1]);
            adj[v[1]].push_back(v[0]);
        }
        
        const int min_degree = std::min_element(
            adj.cbegin(),
            adj.cend(),
            [](const auto &x, const auto &y)
            {
                return x.size() < y.size();
            }
        )->size();
        
        vector<int> corners;
        for(int i = 0; i < n; ++i)
            if(adj[i].size() == min_degree)
                corners.push_back(i);
                
        auto dist = [&](int i)
        {
            vector<int> dists(n, INT_MAX);
            queue<int> q;
            q.push(i);
            dists[i] = 1;
            
            while(!q.empty())
            {
                int x = q.front();
                q.pop();
                for(int y : adj[x])
                    if(dists[y] == INT_MAX)
                    {
                        dists[y] = dists[x] + 1;
                        q.push(y);
                    }
            }
            return dists;
        };
        
        int c0 = corners[0];
        auto d0 = dist(c0);
        int c1 = corners[1];
        if(corners.size() > 2 && d0[corners[2]] < d0[c1])
            c1 = corners[2];
        auto d1 = dist(c1);
        vector<int> flat(n);
        std::iota(flat.begin(), flat.end(), 0);
        std::sort(flat.begin(), flat.end(),
            [&](int x, int y)
            {
                if(d0[x] + d1[x] != d0[y] + d1[y])
                    return d0[x] + d1[x] < d0[y] + d1[y];
                return d0[x] < d0[y];
            }
        );
        int cols = d0[c1];
        int rows = n / cols;
        vector<vector<int>> res(rows, vector<int>(cols));
        for(int i = 0; i < rows; ++i)
            for(int j = 0; j < cols; ++j)
                res[i][j] = flat[i * cols + j];
        return res;
    }
};
"""