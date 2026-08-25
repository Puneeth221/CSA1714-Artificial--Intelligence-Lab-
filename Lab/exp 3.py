from collections import deque

def water_jug(jug1, jug2, target):
    queue = deque()
    visited = set()

    queue.append((0, 0, []))

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        path = path + [(a, b)]

        if a == target or b == target:
            print("Solution:")
            for state in path:
                print(state)
            return

        states = [
            (jug1, b),       # Fill Jug 1
            (a, jug2),       # Fill Jug 2
            (0, b),          # Empty Jug 1
            (a, 0),          # Empty Jug 2
            (a - min(a, jug2-b), b + min(a, jug2-b)),  # Jug1 -> Jug2
            (a + min(b, jug1-a), b - min(b, jug1-a))   # Jug2 -> Jug1
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

jug1 = 4
jug2 = 3
target = 2

water_jug(jug1, jug2, target)
