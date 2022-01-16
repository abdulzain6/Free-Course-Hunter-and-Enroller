from .Real_Discount import *
from .models import *


class coupon_eagle (real_disc):
    def get_free_courses_from_page (self , url , headers):
        courses = []
        links = []
        request  = requests.get(url , allow_redirects=True , headers=headers)
        soup = BeautifulSoup(request.text , "html.parser")
        h2s = soup.find_all("h2" , class_="font130 mt0 mb10 mobfont120 lineheight25")

        for h2 in h2s:

            a = h2.find("a")

            course_name = a.text

            link = a["href"].strip()

            r  = requests.get(link , allow_redirects=True , headers=headers)

            soup = BeautifulSoup(r.text , "html.parser")

            a = soup.find("a" , class_="btn_offer_block re_track_btn")

            course_link = a["href"].strip()

            c = course(course_name , course_link , "CouponEagle")

            courses.append(c)

        return courses

    def get_category_url(self , category=None , value_13=None):
        url = ""
        categories = {1 : "Development", 2 : "IT & Software" , 3 : "Business", 4 : "Design" , 5 : "Lifestyle" , 6 : "Marketing", 7 : "Finance & Accounting", 8 : "Health & Fitness" , 9 : "Office-Productivity" , 10 : "Personal Development" , 11 : "Photography & Video" , 12 : "Teaching & Academics"}

        if category in [1,3,9,6]:
            word = categories[category]
            url = f"https://couponseagle.com/category/{word}/page/"
        elif category == 2:
            url = 'https://couponseagle.com/page/REPLACEME/?s=it+and+software&post_type=post'

        elif category == 4:
            url = 'https://couponseagle.com/page/REPLACEME/?s=DESIGN&post_type=post'
        elif category == 5:
            url = 'https://couponseagle.com/page/REPLACEME/?s=lifestyle&post_type=post'
        elif category == 7:
            url = 'https://couponseagle.com/page/REPLACEME/?s=Finance+%26+Accounting&post_type=post'

        elif category == 8:
            url = 'https://couponseagle.com/page/REPLACEME/?s=Health+%26+Fitness&post_type=post'

        elif category == 10:
            url = 'https://couponseagle.com/page/REPLACEME/?s=Personal+Development&post_type=post'

        elif category == 11:
            url = 'https://couponseagle.com/page/REPLACEME/?s=Teaching&post_type=post'
        elif category == 12:
            url = 'https://couponseagle.com/page/REPLACEME/?s=Photography+%26+Video&post_type=post'

        elif category == 13:
            url = f"https://couponseagle.com/page/REPLACEME/?s={quote_plus(value_13)}"
        elif category == 14:
            url = "https://couponseagle.com/page/"
        else:
            print("Please enter between 1 and 14.")

        return url


 



