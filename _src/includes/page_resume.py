from includes.global_includes import *

def gen_page_resume():
    output = gen_header()
    output += '''<div class="container text-center mt-5">
	<div class="row">
		<h3>Work Experiences</h3>
	</div>
	<hr class="mt-3 mb-3">
	
	<div class="row">
	
		<div class="col-6">
			<div class="row">
				<h3>Electrical Engineer</h3>
			</div>
			<div class="row">
				<h6>May 2023 - August 2024</h6>
			</div>
			<div class="row">
				<h6>Vermeer Corporation</h6>
			</div>
			<div class="row text-start">
				<ul>
					<li>Designed electronic circuits and PCBs</li>
					<li>Built Programming fixtures from the ground up</li>
					<li>Quickly prototyped MVP devices for future products</li>
					<li>Learned to design for EMI and EMC compliance</li>
					<li>Improved documentation and requirement writing abilities</li>
					<li>Evaluated in peer and mentor design reviews</li>
				</ul>
			</div>
		</div>
		
	
		<div class="col-6">
			<div class="row">
				<h3>Software Engineer</h3>
			</div>
			<div class="row">
				<h6>May 2022 - August 2022</h6>
			</div>
			<div class="row">
				<h6>RACOM Corporation</h6>
			</div>
			<div class="row text-start">
				<ul>
					<li>Headed design effort on new Project</li>
					<li>Full Stack Software System Design</li>
					<li>Presented in dedicated client meetings</li>
					<li>Incorporated feedback into iterative designs</li>
				</ul>
			</div>
		</div>
	</div>
  
	<hr class="mt-3 mb-3">
  
	 <object data="docs/resume5.pdf" type="application/pdf" style="width:100%; min-height:50vh">
		<p>Potentially unable to display PDF file. <a href="docs/resume5.pdf">Download</a> instead.</p>
		<embed src="https://docs.google.com/file/d/1c-jFkRbqQhTZU04dsjiKzx7p4RbXrcAxMh5UvZisGz4/preview?usp=sharing" style="width:100%; height:50vh"/>
     </object>
    </div><!-- /.container -->'''
    output += gen_footer()
    return output