
Checklist for a Backend Project
===============================

Here is a list of things you may want to keep in mind when starting a project that involves a Python backend.
I wrote much of it following the tracks of the [12 Factor App](https://12factor.net/) paradigm:

Project Communication
---------------------

- What is the business value the project generates?
- Who is on the project team?
- How does the team communicate (face2face, chat, email, calendar, file exchange, Wiki, JIRA)?
- Does the team work in iterations? How long are they?
- Is there a requirements document? Is it updated?
- Is there a single git repository available?

Architecture
------------

- What are your main use cases?
- What is your data flow?
- Do you have a pattern for the systems overall architecture (layered, star-shaped, hexagonal etc.)
- How many separate physical machines does the project require?
- Does a prototype exist?
- What are your most important non-functional requirements?
- What legal requlations do you need to comply to (GDPR etc.)
- Are you using containers?
- Do you need enough containers to justify Kubernetes?
- welche Container gibt es?
- How does the release/deployment process look like?
- Will there be separate test/staging servers?
- What special security / safety risks exist?

Credentials
-----------

- How is authentication managed? 
- What roles are defined in the project?
- Do end users need to authenticate?
- Which protocols for authentication do you need (SSL, OAUTH2, two-factor-auth, Kerberos etc.)
- Is there a central authentication service?
- Within services, are credentials stored mainly in the environment?
- What is the procedure when a team member leaves?
- What is the procedure when you learn that your credentials have been compromised?

Databases
---------

- How much data are you expecting (now and in the future)?
- How much traffic are you expecting?
- Is there a data model already?
- Which database system(s) do you choose? Consider: ease of use, rigor of the data model, core features, tool support, scalability, speed.
- How will you migrate the data when the data model changes?
- What data import processes do you anticipate?
- Will it be possible to re-create the entire database from scratch?
- How are backups of the database handled?

Web Servers
-----------

- What availability do you need?
- Does the project expose an API?
- Is the API going to be public?
- Will there be a HTML front-end?
- Will there be a mobile app?
- Will there be a proxy server (e.g. nginx)?
- Will the backend use an ORM?
- Will you use pydantic models for API endpoints?
- How will you manage requirements?
- Which language(s) will you use for the back-end/front-end parts?
- How will you manage versions of the software (front-end and back-end)?

Software Quality
----------------

- How will you write automated tests for the backend?
- How will you write automated tests for the front-end?
- How will you write end-to-end tests covering both parts?
- Can you run slim tests against the production server?
- Which CI tool are you going to use?
- What software quality gates will you apply (pyflakes, mypy)?
- Can you autmatically check for known security issues?
- How is logging done? How can you access logs?
- How is monitoring done (who is messaged when something goes wrong)?
- do you have test users?
