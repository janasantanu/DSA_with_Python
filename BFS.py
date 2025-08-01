from Queue_using_list import *
def bfs(graph, start):
    # Create a queue object
    queue = Queue()
    
    # Enqueue the start node
    queue.enqueue(start)
    
    # Track visited nodes
    visited = []
    
    # BFS traversal loop
    while not queue.is_empty():
        # Dequeue a node from the queue
        node = queue.dequeue()
        
        # If the node hasn't been visited, process it
        if node not in visited:
            visited.append(node)
            
            # Enqueue all the unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.enqueue(neighbor)
    
    return visited

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

start_node = 0
print(f"BFS traversal starting from node {start_node}: {bfs(graph, start_node)}")