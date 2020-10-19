time = int(input("\033[34m" "Input time in seconds: "))

day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time

print("\033[0m\033[36m" "d:h:m:s -> %d:%d:%d:%d" % (day, hour, minutes, seconds))