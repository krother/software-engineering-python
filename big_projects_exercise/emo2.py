

def get_emoji(nazwa):
    if nazwa == "wesoly":
        return(":-)")
    elif nazwa == "smutny":
        return(":-(")


if __name__ == '__main__':
    nazwa = input()
    emoji = get_emoji(nazwa)
    print(emoji)