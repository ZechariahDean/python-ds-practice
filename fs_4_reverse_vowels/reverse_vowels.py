def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = set('aeiou')
    str_lst = list(s)
    idx = 0
    jdx = len(s) - 1
    while idx < jdx:
        if str_lst[idx].lower() not in vowels:
            idx += 1
        elif str_lst[jdx].lower() not in vowels:
            jdx -= 1
        else:
            str_lst[idx], str_lst[jdx] = str_lst[jdx], str_lst[idx]
            jdx -= 1
            idx += 1
return ''.join(str_lst)
