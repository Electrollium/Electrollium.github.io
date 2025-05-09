from includes.global_includes import *

import json

def get_projects():    
    with open('./data_sources/projects.json','r') as file: 
        projects = json.loads(file.read())
    
    return projects
    
    
    

def formatted_project_list_item(project):
    output = f'<div class="border border-3 border-dark-subtle rounded-4 shadow mx-2 my-3 py-2 row project-row" modalurl="{project["modalurl"]}">' #row for project
    
    output += '<div class="col-md-9 order-md-1"><div class="row">' #start of text
    output += f'<h3> {project["title"]} </h3>'
    output += f'<p> {project["blurb"]} </p>'
    output += '</div></div>'#end of text
    
    output += f'<div class="col-md-3 order-md-2"><img class="img-fluid" src="images/{project["thumbnail"]}"></div>'
    output += '</div>' #close the row div
    return output
    

def gen_page_projects():

    projects = get_projects()

    output = gen_header()
    output += '<div class="container mt-5">'
    output += '''<div class="row">
    
        <div class="col-md-9 order-md-2 d-flex align-items-center">
            <div class="row">
                <h3> Projects Directory </h3>
                <p> This directory houses the many projects I have done over the years. Stay tuned as there are always new projects in the pipeline. Select any project to view more details.</p>
            </div>
        </div>
        
        <div class="col-md-3 order-md-1">
            <img class="img-fluid rounded shadow" src="images/headshot_sq_sm.png">
        </div>
    </div>'''
    
    for proj in projects:
        output += formatted_project_list_item(proj)
    
    output +='</div><!-- container -->'
    output += gen_footer()
    return output