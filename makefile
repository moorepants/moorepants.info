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
	rsync ~/Documents/resume/JasonMoore_cv.pdf content/media/docs/JasonMoore_cv.pdf
	rsync ~/Projects/appropriate-tech/HumanPowerPresentation/hppres.pdf content/media/docs/hppres.pdf
	rsync ~/Projects/appropriate-tech/HumanPowerPresentation/hppres-notes.pdf content/media/docs/hppres-notes.pdf
	rsync ~/Research/structuralid/Hess_Moore_MST_Paper.pdf content/media/docs/hess-moore-mst-final.pdf

buildstatements:
	rst2latex --date --documentoptions="letter,10pt" --use-latex-docinfo --latex-preamble="$(statementpreamble)" content/research/$(rs).rst $(docdir)/$(rs).tex
	pdflatex --output-directory=$(docdir) $(docdir)/$(rs).tex > /dev/null
	rm $(docdir)/$(rs).aux $(docdir)/$(rs).out $(docdir)/$(rs).log $(docdir)/$(rs).tex
	rst2latex --date --documentoptions="letter,10pt" --use-latex-docinfo --latex-preamble="$(statementpreamble)" content/$(ts).rst $(docdir)/$(ts).tex
	pdflatex --output-directory=$(docdir) $(docdir)/$(ts).tex > /dev/null
	rm $(docdir)/$(ts).aux $(docdir)/$(ts).out $(docdir)/$(ts).log $(docdir)/$(ts).tex

push: getresume buildstatements
	hyde gen -r -c prod.yaml
	rsync -r -t --delete --progress $(source) $(username)@$(server):$(destination)
	#ssh $(username)@$(server) 'chmod -R u+w,a+rX $(destination)'
	ssh $(username)@$(server) 'find $(destination) -type f -exec chmod 644 {} \;'
	ssh $(username)@$(server) 'find $(destination) -type d -exec chmod 755 {} \;'

clean:
	rm -rf $(source)
