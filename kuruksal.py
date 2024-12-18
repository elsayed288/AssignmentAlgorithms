def find_set(parent, i):
    if parent[i] != i:
        parent[i] = find_set(parent, parent[i])
    return parent[i]

def union_set(parent, rank, x, y):
    rootX = find_set(parent, x)
    rootY = find_set(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def kruskal(vertices, edges):
    edges.sort(key=lambda edge: edge[2])

    parent = [i for i in range(vertices)]
    rank = [0] * vertices
    mst = []

    for edge in edges:
        u, v, weight = edge
        if find_set(parent, u) != find_set(parent, v):
            mst.append(edge)
            union_set(parent, rank, u, v)

    return mst

vertices = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst = kruskal(vertices, edges)

print("Edges in the MST are:", mst)
