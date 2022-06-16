# Alarm Clock
# A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
import time

def runAlarm(minutes):

    seconds = minutes * 60
    print("Stating Timer")
    time.sleep(seconds)
    print("Timer Done")


def main():

    runAlarm(.1)
    # unittest.main()

if __name__ == '__main__':
    main()