def main():
    faces = input()
    print(convert(faces))


def convert(to):
    converted = to.replace(":)", "🙂").replace(":(", "🙁")
    return converted


main()