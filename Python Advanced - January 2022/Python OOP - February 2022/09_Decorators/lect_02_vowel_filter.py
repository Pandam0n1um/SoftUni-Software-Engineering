def vowel_filter(function):
    def wrapper():
        initial_list=function()
        vowels='aouei'
        return [vowel for vowel in initial_list if vowel.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())