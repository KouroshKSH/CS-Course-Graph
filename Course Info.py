from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


courses_file = open("dta","r")
result = open("result","w")

courses_list = str(courses_file.read()).split("\n")

result_data = ""

for course in courses_list:
    # course_info += course + "\t"
    
    courseurl = "http://suis.sabanciuniv.edu/prod/sabanci_www.p_get_courses?levl_code=UG&subj_code=" + course.replace(" ","&crse_numb=") + "&lang=eng"
  
    website_html = str(urlopen(courseurl).read())

    website_soup = BeautifulSoup(website_html, features="html.parser")

    website_data = website_soup.get_text()
    # print(website_data)

    course_info = website_data[website_data.find("Prerequisite: "):].replace("\\n", "\n")
    course_info = re.sub(r'\n\s*\n', ',',course_info)
    prereqs = course_info[course_info.find("Prerequisite: ") + len("Prerequisite: "): course_info.find(",Corequisite: ")].split(",")
    for item in prereqs:
        result_data += item.split(" - ")[0]
    coreq = course_info[course_info.find("Corequisite: ") + len("Corequisite: "): course_info.find(",ECTS Credit: ")]
    genreq = course_info[course_info.find("General Requirements: ") + len("General Requirements: "):].replace("\n"," ")[:-2]
    result_data += ('\t' + coreq + '\t' + genreq)
    result_data += "\n"
    
result.write(result_data)
    
print("process finished")
result.close()

courses_file.close()
