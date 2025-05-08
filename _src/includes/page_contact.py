from includes.global_includes import *

def gen_page_contact():
    output = gen_header()
    output += '''<div class="container mt-5">
        <div class="row featurette">
         
            <div class="col-3"></div>
            <div class="col-6">
                <p>The best way to contact me is through my email, <a href="mailto:mjablon@iastate.edu">mjablon@iastate.edu</a>. I check it daily and will get back to you as soon as reasonably possible.</p>
                
            </div>
            <div class="col-3"></div>
            
        </div>
    </div><!-- /.container -->'''
    output += gen_footer()
    return output