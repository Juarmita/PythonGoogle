import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])#naughty_user
