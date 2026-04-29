class Time:

    # constructor
    def __init__(self, seconds):
        self.seconds = seconds

    # function to convert and return a string of minutes and seconds
    def convert_to_minutes(self):
        mins = self.seconds // 60
        secs = self.seconds - (mins * 60)

        return "%d:%d" % (mins, secs)

    # function to convert and return string of hours, minutes, and seconds
    def convert_to_hours(self):
        secs = self.seconds

        hours = secs // 3600
        secs = secs - (hours * 3600)

        mins = secs // 60
        secs = secs - (mins * 60)

        return "%d:%d:%d" % (hours, mins, secs)


def main():

    # test the Time class
    time = Time(230)
    print(time.convert_to_minutes())

    time = Time(4520)
    print(time.convert_to_hours())


# call the main function
main()
