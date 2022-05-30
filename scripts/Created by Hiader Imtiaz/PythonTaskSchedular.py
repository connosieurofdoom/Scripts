# Python Task Schedular
# pip install scheduler
from scheduler import Scheduler
import scheduler.trigger as trigger
import datetime as date
# Function to be executed
def func():
    print("Do Something Here...")
sch = Scheduler()
# Run in Cycles
sch.cyclic(func, date.timedelta(minutes=3))
# Run after Minutes
sch.minutely(func, date.timedelta(seconds=3))
# Run after hour
sch.hourly(func, date.timedelta(minutes=3))
# Run after day
sch.daily(func, date.timedelta(hours=3))
# Run after week
sch.weekly(func, date.timedelta(days=3))
# Run after month
sch.monthly(func, date.timedelta(weeks=3))
# Run only Once
sch.once(func, date.datetime(year=2022, month=7, day=23, minute=25))