class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((t,v))
        dist = [inf] * (n+1) #verbalize what this means
        dist[0] = 0
        hp = [(0,k)]
        while hp:
            time,node = heappop(hp)
            if dist[node] != inf: continue
            dist[node] = time
            for t,v in adj[node]:
                heappush(hp,(time+t, v))

        print(dist)
        return -1 if inf in dist else max(dist)