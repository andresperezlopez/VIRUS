VIRUS
=====

VLC Iterative Recommender Under SoundCloud

Very simple Python-based social recommender for artists in SoundCloud.

It provides a VLC streaming playlist with randomly chosen songs, selected from users located at the given network distance from the starting artist. See a more complete description at http://wp.me/p49hsK-K

Only tested for Linux.

Usage
-----
python VIRUS_(followers/favorites) [username (as in the soundcloud url)] [network distance] [number of songs]

defaults: [vagabundobarbudo] [2] [5]


Requirements
-----------
- SoundCloud Python Wrapper
- SoundCloud Client ID
- VLC player
