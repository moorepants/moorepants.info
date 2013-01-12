genserve:
	rsync /media/Data/Documents/Resume/JasonMoore_cv.pdf content/media/docs/JasonMoore_cv.pdf
	hyde gen -r
	hyde serve
