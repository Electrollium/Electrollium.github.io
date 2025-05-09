from includes.page_index import *
from includes.page_projects import *
from includes.page_contact import *
from includes.page_resume import *


page_config = [
    ['Home','index.html',gen_page_index()],
    ['Projects','projects.html',gen_page_projects()],
    ['Work Experience','resume.html',gen_page_resume()],
    ['Contact Me','contact.html',gen_page_contact()]
    ]

for page in page_config:
    with open('../'+page[1],'w') as file: #page[0] is the file name
        file.write(page[2])#generation output