from includes.page_index import *

page_config = [
    ['index.html',gen_page_index()]
    ]


for page in page_config:
    
    with open(page[0],'w') as file:
        file.write(page[1])