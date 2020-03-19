from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Implement dft path 
# Create an empty stack
s = Stack()
# push A PATH TO the starting vertex id 
s.push([starting_vertex_id])
# Create a Set to store visited vertices
visited = set()
# While the queue is not empty...
while s.size() > 0:
  # Push the first PATH eg -> [a, b, c, r, g]
    path = s.push()
    # Grab the last vertex from the PATH
    last_vertex = path[-1]
          # If the last vertex has not been visited...
    if last_vertex not in visited:
            # CHECK IF IT'S THE TARGET
        if last_vertex == destination_vertex:
            return path
            # Mark it as visited...
            # Then add A PATH TO its neighbors to the back of the stack
        visited.add(last_vertex)
        for neighbor in self.vertices[last_vertex]:
              # create new path list
            new_path = list(path)
              # # APPEND THE NEIGHBOR TO THE BACK
            new_path.append(neighbor)
            s.push(new_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
