def gen_header():
    
    output = '''<!doctype html>
        <html lang="en" data-bs-theme="auto">
          <head>

            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Marek Jablonski's Personal Portfolio</title>    

            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">

            
            <!-- Custom styles for this template -->
            <link href="main.css" rel="stylesheet">
          </head>
          
        <body>
            
        <!-- header bar -->
        <header data-bs-theme="dark">
          <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <div class="container-fluid">
              <a class="navbar-brand" href="#">Marek Jablonski</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" >
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav ms-auto mb-2 mb-md-0">
                  <li class="nav-item">
                    <a class="nav-link" href="index.html">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="projects.html">Projects</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="resume.html">Work Experience</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link"  href="contact.html">Contact Me</a>
                  </li>

                </ul>
              </div>
            </div>
          </nav>
        </header>

        <main>'''
        
    return output
    
def gen_footer():
    with open('./includes/footer.html','r') as file: 
        output = file.read()
    return output
    