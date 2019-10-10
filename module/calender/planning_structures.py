from person import Person
from person import unknown

# =========== ToDo-Class ============= #
# This class handles ToDo-Items (ToDos)
# They have a name, a status, a priority and a deadline
# The name depends on what you have to do, so if you have to wash a car the name is "Wash my car"
# The status explains if the ToDo is finished, not finished or is going to be pushed to another day
# Unfinished = "-" | Finished = "x" | Migrated = ">"
# Priority structures ToDos hierarchically.
# Priority = 1 means: "Urgent and important"
# Priority = 2 means: "Not urgent but important"
# Priority = 3 means: "Urgent but not important"
# Priority = 4 means: "Not Urgent and not important" -> will be deleted automatically after 3 days
# The deadline is the last day a ToDo has the possibility to be solved
# Only Name and Status have to be entered the rest is voluntarily

class ToDo():

    def __init__(self, name_ = unknown, status_ = unknown, priority_ = unknown, deadline_ = unknown):
        self.name = name_
        self.status = status_
        self.priority = priority_
        self.deadline = deadline_

    def getStatus(self):
        return self.status

    def setStatus(self, status_):
        self.status = status_

    def getPrio(self):
        return self.priority

    def setPrio(self, priority_):
        self.priority = priority_

    def getDeadline(self):
        return self.deadline

    def setDeadline(self, deadline_):
        self.deadline = deadline_

    def printToDo(self):
        print(self.status + " " + self.name + " " + self.prio + " " + self.deadline)

# =========== Appointment-Class ============= #
#   Actually Appointments are ToDos with a certain Deadline.
#   But Due to different display I seperated them from Todos and added other typical attributes.
#   Inheriting might be another solution but its just easier to keep it seperated in my opinion.
#   time is obviously the time of the appointment and name the name
#   place is a string for now on but will have a second attribute with coordinates

class Appointment():

    def __init__(self, name_ = unknown, time_ = unknown, place_ = unknown, date_ = unknown, contents_ = unknown):   # date_ = Person mit der man verabredet ist
        self.name = name_
        self.time = time_
        self.place = place_
        self.date = date_
        self.contents = contents_
