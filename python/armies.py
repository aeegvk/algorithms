class DisjointSet:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        elif x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def is_war(row, col, terrain):
    ds = DisjointSet()
    army_count = {}

    for i in range(row):
        for j in range(col):
            if terrain[i][j] == '#':
                continue

            if i > 0 and terrain[i-1][j] != '#':
                ds.union((i, j), (i-1, j))
            if j > 0 and terrain[i][j-1] != '#':
                ds.union((i, j), (i, j-1))

            if terrain[i][j] == 'X':
                plain_id = ds.find((i, j))
                army_count[plain_id] = army_count.get(plain_id, 0) + 1
                if army_count[plain_id] > 1:
                    print(ds.parent)
                    return True

    return False

# Example usage:
row = 10
col = 10

terrain = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '#', '#', '#', '#', '#'],
    ['#', '.', 'X', '.', '.', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '.', '.', '#', '.', 'X', '.', '#'],
    ['#', '#', '#', '#', '.', '#', '#', '#', '.', '#'],
    ['#', '#', '#', '#', '.', '#', '#', '#', '.', '#'],
    ['#', '#', '#', '#', '.', '#', '#', '#', '.', '#'],
    ['#', '#', '#', '#', '.', '#', '#', '#', 'X', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

if is_war(row, col, terrain):
    print("War is occurring!")
else:
    print("No war is occurring.")
