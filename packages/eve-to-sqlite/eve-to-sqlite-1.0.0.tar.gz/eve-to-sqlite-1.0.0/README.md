# eve-to-sqlite

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/badboy/eve-to-sqlite/blob/main/LICENSE)

Convert [Eve](https://www.evehome.com/) measurement exports to a SQLite database.

## How to install

    $ pip install eve-to-sqlite

## How to use

First you need to export your Eve data.

1. On your iPhone, open the "Eve" app.
2. Go to the Rooms overview and select your accessory.
3. Go to the details information (the little blue `i` below the overview).
4. Click "Measurements".
5. Click the "Export" button on the top of that page.
4. Save the resulting file somewhere you can access it, or AirDrop it directly to your laptop.

Now you can convert the resulting `Eve_Temperature.xlsx` file (or similar) to SQLite like so:

    $ eve-to-sqlite Eve_Temperature.xlsx eve.db

You can pass multiple Excel files at once.

You can explore the resulting data using [Datasette](https://datasette.readthedocs.io/) like this:

    $ datasette eve.db

## More

* [Dogsheep](https://dogsheep.github.io/) - collection of tools for *personal analytics* using SQLite and Datasette.
