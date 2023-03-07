def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    flipped_case_phrase = ""
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            if letter == letter.upper():
                flipped_case_phrase += letter.lower()
            else:
                flipped_case_phrase += letter.upper()
        else:
            flipped_case_phrase += letter
    return flipped_case_phrase