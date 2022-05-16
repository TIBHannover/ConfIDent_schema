

CREATE TABLE "AcademicEvent" (
	type VARCHAR(14), 
	doi TEXT, 
	landing_page TEXT, 
	organizers TEXT, 
	academic_fields TEXT, 
	website TEXT, 
	sponsors TEXT, 
	publications TEXT, 
	wikidata_id TEXT, 
	wikicfp_id TEXT, 
	dpbl_id TEXT, 
	gnd_id TEXT, 
	metrics TEXT, 
	context_info TEXT, 
	start_date DATETIME NOT NULL, 
	end_date DATETIME NOT NULL, 
	event_status VARCHAR(12) NOT NULL, 
	in_series TEXT, 
	event_format TEXT, 
	at_location TEXT, 
	ordinal INTEGER, 
	event_mode VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	external_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(in_series) REFERENCES "AcademicEventSeries" (id)
);

CREATE TABLE "AcademicEventSeries" (
	type TEXT, 
	doi TEXT, 
	landing_page TEXT, 
	organizers TEXT, 
	academic_fields TEXT, 
	website TEXT, 
	sponsors TEXT, 
	publications TEXT, 
	wikidata_id TEXT, 
	wikicfp_id TEXT, 
	dpbl_id TEXT, 
	gnd_id TEXT, 
	metrics TEXT, 
	context_info TEXT, 
	series_of TEXT, 
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	external_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(series_of) REFERENCES "AcademicEvent" (id)
);

CREATE TABLE "AcademicField" (
	value TEXT NOT NULL, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (value, schema_name, schema_base_uri)
);

CREATE TABLE "Attendee" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "City" (
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ConfIDentRecords" (
	events TEXT, 
	series TEXT, 
	PRIMARY KEY (events, series)
);

CREATE TABLE "ContactPerson" (
	type TEXT, 
	name TEXT, 
	external_id TEXT, 
	contact TEXT, 
	email TEXT, 
	telephone TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(contact) REFERENCES "ContactPerson" (id)
);

CREATE TABLE "Context" (
	text TEXT, 
	license_str TEXT, 
	license_url TEXT, 
	PRIMARY KEY (text, license_str, license_url)
);

CREATE TABLE "Contributor" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Country" (
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DblpId" (
	value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (value, schema_name, schema_base_uri)
);

CREATE TABLE "DigitalObjectId" (
	value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (value, schema_name, schema_base_uri)
);

CREATE TABLE "EventFormatSpecification" (
	specified_as TEXT NOT NULL, 
	PRIMARY KEY (specified_as)
);

CREATE TABLE "ExternalIdentifier" (
	value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (value, schema_name, schema_base_uri)
);

CREATE TABLE "GndId" (
	value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (value, schema_name, schema_base_uri)
);

CREATE TABLE "KeynoteSpeaker" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Metric" (
	type VARCHAR(21), 
	int_value INTEGER, 
	str_value TEXT, 
	rate_value FLOAT, 
	truth_value BOOLEAN, 
	description TEXT, 
	PRIMARY KEY (type, int_value, str_value, rate_value, truth_value, description)
);

CREATE TABLE "Moderator" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Presenter" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ProcessName" (
	official_name TEXT NOT NULL, 
	acronym TEXT, 
	former_name TEXT, 
	translated_name TEXT, 
	aliases TEXT, 
	PRIMARY KEY (official_name, acronym, former_name, translated_name, aliases)
);

CREATE TABLE "Publication" (
	doi TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Region" (
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Reviewer" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Sponsor" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TibkatId" (
	value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (value, schema_name, schema_base_uri)
);

CREATE TABLE "Venue" (
	street TEXT, 
	zip_code TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "WikiCfpId" (
	value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (value, schema_name, schema_base_uri)
);

CREATE TABLE "WikidataId" (
	value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (value, schema_name, schema_base_uri)
);

CREATE TABLE "CommitteeChair" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	contact TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(contact) REFERENCES "ContactPerson" (id)
);

CREATE TABLE "CommitteeMember" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	contact TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(contact) REFERENCES "ContactPerson" (id)
);

CREATE TABLE "Deadline" (
	type VARCHAR(21) NOT NULL, 
	deadline_date DATETIME NOT NULL, 
	deadline_other TEXT, 
	"AcademicEvent_id" TEXT, 
	PRIMARY KEY (type, deadline_date, deadline_other, "AcademicEvent_id"), 
	FOREIGN KEY("AcademicEvent_id") REFERENCES "AcademicEvent" (id)
);

CREATE TABLE "Location" (
	city TEXT, 
	country TEXT, 
	region TEXT, 
	venue TEXT, 
	lattitude FLOAT, 
	longitude FLOAT, 
	meeting_url TEXT, 
	PRIMARY KEY (city, country, region, venue, lattitude, longitude, meeting_url), 
	FOREIGN KEY(city) REFERENCES "City" (id), 
	FOREIGN KEY(country) REFERENCES "Country" (id), 
	FOREIGN KEY(region) REFERENCES "Region" (id), 
	FOREIGN KEY(venue) REFERENCES "Venue" (id)
);

CREATE TABLE "Organizer" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	contact TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(contact) REFERENCES "ContactPerson" (id)
);

CREATE TABLE "ProcessRelation" (
	type VARCHAR(18), 
	"AcademicEvent_id" TEXT, 
	PRIMARY KEY (type, "AcademicEvent_id"), 
	FOREIGN KEY("AcademicEvent_id") REFERENCES "AcademicEvent" (id)
);

CREATE TABLE "AcademicEvent_topics" (
	backref_id TEXT, 
	topics TEXT, 
	PRIMARY KEY (backref_id, topics), 
	FOREIGN KEY(backref_id) REFERENCES "AcademicEvent" (id)
);

CREATE TABLE "AcademicEventSeries_topics" (
	backref_id TEXT, 
	topics TEXT, 
	PRIMARY KEY (backref_id, topics), 
	FOREIGN KEY(backref_id) REFERENCES "AcademicEventSeries" (id)
);
