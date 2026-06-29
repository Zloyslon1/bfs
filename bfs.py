from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'H'],
    'H': ['D', 'E', 'G'],
}


def bfs(graph, start):
    visited = {start}
    order = [start]
    queue = deque([start])
    print(f'Старт: добавляем «{start}» в очередь.')
    print(f'Очередь: {list(queue)}\n')
    while queue:
        node = queue.popleft()
        print(f'Извлекаем «{node}» из очереди.')
        print(f'Очередь после извлечения: {list(queue)}')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                order.append(neighbor)
                queue.append(neighbor)
                print(f'   «{neighbor}» новый -> добавляем в очередь. '
                      f'Очередь: {list(queue)}')
            else:
                print(f'   «{neighbor}» уже посещён -> пропускаем')
        print()
    print(f'Порядок обхода: {order}')
    return order


if __name__ == '__main__':
    bfs(graph, 'A')
