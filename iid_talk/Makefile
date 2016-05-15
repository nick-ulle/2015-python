slides.html: slides.mdown
	pandoc -t revealjs -s $< -o $@

view: slides.html
	open $<
