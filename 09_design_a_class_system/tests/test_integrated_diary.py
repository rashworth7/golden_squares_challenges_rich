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
We add two diary entries
Select a diary entry to read and return to the user
"""
def test_integrated_read_diary_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
    entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.read_diary_entry(entry_1) == "This is my first diary entry"

"""
Given a Diary
We add two diary entries
Return the most appropriate Diary entry based on time and wpm when both have time to be read
"""
def test_return_most_appropriate_entry_both_valid():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
    entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.read_diary_entry_given_time(wpm=2, minutes=5) 
    assert result == "This is now my second diary entry, how exciting!"

"""
Given a Diary
We add two diary entries
Return the most appropriate Diary entry based on time and wpm when NOT both have time to be read
"""
def test_return_most_appropriate_entry_when_not_time_to_read_both():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
    entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting for me!")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.read_diary_entry_given_time(wpm=2, minutes=4) == "This is my first diary entry"

"""
Given a Diary
We add two diary entries
Return the the list of mobile numbers associated with the Diary.
"""
def test_list_mobile_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is my first diary entry", "07999888666")
    entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!", "07111222333")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.display_mobile_nums() == ["07999888666", "07111222333"]