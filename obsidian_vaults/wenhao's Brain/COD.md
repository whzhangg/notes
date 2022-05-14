# Crystallographic open database

Created: October 14, 2021 12:24 PM
Description: using the COD
Tags: Database
Type: API

Obtain the entire database

[ [https://wiki.crystallography.net/howtoobtaincod/](https://wiki.crystallography.net/howtoobtaincod/) ]

for downloading cif files

`rsync -av --delete rsync://www.crystallography.net/cif/ cif/`

COD, TCOD, PCOD

**TCOD**

theoretical COD, where structures are theoretically calculated or refined

[ [http://www.crystallography.net/tcod/](http://www.crystallography.net/tcod/) ]

contains 2906 entry

**PCOD**

predicated crystallography open database by programs

[ [http://www.crystallography.net/pcod/](http://www.crystallography.net/pcod/) ]

**Import COD files**

a sync of the reposity is done to the COD/ folder in external drive on macbook (cannot be done through proxy)

The data is robocopied to `C:/wenhao/COD_database` on office desktop computer

the database contain 71 G of cif files with total 478474 separate structures

To perform a pre-import check, a cif parser PycifRW is used

[ [https://anaconda.org/conda-forge/pycifrw](https://anaconda.org/conda-forge/pycifrw) ] which is able to parse the cif files

`conda install -c conda-forge pycifrw`

**Statistics of filtering COD**

Total number of entries in the database : 478474

Problem parsing : 2053ll

no formula in cif : 501

contain unwanted elements : 415642

non_stoichiometric : 17805

non information on partial occupancies : 7096

contain partial occupancy : 7057

Remain : 24845