

class DiaryEntry():
    # User facing properties:
    #   diary title
    #   diary content
    #   mobile number

    def __init__(self, title, contents, mobile = None):
        # Parameters
        #   title: string
        #   content: string
        #   mobile: string
        self.title = title
        self.contents = contents
        self.mobile = mobile
    
    def word_count(self):
        # returns word count for diary entry
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: integer for how many wpm user can read 
        # Returns:
        #   the reading time in minutes (rounded to 1dp)
        pass