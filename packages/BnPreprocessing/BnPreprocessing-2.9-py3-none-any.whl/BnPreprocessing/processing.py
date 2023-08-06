"""
Author = Kowsher Ahmed, Avishek Das,
Email = ahmedshuvo969@gmail.com, avishek.das.ayan@gmail.com
"""




def remove_punc(text):
    pattern = re.compile('[1234567890১২৩৪৫৬৭৮৯০!@#$%‘’^“”&√*()_+-={}\[\];:\'\"\|<>,.///?`~।]', flags=re.I)
    return pattern.sub(r' ', text).replace("\\", "") 

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
    # xtr_symbols = ['❤','✌','🥰','♪', '♬', '♩','🤡', '🤣']
    xtr_symbols_pattern = re.compile('❤✌🥰♪♬♩🤡🤣' , flags=re.I)
    level_2 = xtr_symbols_pattern.sub(r' ', text)

    return level_2

def remove_sw(text):
    x1 = [i for i in  text.split() if i not in stop_words]
    return ' '.join([i for i in x1])

def remove_noise(text):
    return remove_sw(remove_emoticons(remove_nonBangla(remove_punc(text))))