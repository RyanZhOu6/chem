# use sqlalchemy and flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import os
import pandas as pd
import numpy as np

from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP

app = Flask(__name__)
app.secret_key = "Secret Key"


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/chemistry'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
db = SQLAlchemy(app)



# Create database
# database name: filtered
class filtered(db.Model):
    ec_number = db.Column(db.Text)
    uniprot = db.Column(db.Text)
    organism = db.Column(db.Text)
    substrate_kinetics = db.Column(db.Text)
    temperature = db.Column(db.Text)
    clean_mut_wt = db.Column(db.Text)
    kcat_mut = db.Column(db.Text)
    select_key = db.Column(db.String(255), primary_key=True)
    Km_mut = db.Column(db.Text)
    select_key_1 = db.Column(db.Text)
    kcat_wt = db.Column(db.Text)
    Km_wt = db.Column(db.Text)
    PDBID = db.Column(db.Text)
    pdb_as = db.Column(db.Text)
    Mutant = db.Column(db.Text)
    dG_mut = db.Column(db.Text)
    dG_wt = db.Column(db.Numeric)
    ddG = db.Column(db.Numeric)
    Y = db.Column(db.Text)
    wt = db.Column(db.Text)
    mut = db.Column(db.Text)
    wt_aa = db.Column(db.Text)
    mut_aa = db.Column(db.Text)
    compare_key = db.Column(db.Text)
    reaction_kcat = db.Column(db.Text)

    def __init__(self, ec_number, uniprot, organism, substrate_kinetics, temperature, clean_mut_wt, kcat_mut,
                 select_key,
                 Km_mut, select_key_1, kcat_wt, Km_wt, PDBID, pdb_as, Mutant, dG_mut, dG_wt, ddG, Y, wt,
                 mut, wt_aa, mut_aa, compare_key, reaction_kcat):
        self.ec_number = ec_number
        self.uniprot = uniprot
        self.organism = organism
        self.substrate_kinetics = substrate_kinetics
        self.temperature = temperature
        self.clean_mut_wt = clean_mut_wt
        self.kcat_mut = kcat_mut
        self.select_key = select_key
        self.Km_mut = Km_mut
        self.select_key_1 = select_key_1
        self.kcat_wt = kcat_wt
        self.Km_wt = Km_wt
        self.PDBID = PDBID
        self.pdb_as = pdb_as
        self.Mutant = Mutant
        self.dG_mut = dG_mut
        self.dG_wt = dG_wt
        self.ddG = ddG
        self.Y = Y
        self.wt = wt
        self.mut = mut
        self.wt_aa = wt_aa
        self.mut_aa = mut_aa
        self.compare_key = compare_key
        self.reaction_kcat = reaction_kcat




@app.route('/')
def Index():
    all_data = filtered.query.all()
    return render_template("index.html", chem_data = all_data)




# insert data
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        ec_number = request.form['ec_number']
        uniprot = request.form['uniprot']
        organism = request.form['organism']
        substrate_kinetics = request.form['substrate_kinetics']
        temperature = request.form['temperature']
        clean_mut_wt = request.form['clean_mut_wt']
        kcat_mut = request.form['kcat_mut']
        select_key = request.form['select_key']
        Km_mut = request.form['Km_mut']
        select_key_1 = request.form['select_key_1']
        kcat_wt = request.form['kcat_wt']
        Km_wt = request.form['Km_wt']
        PDBID = request.form['PDBID']
        pdb_as = request.form['pdb_as']
        Mutant = request.form['Mutant']
        dG_mut = request.form['dG_mut']
        dG_wt = request.form['dG_wt']
        ddG = request.form['ddG']
        Y = request.form['Y']
        wt = request.form['wt']
        mut = request.form['mut']
        wt_aa = request.form['wt_aa']
        mut_aa = request.form['mut_aa']
        compare_key = request.form['compare_key']
        reaction_kcat = request.form['reaction_kcat']
        my_data = filtered(ec_number, uniprot, organism, substrate_kinetics, temperature, clean_mut_wt, kcat_mut, select_key,
                           Km_mut, select_key_1, kcat_wt, Km_wt, PDBID, pdb_as, Mutant, dG_mut, dG_wt, ddG, Y,
                           wt, mut, wt_aa, mut_aa, compare_key, reaction_kcat)
        db.session.add(my_data)
        db.session.commit()
        flash("Data Inserted Successfully")
        return redirect(url_for('Index'))



# update data
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = filtered.query.get(request.form.get('select_key'))
        my_data.ec_number = request.form['ec_number']
        my_data.uniprot = request.form['uniprot']
        my_data.organism = request.form['organism']
        my_data.substrate_kinetics = request.form['substrate_kinetics']
        my_data.temperature = request.form['temperature']
        my_data.clean_mut_wt = request.form['clean_mut_wt']
        my_data.kcat_mut = request.form['kcat_mut']
        #my_data.select_key = request.form['select_key']
        my_data.Km_mut = request.form['Km_mut']
        my_data.select_key_1 = request.form['select_key_1']
        my_data.kcat_wt = request.form['kcat_wt']
        my_data.Km_wt = request.form['Km_wt']
        my_data.PDBID = request.form['PDBID']
        my_data.pdb_as = request.form['pdb_as']
        my_data.Mutant = request.form['Mutant']
        my_data.dG_mut = request.form['dG_mut']
        my_data.dG_wt = request.form['dG_wt']
        my_data.ddG = request.form['ddG']
        my_data.Y = request.form['Y']
        my_data.wt = request.form['wt']
        my_data.mut = request.form['mut']
        my_data.wt_aa = request.form['wt_aa']
        my_data.mut_aa = request.form['mut_aa']
        my_data.compare_key = request.form['compare_key']
        my_data.reaction_kcat = request.form['reaction_kcat']
        db.session.commit()
        flash("Data Updated Successfully")
        return redirect(url_for('Index'))




# delete data
@app.route('/delete/<select_key>/', methods = ['GET', 'POST'])
def delete(select_key):
    my_data = filtered.query.get(select_key)
    db.session.delete(my_data)
    db.session.commit()
    flash("Data Deleted Successfully")
    return redirect(url_for('Index'))


# search data
@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        search = "%{0}%".format(search_value)
        result = filtered.query.filter(or_(filtered.ec_number.like(search),
                                           filtered.uniprot.like(search),
                                           filtered.organism.like(search),
                                           filtered.substrate_kinetics.like(search),
                                           filtered.temperature.like(search),
                                           filtered.clean_mut_wt.like(search),
                                           filtered.kcat_mut.like(search),
                                           filtered.select_key.like(search),
                                           filtered.Km_mut.like(search),
                                           filtered.select_key_1.like(search),
                                           filtered.kcat_wt.like(search),
                                           filtered.Km_wt.like(search),
                                           filtered.PDBID.like(search),
                                           filtered.pdb_as.like(search),
                                           filtered.Mutant.like(search),
                                           filtered.dG_mut.like(search),
                                           filtered.dG_wt.like(search),
                                           filtered.ddG.like(search),
                                           filtered.Y.like(search),
                                           filtered.wt.like(search),
                                           filtered.mut.like(search),
                                           filtered.wt_aa.like(search),
                                           filtered.mut_aa.like(search),
                                           filtered.compare_key.like(search),
                                           filtered.reaction_kcat.like(search),
                                           )).all()
        return render_template('index.html',chem_data=result)



# calculate the length of the input
@app.route('/length', methods=['POST'])
def length():
    if request.method == 'POST':
        len_series = request.form['len_series']
        lens=len(str(len_series))
        return render_template('index.html',lens=lens)


# upload the csv to database
@app.route("/upload", methods=['POST'])
def upload():

      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)

           uploaded_file.save(file_path)
           parseCSV(file_path)

      return redirect(url_for('Index'))



def parseCSV(filePath):

    col_names = ['ec_number', 'uniprot', 'organism', 'substrate_kinetics', 'temperature',
       'clean_mut_wt', 'kcat_mut', 'select_key', 'Km_mut', 'select_key_1',
       'kcat_wt', 'Km_wt', 'PDBID', 'pdb_as', 'Mutant', 'dG_mut', 'dG_wt',
       'ddG', 'Y', 'wt', 'mut', 'wt_aa', 'mut_aa', 'compare_key',
       'reaction_kcat']

    csvData = pd.read_csv(filePath, names=col_names, header=None)
    # replace none value in database to 0
    csvData.replace(np.nan,0, inplace=True)

    if request.method == 'POST':
        for i, row in csvData.iterrows():
            # save or update function
            # if the primary is already in the database, then delete the primary key and data related to primary key.
            # if not, just upload the data
            if filtered.query.get(row['select_key']):
                my_data = filtered.query.get(row['select_key'])
                db.session.delete(my_data)
                db.session.commit()
                ec_number = row['ec_number']
                uniprot = row['uniprot']
                organism = row['organism']
                substrate_kinetics = row['substrate_kinetics']
                temperature = row['temperature']
                clean_mut_wt = row['clean_mut_wt']
                kcat_mut = row['kcat_mut']
                select_key = row['select_key']
                Km_mut = row['Km_mut']
                select_key_1 = row['select_key_1']
                kcat_wt = row['kcat_wt']
                Km_wt = row['Km_wt']
                PDBID = row['PDBID']
                pdb_as = row['pdb_as']
                Mutant = row['Mutant']
                dG_mut = row['dG_mut']
                dG_wt = row['dG_wt']
                ddG = row['ddG']
                Y = row['Y']
                wt = row['wt']
                mut = row['mut']
                wt_aa = row['wt_aa']
                mut_aa = row['mut_aa']
                compare_key = row['compare_key']
                reaction_kcat = row['reaction_kcat']
                my_data = filtered(ec_number, uniprot, organism, substrate_kinetics, temperature, clean_mut_wt,
                                   kcat_mut,
                                   select_key,
                                   Km_mut, select_key_1, kcat_wt, Km_wt, PDBID, pdb_as, Mutant, dG_mut, dG_wt, ddG, Y,
                                   wt, mut, wt_aa, mut_aa, compare_key, reaction_kcat)
                db.session.add(my_data)
                db.session.commit()
            else:
                ec_number = row['ec_number']
                uniprot = row['uniprot']
                organism = row['organism']
                substrate_kinetics = row['substrate_kinetics']
                temperature = row['temperature']
                clean_mut_wt = row['clean_mut_wt']
                kcat_mut = row['kcat_mut']
                select_key = row['select_key']
                Km_mut = row['Km_mut']
                select_key_1 = row['select_key_1']
                kcat_wt = row['kcat_wt']
                Km_wt = row['Km_wt']
                PDBID = row['PDBID']
                pdb_as = row['pdb_as']
                Mutant = row['Mutant']
                dG_mut = row['dG_mut']
                dG_wt = row['dG_wt']
                ddG = row['ddG']
                Y = row['Y']
                wt = row['wt']
                mut = row['mut']
                wt_aa = row['wt_aa']
                mut_aa = row['mut_aa']
                compare_key = row['compare_key']
                reaction_kcat = row['reaction_kcat']
                my_data = filtered(ec_number, uniprot, organism, substrate_kinetics, temperature, clean_mut_wt,
                                   kcat_mut,
                                   select_key,
                                   Km_mut, select_key_1, kcat_wt, Km_wt, PDBID, pdb_as, Mutant, dG_mut, dG_wt, ddG, Y,
                                   wt, mut, wt_aa, mut_aa, compare_key, reaction_kcat)
                db.session.add(my_data)
                db.session.commit()


        flash("Data Upload Successfully")
        return redirect(url_for('Index'))









# dssp
# p = PDBParser()
# structure = p.get_structure("1MOT", "/local-pdb/1mot.pdb")
# model = structure[0]
# dssp = DSSP(model, "/local-pdb/1mot.pdb")


if __name__ == "__main__":
    app.run()
