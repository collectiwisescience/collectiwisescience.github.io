Run pelican content to generate the HTML.
Switch to the output directory.
Run python -m pelican.server.
Visit localhost:8000 in your browser to preview the blog.


To publish the changes:

Edit SITEURL in publishconf.py, so that it is set to http://username.github.io, where username is your GitHub username.
