import time
from dateutil import parser


A=time.strftime("%Y-%m-%d %H:%M:%S",time.strptime("Aug 28 2015 12:00AM","%b %d %Y %H:%M%p"))
print(A)



dt = parser.parse("Aug 28 2015 12:00:00")
print(dt)
dt=parser.parse("Thu Dec 10 10:45:00 2020")

print(dt)

print(parser.parse("3,23"))
print(parser.parse("20181021"))