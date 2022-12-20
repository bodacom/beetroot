# done 1. Збери декілька текстів англійської мови. Наприклад звернення Президента з телеграму, або щось із твітеру,
#  новин.
# done 2. Запиши англійські тексти у текстовий файл
# done 3. Відкрити текстовий файл, зчитати інформацію та перекласти на українську мову, нижче кинув туторіал, доволі 
# просто.
# done 4. Навмисно програмою придумати якісь помилки у виниклому перекладі, або ж вони можуть там з‘явитися самі собою, 
# наприклад:
#     1. Після розділових знаків може не бути пробілу.
#     2. Слова з дефісом можуть записуватись як "Нью -Йорк".
#     3. Перед словом "що" не завжди стоїть кома(вона і не завжди потрібна, але в переважній більшості випадків - так).
# 5. Виправити ці та інші можливі помилки.
# 6. Отримати готовий і відредагований текст, який буде записано у текстовий файл із назвою _translated
# done 7. Бонус! Зробити так, щоб програма виводила:
# done     1. Найдовше речення з перекладеного тексту.
# done     2. Кількість слів у цьому тексті.
# done     3. Топ найбільш вживаних слів. (edited)


# import googletrans
from googletrans import Translator
import random


def generate_mistakes(text: str):
    """
    Функція додає пробіли перед розділовими знаками (.,!?) в рандомних локаціях рандомну кількість раз.
    
    """
    symbols = '.,!?'
    locations = []
    previous_index = 0
    
    # Generating list of relative locations of punctuation marks throughout the text
    for index, symbol in enumerate(text):
        if symbol in symbols:
            locations.append(index - previous_index)
            previous_index = index
    
    # If list of relative locations not empty we will add some additional whitespaces 
    # before random punctuation marks from locations. Relative locations are going to be modified each time.
    if locations:
        number_of_mistakes = random.randint(1, len(locations))
        for _ in range(0, number_of_mistakes):
            mistake = random.randint(0,len(locations)-1)
            mistake_location = 0
            for el in locations[0:mistake+1]:
                mistake_location += el
            text = text[0:mistake_location] + ' ' + text[mistake_location:]
            locations[mistake] += 1
    else:
        print('No punctuation were found in the text. Mo mistakes were generated.')

    return text


def fix_mistakes(text: str):
    """
    Функція видаляє пробіли перед розділовими знаками (.,!?)

    """
    symbols = '.,!?'
    the_end_of_text = False
    index = 0
    
    # As there is a chance on multiple whitespaces before some punctuation mark let's use while loop
    while not the_end_of_text:
        if text[index] in symbols:
            if index != 0:
                if text[index-1] == ' ':
                    text = text[0:index-1] + text[index:]
                    index -= 1 # going back to one index trying to find more whitespaces
                    continue # skipping of index increasing
        if not index == len(text) - 1:
            index += 1
        else:
            the_end_of_text = True # setting the variable to exit the loop

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
        #print(word, words_frequency[word])

    return list_of_frequencies[0: num_of_words]




translator = Translator()

text = read_text_file('texts.txt')

result = translator.translate(text, src='en', dest='uk')
str_result = str(result)

save_text_file(str_result)

text = generate_mistakes(str_result)
print(text)
text = fix_mistakes(text)
print(text)

print(longest_sentence(text))
print(num_of_words(text))
print(most_frequent_words(text, 10))