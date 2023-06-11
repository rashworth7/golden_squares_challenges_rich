## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

```python

class Music():

    def __init__(self):
        # Parameters:
        #   track_list: list
        # Side effects:
        #   Creates an empty list which is assigned to the instance of the class

    def display_tracks(self):
        # Parameters:
        #   None
        # Returns:
        #   A list a songs currently listening to
        # Side effects:
        #   None

    def add_track(self, song):
        # Parameter:
        #   song: string
        # Returns:
        #   Error messaage if song is already on the list
        # Side effects;
        #   Updates the track list to include the new track. 

    def remove_track(self, song):
        # Parameters:
        #   Song: string
        # Returns:
        #   Error message if the song isn't on the list
        # Side effects:
        #   Song is removed from the track list

```

## 3. Create Examples as Tests


```python

"""
Create instance of class
Creates an empty list of tracks
"""

music = Music():
music.track_list == []

"""
Creates instance of class
Use display track to return a string telling the user
there are no tracks on the list
"""
music = Music()
music.display_tracks() # => "There are currently no tracks on the list"

"""
Add a single track to the list
Updates track list with the song
"""
music = Music()
music.add_track("Yellow") # => track_list == ["Yellow"]

"""
Add two tracks to the list
Udpates track list with both songs
"""
music = Music()
music.add_track("Yellow")
music.add_track("Paradise")
music.track_list # => ["Yellow", "Paradise"]

"""
display tracks when songs are on the list
returns a list of the tracks listened to
"""
music = Music()
music.add_track("Yellow")
music.add_track("Paradise")
music.display_tracks # => ["Yellow", "Paradise"]


"""
Add a track that is already on the list
Returns an error message
"""
music = Music()
music.add_track("Yellow")
music.add_track("Yellow") # => raises error with message "Track is already on the list"

"""
Remove a single track from the list
"""
music = Music()
music.add_track("Yellow")
music.remove_track("Yellow") # => track_list = []

"""
Remove a track from the list that isn't on the list
remove_track raises an error
"""
music = Music()
music.remove_track("Yellow") # => raises an error with the message "That track is not on the list"

```


## 4. Implement the Behaviour

