#Uses of enviroment variables

import os

print("HOME: " +os.environ.get("HOME",""))
print("SHELL: " +os.environ.get("SHELL",""))
print("FRUIT: " +os.environ.get("FRUIT",""))
#En linux obtendriamos el PATH en donde esta cada uno