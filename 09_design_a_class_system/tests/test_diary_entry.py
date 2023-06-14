from lib.diary_entry import *

## DiaryEntry tests ##

"""
Given a DiaryEntry with title and contents
We see that relfected in it's title property
"""
def test_diary_entry_title():
    entry = DiaryEntry("Title", "Contents")
    assert entry.title == "Title"

"""
Given a DiaryEntry with title and contents
We see that relfected in it's contents property
"""
def test_diary_contents():
    entry = DiaryEntry("Title", "Contents")
    assert entry.contents == "Contents"

"""
Given a DiaryEntry with title and contents
We see that relfected the mobile number is None
"""
def test_mobile_number_none():
    entry = DiaryEntry("Title", "Contents")
    assert entry.mobile == None

"""
Given a DiaryEntry with title and contents and mobile number
We see that relfected in it's mobile_num property
"""
def test_mobile_number_added():
    entry = DiaryEntry("Title", "Contents", "07111222333")
    assert entry.mobile == "07111222333"

"""
Given a DiaryEntry with title and contents and mobile number
Check word count returns the correct number of words
"""
def test_word_count():
    entry = DiaryEntry("Title", "Contents of my Diary", "07111222333")
    assert entry.word_count() == 4

"""
Given a DiaryEntry with title and contents and mobile number
Check reading time returns the correct reading time
"""
def test_reading_time():
    entry = DiaryEntry("Title", "Contents of my Diary is here to stay", "07111222333")
    assert entry.reading_time(3) == 3
    