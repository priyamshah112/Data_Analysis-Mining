import os
import errno

filename = "C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user/user1.txt"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(filename, "w") as f:
    f.write("FOOBAR")
