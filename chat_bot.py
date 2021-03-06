import random
import re

brain = []

tops=['top', 'jacket', 'shirt']
bottoms=['pants','bottom', 'skirt']
shoes=['shoes', 'boots', 'jorden']
category = [tops,bottoms,shoes]

colors = ['red','blue','green']

not_found_ans = [
    'I can\'t understand what you are saying.',
    'Could you check your respones, please?',
    'Is there any typo in your respones?'
]

def cate_answer(answ):
    found_keys=[]
    for keylist in category:
        for key in keylist:
            p = re.compile(key)
            detected_key = p.findall(answ)
            if detected_key:
                found_keys.append(detected_key[0])
            else:
                continue

    if found_keys:
        if len(found_keys) == 1:
            brain.append(found_keys[0])
            print('Among the red, blue and green,\nWhat color of',found_keys[0],'are you looking for?')
            color_ans = input('>')
            if color_ans in colors:
                color_answer(color_ans)
            else:
                print('Sorry, there is no such product available.')
        
        else:
            print('Amog the top, bottom and shoes, choose one category.')
            repeated_ans = input('>')
            cate_answer(repeated_ans)
    
    else:
        print(not_found_ans[random.randint(0,2)])

def color_answer(answ):
    for coloer in colors:
        pp = re.compile(coloer)
        detected_color = pp.search(answ)
        
        try:
            cnt=0
            if detected_color.group() in colors:
                brain.append(detected_color.group())
                print('Do you want',detected_color.group(),brain[0],'?\nYes(1) or No(0)')
                yn_ans = int(input('>'))
                final_answer(yn_ans)            

        except AttributeError:
            continue

def final_answer(num):
    ref_address = 'https://search.musinsa.com/search/musinsa/integration?type=&q='#red+jorden'
    real_address = ref_address+brain[1]+'+'+brain[0]
    if num ==1:
        print('Here is the search result of',brain[1],brain[0],'.\n>',real_address)
        
    elif num == 0:
        while brain:
            del brain[0]            

        print('Let\'s try again.\nTop? Bottom? Shoes?')
        again_ans = input('>')
        cate_answer(again_ans)

print('***Except word "I" please us SMALL LETTER***\nGood day! What are you looking for to day?\nTop? Bottom? Shoes?')
ans = input('>')

cate_answer(ans)