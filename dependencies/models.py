class course:
    courses : str
    coupon_link : str
    website : str
    money_saved :int

    def __init__(self , courses = "" , coupon_link = "" , website = "" ,money_saved = 0):
        self.courses = courses
        self.coupon_link = coupon_link
        self.website = website
        self.money_saved = money_saved
    def __repr__(self):
        return f"({self.courses} , {self.coupon_link} , {self.website}, {self.money_saved})"

    