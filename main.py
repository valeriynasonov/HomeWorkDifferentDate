def read_file(name_file):
    import json
    with open(name_file, encoding="utf-8") as f:
        data = json.load(f)
    return data

def create_list(name_file, data):
    list_of_words = [ ]
    for v in data["rss"]["channel"]["items"]:
        for key, value in v.items():
            if key == "description":
                list_of_words.extend(value.split(" "))
    return list_of_words

def create_list_word(name_file, list_of_words):
    list_of_word = []
    for element in list_of_words:
        lenght_word = len(element)
        if lenght_word > 6:
            list_of_word.append(element)
    return list_of_word


def create_dict(name_file, list_of_word):
    counter_dict = {}
    for element in list_of_word:
        enter_count = list_of_word.count(element)
        counter_dict[element] = enter_count
    return counter_dict

def sort_dict(name_file):
    data = read_file(name_file)
    print(data)
    list_of_words = create_list(name_file, data)
    print(list_of_words)
    list_of_word = create_list_word(name_file, list_of_words)
    print(list_of_word)
    counter_dict = create_dict(name_file, list_of_word)
    list_lider_word = list(counter_dict.items())
    list_lider_word.sort(key=lambda i: i[1])
    list_lider_word.reverse()
    return list_lider_word[0:3]

print(sort_dict("newsafr.json"))









