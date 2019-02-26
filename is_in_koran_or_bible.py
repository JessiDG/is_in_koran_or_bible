import string
import fileinput

class Is_In_Koran_Or_Bible:

    def __init__(self, manuscript, dictionary):
        self.manuscript = self.to_unique_set(manuscript)
        self.dictionary = self.to_unique_set(dictionary)

    def to_unique_set(self, text):

        if type(text) is not str:
            raise TypeError("Please input a string")

        to_remove = string.punctuation + '-' + "\"" + "\'" + "“" + "‘" + "’" + "”" + string.digits
        stripped_string = ""
        for char in str(text):
            if char in to_remove:
                stripped_string += ' '
            else:
                stripped_string += char.lower()

        list_stripped_string = stripped_string.split()

        unique_words_set = set(list_stripped_string)
        return unique_words_set


    def find_difference(self):
        return self.manuscript - self.dictionary


    def __str__(self):
        i = 0
        difference = self.find_difference()
        return_str = ""
        for word in difference:
            if word is not None:
                return_str += str(i) + ": " + str(word) + "\n"
            i += 1
        return return_str


if __name__ == "__main__":
    with open('words.txt', 'r') as words:
        with open('holy_bible_word_english_bible.txt', 'r') as web:
                with open('holy_koran_translated_by_Maulana_Muhammad_Ali.txt', 'r') as mm_ali:
                    with open('holy_bible_translated_by_douay_rheims.txt', 'r') as douay_rheims:
                        with open('holy_koran_translated_from_arabic_by_JM_Rodwell.txt', 'r') as rodwell:
                            with open('holy_koran_translated_by_AY_Ali_M_Pickthall_MH_Shakir.txt', 'r') as three_translators:
                                with open('holy_bible_translated_king_james_version.txt', 'r') as kvg:

                                    manuscript = words.read()
                                    web_read = web.read()
                                    mm_ali_read = mm_ali.read()
                                    douay_rheims_read = douay_rheims.read()
                                    rodwell_read = rodwell.read()
                                    three_translators_read = three_translators.read()
                                    kvg_read = kvg.read()

                                    print("Comparing words against Word English translation "
                                          "of the Holy Bible")
                                    web_compare = Is_In_Koran_Or_Bible(manuscript, web_read)
                                    print("Comparing words against M. Ali translation "
                                          "of the Holy Koran")
                                    mm_ali_compare = Is_In_Koran_Or_Bible(web_compare.__str__(), mm_ali_read)
                                    print("Comparing words against Douay-Rheims translation "
                                          "of the Holy Bible")
                                    douay_rheims_compare = Is_In_Koran_Or_Bible(mm_ali_compare.__str__(),
                                                                                douay_rheims_read)
                                    print("Comparing words against Rodwell translation "
                                          "of the Holy Koran")
                                    rodwell_compare = Is_In_Koran_Or_Bible(douay_rheims_compare.__str__(),
                                                                           rodwell_read)
                                    print("Comparing words against AY ali, M Pickthall, "
                                          "and MH Shakir translations "
                                          "of the Holy Koran")
                                    three_compare = Is_In_Koran_Or_Bible(rodwell_compare.__str__(),
                                                                         three_translators_read)
                                    print("Comparing words against King James translation "
                                          "of the Holy Bible")
                                    all_compare = Is_In_Koran_Or_Bible(three_compare.__str__(), kvg_read)

                                    length = len(manuscript) + len(web_read) + len(
                                        mm_ali_read) + len(douay_rheims_read) + len(rodwell_read)\
                                             + len(three_translators_read) + len(kvg_read)
                                    print("Compared against: " + "{:,}".format(length) + " words "
                                                                                         "used in holy books \n")

                                    print(all_compare)
