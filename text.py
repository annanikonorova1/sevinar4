def most_frequent(text: str) -> list[str]:
    dict_counts = {}
    SHOW_LIMIT = 10
    new_sorted_dictionary = {}
    new_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower(). \
        strip()
    words_list = new_text.split()
    for word in words_list:
        counter = words_list.count(word)
        dict_counts[word] = counter
    sorted_values = sorted(dict_counts.values())[::-1]
    for i in sorted_values:
        for k in dict_counts.keys():
            if dict_counts[k] == i:
                new_sorted_dictionary[k] = dict_counts[k]
    return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]


text = 'Написание программ (или программирование)  – это весьма креативная и плодотворная деятельность.\
Вы можете писать программы по многим причинам, посвятив всю свою жизнь решению трудных задач анализа данных\,или получать удовольствие, помогая кому-нибудь другому решить трудную\
задачу. Эта книга предполагает, что каждый должен знать, как написать программу, а как только вы узнаете, как написать программу, то определите, что\именно вы хотите сделать с помощью новоприобретенных умений и навыков.'
print(most_frequent(text))
