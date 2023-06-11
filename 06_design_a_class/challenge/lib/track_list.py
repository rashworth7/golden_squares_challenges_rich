class Music():
    
    def __init__(self) -> None:
        self.track_list = []

    def display_tracks(self):
        if self.track_list == []:
            return "There are currently no tracks on the list"
        return self.track_list
    
    def add_track(self, song):
        if song in self.track_list:
            raise Exception("Track is already on the list")
        else:
            self.track_list.append(song)

    def remove_track(self, song):
        if song in self.track_list:
            self.track_list.remove(song)
        else:
            raise Exception("That track is not on the list")

