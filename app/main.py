import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from fpdf import FPDF
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image
import base64
import tempfile
from datetime import datetime, date

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Télécharger le Compte-Rendu</a>'
        

st.set_page_config(layout="wide")

# Titre de l'application
st.header('Suivi Tension Artérielle', divider=True)


data = [{"Jour": 'Jour 1 Matin', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 1 Soir', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 2 Matin', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 2 Soir', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 3 Matin', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 3 Soir', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 4 Matin', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 4 Soir', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 5 Matin', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 5 Soir', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 6 Matin', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 6 Soir', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 7 Matin', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None},
            {"Jour": 'Jour 7 Soir', "M1 SYS": None, "M1 DIA": None, "M2 SYS": None, "M2 DIA": None, "M3 SYS": None, "M3 DIA": None}]

data_df = pd.DataFrame(data)

with st.form('input_form'):
    st.write("Veuillez remplir les informations suivantes ainsi que les valeurs de tension artérielle")
    with st.expander("Informations du patient"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom") 
        age = st.number_input("Age", value=None, step=1, min_value=0, max_value=120)
        sexe = st.radio("Sexe", ["Homme", "Femme"])
        poids = st.number_input("Poids", value=None, step=1, min_value=30, max_value=300, placeholder="Poids en kg")
        taille = st.number_input("Taille", value=None, step=1, min_value=100, max_value=300, placeholder="Taille en cm")   
        traitement = st.text_area("Traitement pour la tension arterielle", value='', height=None, max_chars=None, key=None, help="Laisser vide si aucun traitement", placeholder='Uniquement les traitements pour la tension artérielle. Laisser vide si aucun traitement.')
    with st.expander("Mesures de tension artérielle"):
        with st.container(height=550, border=False):
            edited_df = st.data_editor(data_df, width=800, height=525,
                                        num_rows="fixed", 
                                        column_config={
                                        "Jour": st.column_config.Column(disabled=True),
                                        "M1 SYS": st.column_config.NumberColumn(
                                                help="Valeur de la première mesure de la tension artérielle systolique",
                                                min_value=60,
                                                max_value=300,
                                                step=1,
                                                default=None),
                                        "M1 DIA": st.column_config.NumberColumn(
                                                help="Valeur de la première mesure de la tension artérielle diastolique",
                                                min_value=40,
                                                max_value=140,
                                                step=1,
                                                default=None), 
                                        "M2 SYS": st.column_config.NumberColumn(
                                                help="Valeur de la deuxième mesure de la tension artérielle systolique",
                                                min_value=60,
                                                max_value=300,
                                                step=1,
                                                default=None), 
                                        "M2 DIA": st.column_config.NumberColumn(
                                                help="Valeur de la deuxième mesure de la tension artérielle diastolique",
                                                min_value=40,
                                                max_value=140,
                                                step=1,
                                                default=None), 
                                        "M3 SYS": st.column_config.NumberColumn(
                                                help="Valeur de la troisième mesure de la tension artérielle systolique",
                                                min_value=60,
                                                max_value=300,
                                                step=1,
                                                default=None), 
                                            "M3 DIA": st.column_config.NumberColumn(
                                                help="Valeur de la troisième mesure de la tension artérielle diastolique",
                                                min_value=40,
                                                max_value=140,
                                                step=1,
                                                default=None)},
                                        hide_index=True)
            #st.markdown(''' SYS : Systole ; DIA : Diastole  
                            #M1 : Mesure 1 ; M2 : Mesure 2 ; M3 : Mesure 3 hdsjb''')
    submitted = st.form_submit_button("Soumettre le formulaire")
    
    if submitted:
        #calcul des moyennes
        #Moyenne systole jour 1
        if edited_df.loc[0, 'Mesure 1 Systole'] != None and edited_df.loc[0, 'Mesure 2 Systole'] != None and edited_df.loc[0, 'Mesure 3 Systole'] != None and edited_df.loc[1, 'Mesure 1 Systole'] != None and edited_df.loc[1, 'Mesure 2 Systole'] != None and edited_df.loc[1, 'Mesure 3 Systole'] != None:
            moyenne_systole_jour_1 = (edited_df.loc[0, 'Mesure 1 Systole'] + edited_df.loc[0, 'Mesure 2 Systole'] + edited_df.loc[0, 'Mesure 3 Systole'] + edited_df.loc[1, 'Mesure 1 Systole'] + edited_df.loc[1, 'Mesure 2 Systole'] + edited_df.loc[1, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_1_sans_premiere_mesure = (edited_df.loc[0, 'Mesure 2 Systole'] + edited_df.loc[0, 'Mesure 3 Systole'] + edited_df.loc[1, 'Mesure 2 Systole'] + edited_df.loc[1, 'Mesure 3 Systole']) / 4
            moyenne_systole_jour_1_matin = (edited_df.loc[0, 'Mesure 1 Systole'] + edited_df.loc[0, 'Mesure 2 Systole'] + edited_df.loc[0, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_1_soir = (edited_df.loc[1, 'Mesure 1 Systole'] + edited_df.loc[1, 'Mesure 2 Systole'] + edited_df.loc[1, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_1_sans_premiere_mesure_matin = (edited_df.loc[0, 'Mesure 2 Systole'] + edited_df.loc[0, 'Mesure 3 Systole']) / 2
            moyenne_systole_jour_1_sans_premiere_mesure_soir = (edited_df.loc[1, 'Mesure 2 Systole'] + edited_df.loc[1, 'Mesure 3 Systole']) / 2
        else :
            moyenne_systole_jour_1 = 0
            moyenne_systole_jour_1_sans_premiere_mesure = 0
            moyenne_systole_jour_1_matin = 0
            moyenne_systole_jour_1_soir = 0
            moyenne_systole_jour_1_sans_premiere_mesure_matin = 0
            moyenne_systole_jour_1_sans_premiere_mesure_soir = 0
            
        #Moyenne diastole jour 1
        if edited_df.loc[0, 'Mesure 1 Diastole'] != None and edited_df.loc[0, 'Mesure 2 Diastole'] != None and edited_df.loc[0, 'Mesure 3 Diastole'] != None and edited_df.loc[1, 'Mesure 1 Diastole'] != None and edited_df.loc[1, 'Mesure 2 Diastole'] != None and edited_df.loc[1, 'Mesure 3 Diastole'] != None:
            moyenne_diastole_jour_1 = (edited_df.loc[0, 'Mesure 1 Diastole'] + edited_df.loc[0, 'Mesure 2 Diastole'] + edited_df.loc[0, 'Mesure 3 Diastole'] + edited_df.loc[1, 'Mesure 1 Diastole'] + edited_df.loc[1, 'Mesure 2 Diastole'] + edited_df.loc[1, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_1_sans_premiere_mesure = (edited_df.loc[0, 'Mesure 2 Diastole'] + edited_df.loc[0, 'Mesure 3 Diastole'] + edited_df.loc[1, 'Mesure 2 Diastole'] + edited_df.loc[1, 'Mesure 3 Diastole']) / 4
            moyenne_diastole_jour_1_matin = (edited_df.loc[0, 'Mesure 1 Diastole'] + edited_df.loc[0, 'Mesure 2 Diastole'] + edited_df.loc[0, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_1_soir = (edited_df.loc[1, 'Mesure 1 Diastole'] + edited_df.loc[1, 'Mesure 2 Diastole'] + edited_df.loc[1, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_1_sans_premiere_mesure_matin = (edited_df.loc[0, 'Mesure 2 Diastole'] + edited_df.loc[0, 'Mesure 3 Diastole']) / 2
            moyenne_diastole_jour_1_sans_premiere_mesure_soir = (edited_df.loc[1, 'Mesure 2 Diastole'] + edited_df.loc[1, 'Mesure 3 Diastole']) / 2
        
        else :
            moyenne_diastole_jour_1 = 0
            moyenne_diastole_jour_1_sans_premiere_mesure = 0
            moyenne_diastole_jour_1_matin = 0
            moyenne_diastole_jour_1_soir = 0
            moyenne_diastole_jour_1_sans_premiere_mesure_matin = 0
            moyenne_diastole_jour_1_sans_premiere_mesure_soir = 0
            
        
        #Moyenne systole jour 2
        if edited_df.loc[2, 'Mesure 1 Systole'] != None and edited_df.loc[2, 'Mesure 2 Systole'] != None and edited_df.loc[2, 'Mesure 3 Systole'] != None and edited_df.loc[3, 'Mesure 1 Systole'] != None and edited_df.loc[3, 'Mesure 2 Systole'] != None and edited_df.loc[3, 'Mesure 3 Systole'] != None:
            moyenne_systole_jour_2 = (edited_df.loc[2, 'Mesure 1 Systole'] + edited_df.loc[2, 'Mesure 2 Systole'] + edited_df.loc[2, 'Mesure 3 Systole'] + edited_df.loc[3, 'Mesure 1 Systole'] + edited_df.loc[3, 'Mesure 2 Systole'] + edited_df.loc[3, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_2_sans_premiere_mesure = (edited_df.loc[2, 'Mesure 2 Systole'] + edited_df.loc[2, 'Mesure 3 Systole'] + edited_df.loc[3, 'Mesure 2 Systole'] + edited_df.loc[3, 'Mesure 3 Systole']) / 4
            moyenne_systole_jour_2_matin = (edited_df.loc[2, 'Mesure 1 Systole'] + edited_df.loc[2, 'Mesure 2 Systole'] + edited_df.loc[2, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_2_soir = (edited_df.loc[3, 'Mesure 1 Systole'] + edited_df.loc[3, 'Mesure 2 Systole'] + edited_df.loc[3, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_2_sans_premiere_mesure_matin = (edited_df.loc[2, 'Mesure 2 Systole'] + edited_df.loc[2, 'Mesure 3 Systole']) / 2
            moyenne_systole_jour_2_sans_premiere_mesure_soir = (edited_df.loc[3, 'Mesure 2 Systole'] + edited_df.loc[3, 'Mesure 3 Systole']) / 2
        else :
            moyenne_systole_jour_2 = 0
            moyenne_systole_jour_2_sans_premiere_mesure = 0
            moyenne_systole_jour_2_matin = 0
            moyenne_systole_jour_2_soir = 0
            moyenne_systole_jour_2_sans_premiere_mesure_matin = 0
            moyenne_systole_jour_2_sans_premiere_mesure_soir = 0
        #Moyenne diastole jour 2
        if edited_df.loc[2, 'Mesure 1 Diastole'] != None and edited_df.loc[2, 'Mesure 2 Diastole'] != None and edited_df.loc[2, 'Mesure 3 Diastole'] != None and edited_df.loc[3, 'Mesure 1 Diastole'] != None and edited_df.loc[3, 'Mesure 2 Diastole'] != None and edited_df.loc[3, 'Mesure 3 Diastole'] != None:
            moyenne_diastole_jour_2 = (edited_df.loc[2, 'Mesure 1 Diastole'] + edited_df.loc[2, 'Mesure 2 Diastole'] + edited_df.loc[2, 'Mesure 3 Diastole'] + edited_df.loc[3, 'Mesure 1 Diastole'] + edited_df.loc[3, 'Mesure 2 Diastole'] + edited_df.loc[3, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_2_sans_premiere_mesure = (edited_df.loc[2, 'Mesure 2 Diastole'] + edited_df.loc[2, 'Mesure 3 Diastole'] + edited_df.loc[3, 'Mesure 2 Diastole'] + edited_df.loc[3, 'Mesure 3 Diastole']) / 4
            moyenne_diastole_jour_2_matin = (edited_df.loc[2, 'Mesure 1 Diastole'] + edited_df.loc[2, 'Mesure 2 Diastole'] + edited_df.loc[2, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_2_soir = (edited_df.loc[3, 'Mesure 1 Diastole'] + edited_df.loc[3, 'Mesure 2 Diastole'] + edited_df.loc[3, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_2_sans_premiere_mesure_matin = (edited_df.loc[2, 'Mesure 2 Diastole'] + edited_df.loc[2, 'Mesure 3 Diastole']) / 2
            moyenne_diastole_jour_2_sans_premiere_mesure_soir = (edited_df.loc[3, 'Mesure 2 Diastole'] + edited_df.loc[3, 'Mesure 3 Diastole']) / 2
        else :
            moyenne_diastole_jour_2 = 0
            moyenne_diastole_jour_2_sans_premiere_mesure = 0
            moyenne_diastole_jour_2_matin = 0
            moyenne_diastole_jour_2_soir = 0
            moyenne_diastole_jour_2_sans_premiere_mesure_matin = 0
            moyenne_diastole_jour_2_sans_premiere_mesure_soir = 0
        #Moyenne systole jour 3
        if edited_df.loc[4, 'Mesure 1 Systole'] != None and edited_df.loc[4, 'Mesure 2 Systole'] != None and edited_df.loc[4, 'Mesure 3 Systole'] != None and edited_df.loc[5, 'Mesure 1 Systole'] != None and edited_df.loc[5, 'Mesure 2 Systole'] != None and edited_df.loc[5, 'Mesure 3 Systole'] != None:
            moyenne_systole_jour_3 = (edited_df.loc[4, 'Mesure 1 Systole'] + edited_df.loc[4, 'Mesure 2 Systole'] + edited_df.loc[4, 'Mesure 3 Systole'] + edited_df.loc[5, 'Mesure 1 Systole'] + edited_df.loc[5, 'Mesure 2 Systole'] + edited_df.loc[5, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_3_sans_premiere_mesure = (edited_df.loc[4, 'Mesure 2 Systole'] + edited_df.loc[4, 'Mesure 3 Systole'] + edited_df.loc[5, 'Mesure 2 Systole'] + edited_df.loc[5, 'Mesure 3 Systole']) / 4
            moyenne_systole_jour_3_matin = (edited_df.loc[4, 'Mesure 1 Systole'] + edited_df.loc[4, 'Mesure 2 Systole'] + edited_df.loc[4, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_3_soir = (edited_df.loc[5, 'Mesure 1 Systole'] + edited_df.loc[5, 'Mesure 2 Systole'] + edited_df.loc[5, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_3_sans_premiere_mesure_matin = (edited_df.loc[4, 'Mesure 2 Systole'] + edited_df.loc[4, 'Mesure 3 Systole']) / 2
            moyenne_systole_jour_3_sans_premiere_mesure_soir = (edited_df.loc[5, 'Mesure 2 Systole'] + edited_df.loc[5, 'Mesure 3 Systole']) / 2
        else :
            moyenne_systole_jour_3 = 0
            moyenne_systole_jour_3_sans_premiere_mesure = 0
            moyenne_systole_jour_3_matin = 0
            moyenne_systole_jour_3_soir = 0
            moyenne_systole_jour_3_sans_premiere_mesure_matin = 0
            moyenne_systole_jour_3_sans_premiere_mesure_soir = 0
        
        #Moyenne diastole jour 3
        if edited_df.loc[4, 'Mesure 1 Diastole'] != None and edited_df.loc[4, 'Mesure 2 Diastole'] != None and edited_df.loc[4, 'Mesure 3 Diastole'] != None and edited_df.loc[5, 'Mesure 1 Diastole'] != None and edited_df.loc[5, 'Mesure 2 Diastole'] != None and edited_df.loc[5, 'Mesure 3 Diastole'] != None:
            moyenne_diastole_jour_3 = (edited_df.loc[4, 'Mesure 1 Diastole'] + edited_df.loc[4, 'Mesure 2 Diastole'] + edited_df.loc[4, 'Mesure 3 Diastole'] + edited_df.loc[5, 'Mesure 1 Diastole'] + edited_df.loc[5, 'Mesure 2 Diastole'] + edited_df.loc[5, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_3_sans_premiere_mesure = (edited_df.loc[4, 'Mesure 2 Diastole'] + edited_df.loc[4, 'Mesure 3 Diastole'] + edited_df.loc[5, 'Mesure 2 Diastole'] + edited_df.loc[5, 'Mesure 3 Diastole']) / 4
            moyenne_diastole_jour_3_matin = (edited_df.loc[4, 'Mesure 1 Diastole'] + edited_df.loc[4, 'Mesure 2 Diastole'] + edited_df.loc[4, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_3_soir = (edited_df.loc[5, 'Mesure 1 Diastole'] + edited_df.loc[5, 'Mesure 2 Diastole'] + edited_df.loc[5, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_3_sans_premiere_mesure_matin = (edited_df.loc[4, 'Mesure 2 Diastole'] + edited_df.loc[4, 'Mesure 3 Diastole']) / 2
            moyenne_diastole_jour_3_sans_premiere_mesure_soir = (edited_df.loc[5, 'Mesure 2 Diastole'] + edited_df.loc[5, 'Mesure 3 Diastole']) / 2
            
        else :
            moyenne_diastole_jour_3 = 0
            moyenne_diastole_jour_3_sans_premiere_mesure = 0
            moyenne_diastole_jour_3_matin = 0
            moyenne_diastole_jour_3_soir = 0
            moyenne_diastole_jour_3_sans_premiere_mesure_matin = 0
            moyenne_diastole_jour_3_sans_premiere_mesure_soir = 0
        
        #Moyenne systole jour 4
        if edited_df.loc[6, 'Mesure 1 Systole'] != None and edited_df.loc[6, 'Mesure 2 Systole'] != None and edited_df.loc[6, 'Mesure 3 Systole'] != None and edited_df.loc[7, 'Mesure 1 Systole'] != None and edited_df.loc[7, 'Mesure 2 Systole'] != None and edited_df.loc[7, 'Mesure 3 Systole'] != None:
            moyenne_systole_jour_4 = (edited_df.loc[6, 'Mesure 1 Systole'] + edited_df.loc[6, 'Mesure 2 Systole'] + edited_df.loc[6, 'Mesure 3 Systole'] + edited_df.loc[7, 'Mesure 1 Systole'] + edited_df.loc[7, 'Mesure 2 Systole'] + edited_df.loc[7, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_4_sans_premiere_mesure = (edited_df.loc[6, 'Mesure 2 Systole'] + edited_df.loc[6, 'Mesure 3 Systole'] + edited_df.loc[7, 'Mesure 2 Systole'] + edited_df.loc[7, 'Mesure 3 Systole']) / 4
            moyenne_systole_jour_4_matin = (edited_df.loc[6, 'Mesure 1 Systole'] + edited_df.loc[6, 'Mesure 2 Systole'] + edited_df.loc[6, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_4_soir = (edited_df.loc[7, 'Mesure 1 Systole'] + edited_df.loc[7, 'Mesure 2 Systole'] + edited_df.loc[7, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_4_sans_premiere_mesure_matin = (edited_df.loc[6, 'Mesure 2 Systole'] + edited_df.loc[6, 'Mesure 3 Systole']) / 2
            moyenne_systole_jour_4_sans_premiere_mesure_soir = (edited_df.loc[7, 'Mesure 2 Systole'] + edited_df.loc[7, 'Mesure 3 Systole']) / 2
        else :
            moyenne_systole_jour_4 = 0
            moyenne_systole_jour_4_sans_premiere_mesure = 0
            moyenne_systole_jour_4_matin = 0
            moyenne_systole_jour_4_soir = 0
            moyenne_systole_jour_4_sans_premiere_mesure_matin = 0
            moyenne_systole_jour_4_sans_premiere_mesure_soir = 0
            
        #Moyenne diastole jour 4
        if edited_df.loc[6, 'Mesure 1 Diastole'] != None and edited_df.loc[6, 'Mesure 2 Diastole'] != None and edited_df.loc[6, 'Mesure 3 Diastole'] != None and edited_df.loc[7, 'Mesure 1 Diastole'] != None and edited_df.loc[7, 'Mesure 2 Diastole'] != None and edited_df.loc[7, 'Mesure 3 Diastole'] != None:
            moyenne_diastole_jour_4 = (edited_df.loc[6, 'Mesure 1 Diastole'] + edited_df.loc[6, 'Mesure 2 Diastole'] + edited_df.loc[6, 'Mesure 3 Diastole'] + edited_df.loc[7, 'Mesure 1 Diastole'] + edited_df.loc[7, 'Mesure 2 Diastole'] + edited_df.loc[7, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_4_sans_premiere_mesure = (edited_df.loc[6, 'Mesure 2 Diastole'] + edited_df.loc[6, 'Mesure 3 Diastole'] + edited_df.loc[7, 'Mesure 2 Diastole'] + edited_df.loc[7, 'Mesure 3 Diastole']) / 4
            moyenne_diastole_jour_4_matin = (edited_df.loc[6, 'Mesure 1 Diastole'] + edited_df.loc[6, 'Mesure 2 Diastole'] + edited_df.loc[6, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_4_soir = (edited_df.loc[7, 'Mesure 1 Diastole'] + edited_df.loc[7, 'Mesure 2 Diastole'] + edited_df.loc[7, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_4_sans_premiere_mesure_matin = (edited_df.loc[6, 'Mesure 2 Diastole'] + edited_df.loc[6, 'Mesure 3 Diastole']) / 2
            moyenne_diastole_jour_4_sans_premiere_mesure_soir = (edited_df.loc[7, 'Mesure 2 Diastole'] + edited_df.loc[7, 'Mesure 3 Diastole']) / 2
        else :
            moyenne_diastole_jour_4 = 0
            moyenne_diastole_jour_4_sans_premiere_mesure = 0
            moyenne_diastole_jour_4_matin = 0
            moyenne_diastole_jour_4_soir = 0
            moyenne_diastole_jour_4_sans_premiere_mesure_matin = 0
            moyenne_diastole_jour_4_sans_premiere_mesure_soir = 0
            
        #Moyenne systole jour 5
        if edited_df.loc[8, 'Mesure 1 Systole'] != None and edited_df.loc[8, 'Mesure 2 Systole'] != None and edited_df.loc[8, 'Mesure 3 Systole'] != None and edited_df.loc[9, 'Mesure 1 Systole'] != None and edited_df.loc[9, 'Mesure 2 Systole'] != None and edited_df.loc[9, 'Mesure 3 Systole'] != None:
            moyenne_systole_jour_5 = (edited_df.loc[8, 'Mesure 1 Systole'] + edited_df.loc[8, 'Mesure 2 Systole'] + edited_df.loc[8, 'Mesure 3 Systole'] + edited_df.loc[9, 'Mesure 1 Systole'] + edited_df.loc[9, 'Mesure 2 Systole'] + edited_df.loc[9, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_5_sans_premiere_mesure = (edited_df.loc[8, 'Mesure 2 Systole'] + edited_df.loc[8, 'Mesure 3 Systole'] + edited_df.loc[9, 'Mesure 2 Systole'] + edited_df.loc[9, 'Mesure 3 Systole']) / 4
            moyenne_systole_jour_5_matin = (edited_df.loc[8, 'Mesure 1 Systole'] + edited_df.loc[8, 'Mesure 2 Systole'] + edited_df.loc[8, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_5_soir = (edited_df.loc[9, 'Mesure 1 Systole'] + edited_df.loc[9, 'Mesure 2 Systole'] + edited_df.loc[9, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_5_sans_premiere_mesure_matin = (edited_df.loc[8, 'Mesure 2 Systole'] + edited_df.loc[8, 'Mesure 3 Systole']) / 2
            moyenne_systole_jour_5_sans_premiere_mesure_soir = (edited_df.loc[9, 'Mesure 2 Systole'] + edited_df.loc[9, 'Mesure 3 Systole']) / 2
        else :
            moyenne_systole_jour_5 = 0
            moyenne_systole_jour_5_sans_premiere_mesure = 0
            moyenne_systole_jour_5_matin = 0
            moyenne_systole_jour_5_soir = 0
            moyenne_systole_jour_5_sans_premiere_mesure_matin = 0
            moyenne_systole_jour_5_sans_premiere_mesure_soir = 0
        
        #Moyenne diastole jour 5
        if edited_df.loc[8, 'Mesure 1 Diastole'] != None and edited_df.loc[8, 'Mesure 2 Diastole'] != None and edited_df.loc[8, 'Mesure 3 Diastole'] != None and edited_df.loc[9, 'Mesure 1 Diastole'] != None and edited_df.loc[9, 'Mesure 2 Diastole'] != None and edited_df.loc[9, 'Mesure 3 Diastole'] != None:
            moyenne_diastole_jour_5 = (edited_df.loc[8, 'Mesure 1 Diastole'] + edited_df.loc[8, 'Mesure 2 Diastole'] + edited_df.loc[8, 'Mesure 3 Diastole'] + edited_df.loc[9, 'Mesure 1 Diastole'] + edited_df.loc[9, 'Mesure 2 Diastole'] + edited_df.loc[9, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_5_sans_premiere_mesure = (edited_df.loc[8, 'Mesure 2 Diastole'] + edited_df.loc[8, 'Mesure 3 Diastole'] + edited_df.loc[9, 'Mesure 2 Diastole'] + edited_df.loc[9, 'Mesure 3 Diastole']) / 4
            moyenne_diastole_jour_5_matin = (edited_df.loc[8, 'Mesure 1 Diastole'] + edited_df.loc[8, 'Mesure 2 Diastole'] + edited_df.loc[8, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_5_soir = (edited_df.loc[9, 'Mesure 1 Diastole'] + edited_df.loc[9, 'Mesure 2 Diastole'] + edited_df.loc[9, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_5_sans_premiere_mesure_matin = (edited_df.loc[8, 'Mesure 2 Diastole'] + edited_df.loc[8, 'Mesure 3 Diastole']) / 2
            moyenne_diastole_jour_5_sans_premiere_mesure_soir = (edited_df.loc[9, 'Mesure 2 Diastole'] + edited_df.loc[9, 'Mesure 3 Diastole']) / 2
        else :
            moyenne_diastole_jour_5 = 0
            moyenne_diastole_jour_5_sans_premiere_mesure = 0
            moyenne_diastole_jour_5_matin = 0
            moyenne_diastole_jour_5_soir = 0
            moyenne_diastole_jour_5_sans_premiere_mesure_matin = 0
            moyenne_diastole_jour_5_sans_premiere_mesure_soir = 0
        #Moyenne systole jour 6
        if edited_df.loc[10, 'Mesure 1 Systole'] != None and edited_df.loc[10, 'Mesure 2 Systole'] != None and edited_df.loc[10, 'Mesure 3 Systole'] != None and edited_df.loc[11, 'Mesure 1 Systole'] != None and edited_df.loc[11, 'Mesure 2 Systole'] != None and edited_df.loc[11, 'Mesure 3 Systole'] != None:
            moyenne_systole_jour_6 = (edited_df.loc[10, 'Mesure 1 Systole'] + edited_df.loc[10, 'Mesure 2 Systole'] + edited_df.loc[10, 'Mesure 3 Systole'] + edited_df.loc[11, 'Mesure 1 Systole'] + edited_df.loc[11, 'Mesure 2 Systole'] + edited_df.loc[11, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_6_sans_premiere_mesure = (edited_df.loc[10, 'Mesure 2 Systole'] + edited_df.loc[10, 'Mesure 3 Systole'] + edited_df.loc[11, 'Mesure 2 Systole'] + edited_df.loc[11, 'Mesure 3 Systole']) / 4
            moyenne_systole_jour_6_matin = (edited_df.loc[10, 'Mesure 1 Systole'] + edited_df.loc[10, 'Mesure 2 Systole'] + edited_df.loc[10, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_6_soir = (edited_df.loc[11, 'Mesure 1 Systole'] + edited_df.loc[11, 'Mesure 2 Systole'] + edited_df.loc[11, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_6_sans_premiere_mesure_matin = (edited_df.loc[10, 'Mesure 2 Systole'] + edited_df.loc[10, 'Mesure 3 Systole']) / 2
            moyenne_systole_jour_6_sans_premiere_mesure_soir = (edited_df.loc[11, 'Mesure 2 Systole'] + edited_df.loc[11, 'Mesure 3 Systole']) / 2
        else :
            moyenne_systole_jour_6 = 0
            moyenne_systole_jour_6_sans_premiere_mesure = 0
            moyenne_systole_jour_6_matin = 0
            moyenne_systole_jour_6_soir = 0
            moyenne_systole_jour_6_sans_premiere_mesure_matin = 0
            moyenne_systole_jour_6_sans_premiere_mesure_soir = 0
        #Moyenne diastole jour 6
        if edited_df.loc[10, 'Mesure 1 Diastole'] != None and edited_df.loc[10, 'Mesure 2 Diastole'] != None and edited_df.loc[10, 'Mesure 3 Diastole'] != None and edited_df.loc[11, 'Mesure 1 Diastole'] != None and edited_df.loc[11, 'Mesure 2 Diastole'] != None and edited_df.loc[11, 'Mesure 3 Diastole'] != None:
            moyenne_diastole_jour_6 = (edited_df.loc[10, 'Mesure 1 Diastole'] + edited_df.loc[10, 'Mesure 2 Diastole'] + edited_df.loc[10, 'Mesure 3 Diastole'] + edited_df.loc[11, 'Mesure 1 Diastole'] + edited_df.loc[11, 'Mesure 2 Diastole'] + edited_df.loc[11, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_6_sans_premiere_mesure = (edited_df.loc[10, 'Mesure 2 Diastole'] + edited_df.loc[10, 'Mesure 3 Diastole'] + edited_df.loc[11, 'Mesure 2 Diastole'] + edited_df.loc[11, 'Mesure 3 Diastole']) / 4
            moyenne_diastole_jour_6_matin = (edited_df.loc[10, 'Mesure 1 Diastole'] + edited_df.loc[10, 'Mesure 2 Diastole'] + edited_df.loc[10, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_6_soir = (edited_df.loc[11, 'Mesure 1 Diastole'] + edited_df.loc[11, 'Mesure 2 Diastole'] + edited_df.loc[11, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_6_sans_premiere_mesure_matin = (edited_df.loc[10, 'Mesure 2 Diastole'] + edited_df.loc[10, 'Mesure 3 Diastole']) / 2
            moyenne_diastole_jour_6_sans_premiere_mesure_soir = (edited_df.loc[11, 'Mesure 2 Diastole'] + edited_df.loc[11, 'Mesure 3 Diastole']) / 2
        else :
            moyenne_diastole_jour_6 = 0
            moyenne_diastole_jour_6_sans_premiere_mesure = 0
            moyenne_diastole_jour_6_matin = 0
            moyenne_diastole_jour_6_soir = 0
            moyenne_diastole_jour_6_sans_premiere_mesure_matin = 0
            moyenne_diastole_jour_6_sans_premiere_mesure_soir = 0
        
        #Moyenne systole jour 7
        if edited_df.loc[12, 'Mesure 1 Systole'] != None and edited_df.loc[12, 'Mesure 2 Systole'] != None and edited_df.loc[12, 'Mesure 3 Systole'] != None and edited_df.loc[13, 'Mesure 1 Systole'] != None and edited_df.loc[13, 'Mesure 2 Systole'] != None and edited_df.loc[13, 'Mesure 3 Systole'] != None:
            moyenne_systole_jour_7 = (edited_df.loc[12, 'Mesure 1 Systole'] + edited_df.loc[12, 'Mesure 2 Systole'] + edited_df.loc[12, 'Mesure 3 Systole'] + edited_df.loc[13, 'Mesure 1 Systole'] + edited_df.loc[13, 'Mesure 2 Systole'] + edited_df.loc[13, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_7_sans_premiere_mesure = (edited_df.loc[12, 'Mesure 2 Systole'] + edited_df.loc[12, 'Mesure 3 Systole'] + edited_df.loc[13, 'Mesure 2 Systole'] + edited_df.loc[13, 'Mesure 3 Systole']) / 4
            moyenne_systole_jour_7_matin = (edited_df.loc[12, 'Mesure 1 Systole'] + edited_df.loc[12, 'Mesure 2 Systole'] + edited_df.loc[12, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_7_soir = (edited_df.loc[13, 'Mesure 1 Systole'] + edited_df.loc[13, 'Mesure 2 Systole'] + edited_df.loc[13, 'Mesure 3 Systole']) / 3
            moyenne_systole_jour_7_sans_premiere_mesure_matin = (edited_df.loc[12, 'Mesure 2 Systole'] + edited_df.loc[12, 'Mesure 3 Systole']) / 2
            moyenne_systole_jour_7_sans_premiere_mesure_soir = (edited_df.loc[13, 'Mesure 2 Systole'] + edited_df.loc[13, 'Mesure 3 Systole']) / 2
        else :
            moyenne_systole_jour_7 = 0
            moyenne_systole_jour_7_sans_premiere_mesure = 0
            moyenne_systole_jour_7_matin = 0
            moyenne_systole_jour_7_soir = 0
            moyenne_systole_jour_7_sans_premiere_mesure_matin = 0
            moyenne_systole_jour_7_sans_premiere_mesure_soir = 0
        #Moyenne diastole jour 7
        if edited_df.loc[12, 'Mesure 1 Diastole'] != None and edited_df.loc[12, 'Mesure 2 Diastole'] != None and edited_df.loc[12, 'Mesure 3 Diastole'] != None and edited_df.loc[13, 'Mesure 1 Diastole'] != None and edited_df.loc[13, 'Mesure 2 Diastole'] != None and edited_df.loc[13, 'Mesure 3 Diastole'] != None:
            moyenne_diastole_jour_7 = (edited_df.loc[12, 'Mesure 1 Diastole'] + edited_df.loc[12, 'Mesure 2 Diastole'] + edited_df.loc[12, 'Mesure 3 Diastole'] + edited_df.loc[13, 'Mesure 1 Diastole'] + edited_df.loc[13, 'Mesure 2 Diastole'] + edited_df.loc[13, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_7_sans_premiere_mesure = (edited_df.loc[12, 'Mesure 2 Diastole'] + edited_df.loc[12, 'Mesure 3 Diastole'] + edited_df.loc[13, 'Mesure 2 Diastole'] + edited_df.loc[13, 'Mesure 3 Diastole']) / 4
            moyenne_diastole_jour_7_matin = (edited_df.loc[12, 'Mesure 1 Diastole'] + edited_df.loc[12, 'Mesure 2 Diastole'] + edited_df.loc[12, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_7_soir = (edited_df.loc[13, 'Mesure 1 Diastole'] + edited_df.loc[13, 'Mesure 2 Diastole'] + edited_df.loc[13, 'Mesure 3 Diastole']) / 3
            moyenne_diastole_jour_7_sans_premiere_mesure_matin = (edited_df.loc[12, 'Mesure 2 Diastole'] + edited_df.loc[12, 'Mesure 3 Diastole']) / 2
            moyenne_diastole_jour_7_sans_premiere_mesure_soir = (edited_df.loc[13, 'Mesure 2 Diastole'] + edited_df.loc[13, 'Mesure 3 Diastole']) / 2
        else :
            moyenne_diastole_jour_7 = 0
            moyenne_diastole_jour_7_sans_premiere_mesure = 0
            moyenne_diastole_jour_7_matin = 0
            moyenne_diastole_jour_7_soir = 0
            moyenne_diastole_jour_7_sans_premiere_mesure_matin = 0
            moyenne_diastole_jour_7_sans_premiere_mesure_soir = 0
        
        #Def chart_data
        chart_data = {
        'Jour' : ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
        'Systole' : [moyenne_systole_jour_1, moyenne_systole_jour_2, moyenne_systole_jour_3, moyenne_systole_jour_4, moyenne_systole_jour_5, moyenne_systole_jour_6, moyenne_systole_jour_7],
        'Diastole' : [moyenne_diastole_jour_1, moyenne_diastole_jour_2, moyenne_diastole_jour_3, moyenne_diastole_jour_4, moyenne_diastole_jour_5, moyenne_diastole_jour_6, moyenne_diastole_jour_7],
        'seuil_systole' : [135, 135, 135, 135, 135, 135, 135],
        'seuil_diastole' : [85, 85, 85, 85, 85, 85, 85]
    }   
        
        chart_data_without_first_measure = {
        'Jour' : ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
        'Systole' : [moyenne_systole_jour_1_sans_premiere_mesure, moyenne_systole_jour_2_sans_premiere_mesure, moyenne_systole_jour_3_sans_premiere_mesure, moyenne_systole_jour_4_sans_premiere_mesure, moyenne_systole_jour_5_sans_premiere_mesure, moyenne_systole_jour_6_sans_premiere_mesure, moyenne_systole_jour_7_sans_premiere_mesure],
        'Diastole' : [moyenne_diastole_jour_1_sans_premiere_mesure, moyenne_diastole_jour_2_sans_premiere_mesure, moyenne_diastole_jour_3_sans_premiere_mesure, moyenne_diastole_jour_4_sans_premiere_mesure, moyenne_diastole_jour_5_sans_premiere_mesure, moyenne_diastole_jour_6_sans_premiere_mesure, moyenne_diastole_jour_7_sans_premiere_mesure]
    }
        chart_data_without_measure_day_1 = {
        'Jour' : ['Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
        'Systole' : [moyenne_systole_jour_2_sans_premiere_mesure, moyenne_systole_jour_3_sans_premiere_mesure, moyenne_systole_jour_4_sans_premiere_mesure, moyenne_systole_jour_5_sans_premiere_mesure, moyenne_systole_jour_6_sans_premiere_mesure, moyenne_systole_jour_7_sans_premiere_mesure],
        'Diastole' : [moyenne_diastole_jour_2_sans_premiere_mesure, moyenne_diastole_jour_3_sans_premiere_mesure, moyenne_diastole_jour_4_sans_premiere_mesure, moyenne_diastole_jour_5_sans_premiere_mesure, moyenne_diastole_jour_6_sans_premiere_mesure, moyenne_diastole_jour_7_sans_premiere_mesure],
    }   
        line_systole = pd.DataFrame(
            {
                'Jour' : ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
                'Systole' : [135, 135, 135, 135, 135, 135, 135]
            }
        )
        
        line_diastole = pd.DataFrame(
            {
                'Jour' : ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
                'Diastole' : [85, 85, 85, 85, 85, 85, 85]
            }
        )
        
        line_systole_without_first_measure = pd.DataFrame(
            {
                'Jour' : ['Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
                'Systole' : [135, 135, 135, 135, 135, 135]
            }
        )
        
        line_diastole_without_first_measure = pd.DataFrame(
            {
                'Jour' : ['Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
                'Diastole' : [85, 85, 85, 85, 85, 85]
            }
        )
        
        
        #Calcul moyenne globale systole
        liste_systole_globale = [i for i in chart_data['Systole'] if i != 0]
        if len(liste_systole_globale) != 0:
            moyenne_globale_systole = sum(liste_systole_globale) / len(liste_systole_globale)
        else : 
            moyenne_globale_systole = 0
        #Calcul moyenne globale diastole
        liste_diastole_globale = [i for i in chart_data['Diastole'] if i != 0]
        if len(liste_diastole_globale) != 0:
            moyenne_globale_diastole = sum(liste_diastole_globale) / len(liste_diastole_globale)
        else : 
            moyenne_globale_diastole = 0    
        #Calcul moyenne globale systole matin
        liste_systole_globale_matin = [i for i in [moyenne_systole_jour_1_matin, moyenne_systole_jour_2_matin, moyenne_systole_jour_3_matin, moyenne_systole_jour_4_matin, moyenne_systole_jour_5_matin, moyenne_systole_jour_6_matin, moyenne_systole_jour_7_matin] if i != 0]
        if len(liste_systole_globale_matin) != 0:
            moyenne_globale_systole_matin = sum(liste_systole_globale_matin) / len(liste_systole_globale_matin)
        else: 
            moyenne_globale_systole_matin = 0
        #Calcul moyenne globale diastole matin
        liste_diastole_globale_matin = [i for i in [moyenne_diastole_jour_1_matin, moyenne_diastole_jour_2_matin, moyenne_diastole_jour_3_matin, moyenne_diastole_jour_4_matin, moyenne_diastole_jour_5_matin, moyenne_diastole_jour_6_matin, moyenne_diastole_jour_7_matin] if i != 0]
        if len(liste_diastole_globale_matin) != 0:
            moyenne_globale_diastole_matin = sum(liste_diastole_globale_matin) / len(liste_diastole_globale_matin)
        else:
            moyenne_globale_diastole_matin = 0
        #Calcul moyenne globale systole soir
        liste_systole_globale_soir = [i for i in [moyenne_systole_jour_1_soir, moyenne_systole_jour_2_soir, moyenne_systole_jour_3_soir, moyenne_systole_jour_4_soir, moyenne_systole_jour_5_soir, moyenne_systole_jour_6_soir, moyenne_systole_jour_7_soir] if i != 0]
        if len(liste_systole_globale_soir) != 0:
            moyenne_globale_systole_soir = sum(liste_systole_globale_soir) / len(liste_systole_globale_soir)
        else: 
            moyenne_globale_systole_soir = 0 
        #Calcul moyenne globale diastole soir
        liste_diastole_globale_soir = [i for i in [moyenne_diastole_jour_1_soir, moyenne_diastole_jour_2_soir, moyenne_diastole_jour_3_soir, moyenne_diastole_jour_4_soir, moyenne_diastole_jour_5_soir, moyenne_diastole_jour_6_soir, moyenne_diastole_jour_7_soir] if i != 0]
        if len(liste_diastole_globale_soir) != 0:
            moyenne_globale_diastole_soir = sum(liste_diastole_globale_soir) / len(liste_diastole_globale_soir)
        else:
            moyenne_globale_diastole_soir = 0
        #Calcul moyenne globale systole sans la première mesure
        liste_systole_globale_sans_premiere_mesure = [i for i in [moyenne_systole_jour_1_sans_premiere_mesure, moyenne_systole_jour_2_sans_premiere_mesure, moyenne_systole_jour_3_sans_premiere_mesure, moyenne_systole_jour_4_sans_premiere_mesure, moyenne_systole_jour_5_sans_premiere_mesure, moyenne_systole_jour_6_sans_premiere_mesure, moyenne_systole_jour_7_sans_premiere_mesure] if i != 0] 
        if len(liste_systole_globale_sans_premiere_mesure) != 0:
            moyenne_globale_systole_sans_premiere_mesure = sum(liste_systole_globale_sans_premiere_mesure) / len(liste_systole_globale_sans_premiere_mesure)
        else:
            moyenne_globale_systole_sans_premiere_mesure = 0
        #Calcul moyenne globale diastole sans la première mesure
        liste_diastole_globale_sans_premiere_mesure = [i for i in [moyenne_diastole_jour_1_sans_premiere_mesure, moyenne_diastole_jour_2_sans_premiere_mesure, moyenne_diastole_jour_3_sans_premiere_mesure, moyenne_diastole_jour_4_sans_premiere_mesure, moyenne_diastole_jour_5_sans_premiere_mesure, moyenne_diastole_jour_6_sans_premiere_mesure, moyenne_diastole_jour_7_sans_premiere_mesure] if i != 0]
        if len(liste_diastole_globale_sans_premiere_mesure) != 0:
            moyenne_globale_diastole_sans_premiere_mesure = sum(liste_diastole_globale_sans_premiere_mesure) / len(liste_diastole_globale_sans_premiere_mesure)
        else:
            moyenne_globale_diastole_sans_premiere_mesure = 0
        #Calcul moyenne globale systole sans la première mesure matin
        liste_systole_globale_sans_premiere_mesure_matin = [i for i in [moyenne_systole_jour_1_sans_premiere_mesure_matin, moyenne_systole_jour_2_sans_premiere_mesure_matin, moyenne_systole_jour_3_sans_premiere_mesure_matin, moyenne_systole_jour_4_sans_premiere_mesure_matin, moyenne_systole_jour_5_sans_premiere_mesure_matin, moyenne_systole_jour_6_sans_premiere_mesure_matin, moyenne_systole_jour_7_sans_premiere_mesure_matin] if i != 0]
        if len(liste_systole_globale_sans_premiere_mesure_matin) != 0:
            moyenne_globale_systole_sans_premiere_mesure_matin = sum(liste_systole_globale_sans_premiere_mesure_matin) / len(liste_systole_globale_sans_premiere_mesure_matin)
        else:
            moyenne_globale_systole_sans_premiere_mesure_matin = 0
        #Calcul moyenne globale diastole sans la première mesure matin
        liste_diastole_globale_sans_premiere_mesure_matin = [i for i in [moyenne_diastole_jour_1_sans_premiere_mesure_matin, moyenne_diastole_jour_2_sans_premiere_mesure_matin, moyenne_diastole_jour_3_sans_premiere_mesure_matin, moyenne_diastole_jour_4_sans_premiere_mesure_matin, moyenne_diastole_jour_5_sans_premiere_mesure_matin, moyenne_diastole_jour_6_sans_premiere_mesure_matin, moyenne_diastole_jour_7_sans_premiere_mesure_matin] if i != 0]
        if len(liste_diastole_globale_sans_premiere_mesure_matin) != 0:
            moyenne_globale_diastole_sans_premiere_mesure_matin = sum(liste_diastole_globale_sans_premiere_mesure_matin) / len(liste_diastole_globale_sans_premiere_mesure_matin)
        else:
            moyenne_globale_diastole_sans_premiere_mesure_matin = 0
        #Calcul moyenne globale systole sans la première mesure soir
        liste_systole_globale_sans_premiere_mesure_soir = [i for i in [moyenne_systole_jour_1_sans_premiere_mesure_soir, moyenne_systole_jour_2_sans_premiere_mesure_soir, moyenne_systole_jour_3_sans_premiere_mesure_soir, moyenne_systole_jour_4_sans_premiere_mesure_soir, moyenne_systole_jour_5_sans_premiere_mesure_soir, moyenne_systole_jour_6_sans_premiere_mesure_soir, moyenne_systole_jour_7_sans_premiere_mesure_soir] if i != 0]
        if len(liste_systole_globale_sans_premiere_mesure_soir) != 0:
            moyenne_globale_systole_sans_premiere_mesure_soir = sum(liste_systole_globale_sans_premiere_mesure_soir) / len(liste_systole_globale_sans_premiere_mesure_soir)
        else:
            moyenne_globale_systole_sans_premiere_mesure_soir = 0
        #Calcul moyenne globale diastole sans la première mesure soir
        liste_diastole_globale_sans_premiere_mesure_soir = [i for i in [moyenne_diastole_jour_1_sans_premiere_mesure_soir, moyenne_diastole_jour_2_sans_premiere_mesure_soir, moyenne_diastole_jour_3_sans_premiere_mesure_soir, moyenne_diastole_jour_4_sans_premiere_mesure_soir, moyenne_diastole_jour_5_sans_premiere_mesure_soir, moyenne_diastole_jour_6_sans_premiere_mesure_soir, moyenne_diastole_jour_7_sans_premiere_mesure_soir] if i != 0]
        if len(liste_diastole_globale_sans_premiere_mesure_soir) != 0:
            moyenne_globale_diastole_sans_premiere_mesure_soir = sum(liste_diastole_globale_sans_premiere_mesure_soir) / len(liste_diastole_globale_sans_premiere_mesure_soir)
        else:
            moyenne_globale_diastole_sans_premiere_mesure_soir = 0
        #Calcul moyenne globale systole sans les mesures du jour 1
        liste_systole_globale_sans_mesure_jour_1 = [i for i in chart_data_without_measure_day_1['Systole'] if i != 0]
        if len(liste_systole_globale_sans_mesure_jour_1) != 0:
            moyenne_globale_systole_sans_mesure_jour_1 = sum(liste_systole_globale_sans_mesure_jour_1) / len(liste_systole_globale_sans_mesure_jour_1)
        else: 
            moyenne_globale_systole_sans_mesure_jour_1 = 0
        #Calcul moyenne globale diastole sans les mesures du jour 1
        liste_diastole_globale_sans_mesure_jour_1 = [i for i in chart_data_without_measure_day_1['Diastole'] if i != 0]
        if len(liste_diastole_globale_sans_mesure_jour_1) != 0:
            moyenne_globale_diastole_sans_mesure_jour_1 = sum(liste_diastole_globale_sans_mesure_jour_1) / len(liste_diastole_globale_sans_mesure_jour_1)
        else:
            moyenne_globale_diastole_sans_mesure_jour_1 = 0

        #draw chart
        st.write("")
        fig1, ax1 = plt.subplots(1,figsize=(10, 5))
        ax1.scatter(chart_data['Jour'], chart_data['Systole'], label='Systole', color='#F90000')
        ax1.scatter(chart_data['Jour'], chart_data['Diastole'], label='Diastole', color='#0095F9')
        ax1.plot(line_systole['Jour'], line_systole['Systole'], color='#F90000', linestyle='dashed', label='Seuil systole')
        ax1.plot(line_diastole['Jour'], line_diastole['Diastole'], color='#0095F9', linestyle='dashed', label='Seuil diastole')
        ax1.set_ylabel('Pression artérielle (mmHg)')
        ax1.set_title('Valeurs moyennes de la pression artérielle')
        ax1.legend()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile1:
             plt.savefig(tmpfile1.name, format="png")
        text1 ='''**3 mesures par série** : moyenne quotidienne des 3 mesures de chaque série  
                    PA = ''' + str(round(moyenne_globale_systole)) + "/" + str(round(moyenne_globale_diastole)) + " mmHg" + "; " + "PA matin : " + str(round(moyenne_globale_systole_matin)) + "/" + str(round(moyenne_globale_diastole_matin)) + " mmHg" + "; " + "PA soir : " + str(round(moyenne_globale_systole_soir)) + "/" + str(round(moyenne_globale_diastole_soir)) + " mmHg"
        st.markdown(text1)
        st.pyplot(fig1)
        
        fig2, ax2 = plt.subplots(1,figsize=(10, 5))
        ax2.scatter(chart_data_without_first_measure['Jour'], chart_data_without_first_measure['Systole'], label='Systole', color='#F90000')
        ax2.scatter(chart_data_without_first_measure['Jour'], chart_data_without_first_measure['Diastole'], label='Diastole', color='#0095F9')
        ax2.plot(line_systole['Jour'], line_systole['Systole'], color='#F90000', linestyle='dashed', label='Seuil systole')
        ax2.plot(line_diastole['Jour'], line_diastole['Diastole'], color='#0095F9', linestyle='dashed', label='Seuil diastole')
        ax2.set_ylabel('Pression artérielle (mmHg)')
        ax2.set_title('Valeurs moyennes de la pression artérielle sans la première mesure')
        ax2.legend()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile2:
             plt.savefig(tmpfile2.name, format="png")
        text2 = '''**2 mesures par série** : exclusion de la première mesure de chaque série  
                    PA = ''' + str(round(moyenne_globale_systole_sans_premiere_mesure)) + "/" + str(round(moyenne_globale_diastole_sans_premiere_mesure)) + " mmHg" + "; " + "PA matin : " + str(round(moyenne_globale_systole_sans_premiere_mesure_matin)) + "/" + str(round(moyenne_globale_diastole_sans_premiere_mesure_matin)) + " mmHg" + "; " + "PA soir : " + str(round(moyenne_globale_systole_sans_premiere_mesure_soir)) + "/" + str(round(moyenne_globale_diastole_sans_premiere_mesure_soir)) + " mmHg"
        st.markdown(text2)
        st.pyplot(fig2)
        

        fig3, ax3 = plt.subplots(1,figsize=(10, 5))
        ax3.scatter(chart_data_without_measure_day_1['Jour'], chart_data_without_measure_day_1['Systole'], label='Systole', color='#F90000')
        ax3.scatter(chart_data_without_measure_day_1['Jour'], chart_data_without_measure_day_1['Diastole'], label='Diastole', color='#0095F9')
        ax3.plot(line_systole_without_first_measure['Jour'], line_systole_without_first_measure['Systole'], color='#F90000', linestyle='dashed', label='Seuil systole')
        ax3.plot(line_diastole_without_first_measure['Jour'], line_diastole_without_first_measure['Diastole'], color='#0095F9', linestyle='dashed', label='Seuil diastole')
        ax3.set_ylabel('Pression artérielle (mmHg)')
        ax3.set_title('Valeurs moyennes de la pression artérielle sans les mesures du jour 1')
        ax3.legend()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile3:
            plt.savefig(tmpfile3.name, format="png")
        text3 = '''**2 mesures par série sans J1** : exclusion de la première mesure de chaque série sans le 1e jour  
                    PA = ''' + str(round(moyenne_globale_systole_sans_mesure_jour_1)) + "/" + str(round(moyenne_globale_diastole_sans_mesure_jour_1)) + " mmHg" + "; " + "PA matin : " + str(round(moyenne_globale_systole_sans_mesure_jour_1)) + "/" + str(round(moyenne_globale_diastole_sans_mesure_jour_1)) + " mmHg" + "; " + "PA soir : " + str(round(moyenne_globale_systole_sans_mesure_jour_1)) + "/" + str(round(moyenne_globale_diastole_sans_mesure_jour_1)) + " mmHg"
        st.markdown(text3)
        st.pyplot(fig3)

        COLUMNS = [list(edited_df)]  # Get list of dataframe columns
        ROWS = edited_df.values.tolist()  # Get list of dataframe rows
        DATA = COLUMNS + ROWS  # Combine columns and rows in one list
        
        ##PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size=15)
        #pdf.cell(0, 5, "Compte-rendu de l'automesure", ln=True)
        pdf.set_font(style="B")
        pdf.text(70, 5, "Compte-rendu de l'automesure")
        pdf.set_font("Times", size=12)
        pdf.set_font(style="B")
        pdf.text(15, 12, nom + ' ' + prenom + ' ' + str((age)) + ' ans')
        pdf.set_font("Times", size=12)
        pdf.text(120, 17, "Sexe : " + sexe)
        if taille != 0 and poids != None:
                imc = round(poids / ((taille/100) ** 2),1)
                pdf.text(120, 12, "Poids : " + str(poids) + " kg" + " " + "Taille : " + str(taille) + " cm" + " " + "IMC : " + str(imc))
        else : 
            pdf.text(120, 12, "Poids : " + " " + "Taille : " + " " + "IMC : ")
        pdf.set_font("Times", size=10)
        pdf.set_xy(14, 15)
        pdf.cell(w=pdf.epw/1.8, h=pdf.eph/98, text='Traitement : ' + traitement, border=False)
        pdf.set_xy(15, 20)
        pdf.set_font("Times", size=10)
        with pdf.table(
            borders_layout="MINIMAL",
            align="LEFT",
            cell_fill_color=200,  # grey
            cell_fill_mode="ROWS",
            line_height=pdf.font_size/0.9,
            text_align="CENTER",
            width=160,
        ) as table:
            for data_row in DATA:
                row = table.row()
                for datum in data_row:
                    if datum is None:
                        row.cell('')
                    else : row.cell(str(datum))
        pdf.image(tmpfile1.name, h=pdf.eph/3.8, w=pdf.epw/1.5, x=5, y=90)
        text1 ='''3 mesures par série : moyenne quotidienne des 3 mesures de chaque série  
                    PA = ''' + str(round(moyenne_globale_systole)) + "/" + str(round(moyenne_globale_diastole)) + " mmHg" + "; " + "PA matin : " + str(round(moyenne_globale_systole_matin)) + "/" + str(round(moyenne_globale_diastole_matin)) + " mmHg" + "; " + "PA soir : " + str(round(moyenne_globale_systole_soir)) + "/" + str(round(moyenne_globale_diastole_soir)) + " mmHg"
        text2 = '''2 mesures par série : exclusion de la première mesure de chaque série  
                    PA = ''' + str(round(moyenne_globale_systole_sans_premiere_mesure)) + "/" + str(round(moyenne_globale_diastole_sans_premiere_mesure)) + " mmHg" + "; " + "PA matin : " + str(round(moyenne_globale_systole_sans_premiere_mesure_matin)) + "/" + str(round(moyenne_globale_diastole_sans_premiere_mesure_matin)) + " mmHg" + "; " + "PA soir : " + str(round(moyenne_globale_systole_sans_premiere_mesure_soir)) + "/" + str(round(moyenne_globale_diastole_sans_premiere_mesure_soir)) + " mmHg"
        text3 = '''2 mesures par série sans J1 : exclusion de la première mesure de chaque série sans le 1e jour  
                    PA = ''' + str(round(moyenne_globale_systole_sans_mesure_jour_1)) + "/" + str(round(moyenne_globale_diastole_sans_mesure_jour_1)) + " mmHg" + "; " + "PA matin : " + str(round(moyenne_globale_systole_sans_mesure_jour_1)) + "/" + str(round(moyenne_globale_diastole_sans_mesure_jour_1)) + " mmHg" + "; " + "PA soir : " + str(round(moyenne_globale_systole_sans_mesure_jour_1)) + "/" + str(round(moyenne_globale_diastole_sans_mesure_jour_1)) + " mmHg"
        pdf.set_xy(1, 83)
        pdf.multi_cell(pdf.epw,5, text1)
        pdf.image(tmpfile2.name, h=pdf.eph/3.8, w=pdf.epw/1.5, x=5, y=160)
        pdf.set_xy(1, 155)
        pdf.multi_cell(pdf.epw,5, text2)
        pdf.image(tmpfile3.name, h=pdf.eph/3.8, w=pdf.epw/1.5, x=5, y=230)
        pdf.set_xy(1, 225)
        pdf.multi_cell(pdf.epw,5, text3)
        html = create_download_link(pdf.output(), "compte-rendu-automesure")

        st.markdown(html, unsafe_allow_html=True)
        
    else:
        st.markdown('''Une fois les valeurs complétées, cliquer sur \"Soumettre le formulaire\" afin  d'afficher les courbes des valeurs moyennes.  
                    **Pour télécharger le compte-rendu, cliquer sur le lien qui apparaitra en bas de page.**''')
