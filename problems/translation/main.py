# done 1. Збери декілька текстів англійської мови. Наприклад звернення Президента з телеграму, або щось із твітеру, новин.
# done 2. Запиши англійські тексти у текстовий файл
# 3. Відкрити текстовий файл, зчитати інформацію та перекласти на українську мову, нижче кинув туторіал, доволі просто.
# 4. Навмисно програмою придумати якісь помилки у виниклому перекладі, або ж вони можуть там з‘явитися самі собою, наприклад:
#     1. Після розділових знаків може не бути пробілу.
#     2. Слова з дефісом можуть записуватись як "Нью -Йорк".
#     3. Перед словом що не завжди стоїть кома(вона і не завжди потрібна, але в переважній більшості випадків - так).
# 5. Виправити ці та інші можливі помилки.
# 6. Отримати готовий і відредагований текст, який буде записано у текстовий файл із назвою _translated
# done 7. Бонус! Зробити так, щоб програма виводила:
# done     1. Найдовше речення з перекладеного тексту.
# done     2. Кількість слів у цьому тексті.
# done     3. Топ найбільш вживаних слів. (edited)


# import googletrans
# from googletrans import Translator


def generate_mistakes(text: str):
    """
    Навмисно програмою придумати якісь помилки у виниклому перекладі, або ж вони можуть там з‘явитися самі собою, наприклад:
     1. Після розділових знаків може не бути пробілу.
     2. Слова з дефісом можуть записуватись як "Нью -Йорк".
     3. Перед словом що не завжди стоїть кома(вона і не завжди потрібна, але в переважній більшості випадків - так).
    Сигнатури помилок?

    """
    return text


def fix_mistakes(text: str):
    """
    Виправити ці та інші можливі помилки.
    Сигнатури помилок?

    """
    return text


def save_text_file(translated_text: str):
    """
    Saves translated text in '_translated.txt' file

    Tested.

    """

    with open('_translated.txt', 'w') as translated_file:
        translated_file.write(translated_text)


def read_text_file(text_file_to_read: str):
    """
    Reads text in text_file_to_read file.
    Returns text as str

    Tested.

    """

    with open(text_file_to_read, 'r') as text_file:
        text = text_file.read()
    return text


def longest_sentence(text: str):
    """
    Splits the text to the sentences. 
    Counts length of the sentences. 
    Returns the length of the longest one.
    
    """
    # no_paragraphs_list = text.splitlines()
    # # print(no_paragraphs_list)
    # no_paragraphs_text = ''.join(no_paragraphs_list)
    # # print(no_paragraphs_text)
    # no_paragraphs_text = no_paragraphs_text.replace('!', '.').replace('?', '.')
    # sentences = no_paragraphs_text.split('.')
    # # print(sentences)
    
    sentences = ''.join(text.splitlines()).replace('!', '.').replace('?', '.').split('.')

    sentence_max_length = 0

    for sentence in sentences:
        if len(sentence.split()) > sentence_max_length:
            sentence_max_length = len(sentence.split())

    return sentence_max_length


def num_of_words(text: str):
    """
    Splits the text to the words. 
    Counts these. 
    Returns the length of the text.
    
    """
    # no_paragraphs_list = text.splitlines()
    # # print(no_paragraphs_list)
    # no_paragraphs_text = ''.join(no_paragraphs_list)
    # # print(no_paragraphs_text)
    # no_paragraphs_text = no_paragraphs_text.replace('!', '.').replace('?', '.')
    # sentences = no_paragraphs_text.split('.')
    # # print(sentences)

    words = ''.join(text.splitlines()).replace('!', ' ').replace('?', ' ').replace('.', ' ').split(' ')

    return len(words)


def most_frequent_words(text: str, num_of_words: int):
    """
    Creates a rating of num_of_words most frequent words

    """

    text = text.lower()
    words = text.replace('\n', ' ').replace('!', ' ').replace('?', ' ').replace('.', ' ').split(' ')
    words_frequency = {}

    for word in words:
        if word != '':
            if words_frequency.get(word):
                words_frequency[word] += 1
            else:
                words_frequency[word] = 1

    list_of_words = list(words_frequency)

    def frequency(word):
        return words_frequency[word]

    list_of_words.sort(reverse=True, key=frequency)
    list_of_frequencies = []

    for word in list_of_words:
        list_of_frequencies.append([word, words_frequency[word]])
        print(word, words_frequency[word])

    return list_of_words[0: num_of_words]




# print(googletrans.LANGUAGES)

# with open('texts.txt', 'r') as text_file:
#     text = text_file.read()
#     print(text)

# translator = Translator()

# result = translator.translate('hello world')

# print(result.src)
# print(result.dest)
# print(result.origin)
# print(result.text)
# print(result.pronunciation)

text = read_text_file('texts.txt')

save_text_file(text)

print(longest_sentence(text))

print(num_of_words(text))

print(most_frequent_words(text, 20))
