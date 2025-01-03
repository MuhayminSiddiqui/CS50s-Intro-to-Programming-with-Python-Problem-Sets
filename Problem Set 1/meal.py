def main():
    present_time = input("What time is it? ")
    conv_time = convert(present_time)

    if 7.0 <= conv_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= conv_time <= 13.0:
        print("lunch time")
    elif 18.0 <= conv_time <= 19.0:
        print("dinner time")


def convert(time):
    # For 12-Hour Format
    if time.rfind("a.m.") != -1:
        hours, minutes = time.split(":")
        minutes = minutes.removesuffix("a.m.")
        return float(hours) + (float(minutes) / 60)

    elif time.rfind("p.m.") != -1:
        hours, minutes = time.split(":")
        minutes = minutes.removesuffix("p.m.")
        return 12 + float(hours) + (float(minutes) / 60)

    # For 24-Hour Format
    else:
        hours, minutes = time.split(":")
        return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()