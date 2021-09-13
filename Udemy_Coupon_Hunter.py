#!/usr/bin/env python3
import os
import threading
from dependencies import *
from dependencies.funcs import *
complete = False
def loading_animation(text):
    bar = [
        f"{YELLOW}[=     ]   {RED + text}.",
        f"{YELLOW}[ =    ]   {RED + text}.",
        f"{YELLOW}[  =   ]   {RED + text}.",
        f"{YELLOW}[   =  ]   {RED + text}.",
        f"{YELLOW}[    = ]   {RED + text}.",
        f"{YELLOW}[     =]   {RED + text}.",
        f"{YELLOW}[    = ]   {RED + text}.",
        f"{YELLOW}[   =  ]   {RED + text}.",
        f"{YELLOW}[  =   ]   {RED + text}.",
        f"{YELLOW}[ =    ]   {RED + text}.",
    ]
    i = 0
    while complete == False:
        if complete == True:
            print(GREEN+" [DONE]\n")
            break
        print(YELLOW +bar[i % len(bar)], end="\r")
        sleep(.2)
        i += 1   

def scrape_sites(website , headers , pages , category , value_13):
    url = website.get_category_url(value_13=value_13, category=category)
    courses , coupons = website.get_multiple_pages(url , headers , pages)
    for course , coupon in zip(courses , coupons):
        if coupon not in total_coupons:
            if "udemy" in coupon or "youtube" in coupon:
                validation , price = Validate_link_and_get_price(coupon)
                if validation == True:
                    total_saved.append(price)
                    total_courses.append(course) 
                    total_coupons.append(coupon)

def animate(text):
    load_thread = threading.Thread(target=loading_animation, args=(text,))
    load_thread.start()

rd = real_disc()
ud = udemyme()
fd = freedeal()
oc = onlinecourses()
websites = [rd , ud ,oc , fd]
total_courses = []
total_coupons = []
total_saved = []
category = 0
value_13 = None
clear()
category , value_13 = get_categ()
pages = get_pages()
clear()
animate("Looking for courses, Please be patient.")
threads = []
headers = {"User-Agent" : "Mozilla/5.0 (X11; CrOS x86_64 13597.94.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.186 Safari/537.36",
"Accept-Language":"en-US,en;q=0.5"}

for website in websites:    
    threads.append(threading.Thread(target=scrape_sites , args=(website , headers , pages , category , value_13)))
    
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


complete = True
sleep(6)
complete = False
clear()
animate("Searching for courses in youtube. Please be patient.")

youtube_courses  , youtube_links = Feed_queries(category,value_13, pages*10)
complete = True
for c , l in zip(youtube_courses , youtube_links):
    if l not in total_coupons:
        total_coupons.append(l)
        total_courses.append(c)
clear()
choice = "Z"
while choice.lower() not in ["y","n"]:
    choice = input(GREEN +"Write data to a file ? [y/n] ")
    if choice.lower() not in ["y","n"]:
        print(RED +"Invalid choice")
    elif choice.lower() == "y":
        export_data(total_courses , total_coupons ,sum(total_saved) , len(total_coupons) ,  write_data=True)
    elif choice.lower() == "n":
        export_data(total_courses , total_coupons ,sum(total_saved),len(total_coupons) , write_data=False)

choice = "Z"
while choice.lower() not in ["y","n"]:
    choice = input(GREEN +"Enroll in all the courses? [y/n] ")
    if choice.lower() not in ["y","n"]:
        print(RED +"Invalid choice")
    elif choice.lower() == "y":
        choice = "Z"
        while choice.lower() not in ["y","n"]:
            choice = input(GREEN +"Enroll by entering (Email/password) or (client_id , access_token , csrf_token) cookies ? \n\n[y for (Email/password) / n for second option] ")
            if choice.lower() not in ["y","n"]:
                print(RED +"Invalid choice")
            elif choice.lower() == "y":
                again = "y"
                while again.lower() == "y":
                    t = []
                    email , password  = get_email_password()
                    currency, s = try_login(email, password)
                    for coupon in total_coupons:
                        if "udemy" in coupon:
                            thread = threading.Thread(target=enroll_with_email_pass , args=(coupon ,currency ,s))
                            thread.start()
                            t.append(thread)
                            
                            for thread in t:
                                thread.join()
                    again = input(BLUE +"Want to enroll for other account? (y/n)")


            elif choice.lower() == "n":
                again = "y"
                while again.lower() == "y":
                    t = []
                    client_id , access_token , csrf_token = get_cookies()
                    cookie = make_cookie(client_id , access_token , csrf_token)
                    for coupon in total_coupons:
                        if "udemy" in coupon:
                            thread = threading.Thread(target=enroll_with_cookie , args=(coupon,cookie))
                            thread.start()
                            t.append(thread)
                            
                            for thread in t:
                                thread.join()

                    again = input(BLUE +"Want to enroll for other account? (y/n)")

            print(GREEN + "Thanks for using.")
            a = input("")










