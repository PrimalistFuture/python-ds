def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    freq_counter = {}
    for letter in phrase:
        if letter not in freq_counter:
            freq_counter[letter] = 1
        else: freq_counter[letter] += 1
    return freq_counter