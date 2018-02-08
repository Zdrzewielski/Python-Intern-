""" Module allows to calculate value of power of hacks. """


def hack_calculator(hack: str, letters: dict = None, phrases: dict = None):
    """Function calculate and return value of power of hacks.

    Keyword arguments:
    hack -- string which contain combinations of letters
    letters -- dictionary which contain effective letters as a keys of the dictionary and their power as values.
    ( Default {'a': 1, 'b': 2, 'c': 3} )
    phrases -- dictionary which contain special phrases as keys and their power as values
    ( Default {'ba': 10, 'baa': 20} )
    """

    if letters is None:
        letters = {'a': 1, 'b': 2, 'c': 3}
    if phrases is None:
        phrases = {'ba': 10, 'baa': 20}

    if type(hack) is not str or type(letters) is not dict or type(phrases) is not dict:
        raise ValueError('Wrong type of arguments, check your inputs.')

    sum_of_effective_letters = 0
    for element in letters.keys():
        sum_of_effective_letters += hack.count(element)
    if len(hack) > sum_of_effective_letters:
        return 0

    # Calculating power of letters in hack. #
    power = 0
    for element in letters.keys():
        power += letters[element] * sum(range(hack.count(element) + 1))

    sorted_tuples_phrases_values = sorted(
        phrases.items(), key=lambda x: x[1], reverse=True)
    # list of sorted items from the phrases dictionary by its values
    # (descending) #

    temp = 0  # auxiliary variable
    for element in sorted_tuples_phrases_values:
        # replacing each occurrence of a phrase in the text by dot.
        hack = hack.replace(element[0], '.')
        # replacing is necessary because the deleting the letters may cause
        # that some new phrases could appear #
        current = hack.count('.')
        power += (current - temp) * element[1]
        temp = current

    return power