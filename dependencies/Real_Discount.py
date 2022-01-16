from bs4 import BeautifulSoup
import requests
from urllib.parse import *
from concurrent.futures import ThreadPoolExecutor
from .models import *


class real_disc():

    def get_free_courses_from_page(self , url , headers):

        request  = requests.get(url , allow_redirects=True , headers=headers)
        soup = BeautifulSoup(request.text , "html.parser")
        courses = []
        divs = soup.find_all("div" , class_="col-sm-12 col-md-6 col-lg-4 col-xl-4")


        for div in divs:
            try:
                link = "https://www.real.discount"+ div.find("a")["href"]

                r  = requests.get(link , allow_redirects=True , headers=headers)

                soup = BeautifulSoup(r.text , "html.parser")
               
                div = soup.find("div" ,{"class" :"col-xs-12 col-md-12 col-sm-12 text-center" , "style":"margin-top: 20px; "})
                
                a = div.find("a")
                
                url = a["href"]
                
                title  = soup.find("h1" ,class_="card-title").text

                
                c = course(title , url , "RealDiscount")

                courses.append(c)   

            except:
                pass

        return courses

    def get_category_url(self , category=None , value_13=None):
        url = ""
        categories = {1 : "2", 2 : "3" , 3 : "7", 4 : "8" , 5 : "12" , 6 : "4", 7 : "5", 8 : "10" , 9 : "6" , 10 : "9" , 11 : "11" , 12 : "1"}
        sub_categories = {1 : "programming-languages", 2 : "it-certification" , 3 : "Real-Estate", 4 : "Graphic-Design-Illustration" , 5 : "Home-Improvement" , 6 : "social-media-marketing", 7 : "Finance", 8 : "Dieting" , 9 : "Google" , 10 : "Career-Development" , 11 : "Photography-Tools" , 12 : "engineering"}
       
        if category in list(range(1, 13)):
            word = quote_plus(categories[category])
            sub_categ = sub_categories[category]
            url = f"https://www.real.discount/filter/?category={word}&subcategory={sub_categ}&store=All&duration=All&price=0&rating=All&language=All&search=&submit=Filter&page="
        elif category == 13:
            url  = f"https://www.real.discount/filter/?category=All&store=Udemy&duration=All&price=0&rating=All&language=All&search={value_13}&submit=Filter&page="
            return url
        elif category == 14:
            url = 'https://www.real.discount/filter/?category=All&subcategory=All&store=Udemy&duration=All&price=0&rating=All&language=All&search=&submit=Filter&page='

        else:
            print("Please enter between 1 and 14.")


        return url



    def get_multiple_pages(self ,url , headers , pages=None):
        courses = []
        if pages is None:
            pages=self.get_pages()
        else:
            with ThreadPoolExecutor(max_workers=100) as executor:
                futures = []
                for i in range (1, pages+1):
                    if (
                        "https://www.onlinecourses.ooo/page/REPLACEME/" in url
                        or "https://100offdeal.online/page/REPLACEME" in url
                        or "https://couponseagle.com/page/REPLACEME/" in url
                    ):
                        new_url = url.replace("REPLACEME" , str(i))
                    else:    
                        new_url = url+str(i)
                    futures.append((executor.submit(self.get_free_courses_from_page, new_url , headers)))
            for future in futures:
                data  = future.result()

                courses += data
            
        return courses     



        
