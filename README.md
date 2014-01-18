Delpher to Amcat Transferrer
============================

Transfer newspaper articles from Delpher API to Amcat API

What does it do?
----------------

Given search arguments this builds a search query and loads articles from the Delpher API (http://kranten.delpher.nl/nl/api/) of the Koninklijke Bibliotheek (Dutch National Library). These articles are converted and uploaded to Amcat (Vrije Universiteit Amsterdam, http://amcat.vu.nl/api/v4/). The scope of the program is limited to a particular use case but can be easily extended.

How to execute
--------------
1. Adapt `run.py` and files in `settings/` to change the query.
2. Set your Amcat username and password as environment variables: 

        $ export AMCAT_USERNAME=your_username
        $ export AMCAT_PASSWORD=your_password

3. Execute `run.py`:

        `$ python run.py`

Setup
-----

`DelpherToAmcat` takes the start and the end time of the period to search in as parameters. This is to allow splitting transfers to several threads.

All other preferences to the search can be set in `settings/delpher.py`. 

* `ppn` is the identifier of the newspaper in  the Delpher database.
* `ocr_base_url` is the location from where full texts of the articles are loaded.
* `query_template` is the query to get search results. Variables in this query can only be changed by passing different parameters to the constructor of `DelpherAPI`.

Preferences regarding the upload to Amcat can be changed in `settings/amcat.py`. 
* `host` is the base address of the Amcat API. Change this if you want to upload to the development server.
* `username` and `password` are read from the environment (see "How to execute").
* `project` is the id of the project you want to upload to. Create this project using Amcat's web interface.
* `data_provenance` is a field of a set.
* `set_name_template` is the template for the name of the sets.
