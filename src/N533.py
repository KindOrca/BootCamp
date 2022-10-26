from collections import deque
from queue import Queue

bfs_graph = {   # 그래프를 인접리스트로 표현
    1: [2,3,4],
    2: [1,5,6],
    3: [1,6],
    4: [1],
    5: [6,7],
    6: [5],
    7: [6],
}

def bfs_queue(start_node, bfs_graph):
    visited = [False] * (len(bfs_graph) + 1)
    ret = []
    deq = deque()
    deq.append(start_node)
    ret.append(start_node)
    visited[start_node] = True
    while deq:
        num = deq.popleft()
        for i in bfs_graph[num]:
            if visited[i]: continue
            visited[i] = True
            deq.append(i)
            ret.append(i)
    return ret

def dfs_recur(node, dfs_graph, dfs_list=[]):
    dfs_list.append(node)
    for i in dfs_graph[node]:
        if i in dfs_list: continue
        dfs_recur(i, dfs_graph, dfs_list)
    return dfs_list


print(dfs_recur(2, bfs_graph))

nums = 'asdf'
print(nums[:-1])