from includes.global_includes import *

def gen_page_resume():
    output = gen_header()
    output += '''<div class="container text-center mt-5">
	<div class="row">
		<h3>Resume PDF</h3>
	</div>
	<hr class="mt-3 mb-3">
    
    
	 <object data="docs/resume5.pdf" type="application/pdf" style="width:100%; min-height:75vh">
		<p>Potentially unable to display PDF file. <a href="docs/resume5.pdf">Download</a> instead.</p>
		<embed src="https://docs.google.com/file/d/1c-jFkRbqQhTZU04dsjiKzx7p4RbXrcAxMh5UvZisGz4/preview?usp=sharing" style="width:100%; height:50vh"/>
     </object>
    </div><!-- /.container -->'''
    output += gen_footer()
    return output