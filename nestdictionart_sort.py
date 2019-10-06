from operator import itemgetter, attrgetter
from datetime import datetime, timedelta
from collections import OrderedDict


def takeSecond(element):
    return element.date["date"]

class Test:
    def __init__(self,name,date):
        self.date = {}
        self.date["date"] = date #must be public
        self.name = name


datetime_obj1 = datetime.strptime("2015-12-31T16:43:56","%Y-%m-%dT%H:%M:%S")
datetime_obj2 = datetime.strptime("2014-12-31T16:05:56","%Y-%m-%dT%H:%M:%S")
datetime_obj3 = datetime.strptime("2014-12-31T16:55:56","%Y-%m-%dT%H:%M:%S")
test1 = Test('gave', datetime_obj1)
test2 = Test('zane', datetime_obj2)
test3 = Test('lohn', datetime_obj3)
test = [test1,test2,test3]
sortedList = sorted(test, key=takeSecond)


student_tuples = [('gave', 'B', datetime_obj1), ('zane', 'C', datetime_obj2), ('lohn', 'A', datetime_obj3)]
tasks = sorted(student_tuples, key=itemgetter(0))
print("done")

# if dic is a nest dictionary
#self.__activities = OrderedDict(sorted(self.__activities.items(), key=lambda x: (x[1].attri['PlannedStartDate'])))