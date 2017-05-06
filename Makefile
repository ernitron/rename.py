#
# rename.py
# ernitron (c) 2013
#

GOOD = \e[32;01m
WARN = \e[33;01m
BAD = \e[31;01m
HILITE = \e[36;01m
BRACKET = \e[34;01m
BLUE = \e[1;34m 
NORMAL = $<\e[0m

# Variables
INSTALLDIR=/usr/local/bin/
APPLICATION= rename.py \

check:
	python3.6 -m py_compile *.py
	rm -rf *.pyc __pycache__

run: check
	python $(APPLICATION)

install: check
	sudo install $(APPLICATION) $(INSTALLDIR)

clean:
	rm -f *.pyc

ssh: check		
	for s in localhost server zerver1 zerver2 zerver3 chip1 chip2; \
	do \
	   scp $(APPLICATION) root@$$s:/$(INSTALLDIR)/ ;\
	   echo installed in $$s ;\
	done;

rsync: check		
	for s in $(SERVERS); \
	do \
	   echo -e "$(GOOD)===$$s========= $(NORMAL) \n" ;\
	   rsync -av $(APPLICATION) root@$$s:/$(INSTALLDIR)/ ;\
	done;

revsync:
	rsync -av -n --exclude '*.pid' --exclude '*.pyc'  root@$(SERVER):/$(INSTALLDIR)/$(APPLICATION) .

git:
	git commit -m 'update ${DATE}' -a
	git config --global credential.helper 'cache --timeout=7200'
	git push
