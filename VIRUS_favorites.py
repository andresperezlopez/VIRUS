"""
Andres Perez-Lopez, 2014
All wrongs reserved
"""

import soundcloud
import sys
from random import *
from subprocess import call


client_id="" #put here yours
client = soundcloud.Client(client_id=client_id)

# let's say we only know the url
user = client.get('/resolve', url='https://soundcloud.com/vagabundobarbudo')
# so we can get the vagabundobarbudo userID
user_id=user.id #34293518


                
def get_favoriters(trackID):
    
    return client.get('/tracks/'+str(trackID)+'/favoriters')
    
def get_favorites(userID):
    
    return client.get('/users/'+str(userID)+'/favorites')
    
def next_level(track_id):
    favoriters=get_favoriters(track_id)
#    for f in favoriters:
#        print "+++++"+f.username
    favoriter=choice(favoriters)
    print "-->"+favoriter.username
    
    user_id=favoriter.id
    favorites=get_favorites(user_id)
#    for f in favorites:
#        print "-----"+f.title
    favorite=choice(favorites)
    print favorite.title
    
    return favorite.id
        

                
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
        
        print "---------------------"
        tracks=client.get('/users/'+str(user_id)+'/tracks')
    
        """select a track with favoriters"""
        track=choice(tracks)
        while len(client.get('/tracks/'+str(track.id)+'/favoriters')) == 0 :
            track=choice(tracks)
            
        track_id=track.id
        print track.title
#        
        level=init_level
        """go to the track"""
        while level>0:
    #    for l in range(level):
            last_track_id=track_id
            track_id=next_level(track_id)
            if track_id != last_track_id:
                level=level-1
                
    
        track=client.get('/tracks/'+str(track_id))
        track_name=track.title
        artist= client.get('/users/'+str(track.user_id)).username
        
        """get stream url"""
        try: #maybe the song is not public
            stream_url = client.get(track.stream_url, allow_redirects=False)
            stream_url_location=stream_url.location
            
            """store"""
            artist_list.append(artist)
            track_list.append(track_name)
            url_list.append(stream_url_location)
            n=n-1
        except:
            print "private song"
              
    print "--------------------"
    print "..... PLAYLIST ....."
    print "--------------------"
    
    for i in range(num_tracks):
        print artist_list[i]," - ",track_list[i]
    print "--------------------"
        
    call(["vlc"]+url_list)
    
