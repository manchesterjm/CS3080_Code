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

def get_clean_list(webPage) :
    word_list_data = bs4.BeautifulSoup(webPage.text, 'html.parser')
    elems = word_list_data.select('input', name_='query_author')
    lst = [elem.get('value') for elem in elems]
    return lst

def new_wb(lst) :
    # create a new workbook
    wb = openpyxl.Workbook()
    sheet = wb.active # go to active sheet, should only be one
    sheet.title = SHEET_NAME # name the sheet just because I can
    '''fill the XL sheet with the 1000 words from the webpage that we cleaned up and stored in the list
       and make the cell number so we can fill it '''
    for i in range(1, len(str(lst))) :
        print(str(lst))
        sheet['A' + str(i)] = str(lst)
    wb.save(FILE_NAME) # save workbook
    return sheet

''' MAIN '''

# if an XL spreadsheet is already existing in the folder, delete to avoid problems
if os.path.exists(FILE_NAME) : os.remove(FILE_NAME)

cleaned_list_1 = get_clean_list(WEB_PAGE_1)
cleaned_list_2 = get_clean_list(WEB_PAGE_2)
cleaned_list_3 = get_clean_list(WEB_PAGE_3)

clean_lists = [cleaned_list_1, cleaned_list_2, cleaned_list_3]
cleaned_all = cleaned_list_1 + cleaned_list_2 + cleaned_list_3

dict_2021 = {}
dict_2022 = {}
dict_2023 = {}
dict_lst = [dict_2021, dict_2022, dict_2023]

for lst in range(0, len(clean_lists)) :
    for auth in clean_lists[lst] :
        if auth in dict_lst[lst] :
            dict_lst[lst][auth] += 1
        else :
            dict_lst[lst][auth] = 1
    top_three_auths = sorted(dict_lst[lst].items(), key=lambda item: item[1], reverse=True)[:3]
    for key, value in top_three_auths :
        print(f'{key}: {value}')
    print(f'\n')
#sheet = new_wb(cleaned_list)

dict = {}
for auth in cleaned_all :
    if auth in dict :
        dict[auth] += 1
    else :
        dict[auth] = 1
top_auths = sorted(dict.items(), key=lambda item: item[1], reverse=True)[:3]
for key, value in top_auths :
    print(f'{key}: {value}')
    
new_wb(top_auths)