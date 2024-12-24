from collections import deque

house = {
    'bed1': ['bath2', 'closet1', 'hall'],
    'bath2': ['bed1'],
    'closet1': ['bed1'],
    'bed2': ['closet2', 'hall'],
    'closet2': ['bed2'],
    'bed3': ['closet3', 'hall'],
    'closet3': ['bed3'],
    'hall': ['bed1', 'bed2', 'bed3', 'closeth', 'bath1', 'living'],
    'bath1': ['hall'],
    'closeth': ['hall'],
    'living': ['back', 'foyer', 'hall', 'kitchen'],
    'foyer': ['living', 'front', 'coat', 'utility', 'kitchen'],
    'coat': ['foyer'],
    'utility': ['foyer'],
    'kitchen': ['living', 'foyer', 'den', 'garage', 'pantry'],
    'pantry': ['kitchen'],
    'front': ['garage', 'foyer', 'back'],
    'back': ['living', 'mud', 'front'],
    'mud': ['den', 'back'],
    'den': ['mud', 'kitchen'],
    'garage': ['front', 'kitchen']
}

def dfs_connectivity(current_key, target, visited):
    # If we found our target
    if current_key == target:
        return True
    # If we have already been here
    if current_key in visited:
        return False
    # Add the room to the visited set for later
    visited.add(current_key)
    # If any of the connecting rooms can get to the target, return True, otehrwise False
    found = False
    for key in house[current_key]:
        found |= dfs_connectivity(key, target, visited)
    return found

def dfs_longest_path(current_key, longest_paths, stack):
    # If we've already been in this room:
    if current_key in stack:
        # If we've encountered a new longest path
        if len(stack) >= len(longest_paths[0]):
            # If this longest path is longer than the rest
            if len(stack) > len(longest_paths[0]):
                # Clear the longest paths list since this path is longer than the rest
                longest_paths.clear()
            # Copy the path so far and append it to the list of all longest paths
            longest_paths.append(stack[:])
        # Return since we've been in this room already, proceding further would visit the room twice
        return
    # Add the current room to the path
    stack.append(current_key)
    # Visit every room adjacent to this one
    for key in house[current_key]:
        dfs_longest_path(key, longest_paths, stack)
    # Remove the current room from the path
    stack.pop()

def bfs_with_backtrack(queue, visited, current_key, steps, prev=None):
    # If we have already been in this room
    if current_key in visited:
        # If we found an alternate way to get to this room using the same amount of steps
        if steps == visited[current_key][0]:
            # Add the last room to the set of rooms leading to this one on a shortest path from the start
            visited[current_key][1].add(prev)
        # Return since we've been in this room already, proceding further would duplicate work.
        return
    # Add this room to the visited dictionary, adding the last room we were in for backtracking.  Add the amount of steps it took to get here in case another route was found with the same steps
    visited[current_key] = (steps, {prev})
    # Add all rooms adjacent to this one to the queue to visit later
    for key in house[current_key]:
        queue.appendleft((key, steps + 1, current_key))

def bfs(queue, visited, current_key, steps):
    # If we have already been in this room
    if current_key in visited:
        # Return since we've been in this room already, proceding further would duplicate work.
        return
    # Add this room to the visited dictionary, adding the amount of steps it took to get here.
    visited[current_key] = steps
    # Add all rooms adjacent to this one to the queue to visit later
    for key in house[current_key]:
        queue.appendleft((key, steps + 1))

def print_backtrack(visited, current_key, output=None):
    if not output:
        output = []
    if not current_key:
        print(output[::-1])
        return
    output.append(current_key)
    for key in visited[current_key][1]:
        print_backtrack(visited, key, output)
    output.pop()

def find_all_longest_paths():
    longest_paths = [[]]
    for key in house:
        dfs_longest_path(key, longest_paths, [])
    return longest_paths

def trace_shortest_paths_from(start):
    q = deque()
    backtrack = {}
    q.appendleft((start, 0))
    while q:
        bfs_with_backtrack(q, backtrack, *q.pop())
    return backtrack

def find_shortest_amount_of_steps(start):
    q = deque()
    steps_to = {}
    q.appendleft((start, 0))
    while q:
        bfs(q, steps_to, *q.pop())
    return steps_to

start = 'front'
end = 'secret treasure'

print(f'CAN WE GET FROM {start} to {end}?\n')
print(dfs_connectivity(start, end, set()))
print()

end = 'den'

print(f'CAN WE GET FROM {start} to {end}?\n')
print(dfs_connectivity(start, end, set()))
print()

print('LONGEST PATHS WITHOUT REPEATING:\n')
for path in find_all_longest_paths():
    print(path)
print()

print(f'LOWEST AMOUNT OF STEPS from {start} to {end}:\n')
print(find_shortest_amount_of_steps(start)[end])
print()

print(f'SHORTEST PATHS from {start} to {end}:\n')
print_backtrack(trace_shortest_paths_from(start), end)
print()
