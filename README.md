# Graff

> An ~~Minimal~~ Overkill HTML only blog posts previews generator.

## Setup

`pip install pygraff` to install

look at `settings.toml` for example config

Set the `GRAFF_CONF` environment to the location of graff config. 

## Usage

`graff -n <Page name>` to create new blog page in posts_dir.

`graff -g` to generate previews.

## What needs to be done

* ~~Add `<a>` tag to the title of the previews that links to the article~~
* ~~`groff.py`: file where it calls the functions from `settings.py` and `generator.py`~~
* Error handling : ~~missing or wrong values from the settings.toml file should return an error message warranting the user and not starting generation so we need a checker in `settings.py` and also in `generator.py` in case the class of the blog previews doesn't exist or~~ the file isn't even html.
* ~~add creating new blog posts with command `new` and with chosen template~~
