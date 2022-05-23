## Add your own custom Makefile targets here

gendoc: $(DOCDIR)
	cp $(SRC)/docs/*md $(DOCDIR) ; \
	$(RUN) gen-doc -d $(DOCDIR) $(SOURCE_SCHEMA_PATH) \
	--template-directory $(SRC)/docs/jinja_templates