def dfs(graph, current_vertex, target_value, visited=None):
    # Initialize visited if it isn't defined
    if visited is None:
        visited = []

    # Add current vertext to visited nodes
    visited.append(current_vertex)

    if current_vertex == target_value:
        return visited