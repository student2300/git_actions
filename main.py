from datetime import datetime

file = open('timekeep.txt', 'a')

rn = datetime.now()

st = "Time is " + str(rn) + "\n"

file.write(st)
file.close()

print(st)