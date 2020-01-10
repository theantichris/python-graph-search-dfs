def dfs(graph, current_vertex, target_value, visited=None):
    # Initialize visited if it isn't defined
    if visited is None:
        visited = []

    # Add current vertext to visited vertices
    visited.append(current_vertex)

    # Base case: current vertex is target
    if current_vertex == target_value:
        return visited

    # Check each neighboring vertex
    for neighbor in graph[current_vertex]:
        # If we have not been to this vertex
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited) # Search down the new path

            if path:
                return path
