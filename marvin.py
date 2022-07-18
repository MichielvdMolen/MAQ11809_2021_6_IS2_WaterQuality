from IPython.display import Image

import os
teacher_dir  = os.getenv('TEACHER_DIR')
imgpath = teacher_dir + '/JHL_data/pictures/'

def check_my_answer_IS2_1a(x,y):
    dy = 50e6
    if     x == 'increase' and 130e6 - dy <= y <= 130e6 + dy:
        print('Hoera! Your answer is correct! ')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'You see that the initial concentration is a sensitive parameter. It has a large impact on the model concentrations. However, if the water balance and the N inputs are not subject to sudden large changes, you know that the N concentration should be relatively constant. Therefore, this method of tuning is acceptable. It would be good to verify if the model concentrations correspond more or less to observed concentrations though! You can collect these observations in the PBL phase.')
        print('\nAs a game, this time, you are going to get letters of 6 words. At the end, construct the words and put them in the right order to answer the last question.')
        display(Image(filename= imgpath + "IS2_img01.jpg", width=400, height=400))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'increase'                :  print('x  is incorrect')
        if y < 130e6-dy or y>130e6 + dy    :  print('y  is incorrect')
        return False


def check_my_answer_IS2_2a(x1, x2, y1, y2, y3):
    if x1 == 'has' and x2 == 'maximum' and y1 == 'does' and y2 == 'drier' and y3 == 'both':
        print('Hoera! Your answer is correct! Are you ready to go fishing with me? We need to find Nemo!')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'The N concentration in the pond is variable on seasonal and interannual timescales. On seasonal timescales, the concentration is higher in summer, when the input of NH3 is large and the input of water is small. On interannual timescales, the drier years have larger N concentratoins.')
        display(Image(filename= imgpath + "IS2_img02.jpg", width=400, height=400))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x1 != 'has'               : print('x1 is incorrect')
        if x2 != 'maximum'           : print('x2 is incorrect')
        if y1 != 'does'              : print('y1 is incorrect')  
        if y2 != 'drier'             : print('y2 is incorrect')  
        if y3 != 'both'              : print('y3 is incorrect')  
        return False

def check_my_answer_IS2_3a(x1, x2, y1, y2, z):
    if len(x1) > 0 and len(x2) > 0 and len(y1) > 0 and len(y2) > 0 and len(z) > 0:
        print('OK, thanks for the effort.')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'Looking at the simplistic and realistic runs we can conclude the following: The realistic run shows much more pronounced seasonal cycle compared to the simplistic run. This happens because we do not only look at the precipitation as a changing parameter but also at changes in evaporation, air temperature and global radiation, all of which have strong seasonal cycles. It is not always straightforward to define ''sensitive'', because it may depend on what you find important, e.g. absolute value, variability, relative change, etc. This is food for discussion in your report. Nevertheless, the sensitivity of the model gives important information for future use of the model.')
        display(Image(filename= imgpath + "IS2_img03.jpg", width=400, height=400))
        return True
    else:
        print('Your answer is not complete. Please, try again!')
        if len(x1) == 0                : print('x1 is incomplete')
        if len(x2) == 0                : print('x2 is incomplete')
        if len(y1) == 0                : print('y1 is incomplete')
        if len(y2) == 0                : print('y2 is incomplete')
        if len(x1) == 0                : print('z  is incomplete')
        return False
    
def check_my_answer_IS2_4a(x, y, z, q):
    if x == 'inversely proportional' and (y == 'c' or y == 'd') and (z > 0.8) and q == 'pretty cold' :
        print('Hoera! Your answer is correct! Do you see how algae growth is the result of many interacting processes?')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'The chlorophyl is indeed inversely proportional to the visibility inside the pond.')
        display(Image(filename= imgpath + "IS2_img04.jpg", width=400, height=400))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x != 'inversely proportional'              : print('x is incorrect')
        if y != 'd'                                   : print('y is incorrect')
        if z != 1                                     : print('z is incorrect')
        if q != 'pretty cold'                         : print('q is incorrect')    
        return False

def check_my_answer_IS2_5a(quote):
    correctanswer = 'things grow stronger when you integrate'
    quote = quote.lower()
    quote = quote.strip(' ') # removing leading or trailing spaces
    quote = ' '.join(quote.split()) # replace double spaces by single ones.
    quote = quote.replace('.','')   # remove '.' if any.
    if quote == correctanswer:
        print('Hoera! Your answer is correct!\n')
        display(Image(filename= imgpath + "IS2_img05.jpg", width=400, height=400))
        print('\n\nAre you ready for the PBL phase of the course? \nWe hope you feel comfortable integrating with the tools you learned?\nFeel free to discuss with one of the teachers.')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        wordsgiven   = list(filter(None,quote.split(' ')))
        correctwords = correctanswer.split(' ')
        nwordsgiven = len(wordsgiven)
        ncorrectwords = 0
        for iw in range(nwordsgiven):
            if wordsgiven[iw] in correctwords:
                print('The word %-15s is in the solution.'%wordsgiven[iw])
                ncorrectwords = ncorrectwords+1
            else:
                print('The word %-15s is not correct.'%wordsgiven[iw])
        if ncorrectwords == 6:
            print('All words are correct, try a different order.')
        elif ncorrectwords < 6:
            print('You did not supply enough correct words.')
        elif ncorrectwords > 6:
            print('You supplied too many words.')
                
        return False    
    
   