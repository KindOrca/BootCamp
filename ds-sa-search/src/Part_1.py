"""
Bare Minimum Requirements
BFS와 DFS에 대해서 파악해봅시다

요구사항:
    노드의 움직임에 대해서 컴퓨터는 인간처럼 유연하게 생각하지 못합니다.
    때문에 사람들은 목적의 우선순위에 따라 다양한 알고리즘을 개발하였습니다.

    BFS와 DFS도 노드를 찾는다는 대전제에 따라 생겨난 알고리즘입니다.
    기존에 활용했던 반복문과 조건문을 재사용해보면서 코드를 구현합니다.

    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.
    (* 첨부된 BFSDFS_problem.png그림을 참고해주세요.
    그림을 바탕으로 BFS/DFS 출력값이 아래처럼 같습니다. 
    하지만 그래프 구성이 달라지면 출력값이 달라질 수 있다는 것을 테스트코드를 확인하면서 패턴을 파악해보세요.)
    
    입력값:
        dfs_recur(2, dfs_graph, dfs_list=[])
        bfs_queue(2, bfs_graph)
    출력값:
        [2, 5, 7, 6]
"""
from collections import deque
def dfs_recur(node, dfs_graph, dfs_list=[]):
    dfs_list.append(node)
    for i in dfs_graph[node]:
        if i in dfs_list: continue
        dfs_recur(i, dfs_graph, dfs_list)
    return dfs_list


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

