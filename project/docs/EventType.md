
# Enum: EventType


The most common minimal event types. For event types that are not in this list, you can use "other" and provide the label of this other event format using the [Event Format](event_format.md) property.

URI: [confident:EventType](https://raw.githubusercontent.com/TIBHannover/ConfIDent_schema/main/src/linkml/confident_schema.yaml#EventType)


## Other properties

|  |  |  |
| --- | --- | --- |

## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| Colloquium | A colloquium is an academic meeting that usually lasts only a few hours and serves to discuss a specific topic. Colloquia are usually part of the academic exchange in everyday university life with only one speaker, but can also take place on special occasions (anniversaries, start or end of the lecture phase, etc.) and can have more than one speaker. | aeon:0000101 | {'title': 'Colloquium'} |
| Conference | A conference is an academic event that lasts up to several days and serves as a forum for presentations on a specific topic or subject area. In addition to subject-specific conferences, there are also interdisciplinary conferences which allow both a broader focus and more specific questions on a particular (academic) problem. Conferences often have a highly formalized structure of parallel, clearly defined sessions with several short presentations and plenary sessions with invited (keynote) speakers who are considered multipliers in their (research) field. Ideally, the selection of the speakers and their contributions is subject to a review process. | aeon:0000103 |  |
| Congress | A congress is a certain type of conference which is characterised by a larger number of participants (often several hundred) and is oftentimes organised jointly by large, established (e.g. specialised societies) and/or several institutions. Congresses have a broader thematic focus than simple conferences, take place in certain cycles, but can still target an exclusive group of participants (e.g. representatives of a single discipline). | aeon:0000123 |  |
| Session | A session is a clearly defined part of a academic event in which a small number of speakers (usually 2-5) focus on a specific topic. A session is usually formally accompanied by a session chair, who assumes the function of a moderator. | aeon:0000111 |  |
| Poster Session | A poster session is a session at which poster papers are presented. | aeon:0000127 |  |
| Talk | A talk is a central part of a larger academic event, at which a specific topic is being presented in a rather short way. | aeon:0000125 |  |
| Keynote Speech | A keynote speech is a special talk that has the function to set the underlying tone and summarize the core message or most important revelation of the academic event at which it is given. | aeon:00001115 |  |
| Event Track | An academic event that, as a part of a larger academic event, has the function to group even smaller parts of the academic event, like sessions and talks, according to a shared theme or topic. It usually has dedicated chairs and program committees. | aeon:00001117 |  |
| Forum | An academic event whose sociocultural format is determined in an academic event type specification that classifies the academic event as a forum. | aeon:0000105 |  |
| Hackathon | A hackathon is a gathering of software developers with the goal to develop software collaboratively in a short timeframe. | aeon:0000107 |  |
| Seminar | A seminar can serve as a term for older conference series, but in current usage the term mainly describes a specific teaching format that serves to develop content and provides space for discussion. Participation from the audience is usually encouraged. | aeon:0000109 |  |
| Symposium | A symposium is a specific type of conference with a narrower thematic focus, with fewer participants and of shorter duration. The degree of structuring lies between a classic conference and a workshop, allows more discussion than the larger conference, but is usually more formalized than the workshop. | aeon:0000113 |  |
| Tutorial | An academic event that has the function to educate the audience on a certain topic. A tutorial is often realized as an academic event talk or academic event session. | aeon:0000119 |  |
| Workshop | Workshops are smaller academic events that serve to exchange information on a specific topic or problem. They usually last one or two days and offer space for discussion and the development of content and solutions. Group work is often part of the event concept. | aeon:0000121 |  |
| other | This value is to be used if the event format cannot be represented using one of the other permissible values defined in the [Event Type](EventType.md) enum. If this value is chosen the use of [Other Event Format](other_format.md) is mandatory. | aeon:0000001 |  |

