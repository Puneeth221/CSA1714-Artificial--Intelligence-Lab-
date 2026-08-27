print("=" * 60)
print("              MINIMAX FOR GAMING")
print("=" * 60)

# Minimax function
def minimax(depth, node_index, is_max, values, target_depth):
    # Base case: leaf node
    if depth == target_depth:
        return values[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values, target_depth),
            minimax(depth + 1, node_index * 2 + 1, False, values, target_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, target_depth),
            minimax(depth + 1, node_index * 2 + 1, True, values, target_depth)
        )


# Leaf node values
values = [3, 5, 2, 9, 12, 5, 23, 23]

# Calculate tree depth
target_depth = 3

print("\nGame Tree Leaf Values:")
print(values)

print("\nPlayers:")
print("MAX = Maximizing Player")
print("MIN = Minimizing Player")

# Find optimal value using Minimax
optimal_value = minimax(0, 0, True, values, target_depth)

print("\n" + "-" * 60)
print("MINIMAX RESULT")
print("-" * 60)

print("Optimal value for MAX player:", optimal_value)

print("\nExplanation:")
print("MAX player chooses the maximum value.")
print("MIN player chooses the minimum value.")
print("Minimax checks possible future game states")
print("and selects the optimal result.")

print("\n" + "=" * 60)
print("              PROGRAM COMPLETED")
print("=" * 60)