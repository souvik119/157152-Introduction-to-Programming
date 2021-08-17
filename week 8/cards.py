class Card:
    '''
    Defines a class called Card which associates a particular suite and value to a card instance
    '''
    def __init__(self, suite, value):
        '''
        Asssigns card value and suite to new instance
        '''
        self.suite = suite
        self.value = value

    def get_display_string(self):
        '''
        Returns card value and suite in a more readable format
        '''
        value_lookup = {1: 'Ace',
                        2: 'Two',
                        3: 'Three',
                        4: 'Four',
                        5: 'Five',
                        6: 'Six',
                        7: 'Seven',
                        8: 'Eight',
                        9: 'Nine',
                        10: 'Ten',
                        11: 'Jack',
                        12: 'Queen',
                        13: 'King'
                        }

        suite_lookup = {1: 'Clubs',
                        2: 'Spades',
                        3: 'Hearts',
                        4: 'Diamonds'
                        }
        return f'{value_lookup[self.value]} of {suite_lookup[self.suite]}'
