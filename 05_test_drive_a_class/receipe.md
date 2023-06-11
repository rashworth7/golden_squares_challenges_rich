## Class

```python

class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        pass

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        pass

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass
```

##Tests

```python


# Title: "My Diary"
# Content: "This is my Diary:

# Check the function formats correctly
DiaryEntry.format() => "My Dairy: This is my Diary"

# Count words returns the number of words in the diary entry
DiaryEntry.count_words() => 4

# Check the reading time for specified wpm
DiaryEntry.reading_time(1) => 4


# These tests below need to be completed with the same class instance

# Title: "My Diary"
# Content: "text/long_diary_entry.txt"

# Check the correct length reading chunk is returned.
# 100 wpm for 2 minutes returns a string of length 200
DiaryEntry.reading_chunck(100, 2) => "<String with 200 words>"

# Check that the chunck of words starts from the next possible word
# 100 wpm for 2 minutues returns the next 200 words
DiaryEntry.reading_chunck(100, 2) => "<next available 200 words>"

# Check that the chunck of words returned at the end of the text is 150
# if 150 words are left and reading chunck is over 150 words
DiaryEntry.reading_chunck(100, 2) => "<last 150 words>"

# Check that the chunck of words returned after returning all the text
# is the first section of the diary entry
DiaryEntry.reading_chunck(100, 2) => "<first 200 words>"