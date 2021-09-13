from .Real_Discount import *


class udemyme (real_disc):
    def get_free_courses_from_page (self , url , headers):
        courses = []
        links = []
        coupon_link = []
        request  = requests.get(url , allow_redirects=True , headers=headers)
        soup = BeautifulSoup(request.text , "html.parser")
        h3s = soup.find_all("h3" , class_="entry-title td-module-title")
        for h3 in h3s:
            a = h3.find("a",{"rel":"bookmark"})
            courses.append(a.text)
            links.append(a["href"])

        for link in links:
            r  = requests.get(link , allow_redirects=True , headers=headers)
            soup = BeautifulSoup(r.text , "html.parser")
            a = soup.find_all("a" , {"target":"_blank", "rel":"noopener"})
            try:
                coupon_link.append(a[2]["href"].strip())
            except IndexError:
                try:
                    coupon_link.append(a[1]["href"].strip())
                except IndexError:
                    try:
                        coupon_link.append(a[0]["href"].strip())
                    except:
                        return [] , []



        return (courses , coupon_link)

        
    def get_category_url (self , category=None , value_13=None):
        url = ""
        categories = {1 : "Development", 2 : "IT & Software" , 3 : "Business", 4 : "Design" , 5 : "Lifestyle" , 6 : "Marketing", 7 : "Finance & Accounting", 8 : "Health & Fitness" , 9 : "Office Productivity" , 10 : "Personal Development" , 11 : "Photography & Video" , 12 : "Teaching & Academics"}
        
        if category == 1:
            url =f"https://udemycoupons.me/dev/page/"
        elif category == 2:
            url = f"https://udemycoupons.me/it-software-courses/page/"
        elif category == 3:
            url = f"https://udemycoupons.me/business-courses/page/"
        elif category == 4:
            url = f"https://udemycoupons.me/design-courses/page/"
        elif category == 5:
            url = f"https://udemycoupons.me/health-fitness-courses/page/"
        elif category == 6:
            url = f"https://udemycoupons.me/marketing-courses/page/"
        elif category == 7:
            url = f"https://udemycoupons.me/business-courses/page/"
        elif category == 8:
            url = f"https://udemycoupons.me/health-fitness-courses/page/"
        elif category == 9:
            url = f"https://udemycoupons.me/office-productivity-courses/page/"
        elif category == 10:
            url = f"https://udemycoupons.me/personal-development-courses/page/"
        elif category == 11:
            url = f"https://udemycoupons.me/design-courses/page/"
        elif category == 12:
            url = f"https://udemycoupons.me/teaching-academics-courses/page/"
        elif category == 13:
            url = f"https://udemycoupons.me/page/REPLACEME/?s={quote_plus(value_13)}"
        elif category == 14:
            url = f"https://udemycoupons.me/page/"
        else:
            print("Please enter between 1 and 14.")

        return url




