DROP DATABASE IF EXISTS chemistry;
CREATE DATABASE chemistry;

USE chemistry;

DROP TABLE IF EXISTS filtered;
CREATE TABLE filtered(
ec_number  TEXT, 
uniprot TEXT,
organism TEXT, 
substrate_kinetics TEXT, 
temperature TEXT,
clean_mut_wt TEXT, 
kcat_mut TEXT, 
select_key CHAR(255), 
Km_mut TEXT, 
select_key_1 TEXT,
kcat_wt TEXT, 
Km_wt TEXT, 
PDBID TEXT, 
pdb_as TEXT, 
Mutant TEXT, 
dG_mut DOUBLE, 
dG_wt DOUBLE,
ddG DOUBLE, 
Y TEXT, 
wt TEXT, 
mut TEXT, 
wt_aa TEXT, 
mut_aa TEXT, 
compare_key TEXT,
reaction_kcat TEXT,
PRIMARY KEY (select_key)
)ENGINE = INNODB;



LOAD DATA INFILE 'c:\\wamp64\\tmp\\kcat_km_str_clean_filtered.csv' 
INTO TABLE filtered
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

