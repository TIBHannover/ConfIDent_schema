## Add your own custom Makefile targets here


# The following target/rule overrides the Makefile 'gendoc' rule on purpose to include custom Jinja templates with the '--template-directory' flag. This will lead to a warning in the stout.
gendoc: $(DOCDIR)
	cp $(SRC)/docs/*md $(DOCDIR) ; \
	$(RUN) gen-doc -d $(DOCDIR) $(SOURCE_SCHEMA_PATH) \
	--template-directory $(SRC)/docs/jinja_templates