from includes.page_index import *
from includes.page_projects import *
from includes.page_contact import *
from includes.page_resume import *


page_config = [
    ['index.html',gen_page_index()],
    ['projects.html',gen_page_projects()],
    ['contact.html',gen_page_contact()],
    ['resume.html',gen_page_resume()]
    ]

for page in page_config:
    with open('../'+page[0],'w') as file: #page[0] is the file name
        file.write(page[1])#generation output