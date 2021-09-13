from urllib.parse import urlparse , parse_qs , unquote
from bs4 import BeautifulSoup
import requests ,json
from os import system, name 
from time import sleep
RED  = "\u001b[31m"
CYAN = "\u001b[36m"
GREEN = "\u001b[32m"
BLUE = "\u001b[34;1m"
WHITE = "\u001b[37;1m"
YELLOW = "\u001b[33m"
GREY ="\u001b[30;1m"
GREEN2 = "\u001b[32;1m"
def clear(): 

    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
    
def Validate_link_and_get_price(url):
    def make_url(url , id):
        small_parsed = urlparse(url)
        small_parsed_query = parse_qs(small_parsed.query)
        try:
            cp = small_parsed_query["couponCode"][0]
        except:
            cp = "FREE"
        url_big = "https://www.udemy.com/api-2.0/course-landing-components/"+str(id)+"/me/?couponCode="+str(cp)+"&utm_source=aff-campaign&utm_medium=udemyads&components=redeem_coupon,price_text"
        return unquote(url_big)

    headers = {"User-Agent" : "Mozilla/5.0 (X11; CrOS x86_64 13597.94.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.186 Safari/537.36" , "Accept-Language":"en-US,en;q=0.5"}    
    try :
        try :
            r = requests.get(url , headers=headers , allow_redirects=True)
            if r.status_code == 302 or r.status_code == 301 or "is no longer available" in r.text or "no longer" in r.text:
                return False , 0
            soup = BeautifulSoup(r.text , "html.parser")
        except:
            return False ,0
        try:
            id  = soup.find("body")["data-clp-course-id"]
        except:
            id = 123
        r = requests.get(make_url(url, id) , headers=headers)
        if "The coupon code entered" in r.text:
            return False , 0
        else:
            try:
                json_d = json.loads(r.text)
                price = int(json_d["price_text"]["data"]["list_price"]["amount"])
            except:
                price = 0
            return True , price 
    except:
        return False  , 0

def get_categ():
    category = None
    value_13 = None
    if category == None:    
        while category not in [x for x in range(1, 15)]:
            category = int(input(f"""{YELLOW} 
 |  ____|                                            
 | |__ _ __ ___  ___    ___ ___  _   _ _ __ ___  ___ 
 |  __| '__/ _ \/ _ \  / __/ _ \| | | | '__/ __|/ _ \\
 | |  | | |  __/  __/ | (_| (_) | |_| | |  \__ \  __/
 |_|  |_|  \___|\___|_ \___\___/ \__,_|_|  |___/\___|

 | |  | |           | |                              
 | |__| |_   _ _ __ | |_ ___ _ __                    
 |  __  | | | | '_ \| __/ _ \ '__|                   
 | |  | | |_| | | | | ||  __/ |                      
 |_|  |_|\__,_|_| |_|\__\___|_|                      
                                    Made by Zain.            
                                                                
Categories :

{BLUE}[1] {YELLOW}Development
{BLUE}[2] {YELLOW}IT & Software
{BLUE}[3] {YELLOW}Business
{BLUE}[4] {YELLOW}Design
{BLUE}[5] {YELLOW}Lifestyle
{BLUE}[6] {YELLOW}Marketing
{BLUE}[7] {YELLOW}Finance & Accounting
{BLUE}[8] {YELLOW}Health & Fitness
{BLUE}[9] {YELLOW}Office Productivity
{BLUE}[10] {YELLOW} Personal Development
{BLUE}[11] {YELLOW} Photography & Video
{BLUE}[12] {YELLOW} Teaching & Academics
{BLUE}[13] {YELLOW} Look for what you want
{BLUE}[14] {YELLOW} All Categories Latest.

{BLUE}Enter the category to look coupons for:  """))
    if category == 13:
        value_13 = input(F"{BLUE}What do you want to look for ? ")
    else:
        value_13 = None
    return category , value_13



def get_pages (pages=None):
    while isinstance(pages , int) == False or  pages == 0:
        try:
            pages = int(input(f"{BLUE}Enter the number of pages to scrape: "))
        except:
            print(RED + "Invalid number of pages.")

    return pages    

def export_data(total_courses , total_coupons , total_saved, number_courses, write_data = True ):
    yt_course = []
    yt_coupon = []
    udemy_course = []
    udemy_coupon = []
    for course  , coupon in zip(total_courses , total_coupons):
        if "udemy" in coupon:
            udemy_course.append(course)
            udemy_coupon.append(coupon)
        else:
            yt_course.append(course)
            yt_coupon.append(coupon)

    yt_formatted = "\n".join("[+]  [{}]\n\n{}\n\n".format(x, y) for x, y in zip(yt_course, yt_coupon))
    udemy_formatted = "\n".join("[+]  [{}]\n\n{}\n\n".format(x, y) for x, y in zip(udemy_course, udemy_coupon))
    string_start = f"""{GREEN}Here are the courses which we could find (100% Working):
Total worth of Courses: {str(total_saved)} USD
Number of courses : {str(number_courses)}
    

"""
    if write_data == True:
        f = open("Data.txt" , "w")
        f.write(string_start)
        f.write(udemy_formatted)
        f.write("\n\n\n\nYoutube Courses These are often better than the udemy ones.\n\n\n\n")
        f.write(yt_formatted)
        f.close()
    clear()
    print(WHITE + string_start)
    print(WHITE + udemy_formatted)
    print(WHITE + "\n\n\n\nYoutube Courses These are often better than the udemy ones.\n\n\n\n")
    print(WHITE + yt_formatted)
    print(WHITE + yt_formatted)
    print(WHITE + "Data saved to Data.txt")