

CREATE TABLE "AcademicField" (
	schema_value TEXT NOT NULL, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (schema_value, schema_name, schema_base_uri)
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
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	contact TEXT, 
	email TEXT, 
	telephone TEXT, 
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
	schema_value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (schema_value, schema_name, schema_base_uri)
);

CREATE TABLE "DigitalObjectId" (
	schema_value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (schema_value, schema_name, schema_base_uri)
);

CREATE TABLE "Event" (
	id TEXT NOT NULL, 
	official_name TEXT NOT NULL, 
	organized_by TEXT NOT NULL, 
	start_date DATETIME NOT NULL, 
	end_date DATETIME NOT NULL, 
	event_status VARCHAR(12) NOT NULL, 
	has_acronym TEXT, 
	academic_field TEXT, 
	landing_page TEXT, 
	has_publication TEXT, 
	sponsored_by TEXT, 
	website TEXT, 
	has_doi TEXT, 
	type VARCHAR(14), 
	at_location TEXT, 
	in_series TEXT, 
	former_name TEXT, 
	context_info TEXT, 
	has_metric TEXT, 
	external_id TEXT, 
	wikidata_id TEXT, 
	dpbl_id TEXT, 
	gnd_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(in_series) REFERENCES "EventSeries" (id)
);

CREATE TABLE "EventFormatSpecification" (
	other_format TEXT NOT NULL, 
	PRIMARY KEY (other_format)
);

CREATE TABLE "EventSeries" (
	id TEXT NOT NULL, 
	official_name TEXT NOT NULL, 
	organized_by TEXT NOT NULL, 
	has_acronym TEXT, 
	academic_field TEXT, 
	landing_page TEXT, 
	has_publication TEXT, 
	sponsored_by TEXT, 
	website TEXT, 
	has_doi TEXT, 
	series_of TEXT, 
	former_name TEXT, 
	context_info TEXT, 
	has_metric TEXT, 
	external_id TEXT, 
	wikidata_id TEXT, 
	dpbl_id TEXT, 
	gnd_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(series_of) REFERENCES "Event" (id)
);

CREATE TABLE "ExternalIdentifier" (
	schema_value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (schema_value, schema_name, schema_base_uri)
);

CREATE TABLE "GndId" (
	schema_value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (schema_value, schema_name, schema_base_uri)
);

CREATE TABLE "KeynoteSpeaker" (
	type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Metric" (
	type VARCHAR(22), 
	int_value INTEGER, 
	str_value TEXT, 
	rate_value FLOAT, 
	truth_value BOOLEAN, 
	metric_year TEXT, 
	description TEXT, 
	PRIMARY KEY (type, int_value, str_value, rate_value, truth_value, metric_year, description)
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

CREATE TABLE "Publication" (
	has_doi TEXT, 
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

CREATE TABLE "Venue" (
	street TEXT, 
	zip_code TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	external_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "WikidataId" (
	schema_value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	PRIMARY KEY (schema_value, schema_name, schema_base_uri)
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
	"Event_id" TEXT, 
	PRIMARY KEY (type, deadline_date, deadline_other, "Event_id"), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id)
);

CREATE TABLE "Location" (
	has_city TEXT, 
	has_country TEXT, 
	has_region TEXT, 
	has_venue TEXT, 
	lattitude FLOAT, 
	longitude FLOAT, 
	meeting_url TEXT, 
	PRIMARY KEY (has_city, has_country, has_region, has_venue, lattitude, longitude, meeting_url), 
	FOREIGN KEY(has_city) REFERENCES "City" (id), 
	FOREIGN KEY(has_country) REFERENCES "Country" (id), 
	FOREIGN KEY(has_region) REFERENCES "Region" (id), 
	FOREIGN KEY(has_venue) REFERENCES "Venue" (id)
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
	"Event_id" TEXT, 
	PRIMARY KEY (type, "Event_id"), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id)
);

CREATE TABLE "TibkatId" (
	schema_value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	"Event_id" TEXT, 
	PRIMARY KEY (schema_value, schema_name, schema_base_uri, "Event_id"), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id)
);

CREATE TABLE "WikiCfpEventId" (
	schema_value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	"Event_id" TEXT, 
	PRIMARY KEY (schema_value, schema_name, schema_base_uri, "Event_id"), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id)
);

CREATE TABLE "WikiCfpSeriesId" (
	schema_value TEXT, 
	schema_name TEXT, 
	schema_base_uri TEXT, 
	"EventSeries_id" TEXT, 
	PRIMARY KEY (schema_value, schema_name, schema_base_uri, "EventSeries_id"), 
	FOREIGN KEY("EventSeries_id") REFERENCES "EventSeries" (id)
);

CREATE TABLE "Event_alternative_name" (
	backref_id TEXT, 
	alternative_name TEXT, 
	PRIMARY KEY (backref_id, alternative_name), 
	FOREIGN KEY(backref_id) REFERENCES "Event" (id)
);

CREATE TABLE "Event_translated_name" (
	backref_id TEXT, 
	translated_name TEXT, 
	PRIMARY KEY (backref_id, translated_name), 
	FOREIGN KEY(backref_id) REFERENCES "Event" (id)
);

CREATE TABLE "Event_has_topic" (
	backref_id TEXT, 
	has_topic TEXT, 
	PRIMARY KEY (backref_id, has_topic), 
	FOREIGN KEY(backref_id) REFERENCES "Event" (id)
);

CREATE TABLE "EventSeries_alternative_name" (
	backref_id TEXT, 
	alternative_name TEXT, 
	PRIMARY KEY (backref_id, alternative_name), 
	FOREIGN KEY(backref_id) REFERENCES "EventSeries" (id)
);

CREATE TABLE "EventSeries_translated_name" (
	backref_id TEXT, 
	translated_name TEXT, 
	PRIMARY KEY (backref_id, translated_name), 
	FOREIGN KEY(backref_id) REFERENCES "EventSeries" (id)
);

CREATE TABLE "EventSeries_has_topic" (
	backref_id TEXT, 
	has_topic TEXT, 
	PRIMARY KEY (backref_id, has_topic), 
	FOREIGN KEY(backref_id) REFERENCES "EventSeries" (id)
);
