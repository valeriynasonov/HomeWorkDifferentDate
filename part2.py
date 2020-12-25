def read_file(name_file):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(name_file, parser)
    root = tree.getroot()
    news_xml = root.findall("channel/item")
    return news_xml

def create_list(name_file, data):
    list_of_words = [ ]
    for news in data:
        list_of_words.extend(news.find("title").text.split(" "))
    return list_of_words

def create_dict(name_file, list_of_words):
    list_of_word = [ ]
    counter_dict = { }
    for element in list_of_words:
        lenght_word = len(element)
        if lenght_word > 6:
            list_of_word.append(element)
            enter_count = list_of_word.count(element)
            counter_dict[element] = enter_count
    return counter_dict

def sort_dict(name_file):
    data = read_file(name_file)
    list_of_words = create_list(name_file, data)
    counter_dict = create_dict(name_file, list_of_words)
    list_lider_word = list(counter_dict.items())
    list_lider_word.sort(key=lambda i: i[1])
    list_lider_word.reverse()
    return list_lider_word[0:3]

print(sort_dict("newsafr.xml"))



