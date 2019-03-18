### Instructions on using GitHub Pages with _Pelican

## To preview:
Run _pelican content_ to generate the HTML.
Switch to the __output__ directory
Run _python -m pelican.server_
Visit _localhost:8000_ in your browser to preview the blog



## To create publishable the changes:
GitHub Pages need HTML content to be in the root folder. 
Generate HTML content for 'publishing' (not previewing) by running _pelican content -s publishconf.py_
Run _git checkout blog_ to switch to a branch called blog. (We can’t use master to store our notebooks, since that’s the branch that’s used by GitHub Pages)
Create a commit and push to GitHub like normal (using git add, git commit, and git push).


## To publish the changes:
Run _ghp-import output -b master_ to import everything in the output folder to the master branch
Use _git push origin master_ to push your content to GitHub.

Resrouces: https://www.dataquest.io/blog/how-to-setup-a-data-science-blog
