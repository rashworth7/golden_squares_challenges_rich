from lib.diary_entry import *

## DiaryEntry tests ##

"""
Given a DiaryEntry with title and contents
We see that relfected in it's title property
"""
def test_diary_entry_title():
    entry = DiaryEntry("Title", "Contents")
    assert entry.title == "Title"

# """
# Given a DiaryEntry with title and contents
# We see that relfected in it's contents property
# """
# entry = DiaryEntry("Title", "Contents")
# entry.contents # => "contents"

# """
# Given a DiaryEntry with title and contents
# We see that relfected the mobile number is None
# """
# entry = DiaryEntry("Title", "Contents")
# entry.mobile_num # => None

# """
# Given a DiaryEntry with title and contents and mobile number
# We see that relfected in it's mobile_num property
# """
# entry = DiaryEntry("Title", "Contents", "07111222333")
# entry.contents # => "07111222333"

# """
# Given a DiaryEntry with title and contents and mobile number
# Check word count returns the correct number of words
# """
# entry = DiaryEntry("Title", "Contents of my Diary", "07111222333")
# entry.word_count() # => 4

# """
# Given a DiaryEntry with title and contents and mobile number
# Check reading time returns the correct reading time
# """
# entry = DiaryEntry("Title", "Contents of my Diary is here to stay", "07111222333")
# entry.reading_time(3) = 3
# entry.complete # => True