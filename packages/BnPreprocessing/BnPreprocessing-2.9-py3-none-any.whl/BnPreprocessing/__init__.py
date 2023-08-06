"""
Author = Kowsher Ahmed, Avishek Das,
Email = ahmedshuvo969@gmail.com, avishek.das.ayan@gmail.com
"""

from pathlib import Path
import re
script_location = Path(__file__).absolute().parent
sw_loc = script_location / "bn_stopwords.txt"
global stop_words
with open(sw_loc,'r',encoding = 'utf-8') as f:
    stop_words = f.read()


def remove_punc(text):
    pattern = re.compile('[!@#$%‘’^“”&√*()_+-={}\[\];:\'\"\|<>,.///?`~।]', flags=re.I)
    return pattern.sub(r' ', text).replace("\\", "") 

def remove_digits(text):
    pattern = re.compile('[1234567890১২৩৪৫৬৭৮৯০]', flags=re.I)
    return pattern.sub(r'', text)

def remove_nonBangla(text):
    pattern = re.compile('[A-Z]', flags=re.I)
    return pattern.sub(r'', text)

def remove_emoticons(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    
    level_1 = regrex_pattern.sub(r'',text)
    xtr_symbols = ['❤','✌','🥰','♪', '♬', '♩','🤡', '🤣']
#     xtr_symbols_pattern = re.compile('❤✌🥰♪♬♩🤡🤣' , flags=re.UNICODE)
#     level_2 = xtr_symbols_pattern.sub(r' ', level_1)
    for xs in xtr_symbols:
        if xs in level_1:
            level_1 = level_1.replace(xs, "")


    return level_1

def remove_sw(text, input_file=None):
    if input_file is None:
        x1 = [i for i in  text.split() if i not in stop_words]
        return ' '.join([i for i in x1])
    else:
        with open("input_file",'r',encoding = 'utf-8') as f:
            stop_words_custom = f.read()
        x1 = [i for i in  text.split() if i not in stop_words_custom]
        return ' '.join([i for i in x1])

def numETB(text):
    return text.translate(str.maketrans("1234567890", "১২৩৪৫৬৭৮৯০")) 
def numBTE(text):
    return text.translate(str.maketrans("১২৩৪৫৬৭৮৯০", "1234567890")) 

def remove_noise(text):
    return remove_sw(remove_emoticons(remove_nonBangla(remove_digits(remove_punc(text)))))