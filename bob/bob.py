import string


def hey(phrase):
    phrase = phrase.strip()
    if phrase.isspace() or not phrase:
        return 'Fine. Be that way!'
    elif not set(phrase).isdisjoint(string.ascii_uppercase) and set(phrase).isdisjoint(set(string.ascii_lowercase)):
        if phrase[-1] == '?':
            return 'Calm down, I know what I\'m doing!'
        else:
            return 'Whoa, chill out!'
    elif phrase[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'
