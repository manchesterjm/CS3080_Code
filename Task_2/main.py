import bs4, requests, openpyxl, os

''' CONSTANTS '''

FILE_NAME = 'authors.xlsx'
SHEET_NAME = 'authors'

# source URL for the 1000 words we will use

WEB_PAGE_1 = requests.get('https://openaccess.thecvf.com/CVPR2021?day=all')
WEB_PAGE_2 = requests.get('https://openaccess.thecvf.com/CVPR2022?day=all')
WEB_PAGE_3 = requests.get('https://openaccess.thecvf.com/CVPR2023?day=all')

web_list = [WEB_PAGE_1, WEB_PAGE_2, WEB_PAGE_3]

''' PERFORM SOME CHECKS '''

# check that the person running this code has the correct version of openpyxl
if openpyxl.__version__ != '3.1.2' :
    print(f"*********** WARNING ***********")
    print(f"You are using openpyxl version {openpyxl.__version__}")
    print(f"This script was made using openpyxl 3.1.2")
    print(f"You may expirence unwanted behavior")

# test that the webpage is there.  If it is offline or has been deleted, we display an error and terminate program
for page in web_list :
    try:
        page.raise_for_status()
    except Exception as e:
        print(f"\nSomething is wrong with the webpage : {e}\n")
        exit()

''' FUNCTIONS '''

# returns the number of publications for the given year list for the list of supplied authors
def get_auth_pubs(auths, lst) :
    dict = {}
    for auth in auths : # get author name from list
        counter = 0
        for name in lst : # iterate through the list of names in the current year list
            if name == auth : # tally the amount of times the name appears in the list
                counter += 1
        dict[auth] = counter # saves the author name and the number of times the anme appears in the list to a dictionary
    return(dict) # returns the dictionary
        
# returns a cleamup list of names from the website data provided
def get_clean_list(webPage) :
    text_data = bs4.BeautifulSoup(webPage.text, 'html.parser') # get the text of the webpage
    tags_lst = text_data.select('input', name_='query_author') # get tags labeled as imput with name queary_author
    lst = [tag.get('value') for tag in tags_lst] # grabs the value from the input tag where the value = the author name
    return lst

# grabs the top three authors in all years, returns the top three authors
def get_top_auths(lst) :
    dict = {}
    for auth in lst :
        if auth in dict :
            dict[auth] += 1
        else :
            dict[auth] = 1
    ''' used a lambda function here because we went over it in class and I thought it would knock down on typing
        out some code.  Used reverse sort and then grabed the last three entries in the dictionary since those would have
        the highest total publication count'''
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)[:3]

def new_wb(dict) :
    # create a new workbook
    wb = openpyxl.Workbook()
    sheet = wb.active # go to active sheet, should only be one
    sheet.title = SHEET_NAME # name the sheet just because I can
    years = list(dict.keys()) # get list of years from the supplied dictionary
    authors = list(set(auth for year in dict for auth in dict[year])) # get a list of the authors from the dict
    ''' note, I used set() to get a unique list of authors so the above line of code can be generic'''

    sheet.append([''] + authors) # create the top row in the spreadsheet
    
    ''' this makes three rows, one for each year, and in each row it gets the number of papers per
        author for each year .get(author, 0) using list comprehension, then we append that to the sheet'''
    for year in years :
        sheet.append([year] + [dict[year].get(author, 0) for author in authors])

    ''' this makes the last row for the totals.  for each author, we find the amount of publications per year
        and then add them up all sum().  We then append it to the totals row and then append the totals row to the worksheet'''
    totals_row = ['Totals'] # start the totals row
    for author in authors :
        totals_row.append(sum(dict[year].get(author, 0) for year in years))
    sheet.append(totals_row)
    
    wb.save(FILE_NAME) # save workbook
    return 0

''' MAIN '''

# if an XL spreadsheet is already existing in the folder, delete to avoid problems
if os.path.exists(FILE_NAME) : os.remove(FILE_NAME)

yr_2021 = get_clean_list(WEB_PAGE_1)
yr_2022 = get_clean_list(WEB_PAGE_2)
yr_2023 = get_clean_list(WEB_PAGE_3)

clean_lists = [yr_2021, yr_2022, yr_2023]
cleaned_all = yr_2021 + yr_2022 + yr_2023

top_auths = get_top_auths(cleaned_all)

auth_names = [key for key, _ in top_auths]

dict_all = {}
years = ['2021', '2022', '2023']
for lst, year in zip(clean_lists, years) :
    dict_all[year] = get_auth_pubs(auth_names, lst)

new_wb(dict_all)