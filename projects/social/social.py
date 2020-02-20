import random 
from util import Queue
import time


class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True   
    # Same as add vertex
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph_linear(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User_{i+1}")
        # Linear time 
        # Refactor to be O(n) time 
        total_friendships = avg_friendships * num_users // 2
        friendshipsCreated = 0
        collisions = 0
        # Pick a random number 1-n, pick another random number 1-n
        while friendshipsCreated < total_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id= random.randint(1, self.last_id)
        # Create friendship between those 2 ids
            if self.add_friendship(user_id, friend_id):
                friendshipsCreated += 1
            else:
                collisions += 1
        # Until you have friendship count = totalFriendships
        print(f"COLLISIONS: {collisions}")


        # Adding a friendship creates two edges
        # Create friendships
        # Create a list with all possible friendships
        # possible_friendships = []
        # for user_id in self.users:
        #     for friends_id in range(user_id+1, self.last_id + 1):
        #         possible_friendships.append((user_id, friends_id))
        
        # # Shuffle the list
        # random.shuffle(possible_friendships)
        # # print("-------")
        # # print(possible_friendships)
        # # print("----")
        # # Grad the first total_friendship pairs from the list and create friendships
        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     # print(f"This is a friendship - {friendship}")
        #     self.add_friendship(friendship[0], friendship[1])

        # average_friends = total_friendships / num_users
        # total_friendships = avg_friendships = num users 
        # N = avg_friendships + num_users // 2

    def populate_graph_quadratic(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User_{i+1}")

        # Adding a friendship creates two edges
        # Create friendships
        # Create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friends_id in range(user_id+1, self.last_id + 1):
                possible_friendships.append((user_id, friends_id))
        
        # # Shuffle the list
        random.shuffle(possible_friendships)
        # # print("-------")
        # # print(possible_friendships)
        # # print("----")
        # # Grad the first total_friendship pairs from the list and create friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            # print(f"This is a friendship - {friendship}")
            self.add_friendship(friendship[0], friendship[1])

        # average_friends = total_friendships / num_users
        # total_friendships = avg_friendships = num users 
        # N = avg_friendships + num_users // 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        #Return extended network of users 
        visited = {}  # Note that this is a dictionary, not a set
        # Dictionary will have a key and value pair 
        # !!!! IMPLEMENT ME
        q.enqueue([user_id])
        # For every user_id we need to traverse and find connecting nodes
        # for each node find the shortest path 
        # counter = 0
        while q.size() > 0:
            # counter += 1
            # print("Degree",counter)
            path = q.dequeue()
            # print(path)
            v = path[-1]
            if v not in visited:
                # print(v)
                visited[v] = path
                for friend_id in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(friend_id)
                    q.enqueue(path_copy)
                    
                
        # set the shortest path as the value in key value 
        # Track visited 
        # If not visited ...
            #run our bft for shortest path 

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    num_users = 100
    avg_friendships = 5
    start_time = time.time()
    # Only good if you have sparse graphs not good for dense 
    sg.populate_graph_linear(num_users, avg_friendships)
    end_time = time.time()
    print(f"Linear runtime: {end_time - start_time} seconds")
    start_time = time.time()
    sg.populate_graph_quadratic(num_users, avg_friendships)
    end_time = time.time()
    print(f"Quadratic runtime: {end_time - start_time} seconds")
    # print(f"Users - {sg.users}")
    # print(f"Friendships - {sg.friendships}")
    # print(sg.get_all_social_paths(1))
    # connections = sg.get_all_social_paths(1)
    # print(connections)
