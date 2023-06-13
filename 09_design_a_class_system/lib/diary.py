

class Diary():
    #User facing properties
    #   diary entries: list of instances of DiaryEntry

    def __init__(self):
        self.entries = []

    def add(self, diary_entry):
        self.entries.append(diary_entry)

    def read_diary_entry(self, diary_entry):
        # Parameters:
        #   diary_entry: instance of diary entry
        # Returns:
        #   Contents of the diary
        return diary_entry.contents
    
    def read_diary_entry_given_time(self, wpm, minutes):
        # Parameters:
        #   wpm: integer of how many words you can read per minute
        #   minutes: integer - how mnay minutes available to read
        # Returns:
        #   contents with the closest reading time thaty is < minutes
        pass
    
    def display_mobile_nums(self):
        # Returns:
        #   List of mobile numbers associated with diary entries
        pass