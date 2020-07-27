import sys

f = open('SMSSpamCollection', "a")
f.write("\n" + sys.argv[1])
f.close()
