# Installation
pip install [dict-fr-ABU](https://pypi.org/project/dict-fr-ABU/)

# French dictionaries from Association des Bibliophiles Universels (ABU)

## DESCRIPTION
This package contains several dictionaries processed from [those made available](http://abu.cnam.fr/DICO/) by the [Association des Bibliophiles Universels (ABU)](http://abu.cnam.fr/) organization before 2003.

## FILES
All files are installed in Python's */usr/local* equivalent, under *share/dict*.

### Original files

Filename|Description
---|---
dict-fr-ABU-cites|39.076 French cities list (accented, with compound words), along with postal zip code
dict-fr-ABU-Header-cites|French cities list (mandatory header)
dict-fr-ABU-dicorth|1.500 French orthographical difficulties by decreasing frequency (with compound words)
dict-fr-ABU-Header-dicorth|French orthographical difficulties (mandatory header)
dict-fr-ABU-mots_communs|255.282 French common words (including female and plural forms, as well as conjugated verbs), along with singular / unconjugated form, and type 
dict-fr-ABU-pays|170 countries and regions (with compound words)
dict-fr-ABU-Header-pays|Countries and regions (mandatory header)
dict-fr-ABU-prenoms|12.437 firstnames (unaccented)
dict-fr-ABU-Header-prenoms|Firstnames (mandatory header)
dict-fr-ABU-License|ABU 1.1 License

### Generated files

Filename|Description
---|---
dict-fr-ABU-cites.ascii|French cities list (unaccented)
dict-fr-ABU-cites.unicode|French cities list (accented)
dict-fr-ABU-cites.combined|French cities list (with both accented and unaccented words)
dict-fr-ABU-mots_communs.ascii|French common words (unaccented)
dict-fr-ABU-mots_communs.combined|French common words (accented)
dict-fr-ABU-mots_communs.unicode|French common words (with both accented and unaccented words)
dict-fr-ABU-pays.ascii|Countries and regions (unaccented)
dict-fr-ABU-pays.combined|Countries and regions (accented)
dict-fr-ABU-pays.unicode|Countries and regions (with both accented and unaccented words)
dict-fr-ABU-prenoms.ascii|Firstnames (unaccented)

These generated files went through the following transformations:
* extraction of the headers in the *dict-fr-header-\** files above
* conversion from ISO-Latin-1 to UTF-8
* sort
* removal of duplicates
* removal of lemma and grammatical info from dict-fr-ABU-mots_communs
* removal of the zip codes from dict-fr-ABU-cites
* lossless conversion of accents for the *\*-ascii* versions
* combination of the *\*-ascii* and *\*-unicode* versions into the *\*-combined* ones (without duplicates)

## SEE ALSO
[spell(1)](https://www.freebsd.org/cgi/man.cgi?query=spell) like tools,
[anagram(6)](https://github.com/HubTou/anagram/blob/main/README.md)

## HISTORY
These data files were originally intended to be used with the [PNU project](https://github.com/HubTou/PNU)'s
[anagram](https://github.com/HubTou/anagram) command, as well as many other text processing tools.

I wrote an [history of Unix & French dictionaries](https://github.com/HubTou/PNU/wiki/Les-dictionnaires-sous-Unix) (in French only),
which covers this dictionary and many others.

## LICENSE
The original contents, as well as this package, are licensed under the [ABU 1.1 license](http://abu.cnam.fr/cgi-bin/donner_licence).

Some source files had mandatory headers that were kept under *data/dict-fr-ABU-Header-\** rather than in the files themselves, in order to ease direct processing with other tools.

## AUTHORS
[Association des Bibliophiles Universels (ABU)](http://abu.cnam.fr/INFO/) for the original contents.

[Hubert Tournier](https://github.com/HubTou) for the package.

