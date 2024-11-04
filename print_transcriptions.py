import csv
import os

def break_down(word):
    word = word[1:-1]
    
    result = []
    i = 0
    double_symbols = [
        "iː", "aʊ", "uː",
        "əʊ", "ɔɪ", "əː",
        "ɪə", "ɑː", "ɛː",
        "ʊə", "ɔː", "eɪ",
        "ʌɪ", "tʃ", "dʒ"
    ]
    while i < len(word):
        if i < len(word) - 1 and word[i:i+2] in double_symbols:
            result.append(word[i:i+2])
            i += 2
        else:
            result.append(word[i])
            i += 1
    return result

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

menu_dictionary = {'1': 'short_a_transcription.csv',
                   '2': 'short_e_transcription.csv',
                   '3': 'short_i_transcription.csv',
                   '4': 'short_o_transcription.csv',
                   '5': 'short_u_transcription.csv',
                   '6': 'long_a_transcription.csv',
                   '7': 'long_e_transcription.csv',
                   '8': 'long_i_transcription.csv',
                   '9': 'long_o_transcription.csv',
                   '10': 'long_u_transcription.csv',
                   '11': 'hard_g_transcription.csv',
                   '12': 'hard_c_transcription.csv',
                   '13': 'soft_g_transcription.csv',
                   '14': 'soft_c_transcription.csv',
                   '15': 'consonant_blends_transcription.csv',
                   '16': 'consonant_digraphs_transcription.csv',
                   '17': 'diphthongs_transcription.csv',
                   '18': 'r_controlled_vowels_transcription.csv',
                   '19': 'silent_letters_transcription.csv'}
menu_text = """

Menu: (type number and then press RETURN/ENTER)

1 to 5 for short vowels aeiou
6 to 10 for long vowels aeiou
11 to 12 for hard g and c
13 and 14 for soft g and c
15 for consonant blends
16 for consonant digraphs
17 for diphthongs
18 for r-controlled vowels
19 for silent letters
"""

csv_file_name = f"word_lists/{menu_dictionary[input(menu_text)]}"

with open(csv_file_name, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        clear_screen()
        word = row['Word']
        transcription = row['Phonemic Transcription']
        phonics_list = break_down(transcription)
        phonics = ""
        for phone in phonics_list:
            phonics += f" /{phone}/\n"
        print(f"\n  {word}\n\n {transcription}\n\n{phonics}")
        input()