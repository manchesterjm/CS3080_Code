''' HEADER INFO

    Josh Manchester
    CS3080
    Task 2

    Write a python program that gets the top three authors from the input URLs
    and then gathers the author names and the amount of publications they had during each
    respective year, and then sums the publications for each author for all years.  This
    information is then stored in an Excel workbook in a format specified by the asignment
'''

import bs4, requests, openpyxl, os

''' CONSTANTS '''

FILE_NAME = 'authors.xlsx'
SHEET_NAME = 'authors'

# source URLs, can add more or remove urls to this list and the program should work just fine as long as the urls are from this website

webpage_urls = ['https://openaccess.thecvf.com/CVPR2021?day=all', 
                'https://openaccess.thecvf.com/CVPR2022?day=all', 
                'https://openaccess.thecvf.com/CVPR2023?day=all']

''' PERFORM SOME CHECKS '''

# check that the person running this code has the correct version of openpyxl
if openpyxl.__version__ != '3.1.2' :
    print(f"*********** WARNING ***********")
    print(f"You are using openpyxl version {openpyxl.__version__}")
    print(f"This script was made using openpyxl 3.1.2")
    print(f"You may expirence unwanted behavior")

''' FUNCTIONS '''

''' Test that the webpage is there.  If it is offline or has been deleted or just has a problem
    we display an error and terminate program '''
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

''' Returns the number of publications for the given year list for the list of supplied authors '''
def get_auth_pubs(auths, lst) :
    dict = {}
    for auth in auths : # get author name from list
        counter = 0
        for name in lst : # iterate through the list of names in the current year list
            if name == auth : # tally the amount of times the name appears in the list
                counter += 1
        dict[auth] = counter # saves the author name and the number of times the anme appears in the list to a dictionary
    return(dict) # returns the dictionary
        
''' Returns a cleaned list of names from the website data provided '''
def get_clean_list(webPage) :
    text_data = bs4.BeautifulSoup(webPage.text, 'html.parser') # get the text of the webpage
    tags_lst = text_data.select('input', name_='query_author') # get tags labeled as imput with name queary_author
    return [tag.get('value') for tag in tags_lst] # grabs the value from the input tag where the value = the author name

''' Grabs the top three authors in all years, returns the top three authors '''
def get_top_auths(lst) :
    dict = {}
    for auth in lst :
        if auth in dict :
            dict[auth] += 1
        else :
            dict[auth] = 1
    ''' Used a lambda function here because we went over it in class and I thought it would knock down on typing
        out some code.  Used reverse sort and then grabed the last three entries in the dictionary since those would have
        the highest total publication count. NOTE that sorted() turns the dictionary into a list automatically '''
    top_auths = sorted(dict.items(), key=lambda item: item[1], reverse=True)[:3]
    return [name for name, _ in top_auths]

''' Creates a new workbook and fills it with the data required '''
def new_wb(dict) :
    wb = openpyxl.Workbook() # create new workbook
    sheet = wb.active # go to active sheet, should only be one
    sheet.title = SHEET_NAME # name the sheet just because I can
    years = list(dict.keys()) # get list of years from the supplied dictionary
    authors = list(set(auth for year in dict for auth in dict[year])) # get a list of the authors from the dictionary
    ''' NOTE I used set() to get a unique list of authors so the above line of code can be generic '''

    sheet.append([''] + authors) # create the top row in the spreadsheet
    
    ''' this makes three rows, one for each year, and in each row it gets the number of papers per
        author for each year .get(author, 0) using list comprehension, then we append that to the sheet '''
    for year in years :
        sheet.append([year] + [dict[year].get(author, 0) for author in authors])

    ''' this makes the last row for the totals.  for each author, we find the amount of publications per year
        and then add them up all sum().  We then append it to the totals row and then append the totals row to the worksheet '''
    totals_row = ['Totals'] # start the totals row
    for author in authors :
        totals_row.append(sum(dict[year].get(author, 0) for year in years))
    sheet.append(totals_row)
    
    wb.save(FILE_NAME) # save workbook
    return 0

''' MAIN '''

# if an XL spreadsheet is already existing in the folder, delete to avoid problems
if os.path.exists(FILE_NAME) : os.remove(FILE_NAME)

# query webpages and get cleaned up lists of authors
clean_lists = [get_clean_list(check_webpage(url)) for url in webpage_urls]

# make a combined list of all cleaned up lists
cleaned_all = sum(clean_lists, [])

top_auths = get_top_auths(cleaned_all) # get a list of top authors for all years

# get the top authers number of publications for each year
dict_all = {}
years = [url.split('CVPR')[1].split('?')[0] for url in webpage_urls] # get a list of years from the URLs
''' this splits the url at CVPR, creating a list with two elements with the Year in the second element
    then we split again at the ? which leaves the Year in the first element.  That's how we grab the Year '''


for lst, year in zip(clean_lists, years) :
    dict_all[year] = get_auth_pubs(top_auths, lst)
'''NOTE this makes a nested dictionary'''

# make a workbook with the top authors and the number of publications per year
new_wb(dict_all)