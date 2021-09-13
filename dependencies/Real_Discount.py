from bs4 import BeautifulSoup
import requests
from urllib.parse import *
from concurrent.futures import ThreadPoolExecutor

class real_disc():

    def get_free_courses_from_page (self , url , headers):
        courses = []
        links = []
        coupon_link = []
        request  = requests.get(url , allow_redirects=True , headers=headers)
        soup = BeautifulSoup(request.text , "html.parser")
        h3_tags = soup.find_all("h3" ,{"style" :"font-size: 18px;" , "class" :"card-title font-weight-bold mb-0"})
        for h3 in h3_tags:
            courses.append(h3.text)
        divs = soup.find_all("div" , class_="col-sm-12 col-md-6 col-lg-4 col-xl-4")
        for div in divs:
            try:
                links.append("https://app.real.discount"+ div.find("a")["href"])
            except :
                pass

        for i in range(0, len(links)-1):

            if links[i] == "https://app.real.discount/out-ad/77" :
                del links[i]
                del courses[i]
            
        
        for link in links:
            r  = requests.get(link , allow_redirects=True , headers=headers)
            soup = BeautifulSoup(r.text , "html.parser")
            div = soup.find("div" ,{"class" :"col-xs-12 col-md-12 col-sm-12 text-center" , "style":"margin-top: 20px; "})
            a = div.find("a" , {"target":"_blank"})
            url_list = a["href"].split("https://")
            for url in list(url_list):
                url =  "https://" + url
                if "www.udemy.com/course/" in url:
                    coupon_link.append(url)


        return (courses , coupon_link)

    def get_category_url (self , category=None , value_13=None):
        url = ""
        categories = {1 : "Development", 2 : "IT & Software" , 3 : "Business", 4 : "Design" , 5 : "Lifestyle" , 6 : "Marketing", 7 : "Finance & Accounting", 8 : "Health & Fitness" , 9 : "Office Productivity" , 10 : "Personal Development" , 11 : "Photography & Video" , 12 : "Teaching & Academics"}
        if category in [x for x in range(1, 13)]:
            word = quote_plus(categories[category])
            url = f"https://app.real.discount/filter/?category={word}&store=All&duration=All&price=0&rating=All&language=All&search=&submit=Filter&page="
        elif category == 13:
            url  = f"https://app.real.discount/filter/?category=All&store=Udemy&duration=All&price=0&rating=All&language=All&search={value_13}&submit=Filter&page="
            return url
        elif category == 14:
            url = f"https://app.real.discount/filter/?category=All&store=udemy&duration=All&price=0&rating=All&language=All&search=&submit=Filter&page="
        else:
            print("Please enter between 1 and 14.")


        return url



    def get_multiple_pages(self ,url , headers , pages=None):
        total_courses = []
        total_coupons = []
        if pages == None:
            pages=self.get_pages()
        else:
            with ThreadPoolExecutor(max_workers=100) as executor:
                futures = []
                for i in range (1, pages+1):
                    if "https://udemycoupons.me/page/REPLACEME/"in url:
                        new_url = url.replace("REPLACEME" , str(i))
                    elif "https://www.onlinecourses.ooo/page/REPLACEME/"in url:
                        new_url = url.replace("REPLACEME" , str(i))
                    elif "https://100offdeal.online/page/REPLACEME" in url:
                        new_url = url.replace("REPLACEME" , str(i))
                    else:    
                        new_url = url+str(i)
                    futures.append((executor.submit(self.get_free_courses_from_page, new_url , headers)))
            for future in futures:
                data  = future.result()
                total_courses = total_courses+data[0]
                total_coupons = total_coupons+data[1]

        return total_courses , total_coupons       



        
