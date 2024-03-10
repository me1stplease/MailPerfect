# import spacy
import en_core_web_sm
import re

def getPii(text):
    english_nlp = en_core_web_sm.load()

    # english_nlp= spacy.load('en_core_web_sm')

    # text = '''
    # This is a sample text that contains the name Alex Smith who is one of the developers of this project.
    # You can also find the surname Jones here. My name is Mahtab alam and i work in google. you can contact me at 1982346528 and i email is abc1@gmail.com.
    # '''

    spacy_parser = english_nlp(text)

    pii = []
    for entity in spacy_parser.ents:
        print(f'Found: {entity.text} of type: {entity.label_}')
        if entity.label_=='PERSON' or entity.label_=='ORG':
            pii.append(entity.text)

    emails = re.findall(r"[A-Za-z0-9_%+-.]+"
                    r"@[A-Za-z0-9.-]+"
                    r"\.[A-Za-z]{2,5}",text)

    pii.extend(emails)

    digitReg = '[0-9]{7,}'             
        
    numbers = re.findall(digitReg, text)

    pii.extend(numbers)

    print(pii)
    return pii