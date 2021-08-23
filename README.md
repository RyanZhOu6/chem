# chem_backend


# Environment and package
windows10 mysql wamp-server python3.8
flask flask_sqlalchemy sqlalchemy pandas numpy os

# 
app.py is the main python script
html files under the templates

# 
for uploading csv to database, must put the csv files into static/files first.

# 
General functions and restrictions

col_names = ['ec_number', 'uniprot', 'organism', 'substrate_kinetics', 'temperature', 'clean_mut_wt', 'kcat_mut', 'select_key', 'Km_mut', 'select_key_1', 'kcat_wt', 'Km_wt', 'PDBID', 'pdb_as', 'Mutant', 'dG_mut', 'dG_wt', 'ddG', 'Y', 'wt', 'mut', 'wt_aa', 'mut_aa', 'compare_key', 'reaction_kcat']

There's only 25 variables. When upload the csv, please delete the header and you need to make sure the csv's column is same as above. Even if you insert some data with miss values, please make sure the format is the same as above. I replaced nan value with 0.

! The primary could not be updated

app.py
1, insert data function: insert the data manually, should check if the primary key already exist before you insert it.

2, update data function: update the data.

3, delete data function: delete the data.

4, search data function: search the data that matched the keyword.

5, length function: calculate the lens of string.

6, upload and parseCSV function: upload the csv through website instead of mysql. If some data in the csv have same primary key in the database, it will delete the primary key and the data related to primary key first and then update the new one.

