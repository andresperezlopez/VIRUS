"""
Andres Perez-Lopez, 2014
All wrongs reserved
"""

import soundcloud
import sys
from random import *
from subprocess import call


client_id="4f5e5222eff109ec6293e9ce7edfa08d" #put here yours
client = soundcloud.Client(client_id=client_id)
                
def get_followers(userID):
    
    return client.get('/users/'+str(userID)+'/followers')
    
def get_followings(userID):
    
    return client.get('/users/'+str(userID)+'/followings')
    
def next_level(user_id):
    followers=get_followers(user_id)
    "choose a follower who also has followers"
    follower=choice(followers)
    while len(client.get('/users/'+str(follower.id)+'/followers')) == 0 :
        follower=choice(followers)
    print follower.username

    return follower.id
        

                
if __name__ == '__main__':
    
    """argv[1] is the base artist name"""
    try:       
        base_artist=sys.argv[1]
    except:
        base_artist="vagabundobarbudo"
    """argv[2] is the friends depth level"""
    try :       
        init_level=int(sys.argv[2])
    except:
        init_level=2
    """argv[3] is the number of tracks in the playlist"""
    try :       
        num_tracks=int(sys.argv[3])
    except:
        num_tracks=5
    
    user = client.get('/resolve', url='https://soundcloud.com/'+base_artist)
    user_id=user.id #34293518

    artist_list=[]
    track_list=[]
    url_list=[]
        
    n=num_tracks
    while n>0:
        
        user = client.get('/resolve', url='https://soundcloud.com/'+base_artist)
        user_id=user.id #34293518   
        
        print "---------------------"
        level=init_level
        """go to the user"""
        while level>0:
            user_id=next_level(user_id)
            level=level-1
                
        """select randomly a track"""        
        tracks=client.get('/users/'+str(user_id)+'/tracks')
        artist=client.get('/users/'+str(user_id)).username
        try:
            track=choice(tracks)
            print "-"+track.title
        
            """get stream url"""
            stream_url = client.get(track.stream_url, allow_redirects=False)
            stream_url_location=stream_url.location
            
            artist_list.append(artist)
            track_list.append(track.title)
            url_list.append(stream_url_location)
            
            n=n-1
    #        print stream_url_location
#            call(["vlc",stream_url_location])
        except:
            print "USER HAS NO SONGS"
            
    print "--------------------"
    print "..... PLAYLIST ....."
    print "--------------------"
    
    for i in range(num_tracks):
        print artist_list[i]," - ",track_list[i]
    print "--------------------"
        
    call(["vlc"]+url_list)
