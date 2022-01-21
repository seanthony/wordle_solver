from requests import get


def get_five_letter_words(url):
    request = get(url)
    content = request.text
    all_words = content.split()
    five_letter_words = filter(lambda s: len(s) == 5, all_words)
    list_of_words = list(map(lambda s: s.lower(), five_letter_words))
    return list_of_words

def known_letters_checked(list_of_words):
    known_letters = ''
    print('enter known letter placement (leave blank or enter 5 characters)')
    while True:
        known_letters = input('known chars: ').lower()
        print('input:', known_letters, '...checking\n')
        if len(known_letters) == 0:
            print('no known letters entered.')
            return list_of_words, "     "
        elif len(known_letters) == 5:
            known_letters = ''.join([ch if ch.isalpha() else " " for ch in known_letters])
            break
        else:
            print('wrong number of characters entered. oop.\n\n')
    
    print('finding matches for...', known_letters.replace(' ', '_'))
    remaining_words = []
    for word in list_of_words:
        for i in range(len(known_letters)):
            ch = known_letters[i]
            if (ch != word[i]) and (ch != ' '):
                break

            if i == 4:
                remaining_words.append(word)

    print(len(remaining_words), 'words found that match known letters and placement.')
    return remaining_words, known_letters


def other_letters_in_word(remaining_words, known_letters):
    while True:
        response = input('what other letters do you know are in the word? (or leave blank)\n')
        cleaned_response = ''.join([ch.lower() for ch in response if ch.isalpha()])
        print('checking', cleaned_response, '...')
        if len(cleaned_response) == 0:
            print('no other chars entered')
            return remaining_words
        elif len(known_letters.replace(' ', '')) + len(cleaned_response) > 5:
            print('too many chars')
            continue
        else:
            break

    indexes = []
    for i in range(len(known_letters)):
        if known_letters[i].strip():
            continue
        else:
            indexes.append(i)
        
    final_word_list = []
    for word in remaining_words:
        remaining_letters = ''
        for i in indexes:
            remaining_letters += word[i]

        b = True
        for ch in cleaned_response:
            if ch not in remaining_letters:
                b = False
                break
        
        if b:
            final_word_list.append(word)

    print(len(final_word_list), 'words found.')
    return final_word_list    


def get_user_input(list_of_words):
    remaining_words, known_letters = known_letters_checked(list_of_words)
    if remaining_words:
        final_word_list = other_letters_in_word(remaining_words, known_letters)
        if final_word_list:
            print('\n'.join(final_word_list))
        else:
            print('no matching words found')


def main():
    list_of_words = get_five_letter_words('https://raw.githubusercontent.com/raun/Scrabble/master/words.txt')
    while input('continue? (y)\n').lower() == 'y':
        get_user_input(list_of_words)


if __name__ == "__main__":
    main()