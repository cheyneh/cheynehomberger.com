# cheynehomberger.com

This repository uses [Pelican](http://docs.getpelican.com/en/3.6.3/) to generate 
a series of static html pages from markdown. Both the input content and the 
output html are included in this repository. 

Custom theme based on [flasky](https://github.com/fjavieralba/flasky), and 
modified to make it less blog-focused and more suitable for an academic 
portfolio (including the addition of 
[academicons](http://jpswalsh.github.io/academicons/#)). 

## Usage

The raw markdown content and pdfs are placed in the `content` folder. Generate 
the output html by running `pelican` in the top-level directory. The contents of 
`output` are hosted at `http://cheynehomberger.com`. For testing/development, 
you'll want to enable `RELATIVE_LINKS = True` in the `pelicanconf.py`. Otherwise 
all links will be absolute, and based on your `SITEURL` variable. 


