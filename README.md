# Jupyter Notebook + Reveal.js

## Introduction

Microsoft PowerPoint is cool. I like it! It is like a Swiss army knife for consultants. You can make beautiful slides with it. When it comes to code though, PowerPoint sucks. Really! The solution is to use [reveal.js](http://lab.hakim.se/reveal-js/#/). It is cool. You can use Markdown to highlight code. It is responsive but like LaTeX, it can be tedious.

Another way to use reveal.js is through Jupyter Notebook. You just create a notebook and then use `nbconvert` to get reveal.js slides as well. The standard output is however boring. I seriously mean it! This repo therefore tries to bridge this gap by using customized colors and images which are based on the [Pivotal](https://pivotal.io/) color scheme.

Moreover, we live in a cloud native world with a cloud native lifestyle, cloud native storage, cloud native solution. Why not having cloud native presentation slides then? This repo also solves this problem by simply using `cf push`.

## Getting Started

1. You can find a notebook template in the `static` folder which contains some examples like cover and divider slides, markdown syntax and many more. Here is a [link](http://www.slideviper.oquanta.info/tutorial/slideshow_tutorial_slides.html#/3) for a nice intro into creating slides with jupyter notebook.

2. When you are done with editing your notebook, you need to generate the slides with this command `jupyter nbconvert presentation_template.ipynb --to slides --reveal-prefix "reveal.js-3.1.0" --config slides_config.py`. This command basically looks for the reveal.js folder and converts the notebook into a HTML file. The flag `--config slides_config.py` points to some customized settings defined in the `jupyter_template.tpl`. For example there you can control whether the slide numbers are shown or not or you can also add additional plugins etc..

3. Having created the HTML file, it is recommended to use this command `python clean_html.py presentation_template.slides.html` afterwards, especially if you use raw html code in the jupyter notebook. The reason is that in a newer version of nbconvert, it adds section instead of div tags so that data-background doesn't work as expected.

4. Now you can either call `python run.py` to serve the presentation on your local machine or just use `cf push` to push it to the cloud. I use Flask to serve those static files and also be aware that if you change the name of the notebook, this has to be reflected in the `run.py` as well.

#### Requirements:
- Python 3.5.2
- nbconvert 4.2.0
- jupyter 1.0.0
- reveal.js 3.1.0

#### Demo:
- [Presentation Template](http://myslides-on-cf.cfapps.io/)
- [PyData Berlin and London 2016](http://pydata2016.cfapps.io/)

## FAQ

###### How can I change the color of the headline, text, links, list etc.?
You can change everything in the `custom.css` file.

###### How can I change the footer?
If you need to change the footer, open `jupyter_template.tpl` and go to `Change footer here`.

###### Where did you get the image and favicon?
The image used for the cover slide is from [Pexel](https://www.pexels.com/) and the favicon is from [freefavicon](http://www.freefavicon.com/). They are both free to use.

###### Why did you take the color scheme from Pivotal?
Because I work at this company and I use this template for my work and particularly for talks where I represent the company as well.

###### Can I change the name of the jupyter notebook?
Yes, you can but make sure to adjust the code for `jupyter nbconvert new_name.ipynb ...`, `python clean_html.py new_name.ipynb` and also in the `run.py` file.

###### Does it work with other reveal.js version?
Yes, but this is not recommended as the colors might be broken due to differences in the css styles.

## Copyright

See [LICENSE](LICENSE) for details.
Copyright (c) 2016 [Dat Tran](http://www.dat-tran.com/).
