from youtubesearchpython import *


def SearchYoutube(*queries , limit):
    urls = []
    titles = []
    for query in queries:
        customSearch = CustomSearch(query, searchPreferences = "CAMSAhgC",  limit = limit )
        results = customSearch.result()["result"]
        for result in results:
            urls.append(result["link"])
            titles.append(result["title"])
    return titles, urls

def Feed_queries (category , value_13 , limit):
        if category == 1:
            return (SearchYoutube("Freecodecamp" , "Web development Courses" ,  "programming courses" , "coding courses" ,"technology courses", "software development" , "Software engineering" ,"web development courses", "javascript courses" ,"web design courses" , "python courses" ,"html courses" , "java courses" ,"css courses" , "Machine learning courses" , "REinfoecement learning courses" , "Artifical intelligence courses"  , limit=limit))
        elif category == 2:
            return (SearchYoutube("ethical hacking courses" , "data science courses" , "free codecamp IT courses" , "Free code camp softare courses" , "IT and software courses" , "IT Courses" , "CLoud computing courses" , "linux courses" ,"Graphic design courses" , "Video editing courses" , "Adobe photoshop courses" , "Adobe afteraffects courses" , "Data analysis courses" , "Networking courses" , "Computer science courses" , limit = limit))
        elif category == 3:
            return (SearchYoutube("Buisness courses" , "Accounting" , "Marketing courses","Sales courses","Finance courses","International business courses","Human resources courses","Health services administration courses","Management information systems courses","Business administration and management courses" , limit=limit))
        elif category == 4:
            return (SearchYoutube("design  courses"," art  courses"," interiordesign  courses"," architecture  courses"," designer  courses"," fashion  courses"," interior  courses"," love  courses"," graphicdesign  courses"," homedecor  courses"," style  courses"," home  courses"," handmade  courses"," illustration  courses"," decor  courses"," artist  courses"," instagood  courses"," photography  courses"," artwork  courses"," drawing  courses"," creative writing courses" , limit =limit))
        elif category == 5:
            return (SearchYoutube("lifestyle  courses"," love  courses"," life  courses"," motivation  courses"," fitness  courses"," instagram  courses"," fashion  courses"," photography  courses"," beauty  courses"," travel  courses"," nature  courses"," model  courses" , limit =limit))
        elif category == 6:
            return (SearchYoutube("onlinemarketing  courses"," money  courses"," marketingtips  courses"," logo  courses"," contentmarketing  courses"," businessowner  courses"," inspiration  courses"," lifestyle  courses"," brand  courses"," sales  courses"," webdesign  courses"," marketingonline  courses"," realestate  courses"," ecommerce  courses"," marketingagency  courses" , limit =limit))
        elif category == 7:
            return (SearchYoutube("Accounting software courses" , " accounting  courses"," business  courses"," accountant  courses"," finance  courses"," tax  courses"," bookkeeping  courses"," smallbusiness  courses"," cpa  courses"," entrepreneur  courses"," payroll  courses"," accountants  courses"," akuntansi  courses"," accountingservices  courses"," money  courses"," businessowner  courses"," incometax  courses"," audit  courses"," accountingsoftware  courses"," taxconsultant  courses"," marketing  courses"," startup  courses"," management  courses" , limit =limit))
        elif category == 8:
            return (SearchYoutube("Chris heria" , " fitness  courses"," gym  courses"," workout  courses"," fitness courses"," fit  courses"," motivation  courses"," bodybuilding  courses"," training  courses"," love  courses"," health  courses"," lifestyle  courses"," instagood  courses"," fitfam  courses"," healthylifestyle  courses"," sport  courses"," healthy  courses"," gymlife  courses"," instagram  courses"," personaltrainer  courses"," crossfit  courses"," fashion  courses"," fitnessmodel  courses"," gym  courses"," life  courses"," exercise  courses" , limit =limit))
        elif category == 9:
            return (SearchYoutube("productivity  courses", "Excel courses" , "google sheets courses" ,"ms word courses" , "ms office courses"," business  courses"," success  courses"," entrepreneur  courses"," productivitytips  courses"," timemanagement  courses"," smallbusiness  courses"," productivityhacks  courses"," organization  courses"," selfcare  courses", limit=limit))
        elif category == 10:
            return (SearchYoutube("personal development courses" , limit = limit*10))
        elif category == 11:
            return (SearchYoutube("photography courses" , limit = limit*10))
        elif category == 12:
            return (SearchYoutube("teaching  courses" , "academic courses" , "maths courses" ,"science courses" , "Vsauce",  limit = limit*2))
        elif category == 13:
            return (SearchYoutube(value_13,limit = limit*10))
        elif category == 14:
            return (SearchYoutube("Freecodecamp" , "Web development Courses" ,  "programming courses" , "productivity  courses", "Excel courses" , "google sheets courses" ,"ms word courses" , " business  courses"," accountant  courses"," finance  courses" ,"CLoud computing courses" , "linux courses" ,"Graphic design courses" , "Video editing courses" , "Adobe photoshop courses" , "Adobe afteraffects courses" , "Accounting software courses" , "health courses" , "Chris heria" , "fitness courses" , limit=limit))