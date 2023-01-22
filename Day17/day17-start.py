
class User:

    # Initialise attributes - things the object will have
    def __init__(self, id, username):
        self.id = id
        self.username = username
        # Attribute with default value
        self.followers = 0
        self.following = 0

    # Method in a class - Following a user
    def follow(self, user):
        # Users follower count increase by 1
        user.followers += 1
        # User following count increase by 1
        self.following += 1

# Create object from User class
user_1 = User("001", "Hersey")
user_2 = User("002", "Sandy")

# Create a attribute
user_1.home = "Suffolk"

# Printing a attribute
print (f"ID: {user_1.id} Username: {user_1.username} Followers: {user_1.followers}")

print("User 1 Follows User 2")
user_1.follow(user_2)

print(f"User 1: Followers: {user_1.followers} Following: {user_1.following}")
print(f"User 2: Followers: {user_2.followers} Following: {user_2.following}")


