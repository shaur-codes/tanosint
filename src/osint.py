from instaloader import Instaloader, Profile
from core import *  


L = Instaloader()

USERNAME = "s4m_s3pio1"
profile = Profile.from_username(L.context, USERNAME)
L.interactive_login(USERNAME)
print("initiating...")


data = loadx()
if USERNAME not in data:
    data[USERNAME] = {}
    dumpx(data) 

def dump_following():
    data = loadx()
    if USERNAME in data:
        following = []
        print("{} follows these profiles: ".format(profile.username))
        for followee in profile.get_followees():
            following.append(followee.username)
        
        data[USERNAME]["following"] = following
        
        print(following)
        dumpx(data)
    else:
        print("Username not found!!")

def dump_followers():
    data = loadx()
    if USERNAME in data:
        followers = []
        print("{}'s followers: ".format(profile.username))
        for follower in profile.get_followers():
            followers.append(follower.username)
        
        data[USERNAME]["followers"] = followers
        
        print(followers)
        dumpx(data)  
    else:
        print("Username not found!!")

def dont_follow(): 
    data = loadx()
    if USERNAME in data:
        dont_follow = []
        print(f"People who don't follow {profile.username} back")
        
        if "following" in data[USERNAME] and "followers" in data[USERNAME]:
            following = data[USERNAME]['following']
            followers = data[USERNAME]['followers']
            
            for followee in following:
                if followee not in followers:
                    dont_follow.append(followee)
            
            data[USERNAME]["dont_follow"] = dont_follow
            dumpx(data)  
            print(dont_follow)
        else:
            print("Following or Followers data not available. Please run dump_following() and dump_followers() first.")
    else:
        print("Username not found!!")


dump_following()
dump_followers()
dont_follow()
