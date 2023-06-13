## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

#Nouns
Diary entries
List of diary entries
List of mobile phone numbers (attached to diary entry)
Tasks
list of tasks

#Verbs
add (diary entry)
add (task)
read diary entry
select diary entry
see to do list
see phone number list


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
 ┌─────────────────────────────────────────┐        ┌──────────────────────┐
 │                                         │        │                      │
 │  Diary                                  │        │ TaskList             │                
 │                                         │        │                      │                
 │ - add(entry)                            │        │ - add(task)          │                
 │ - list mobile phone numbers             │        │ - list_incomplete()  │                  
 │ - read diary entry(title)               │        │ - list_complete()    │               
 │ - read diary entry(reading time, wpm)   │        │                      │                
 └─────────────────────┬───────────────────┘        └───────────┬──────────┘
                       │                                        │                           
                       │                                        │                          
                       │                                        │                           
                       │                                        │                           
                       ▼                                        ▼                           
┌──────────────────────────────────────────┐       ┌────────────────────────┐               
│                                          │       │                        │               
│ DiaryEntry                               │       │ Task                   │
│                                          │       │                        │
│- initlialise(title, contents, mobile)    │       │- initialise(title)     │
│- word count                              │       │- mark_complete()       │
│- reading time                            │       │- complete(property)    │
│                                          │       │                        │
└──────────────────────────────────────────┘       └────────────────────────┘

```

_Also design the interface of each class in more detail._

```python

class Diary():
    #User facing properties
    #   diary entries: list of instances of DiaryEntry

    def __init__(self):
        pass

    def add(self, diary_entry):
        # Parameters:
        #   diary_entry: instance of DiaryEntry
        # Returns nothing
        # Side effects:
        #   Adds the diary entry to the list of dairy entries
        pass

    def read_diary_entry(self, diary_entry):
        # Parameters:
        #   diary_entry: instance of diary entry
        # Returns:
        #   Contents of the diary
        pass
    
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

class DiaryEntry():
    # User facing properties:
    #   diary title
    #   diary content
    #   mobile number

    def __init__(self):
        # Parameters
        #   title: string
        #   content: string
        #   mobile: string (set to None)
        pass
    
    def word_count(self):
        # returns word count for diary entry
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: integer for how many wpm user can read 
        # Returns:
        #   the reading time in minutes (rounded to 1dp)
        pass

class TaskList():
    # User facing properties:
    #   task list

    def __init__(self):
        #task_list = []
        pass

    def add(self, task):
        # Parameters
        #   task: instance of Task
        # Side effects:
        #   adds task to the list of tasks
        pass

    def list_incomplete(self):
        # Returns:
        #   list of incomplete tasks
        pass
    
    def list_complete(self):
        # Returns:
        #   List of completed tasks
        pass 

class Task():
    # User facing properties:
    # task title
    # Complete: True or False

    def __init__(self, title):
        # Parameters:
        # self.title = title
        # self.complete = False
        pass

    def mark_complete(self):
        # Side effects:
        #   marks self.complete as True
        pass


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

## Diary - Diary Entry Tests ###

"""
Given a Diary
When we add to diary entries
We see those entries reflected in the diary list
"""
diary = Diary()
entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
diary.add(entry_1)
diary.add(entry_2)
diary.entries # => [entry_1, entry_2]

"""
Given a Diary
We we two diary entries
Select a diary entry to read and return to the user
"""
diary = Diary()
entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
diary.add(entry_1)
diary.add(entry_2)
diary.read_diary_entry(entry_1) # => "This is my first diary entry"

"""
Given a Diary
We we two diary entries
Return the most appropriate Diary entry based on time and wpm when both have time to be read
"""
diary = Diary()
entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
diary.add(entry_1)
diary.add(entry_2)
diary.read_diary_entry_given_time(wpm=2, minutes=5) # => "This is now my second diary entry, how exciting!"

"""
Given a Diary
We we two diary entries
Return the most appropriate Diary entry based on time and wpm when NOT both have time to be read
"""
diary = Diary()
entry_1 = DiaryEntry("Title 1", "This is my first diary entry")
entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!")
diary.add(entry_1)
diary.add(entry_2)
diary.read_diary_entry_given_time(wpm=2, minutes=4) # => "This is my first diary entry"

"""
Given a Diary
We we two diary entries
Return a list of mobile numbers
"""
diary = Diary()
entry_1 = DiaryEntry("Title 1", "This is my first diary entry", "07999888666")
entry_2 = DiaryEntry("Title 2", "This is now my second diary entry, how exciting!", "07111222333")
diary.add(entry_1)
diary.add(entry_2)
diary.display_mobile_nums() # => ["07999888666", "07111222333"]
```

-----------------------------------------------------------------------------

## TaskList - Task tests ##

```python

"""
Given a TaskList
Add two tasks
Entries in the task list
"""
task_list = TaskList():
task_1 = Task("Take the bins out")
task_2 = Task("Wash the dishes")
task_list.add(task_1)
task_list.add(task_2)
task_list.tasks # => [task_1, task_2]

"""
Given a TaskList
Add two tasks - one incomplete and one complete
Returns list of incomplete tasks
"""
task_list = TaskList():
task_1 = Task("Take the bins out")
task_2 = Task("Wash the dishes")
task_1.mark_complete()
task_list.add(task_1)
task_list.add(task_2)
task_list.list_incomplete() # => [task_2]

"""
Given a TaskList
Add two tasks - one incomplete and one complete
Returns list of complete tasks
"""
task_list = TaskList():
task_1 = Task("Take the bins out")
task_2 = Task("Wash the dishes")
task_1.mark_complete()
task_list.add(task_1)
task_list.add(task_2)
task_list.list_complete() # => [task_1]

```

## 4. Create Examples as Unit Tests


```python

## DiaryEntry tests ##

"""
Given a DiaryEntry with title and contents
We see that relfected in it's title property
"""
entry = DiaryEntry("Title", "Contents")
entry.title # => "Title"

"""
Given a DiaryEntry with title and contents
We see that relfected in it's contents property
"""
entry = DiaryEntry("Title", "Contents")
entry.contents # => "contents"

"""
Given a DiaryEntry with title and contents
We see that relfected the mobile number is None
"""
entry = DiaryEntry("Title", "Contents")
entry.mobile_num # => None

"""
Given a DiaryEntry with title and contents and mobile number
We see that relfected in it's mobile_num property
"""
entry = DiaryEntry("Title", "Contents", "07111222333")
entry.contents # => "07111222333"

"""
Given a DiaryEntry with title and contents and mobile number
Check word count returns the correct number of words
"""
entry = DiaryEntry("Title", "Contents of my Diary", "07111222333")
entry.word_count() # => 4

"""
Given a DiaryEntry with title and contents and mobile number
Check reading time returns the correct reading time
"""
entry = DiaryEntry("Title", "Contents of my Diary is here to stay", "07111222333")
entry.reading_time(3) = 3
entry.complete # => True
```

------------------------------------------------------------------------------

## DiaryEntry tests ###

```python

"""
Given Task with title
Check reflected in title property
"""
task = Task("Take the bins out")
task.title # => "take the bins out"

"""
Given Task with title
Check it is marked incomplete
"""
task = Task("Take the bins out")
task.complete # => False

"""
Given Task with title
check mark_complete changes complete to True
"""
task = Task("Take the bins out")
task.mark_complete()
task.complete # => True


```
_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._