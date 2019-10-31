def file_read(file_name):
    with open(file_name) as file:
        graph = {}
        for i in file:
            line = i.replace("\n", "").split(" ")
            key = int(line[1])
            value = int(line[0])
            if key in graph:
                graph[key].append(value)
            else:
                graph[key] = [value]
            if value not in graph:
                graph[value] = []

        return dict(sorted(graph.items()))


parent_dict = {}

def dfs(x, graph, visited, stack):
    if x in stack:
        return True
    stack.append(x)
    for i in graph[x]:
        if i not in visited:
            parent_dict[i] = x
            if dfs(i, graph, visited, stack):
                return True
    stack.remove(x)
    visited.append(x)
    return False


def get_cycle(graph):
    visited = []
    stack = []

    for vertex in graph:
        if vertex not in visited:
            parent_dict[vertex] = None
            if dfs(vertex, graph, visited, stack):
                trace = []
                elem = stack[-1]
                parent = parent_dict.get(elem)
                while not parent == stack[-1]:
                    parent = parent_dict.get(elem)
                    trace.insert(0, parent)
                    if parent == stack[-1]:
                        break
                    elem = parent
                return trace
    return False


graph = file_read("test.txt")
print(get_cycle(graph))
