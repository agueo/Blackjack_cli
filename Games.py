# Games
class Player(object):
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep


def ask_yes_no(question):
    ''' ask a yes or no question '''
    response = None
    while response not in ('y', 'n'):
        response = input(question)
    return response

def ask_number(question, low, high):
    ''' ask for a number within a range '''
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


if __name__ == "__main__":
    print("You ran this module directly (and did not import 'import' it).")
