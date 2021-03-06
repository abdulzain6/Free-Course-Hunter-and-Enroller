from .Real_Discount import *
from .models import *


class freedeal (real_disc):
    def get_free_courses_from_page (self , url , headers):
        courses = []
        request  = requests.get(url , allow_redirects=True , headers=headers)
        soup = BeautifulSoup(request.text , "html.parser")
        figures = soup.find_all("figure" , class_="post-featured-image post-img-wrap")
        for figure in figures:
            a = figure.find("a", class_="post-img")

            link = a["href"].strip()

            r  = requests.get(link , allow_redirects=True , headers=headers)

            soup = BeautifulSoup(r.text , "html.parser")

            a = soup.find("a" , class_="maxbutton-1 maxbutton maxbutton-get-this-free-course")
            
            coupon_link = a["href"].strip()

            course_name = soup.find("title").text

            c = course(course_name , coupon_link , "Freedeal")

            courses.append(c)

        return courses


    def get_category_url(self , category=None , value_13=None):
        url = ""
        categories = {1 : "Development", 2 : "IT & Software" , 3 : "Business", 4 : "Design" , 5 : "Lifestyle" , 6 : "Marketing", 7 : "Finance & Accounting", 8 : "Health & Fitness" , 9 : "Office Productivity" , 10 : "Personal Development" , 11 : "Photography & Video" , 12 : "Teaching & Academics"}

        if category == 1:
            url = 'https://100offdeal.online/web-development/page/'
        elif category == 2:
            url = 'https://100offdeal.online/it-software/page/'
        elif category == 3:
            url = 'https://100offdeal.online/business/page/'
        elif category == 4:
            url = 'https://100offdeal.online/design/page/'
        elif category == 5:
            url = 'https://100offdeal.online/lifestyle/page/'
        elif category == 6:
            url = 'https://100offdeal.online/marketing/page/'
        elif category == 7:
            url = 'https://100offdeal.online/finance/page/'
        elif category == 8:
            url = 'https://100offdeal.online/lifestyle/page/'
        elif category == 9:
            url = 'https://100offdeal.online/business/office-productivity/page/'
        elif category == 10:
            url = 'https://100offdeal.online/personal-development-courses/page/'
        elif category == 11:
            url = 'https://100offdeal.online/photography/page/'
        elif category == 12:
            url = 'https://100offdeal.online/free-language-courses/page/'
        elif category == 13:
            url = f"https://100offdeal.online/page/REPLACEME/?s={quote_plus(value_13)}"
        elif category == 14:
            url = 'https://100offdeal.online/page/'
        else:
            print("Please enter between 1 and 14.")

        return url

    

