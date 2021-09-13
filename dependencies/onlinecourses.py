from .Real_Discount import *


class onlinecourses (real_disc):
    def get_free_courses_from_page (self , url , headers):
        courses = []
        links = []
        coupon_link = []
        request  = requests.get(url , allow_redirects=True , headers=headers)
        soup = BeautifulSoup(request.text , "html.parser")
        h3s = soup.find_all("h3" , class_="entry-title")
        for h3 in h3s:
            a = h3.find("a",{"rel":"bookmark"})
            courses.append(a.text)
            links.append(a["href"])

        for link in links:
            r  = requests.get(link , allow_redirects=True , headers=headers)
            soup = BeautifulSoup(r.text , "html.parser")
            a = soup.find("a" , {"target":"_blank", "class":"coupon-code-link"})
            coupon_link.append(a["href"].strip())


        return (courses , coupon_link)

    def get_category_url (self , category=None , value_13=None):
        url = ""
        categories = {1 : "Development", 2 : "IT & Software" , 3 : "Business", 4 : "Design" , 5 : "Lifestyle" , 6 : "Marketing", 7 : "Finance & Accounting", 8 : "Health & Fitness" , 9 : "Office Productivity" , 10 : "Personal Development" , 11 : "Photography & Video" , 12 : "Teaching & Academics"}
        
        if category in [1,3,4,5,6]:
            word = quote_plus(categories[category])
            url = f"https://www.onlinecourses.ooo/coupon-tag/{word}/page/"        
        elif category == 2:
            url =f"https://www.onlinecourses.ooo/coupon-tag/it-software/page/"
        elif category == 7:
            url = f"https://www.onlinecourses.ooo/coupon-tag/finance-accounting/page/"
        elif category == 8:
            url = f"https://www.onlinecourses.ooo/coupon-tag/health-fitness/page/"
        elif category == 9:
            url = f"https://www.onlinecourses.ooo/coupon-tag/office-productivity/page/"
        elif category == 10:
            url = f"https://www.onlinecourses.ooo/coupon-tag/personal-development/page/"
        elif category == 11:
            url = f"https://www.onlinecourses.ooo/coupon-tag/photography-video/page/"
        elif category == 12:
            url = f"https://www.onlinecourses.ooo/coupon-tag/teaching-academics/page/"
        elif category == 13:
            url = f"https://www.onlinecourses.ooo/page/REPLACEME/?s={quote_plus(value_13)}"
        elif category == 14:
            url = "https://www.onlinecourses.ooo/page/"
        else:
            print("Please enter between 1 and 14.")

        return url
