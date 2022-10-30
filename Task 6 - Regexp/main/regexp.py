import re


while True:
    link = input()
    result = re.fullmatch(r"https://(?:(?:[w]{3}.youtube.com/watch\?v=[\w-]{11}(?:&t=\d){0,1})|"
             r"(?:youtu.be/[\w-]{11}(?:\?t=\d){0,1}))", link)

    if result:
        print('Link is valid')
    else:
        print('Link is not valid')
