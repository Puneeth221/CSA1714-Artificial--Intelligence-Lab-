from queue import PriorityQueue

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def copy_state(state):
    return [row[:] for row in state]

def solve(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), start, []))
    visited = []

    while not pq.empty():
        cost, state, path = pq.get()

        if state == goal:
            print("Solution Found!")
            for step in path:
                for row in step:
                    print(row)
                print()
            return

        visited.append(state)

        x, y = find_blank(state)

        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx, dy in moves:
            nx, ny = x+dx, y+dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = copy_state(state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                if new_state not in visited:
                    pq.put((heuristic(new_state)+len(path)+1,
                            new_state,
                            path+[new_state]))

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

solve(start)
