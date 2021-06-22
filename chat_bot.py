import random
import re

tops=['top', 'jacket', 'shirt']
bottoms=['pants','bottom', 'skirt']
shoes=['shoes', 'boots', 'jorden']
category = [tops,bottoms,shoes]

not_found_ans = [
    'I can\'t understand what you are saying.',
    'Could you check your respones, please?',
    'Is there any typo in your respones?'
]

print('***USE SMALL LETTER ONLY***\nGood day! What are you looking for to day?\nTop? Bottom? Shoes?')
ans = input('>')

found_keys=[]
for keylist in category:
    for key in keylist:
        p = re.compile(key)
        detected_key = p.findall(ans)
        if detected_key:
            found_keys.append(detected_key[0])
        else:
            continue

if found_keys:
    if len(found_keys) == 1:
        print(found_keys)
    else:
        print('Choose one')
    
else:
    print(not_found_ans[random.randint(0,2)])