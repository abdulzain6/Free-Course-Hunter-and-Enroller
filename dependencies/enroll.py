import cloudscraper ,time , random
from .Real_Discount import *
RED  = "\u001b[31m"
CYAN = "\u001b[36m"
GREEN = "\u001b[32m"
BLUE = "\u001b[34;1m"
WHITE = "\u001b[37;1m"
YELLOW = "\u001b[33m"
GREY ="\u001b[30;1m"
GREEN2 = "\u001b[32;1m"
def free_checkout(coupon, courseid , s , currency):
    payload = (
        '{"checkout_environment":"Marketplace","checkout_event":"Submit","shopping_info":{"items":[{"discountInfo":{"code":"'
        + coupon
        + '"},"buyable":{"type":"course","id":'
        + str(courseid)
        + ',"context":{}},"price":{"amount":0,"currency":"'
        + currency
        + '"}}]},"payment_info":{"payment_vendor":"Free","payment_method":"free-method"}}'
    )

    r = s.post(
        "https://www.udemy.com/payment/checkout-submit/",
        data=payload,
        verify=False,
    )
    return r.json()


def free_enroll(courseid , s):

    s.get(
        "https://www.udemy.com/course/subscribe/?courseId=" + str(courseid)
    )

    r = s.get(
        "https://www.udemy.com/api-2.0/users/me/subscribed-courses/"
        + str(courseid)
        + "/?fields%5Bcourse%5D=%40default%2Cbuyable_object_type%2Cprimary_subcategory%2Cis_private"
    )
    return r.json()
def get_course_id(url):
    r = requests.get(url, allow_redirects=False)
    if r.status_code in (404, 302, 301):
        return False
    if "/course/draft/" in url:
        return False
    soup = BeautifulSoup(r.content, "html.parser")

    try:
        courseid = soup.find(
            "div",
            attrs={"data-content-group": "Landing Page"},
        )["data-course-id"]
    except:
        courseid = soup.find(
            "body", attrs={"data-module-id": "course-landing-page/udlite"}
        )["data-clp-course-id"]
        # with open("problem.txt","w",encoding="utf-8") as f:
        # f.write(str(soup))
    return courseid


def get_email_password():
    email = input("Enter your Udemy email please. ")
    password = input("Enter your Udemy password.  ")
    return email, password

def get_cookies():
    client_id = input("Enter your Udemy client_id. ")
    access_token = input("Enter your Udemy access_token. ")
    csrf_token = input("Enter your Udemy csrf_token. ")
    return client_id, access_token, csrf_token

def make_cookie(client_id , access_token , csrf_token):
    cookie = {
        "client_id" : client_id,
        "access_token" : access_token,
        "csrf_token" : csrf_token
    }
    return cookie

def get_course_coupon(url):
    query = urlsplit(url).query
    params = parse_qs(query)
    try:
        params = {k: v[0] for k, v in params.items()}
        return params["couponCode"]
    except:
        return ""

def authorize(cookies):
        # Returns session with authorization 
        head = {
        "authorization": "Bearer " + cookies["access_token"],
        "accept": "application/json, text/plain, */*",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77",
        "x-forwarded-for": str(
            ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        ),
        "x-udemy-authorization": "Bearer " + cookies["access_token"],
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.udemy.com",
        "referer": "https://www.udemy.com/",
        "dnt": "1",
        }
        
        s = requests.session()
        s.cookies.update(cookies)
        s.headers.update(head)
        s.keep_alive = False
        
        r = s.get(
            "https://www.udemy.com/api-2.0/contexts/me/?me=True&Config=True"
        ).json()
        currency = r["Config"]["price_country"]["currency"]
        user = ""
        user = r["me"]["display_name"]

        return head, user, currency, s



def try_login(email, password):
    for retry in range(4):
        s = requests.Session()

        r = s.get(
            "https://www.udemy.com/join/signup-popup/",
        )
        soup = BeautifulSoup(r.text, "html.parser")

        csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]

        data = {
            "email": email,
            "password": password,
            "locale": "en_US",
            "csrfmiddlewaretoken": csrf_token,
        }
        s = cloudscraper.create_scraper()

        s.cookies.update(r.cookies)
        s.headers.update({"Referer": "https://www.udemy.com/join/signup-popup/"})
        try:
            r = s.post(
                "https://www.udemy.com/join/login-popup/?locale=en_US",
                data=data,
                allow_redirects=False,
            )
        except cloudscraper.exceptions.CloudflareChallengeError:
            if retry == 3:
                print(RED +"Cloudflare is blocking your requests try again after an hour")
                exit()
            retry -= 1
            continue
        if r.status_code != 302:
            soup = BeautifulSoup(r.content, "html.parser")
            txt = soup.find("div", class_="alert alert-danger js-error-alert").text.strip()
            if txt[0] == "Y":
                print(YELLOW +"Too many logins per hour try later")
            elif txt[0] == "T":
                print(RED +"Email or password incorrect")
            else:
                print(YELLOW +txt)
            time.sleep(1)
            exit()
        cookies = make_cookie(r.cookies["client_id"], r.cookies["access_token"], csrf_token)
        head, user, currency, s = authorize(r.cookies)

        return currency, s



def enroll_with_email_pass(url , currency ,logged_session):
    id  = get_course_id(url)
    coupon = get_course_coupon(url)
    free_enroll(id , logged_session)
    try:
        free_checkout(coupon , id ,logged_session ,currency)
        print(RED +"[Enrolled] " , url)
    except:
        print(RED +"Failed to enroll")

def enroll_with_cookie(url , cookies):
    head, user, currency, s = authorize(cookies)
    id  = get_course_id(url)
    coupon = get_course_coupon(url)
    free_enroll(id , s)
    try:
        free_checkout(coupon , id ,s ,currency)
        print(f"{GREEN}[Enrolled] " , url)
    except:
        print(f"{GREEN}Failed to enroll")


    
