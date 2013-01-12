username=jasonkmoore
server=moorepants.info
source=deploy/
destination=/home/jasonkmoore/moorepants.info/

genserve: getresume
	hyde gen -r
	hyde serve

getresume:
	rsync /media/Data/Documents/Resume/JasonMoore_cv.pdf content/media/docs/JasonMoore_cv.pdf

push: getresume
	hyde gen -r -c prod.yaml
	rsync -r -t -v --delete --progress $(source) $(username)@$(server):$(destination)
	#ssh $(username)@$(server) 'chmod -R u+w,a+rX $(destination)'
	ssh $(username)@$(server) 'find $(destination) -type f -exec chmod 644 {} \;'
	ssh $(username)@$(server) 'find $(destination) -type d -exec chmod 755 {} \;'
