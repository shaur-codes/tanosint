from instaloader import Instaloader, Profile
from core import *  # Assuming core is a custom module you have created

# Initialize Instaloader
L = Instaloader()

USERNAME = "s4m_s3pio1"
profile = Profile.from_username(L.context, USERNAME)
L.interactive_login(USERNAME)

data = loadx()
if data is None:
    data = {}

data['username'] = USERNAME

def dump_followees():

    if data['username'] == USERNAME:
        following = []
        print("{} follows these profiles: ".format(profile.username))
        for followee in profile.get_followees():
            following.append(followee.username)
        data[USERNAME] = {}  
        data[USERNAME]["followees"] = following
        print(following)
    else:
        print("Username not found!!")


def dump_followers():
    if data['username'] == USERNAME:
        followers = []
        print("{}'s followers: ".format(profile.username))
        for follower in profile.get_followers():
            followers.append(follower.username)  # Correct usage
        data[USERNAME] = {}  # Initialize user's dictionary if not existing
        data[USERNAME]["followers"] = followers
        print(followers)
    else:
        print("Username not found!!")


dump_followees()
dump_followers()
