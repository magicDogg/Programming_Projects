import random

kanji_list = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'si', 'su', 'se', 'so',
              'ta', 'chi', 'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'hu', 'he', 'ho',
              'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo', 'n',
              'ga', 'gi', 'gu', 'ge', 'go', 'za', 'zi', 'zu', 'ze', 'zo', 'da', 'di', 'du', 'de', 'do',
              'ba', 'bi', 'bu', 'be', 'bo', 'pa', 'pi', 'pu', 'pe', 'po']

random.shuffle(kanji_list)

print(kanji_list[0:10])
print(kanji_list[10:20])
print(kanji_list[20:30])
print(kanji_list[30:40])
print(kanji_list[40:50])
print(kanji_list[50:60])
print(kanji_list[60:70])
print(kanji_list[70])
