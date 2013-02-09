username=jasonkmoore
server=moorepants.info
source=deploy/
destination=/home/jasonkmoore/moorepants.info/
docdir=content/media/docs
statementpreamble=\usepackage[top=1in,bottom=1in,right=1in,left=1in]{geometry}
rs=research-statement
ts=teaching-statement

genserve: getresume buildstatements
	hyde gen -r
	hyde serve

getresume:
	rsync /media/Data/Documents/Resume/JasonMoore_cv.pdf content/media/docs/JasonMoore_cv.pdf
	rsync /media/Data/Documents/School/UC\ Davis/Appropriate\ Technology/HumanPowerPresentation/hppres.pdf content/media/docs/hppres.pdf
	rsync /media/Data/Documents/School/UC\ Davis/Appropriate\ Technology/HumanPowerPresentation/hppres-notes.pdf content/media/docs/hppres-notes.pdf

buildstatements:
	rst2latex.py --latex-preamble="$(statementpreamble)" content/research/$(rs).rst $(docdir)/$(rs).tex
	pdflatex --output-directory=$(docdir) $(docdir)/$(rs).tex > /dev/null
	rm $(docdir)/$(rs).tex $(docdir)/$(rs).aux $(docdir)/$(rs).out $(docdir)/$(rs).log
	rst2latex.py --latex-preamble="$(statementpreamble)" content/$(ts).rst $(docdir)/$(ts).tex
	pdflatex --output-directory=$(docdir) $(docdir)/$(ts).tex > /dev/null
	rm $(docdir)/$(ts).tex $(docdir)/$(ts).aux $(docdir)/$(ts).out $(docdir)/$(ts).log

push: getresume buildstatements
	hyde gen -r -c prod.yaml
	rsync -r -t -v --delete --progress $(source) $(username)@$(server):$(destination)
	#ssh $(username)@$(server) 'chmod -R u+w,a+rX $(destination)'
	ssh $(username)@$(server) 'find $(destination) -type f -exec chmod 644 {} \;'
	ssh $(username)@$(server) 'find $(destination) -type d -exec chmod 755 {} \;'

clean:
	rm -rf $(source)
