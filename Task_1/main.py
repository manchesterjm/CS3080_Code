import bs4, requests, openpyxl, os
from random import randint

''' CONSTANTS '''

FILE_NAME = '1000_words.xlsx'
SHEET_NAME = '1000_words'

# source URL for the 1000 words we will use
WEB_PAGE = requests.get('https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/')

''' PERFORM SOME CHECKS '''

# check that the person running this code has the correct version of openpyxl
if openpyxl.__version__ != '3.1.2' :
    print(f"*********** WARNING ***********")
    print(f"You are using openpyxl version {openpyxl.__version__}")
    print(f"This script was made using openpyxl 3.1.2")
    print(f"You may expirence unwanted behavior")

# test that the webpage is there.  If it is offline or has been deleted, we display an error and terminate program
try:
    WEB_PAGE.raise_for_status()
except Exception as e:
    print(f"\nSomething is wrong with the webpage : {e}\n")
    exit()

''' FUNCTIONS '''

'''takes in the word and the input letter
   returns a 0 for no match, and the indices for the letter if the letter is correct'''
def chk_word(letter, test_word) :
    # split the test_word into a list of chars
    word = list(test_word)
    # get the index the letters are in and return
    return [indx for indx, letters in enumerate(word) if letters == letter] if letter in word else 0

def rand_cell(lst) :
    return 'A' + str(randint(1, len(lst)))

'''read the data from the html file and then
   the <div, class=content> tag has the words in the second <p> tag under it so [1]
   there are 3 <p> tags under the <div> but we only want the the second
   get a cleaned up list by turning the data into a list and then removing the \n\t (new line and tab)
   along with only selecting data that is a string so the tag <br/> will not be included'''
def get_clean_list(webPage) :
    word_list_data = bs4.BeautifulSoup(webPage.text, 'html.parser').find('div', class_='content').find_all('p')[1]
    return [elem.replace('\n\t', '').replace('\'', '').lower() for elem in list(word_list_data) if isinstance(elem, str)]

def new_wb(lst) :
    # create a new workbook
    wb = openpyxl.Workbook()
    sheet = wb.active # go to active sheet, should only be one
    sheet.title = SHEET_NAME # name the sheet just because I can
    '''fill the XL sheet with the 1000 words from the webpage that we cleaned up and stored in the list
       and make the cell number so we can fill it '''
    for i in range(1, len(lst)) : sheet['A' + str(i)] = lst[i]
    wb.save(FILE_NAME) # save workbook
    return sheet

''' get a random word from the workbook sheet that is at least 6 letters long '''
def get_wrd(lst, sht) :
    guessWord = []
    while len(guessWord) < 6 : guessWord = sht[rand_cell(lst)].value
    return guessWord

def prnt_lst(lst) :
    print(f"{''.join(lst)}\n")

''' MAIN '''

# if an XL spreadsheet is already existing in the folder, delete to avoid problems
if os.path.exists(FILE_NAME) : os.remove(FILE_NAME)
cleaned_list = get_clean_list(WEB_PAGE)
sheet = new_wb(cleaned_list)
guess_word = get_wrd(cleaned_list, sheet)

print(f"\nLet the game begin\n")
print(f"Your word has {len(guess_word)} letters in it\n")

''' fill a temp list with underscores to denote the number and positions of the letters in the word '''
temp_list = ["_ " for _ in range(len(guess_word))]
prnt_lst(temp_list)

count = 5 # give the user 5 misses and then terminate
input_list = [] # save the users inputs so we do not penalize them for duplicates

'''use a while loop counting down to 0'''

while count > 0 :
    user_input = input(f"Please enter a letter : ") # get user input
    
    if user_input not in input_list : input_list.append(user_input)
        
    else : # no penalty for duplicate guesses
        print(f"\nyou have already tried \"{user_input}\", please try again\n")
        continue #skip the rest of the while loop
    
    check = chk_word(user_input, guess_word) # send off to be checked
    
    if check :
        print("you guessed a letter")
        
        '''if there were one or more of the same letter in the word
           add the letter in the correct index in the temp list for display'''
        for elem in check: temp_list[elem] = str(user_input) + " " # preserve the space
        
    else :
        count -= 1 # we didn't guess a correct letter
        
        # while we still have guesses left
        if count > 0 : print(f"Try again, you have {count} guesses left")
            
        else: # no more guesses left
            print(f"\nYou Lost!\n")
            break # terminate while loop
    
    '''print out the current list of unkown and known letters'''        
    prnt_lst(temp_list)
    
    '''check if the list has any underscores left.  If none, then we guessed all the letters and we win'''
    if '_ ' not in temp_list :
        print(f"\nYou won!\n")
        break # terminate while loop
    
print(f"The word was \"{guess_word}\"\n\n") # display word if we win or lose
exit()