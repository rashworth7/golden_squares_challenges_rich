from lib.diary_entry import *
from lib.diary import *

"""
Given a Diary
When we add to diary entries
We see those entries reflected in the diary list
"""
def test_adding_two_entries_integrated_diary_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
    entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.entries == [entry_1, entry_2]

"""
Given a Diary
We we two diary entries
Select a diary entry to read and return to the user
"""
def test_integrated_read_diary_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
    entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.read_diary_entry(entry_1) == "This is my first diary entry"

# """
# Given a Diary
# We we two diary entries
# Return the most appropriate Diary entry based on time and wpm when both have time to be read
# """
# diary = Diary()
# entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
# entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
# diary.add(entry_1)
# diary.add(entry_2)
# diary.read_diary_entry_given_time(wpm=2, minutes=5) # => "This is now my second diary entry, how exciting!"

# """
# Given a Diary
# We we two diary entries
# Return the most appropriate Diary entry based on time and wpm when NOT both have time to be read
# """
# diary = Diary()
# entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
# entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
# diary.add(entry_1)
# diary.add(entry_2)
# diary.read_diary_entry_given_time(wpm=2, minutes=4) # => "This is my first diary entry"

# """
# Given a Diary
# We we two diary entries
# Return the most appropriate Diary entry based on time and wpm when NOT both have time to be read
# """
# diary = Diary()
# entry_1 = DiaryEntry("Title 1", "This is my first diary entry", "07999888666")
# entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!", "07111222333")
# diary.add(entry_1)
# diary.add(entry_2)
# diary.display_mobile_nums() # => ["07999888666", "07111222333"]