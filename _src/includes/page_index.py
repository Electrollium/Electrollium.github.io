from includes.global_includes import *

def gen_page_index():
    output = gen_header()
    output += '''<div class="container text-center mt-5">
        <div class="row featurette">
          <div class="col-md-6 order-md-3 d-flex align-items-center"> <!-- cna add shadow and rounded to class list -->
        
            <div class="row">
                <h2 class="featurette-heading fw-normal lh-1">Hi, I'm Marek</h2>
                <p class="lead">I'm currently a Senior studying Computer Engineering at Iowa State University. I enjoy building projects and fixing things when I'm not  busy studying or helping lead the PRISUM solar car team here at Iowa State. My current Career Objective is to earn my Master's Degree in Computer Engineering and enter the workforce within the fields of embedded and power electronics.</p>
            </div>
            
          </div>
          <div class="col-md-5 order-md-1 d-flex justify-content-center align-content-center" >
            <img class="img-fluid rounded shadow" src="images/headshot_sq_sm.png">
          </div>
          <div class="col-md-1 order-md-2" ></div>
        </div>
        
        <hr class="featurette-divider">

        <!-- Three columns of text below the carousel -->
        <div class="row">
        
          <div class="col-lg">
            <img class="img-fluid" src="images/p16_circle.png"  width="140" height="140" >
            <h2 class="fw-normal">Projects</h2>
            <p>A collection of summaries of the many projects I have been involved with.</p>
            <p><a class="btn btn-secondary" href="projects.html">View details &raquo;</a></p>
          </div>
          
          <div class="col-lg">
            <img class="img-fluid" src="images/work_experience_image.png"  width="140" height="140" >
            <h2 class="fw-normal">Work Experience</h2>
            <p>Documentation of my various work experiences and my current Resume'.</p>
            <p><a class="btn btn-secondary" href="resume.html">View details &raquo;</a></p>
          </div>
          
        </div><!-- /.row -->

    </div><!-- /.container -->'''
    output += gen_footer()
    return output