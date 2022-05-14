# Crystallographic open database

### Obtain the Database
The entire database if open, to obtain the entire database, see: https://wiki.crystallography.net/howtoobtaincod/

For example, to download all cif files
```bash
rsync -av --delete rsync://www.crystallography.net/cif/ cif/
```

### The Three database
##### TCOD
Theoretical COD, where structures are theoretically calculated or refined. It contains 2906 entries. See: http://www.crystallography.net/tcod/

##### PCOD
Predicated crystallography open database by programs http://www.crystallography.net/pcod/

### Import COD files 
This part described what I did when I downloaded the COD database and import it to Python. 
Process:
- A sync of the reposity is done to the COD/ folder in external drive on macbook (cannot be done through proxy)
- The data is robocopied to `C:/wenhao/COD_database` on office desktop computer
- The database contain 71 G of cif files with total 478474 separate structures
- To perform a pre-import check, a cif parser [PycifRW](https://anaconda.org/conda-forge/pycifrw) is used, which is able to parse the cif files.