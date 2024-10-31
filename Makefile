slides:
	jupyter nbconvert --to slides \
		--SlidesExporter.reveal_scroll=True \
		--ServePostProcessor.browser chrome \
		--post serve lecture_$(lec).ipynb
