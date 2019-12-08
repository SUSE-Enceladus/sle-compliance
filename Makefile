DESTDIR=
NAME=slecompliance
dirs = man usr
files = LICENSE

verSpec = $(shell rpm -q --specfile --qf '%{VERSION}' *.spec)

tar:
	rm -rf $(NAME)-$(verSpec)
	mkdir $(NAME)-$(verSpec)
	cp -r $(dirs) $(files) "$(NAME)-$(verSpec)"
	tar -cjf "$(NAME)-$(verSpec).tar.bz2" "$(NAME)-$(verSpec)"
	rm -rf "$(NAME)-$(verSpec)"
