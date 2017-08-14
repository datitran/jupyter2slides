# Jupyter Notebook + Reveal.js

## Introduction

Microsoft PowerPoint is cool. I like it! It is like a Swiss army knife for consultants. You can make beautiful slides with it. When it comes to code though, PowerPoint sucks. Really! The solution is to use [reveal.js](http://lab.hakim.se/reveal-js/#/). It is cool. You can use Markdown to highlight code. It is responsive but like LaTeX, it can be tedious.

Another way to use reveal.js is through Jupyter Notebook. You just create a notebook and then use `nbconvert` to get reveal.js slides as well. The standard output is however boring. I seriously mean it! This repo therefore tries to bridge this gap by using customized colors and images.

Moreover, we live in a cloud native world with a cloud native lifestyle, cloud native storage, cloud native solution. Why not having cloud native presentation slides then? This repo also solves this problem by simply using `cf push`.

## Getting Started

1. You can find a notebook template in the `static` folder which contains some examples like cover and divider slides, markdown syntax and many more. Here is a [link](http://www.slideviper.oquanta.info/tutorial/slideshow_tutorial_slides.html#/3) for a nice intro into creating slides with Jupyter notebook.
2. When you are done with editing your notebook, you need to generate the slides with this command:
    ```
    # from ./jupyter2slides/
    python create_slides.py --file static/presentation_template.ipynb
    ```
3. Now you can either call this command to serve the presentation on your local machine
    ```
    python run.py --file static/presentation_template.slides.html
    ```
    or just use `cf push` to push it to the cloud. I use Flask to serve those static files.

4. To convert the slides to pdf, I use [decktape](https://github.com/astefanutti/decktape):
    ```
    cd decktape-1.0.0/
    ./phantomjs decktape.js generic --keycode=Space "http://0.0.0.0:9099/" presentation_template.pdf
    ```
    or you can also use the [`?print-pdf`](https://github.com/hakimel/reveal.js/#pdf-export) option but this is not recommended as the formatting is not displayed correctly.

#### Requirements:
- Python 3.5.2
- nbconvert 5.2.1
- reveal.js 3.1.0

#### Demo:
- [Presentation Template](http://myslides-on-cf.cfapps.io/) | [PDF](https://www.slideshare.net/DatTran33/presentation-template-from-jupyter2slides)
- [Interactive Template](http://interactive-slides.cfapps.io/) | [PDF](https://www.slideshare.net/DatTran33/interactive-slide-deck-jupyter2slides)

## FAQ

###### How can I change the color of the headline, text, links, list etc.?
You can change everything in the `custom.css` file.

###### How can I change the footer?
If you need to change the footer, open `jupyter_template.tpl` and go to `Change footer here`.

###### Where did you get the image and favicon?
The image used for the cover slide is from [Pexel](https://www.pexels.com/) and the favicon is from [freefavicon](http://www.freefavicon.com/). They are both free to use.

###### Does it work with other reveal.js version?
Yes, but this is not recommended as the colors might be broken due to differences in the css styles.

## Copyright

See [LICENSE](LICENSE) for details.
Copyright (c) 2016 [Dat Tran](http://www.dat-tran.com/).
