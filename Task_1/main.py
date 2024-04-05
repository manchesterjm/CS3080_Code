import bs4, requests, openpyxl, os
from random import randint

''' CONSTANTS '''

FILE_NAME = '1000_words.xlsx'
SHEET_NAME = '1000_words'

# source URL for the 1000 words we will use
url = 'https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/'

''' PERFORM SOME CHECKS '''

# check that the person running this code has the correct version of openpyxl
if openpyxl.__version__ != '3.1.2' :
    print(f"*********** WARNING ***********")
    print(f"You are using openpyxl version {openpyxl.__version__}")
    print(f"This script was made using openpyxl 3.1.2")
    print(f"You may expirence unwanted behavior")

''' FUNCTIONS '''

''' takes the webpage URL and gets the text of the webpage, terminates programs and displays an 
    error if the page does not exist or there was a problem loading the page '''
def check_webpage(page) :
    try:
        check = requests.get(page)
        check.raise_for_status()
        return check
    except requests.exceptions.HTTPError as http_err:
        print(f"There was an HTTP error for {page}: {http_err}")
        exit(1)  # terminate because HTTP error
    except Exception as err:
        print(f"There was an error accessing {page}: {err}")
        exit(1)  # terminate becuase general error

''' takes in the word and the input letter
    returns a 0 for no match, and the indices for the letter if the letter is correct'''
def chk_word(letter, test_word) :
    # split the test_word into a list of chars
    word = list(test_word)
    # get the index the letters are in and return
    return [indx for indx, letters in enumerate(word) if letters == letter] if letter in word else 0

''' gets a random cell from the workbook active sheet '''
def rand_cell(rows) :
    return 'A' + str(randint(1, rows))

''' Read the data from the html file '''
def get_clean_list(webPage) :
    text_data = bs4.BeautifulSoup(webPage.text, 'html.parser')
    p_tags = text_data.select('div.field-item.even > p') # gets the 3 p tags from inside this specific div tag
    word_list = p_tags[1] # we only want the second p tag as it contains the words
    ''' NOTE The word list has a bunch of extra crap in it that needs to be removed or not read at all
        like "<br>" break tags and "\n" new lines and "\t" tabs and "\'" single quotes
        also if something in this p tag is not a string we don't want to include it '''
    return [elem.replace('\n\t', '').replace('\'', '').lower() for elem in list(word_list) if isinstance(elem, str)]

''' creates a new Excell workbook and saves the list of 1000 words to the active sheet '''
def new_wb(lst) :
    # create a new workbook
    wb = openpyxl.Workbook()
    sheet = wb.active # go to active sheet, should only be one
    sheet.title = SHEET_NAME # name the sheet just because I can
    ''' fill the XL sheet with the 1000 words from the webpage that we cleaned up and stored in the list
       and make the cell number so we can fill it '''
    for i in range(1, len(lst)) : sheet['A' + str(i)] = lst[i]
    wb.save(FILE_NAME) # save workbook
    return sheet

''' get a random word from the workbook sheet that is at least 6 letters long '''
def get_wrd(sht) :
    guessWord = []
    while len(guessWord) < 6 : guessWord = sht[rand_cell(sht.max_row)].value
    return guessWord

''' prints the list that is sent to it '''
def prnt_lst(lst) :
    print(f"{''.join(lst)}\n")

''' MAIN '''

# if an XL spreadsheet is already existing in the folder, delete to avoid problems
if os.path.exists(FILE_NAME) : os.remove(FILE_NAME)

# query webpages and get cleanup up lists of words
cleaned_list = get_clean_list(check_webpage(url))

# write list to workbook
sheet = new_wb(cleaned_list)

# get a randome word to guess
guess_word = get_wrd(sheet)

print(f"\nLet the game begin\n")
print(f"Your word has {len(guess_word)} letters in it\n")

''' fill a temp list with underscores to denote the number and positions of the letters in the word '''
temp_list = ["_ " for _ in range(len(guess_word))]
prnt_lst(temp_list)

count = 5 # give the user 5 misses and then terminate
input_list = [] # save the users inputs so we do not penalize them for duplicates

''' use a while loop counting down to 0 '''

while count > 0 :
    user_input = input(f"Please enter a letter : ") # get user input
    
    if user_input not in input_list : input_list.append(user_input)
        
    else : # no penalty for duplicate guesses
        print(f"\nyou have already tried \"{user_input}\", please try again\n")
        continue #skip the rest of the while loop
    
    check = chk_word(user_input, guess_word) # send off to be checked
    
    if check :
        print("you guessed a letter")
        
        ''' if there were one or more of the same letter in the word
            add the letter in the correct index in the temp list for display '''
        for elem in check: temp_list[elem] = str(user_input) + " " # preserve the space
        
    else :
        count -= 1 # we didn't guess a correct letter
        
        # while we still have guesses left
        if count > 0 : print(f"Try again, you have {count} guesses left")
            
        else: # no more guesses left
            print(f"\nYou Lost!\n")
            break # terminate while loop
    
    ''' print out the current list of unkown and known letters '''        
    prnt_lst(temp_list)
    
    ''' check if the list has any underscores left.  If none, then we guessed all the letters and we win '''
    if '_ ' not in temp_list :
        print(f"\nYou won!\n")
        break # terminate while loop
    
print(f"The word was \"{guess_word}\"\n\n") # display word if we win or lose
exit()