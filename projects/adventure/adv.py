from room import Room
from player import Player
from world import World
from util import Stack, Queue

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
# Possible directions

traversal_path = [ ]

class TravelGraph:
    def __init__(self, size=0):
        self.size = size
        self.rooms = {}
        self.exits = {}

# Create graph 
new_graph = TravelGraph()   
# print('worrrrlldd', world_rooms)
path = [None]
opp_direction = { 'n': 's', 's': 'n', 'e': 'w', 'w': 'e' } 

# Starting room with exits added to graph
new_graph.rooms[player.current_room.id] = player.current_room.get_exits()
new_graph.exits[player.current_room.id] = player.current_room.get_exits()

# if length of room is less than 500
while len(new_graph.rooms) < 500:
    # if current room in is not TravelGraph then add room and exits
    if player.current_room.id not in new_graph.rooms:
        new_graph.rooms[player.current_room.id] = player.current_room.get_exits()
        new_graph.exits[player.current_room.id] = player.current_room.get_exits()
        # Remove the last explored room from path
        last_move = path[-1]
        new_graph.exits[player.current_room.id].remove(last_move)

    # Search and find if there is any available exits
    while len(new_graph.exits[player.current_room.id]) == 0:
        last_move = path.pop()
        # add to traversal_path
        traversal_path.append(last_move)
        # travel
        player.travel(last_move)

    exit_move = new_graph.exits[player.current_room.id].pop(0)

    # Player travel
    traversal_path.append(exit_move)
    # turn in opp_direction or exit_move
    path.append(opp_direction[exit_move])
    player.travel(exit_move)

    # if new graph has explored 499 rooms add exits
    if len(new_graph.rooms) == 499:
        new_graph.rooms[player.current_room.id] = player.current_room.get_exits()


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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
