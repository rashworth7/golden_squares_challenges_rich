

class Diary():
    #User facing properties
    #   diary entries: list of instances of DiaryEntry

    def __init__(self):
        self.entries = []
        self.mobile_list = []

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
        entries_under_time_limit = [
            entry for entry in self.entries 
            if entry.reading_time(wpm) <= minutes]
        max_value = 0
        print(entries_under_time_limit)
        for entry in entries_under_time_limit:
            if entry.reading_time(wpm) > max_value:
                max_value = entry.reading_time(wpm)
                max_entry = entry
        
        return max_entry.contents

    
    def display_mobile_nums(self):
        # Returns:
        #   List of mobile numbers associated with diary entries
        for entry in self.entries:
            if entry.mobile != None:
                self.mobile_list.append(entry.mobile)
        return self.mobile_list
