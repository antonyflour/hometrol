import re
from util import util
x = "90-A2-DA-0F-45-D4"
if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", x.lower()):
    print "yes"
else:
    print "no"

print "EV-"+util.randstring()