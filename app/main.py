import pandas as pd
import numpy as np
import streamlit as st
import streamlit_book as stb

# Titre de l'application
st.title('Suivi Tension Artérielle')

st.divider()  # 👈 Draws a horizontal rule

# Créer une liste déroulante pour la navigation entre les pages
page = st.sidebar.selectbox('Choisissez une page', ('Accueil - Suivi de la tension', 'Protocole et règle des 3'))

if page == 'Accueil - Suivi de la tension':
    data = [{"Jour": 'Jour 1 Matin', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 1 Soir', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 2 Matin', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 2 Soir', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 3 Matin', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 3 Soir', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 4 Matin', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 4 Soir', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 5 Matin', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 5 Soir', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 6 Matin', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 6 Soir', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 7 Matin', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None},
                {"Jour": 'Jour 7 Soir', "Mesure 1 Systole": None, "Mesure 1 Diastole": None, "Mesure 2 Systole": None, "Mesure 2 Diastole": None, "Mesure 3 Systole": None, "Mesure 3 Diastole": None}]

    data_df = pd.DataFrame(data)

    with st.form('input_form'):
        with st.expander("Mesures de tension artérielle Jour 1"):
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_1_matin = st.slider('Mesure 1 Systole Jour 1 Matin', min_value=0, max_value=200)
                    mesure_1_diastole_jour_1_matin = st.slider('Mesure 1 Diastole Jour 1 Matin', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_1_matin = st.slider('Mesure 2 Systole Jour 1 Matin', min_value=0, max_value=200)
                    mesure_2_diastole_jour_1_matin = st.slider('Mesure 2 Diastole Jour 1 Matin', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_1_matin = st.slider('Mesure 3 Systole Jour 1 Matin', min_value=0, max_value=200)
                    mesure_3_diastole_jour_1_matin = st.slider('Mesure 3 Diastole Jour 1 Matin', min_value=0, max_value=200)
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_1_soir = st.slider('Mesure 1 Systole Jour 1 Soir', min_value=0, max_value=200)
                    mesure_1_diastole_jour_1_soir = st.slider('Mesure 1 Diastole Jour 1 Soir', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_1_soir = st.slider('Mesure 2 Systole Jour 1 Soir', min_value=0, max_value=200)
                    mesure_2_diastole_jour_1_soir = st.slider('Mesure 2 Diastole Jour 1 Soir', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_1_soir = st.slider('Mesure 3 Systole Jour 1 Soir', min_value=0, max_value=200)
                    mesure_3_diastole_jour_1_soir = st.slider('Mesure 3 Diastole Jour 1 Soir', min_value=0, max_value=200)
        with st.expander("Mesures de tension artérielle Jour 2"):            
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_2_matin = st.slider('Mesure 1 Systole Jour 2 Matin', min_value=0, max_value=200)
                    mesure_1_diastole_jour_2_matin = st.slider('Mesure 1 Diastole Jour 2 Matin', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_2_matin = st.slider('Mesure 2 Systole Jour 2 Matin', min_value=0, max_value=200)
                    mesure_2_diastole_jour_2_matin = st.slider('Mesure 2 Diastole Jour 2 Matin', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_2_matin = st.slider('Mesure 3 Systole Jour 2 Matin', min_value=0, max_value=200)
                    mesure_3_diastole_jour_2_matin = st.slider('Mesure 3 Diastole Jour 2 Matin', min_value=0, max_value=200)
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_2_soir = st.slider('Mesure 1 Systole Jour 2 Soir', min_value=0, max_value=200)
                    mesure_1_diastole_jour_2_soir = st.slider('Mesure 1 Diastole Jour 2 Soir', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_2_soir = st.slider('Mesure 2 Systole Jour 2 Soir', min_value=0, max_value=200)
                    mesure_2_diastole_jour_2_soir = st.slider('Mesure 2 Diastole Jour 2 Soir', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_2_soir = st.slider('Mesure 3 Systole Jour 2 Soir', min_value=0, max_value=200)
                    mesure_3_diastole_jour_2_soir = st.slider('Mesure 3 Diastole Jour 2 Soir', min_value=0, max_value=200)
        with st.expander("Mesures de tension artérielle Jour 3"):
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_3_matin = st.slider('Mesure 1 Systole Jour 3 Matin', min_value=0, max_value=200)
                    mesure_1_diastole_jour_3_matin = st.slider('Mesure 1 Diastole Jour 3 Matin', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_3_matin = st.slider('Mesure 2 Systole Jour 3 Matin', min_value=0, max_value=200)
                    mesure_2_diastole_jour_3_matin = st.slider('Mesure 2 Diastole Jour 3 Matin', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_3_matin = st.slider('Mesure 3 Systole Jour 3 Matin', min_value=0, max_value=200)
                    mesure_3_diastole_jour_3_matin = st.slider('Mesure 3 Diastole Jour 3 Matin', min_value=0, max_value=200)
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_3_soir = st.slider('Mesure 1 Systole Jour 3 Soir', min_value=0, max_value=200)
                    mesure_1_diastole_jour_3_soir = st.slider('Mesure 1 Diastole Jour 3 Soir', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_3_soir = st.slider('Mesure 2 Systole Jour 3 Soir', min_value=0, max_value=200)
                    mesure_2_diastole_jour_3_soir = st.slider('Mesure 2 Diastole Jour 3 Soir', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_3_soir = st.slider('Mesure 3 Systole Jour 3 Soir', min_value=0, max_value=200)
                    mesure_3_diastole_jour_3_soir = st.slider('Mesure 3 Diastole Jour 3 Soir', min_value=0, max_value=200)
        with st.expander("Mesures de tension artérielle Jour 4"):
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_4_matin = st.slider('Mesure 1 Systole Jour 4 Matin', min_value=0, max_value=200)
                    mesure_1_diastole_jour_4_matin = st.slider('Mesure 1 Diastole Jour 4 Matin', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_4_matin = st.slider('Mesure 2 Systole Jour 4 Matin', min_value=0, max_value=200)
                    mesure_2_diastole_jour_4_matin = st.slider('Mesure 2 Diastole Jour 4 Matin', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_4_matin = st.slider('Mesure 3 Systole Jour 4 Matin', min_value=0, max_value=200)
                    mesure_3_diastole_jour_4_matin = st.slider('Mesure 3 Diastole Jour 4 Matin', min_value=0, max_value=200)
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_4_soir = st.slider('Mesure 1 Systole Jour 4 Soir', min_value=0, max_value=200)
                    mesure_1_diastole_jour_4_soir = st.slider('Mesure 1 Diastole Jour 4 Soir', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_4_soir = st.slider('Mesure 2 Systole Jour 4 Soir', min_value=0, max_value=200)
                    mesure_2_diastole_jour_4_soir = st.slider('Mesure 2 Diastole Jour 4 Soir', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_4_soir = st.slider('Mesure 3 Systole Jour 4 Soir', min_value=0, max_value=200)
                    mesure_3_diastole_jour_4_soir = st.slider('Mesure 3 Diastole Jour 4 Soir', min_value=0, max_value=200)
        with st.expander("Mesures de tension artérielle Jour 5"):
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_5_matin = st.slider('Mesure 1 Systole Jour 5 Matin', min_value=0, max_value=200)
                    mesure_1_diastole_jour_5_matin = st.slider('Mesure 1 Diastole Jour 5 Matin', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_5_matin = st.slider('Mesure 2 Systole Jour 5 Matin', min_value=0, max_value=200)
                    mesure_2_diastole_jour_5_matin = st.slider('Mesure 2 Diastole Jour 5 Matin', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_5_matin = st.slider('Mesure 3 Systole Jour 5 Matin', min_value=0, max_value=200)
                    mesure_3_diastole_jour_5_matin = st.slider('Mesure 3 Diastole Jour 5 Matin', min_value=0, max_value=200)
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_5_soir = st.slider('Mesure 1 Systole Jour 5 Soir', min_value=0, max_value=200)
                    mesure_1_diastole_jour_5_soir = st.slider('Mesure 1 Diastole Jour 5 Soir', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_5_soir = st.slider('Mesure 2 Systole Jour 5 Soir', min_value=0, max_value=200)
                    mesure_2_diastole_jour_5_soir = st.slider('Mesure 2 Diastole Jour 5 Soir', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_5_soir = st.slider('Mesure 3 Systole Jour 5 Soir', min_value=0, max_value=200)
                    mesure_3_diastole_jour_5_soir = st.slider('Mesure 3 Diastole Jour 5 Soir', min_value=0, max_value=200)
        with st.expander("Mesures de tension artérielle Jour 6"):
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_6_matin = st.slider('Mesure 1 Systole Jour 6 Matin', min_value=0, max_value=200)
                    mesure_1_diastole_jour_6_matin = st.slider('Mesure 1 Diastole Jour 6 Matin', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_6_matin = st.slider('Mesure 2 Systole Jour 6 Matin', min_value=0, max_value=200)
                    mesure_2_diastole_jour_6_matin = st.slider('Mesure 2 Diastole Jour 6 Matin', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_6_matin = st.slider('Mesure 3 Systole Jour 6 Matin', min_value=0, max_value=200)
                    mesure_3_diastole_jour_6_matin = st.slider('Mesure 3 Diastole Jour 6 Matin', min_value=0, max_value=200)
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_6_soir = st.slider('Mesure 1 Systole Jour 6 Soir', min_value=0, max_value=200)
                    mesure_1_diastole_jour_6_soir = st.slider('Mesure 1 Diastole Jour 6 Soir', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_6_soir = st.slider('Mesure 2 Systole Jour 6 Soir', min_value=0, max_value=200)
                    mesure_2_diastole_jour_6_soir = st.slider('Mesure 2 Diastole Jour 6 Soir', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_6_soir = st.slider('Mesure 3 Systole Jour 6 Soir', min_value=0, max_value=200)
                    mesure_3_diastole_jour_6_soir = st.slider('Mesure 3 Diastole Jour 6 Soir', min_value=0, max_value=200)
        with st.expander("Mesures de tension artérielle Jour 7"):
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_7_matin = st.slider('Mesure 1 Systole Jour 7 Matin', min_value=0, max_value=200)
                    mesure_1_diastole_jour_7_matin = st.slider('Mesure 1 Diastole Jour 7 Matin', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_7_matin = st.slider('Mesure 2 Systole Jour 7 Matin', min_value=0, max_value=200)
                    mesure_2_diastole_jour_7_matin = st.slider('Mesure 2 Diastole Jour 7 Matin', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_7_matin = st.slider('Mesure 3 Systole Jour 7 Matin', min_value=0, max_value=200)
                    mesure_3_diastole_jour_7_matin = st.slider('Mesure 3 Diastole Jour 7 Matin', min_value=0, max_value=200)
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    mesure_1_systole_jour_7_soir = st.slider('Mesure 1 Systole Jour 7 Soir', min_value=0, max_value=200)
                    mesure_1_diastole_jour_7_soir = st.slider('Mesure 1 Diastole Jour 7 Soir', min_value=0, max_value=200)
                with col2:
                    mesure_2_systole_jour_7_soir = st.slider('Mesure 2 Systole Jour 7 Soir', min_value=0, max_value=200)
                    mesure_2_diastole_jour_7_soir = st.slider('Mesure 2 Diastole Jour 7 Soir', min_value=0, max_value=200)
                with col3:
                    mesure_3_systole_jour_7_soir = st.slider('Mesure 3 Systole Jour 7 Soir', min_value=0, max_value=200)
                    mesure_3_diastole_jour_7_soir = st.slider('Mesure 3 Diastole Jour 7 Soir', min_value=0, max_value=200)
        clickSubmit = st.form_submit_button('Soumettre')

    if clickSubmit:
        #jour 1 matin
        data_df.loc[0, 'Mesure 1 Systole'] = mesure_1_systole_jour_1_matin
        data_df.loc[0, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_1_matin
        data_df.loc[0, 'Mesure 2 Systole'] = mesure_2_systole_jour_1_matin
        data_df.loc[0, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_1_matin
        data_df.loc[0, 'Mesure 3 Systole'] = mesure_3_systole_jour_1_matin
        data_df.loc[0, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_1_matin
        
        #jour 1 soir
        data_df.loc[1, 'Mesure 1 Systole'] = mesure_1_systole_jour_1_soir
        data_df.loc[1, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_1_soir
        data_df.loc[1, 'Mesure 2 Systole'] = mesure_2_systole_jour_1_soir
        data_df.loc[1, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_1_soir
        data_df.loc[1, 'Mesure 3 Systole'] = mesure_3_systole_jour_1_soir
        data_df.loc[1, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_1_soir
        
        #jour 2 matin
        data_df.loc[2, 'Mesure 1 Systole'] = mesure_1_systole_jour_2_matin
        data_df.loc[2, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_2_matin
        data_df.loc[2, 'Mesure 2 Systole'] = mesure_2_systole_jour_2_matin
        data_df.loc[2, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_2_matin
        data_df.loc[2, 'Mesure 3 Systole'] = mesure_3_systole_jour_2_matin
        data_df.loc[2, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_2_matin
        
        #jour 2 soir
        data_df.loc[3, 'Mesure 1 Systole'] = mesure_1_systole_jour_2_soir
        data_df.loc[3, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_2_soir
        data_df.loc[3, 'Mesure 2 Systole'] = mesure_2_systole_jour_2_soir
        data_df.loc[3, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_2_soir
        data_df.loc[3, 'Mesure 3 Systole'] = mesure_3_systole_jour_2_soir
        data_df.loc[3, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_2_soir
        
        #jour 3 matin
        data_df.loc[4, 'Mesure 1 Systole'] = mesure_1_systole_jour_3_matin
        data_df.loc[4, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_3_matin
        data_df.loc[4, 'Mesure 2 Systole'] = mesure_2_systole_jour_3_matin
        data_df.loc[4, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_3_matin
        data_df.loc[4, 'Mesure 3 Systole'] = mesure_3_systole_jour_3_matin
        data_df.loc[4, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_3_matin
        
        #jour 3 soir
        data_df.loc[5, 'Mesure 1 Systole'] = mesure_1_systole_jour_3_soir
        data_df.loc[5, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_3_soir
        data_df.loc[5, 'Mesure 2 Systole'] = mesure_2_systole_jour_3_soir
        data_df.loc[5, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_3_soir
        data_df.loc[5, 'Mesure 3 Systole'] = mesure_3_systole_jour_3_soir
        data_df.loc[5, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_3_soir
        
        #jour 4 matin
        data_df.loc[6, 'Mesure 1 Systole'] = mesure_1_systole_jour_4_matin
        data_df.loc[6, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_4_matin
        data_df.loc[6, 'Mesure 2 Systole'] = mesure_2_systole_jour_4_matin
        data_df.loc[6, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_4_matin
        data_df.loc[6, 'Mesure 3 Systole'] = mesure_3_systole_jour_4_matin
        data_df.loc[6, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_4_matin

        #jour 4 soir
        data_df.loc[7, 'Mesure 1 Systole'] = mesure_1_systole_jour_4_soir
        data_df.loc[7, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_4_soir
        data_df.loc[7, 'Mesure 2 Systole'] = mesure_2_systole_jour_4_soir
        data_df.loc[7, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_4_soir
        data_df.loc[7, 'Mesure 3 Systole'] = mesure_3_systole_jour_4_soir
        data_df.loc[7, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_4_soir
        
        #jour 5 matin
        data_df.loc[8, 'Mesure 1 Systole'] = mesure_1_systole_jour_5_matin
        data_df.loc[8, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_5_matin
        data_df.loc[8, 'Mesure 2 Systole'] = mesure_2_systole_jour_5_matin
        data_df.loc[8, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_5_matin
        data_df.loc[8, 'Mesure 3 Systole'] = mesure_3_systole_jour_5_matin
        data_df.loc[8, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_5_matin
        
        #jour 5 soir
        data_df.loc[9, 'Mesure 1 Systole'] = mesure_1_systole_jour_5_soir
        data_df.loc[9, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_5_soir
        data_df.loc[9, 'Mesure 2 Systole'] = mesure_2_systole_jour_5_soir
        data_df.loc[9, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_5_soir
        data_df.loc[9, 'Mesure 3 Systole'] = mesure_3_systole_jour_5_soir
        data_df.loc[9, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_5_soir
        
        #jour 6 matin
        data_df.loc[10, 'Mesure 1 Systole'] = mesure_1_systole_jour_6_matin
        data_df.loc[10, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_6_matin
        data_df.loc[10, 'Mesure 2 Systole'] = mesure_2_systole_jour_6_matin
        data_df.loc[10, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_6_matin
        data_df.loc[10, 'Mesure 3 Systole'] = mesure_3_systole_jour_6_matin
        data_df.loc[10, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_6_matin
        
        #jour 6 soir
        data_df.loc[11, 'Mesure 1 Systole'] = mesure_1_systole_jour_6_soir
        data_df.loc[11, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_6_soir
        data_df.loc[11, 'Mesure 2 Systole'] = mesure_2_systole_jour_6_soir
        data_df.loc[11, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_6_soir
        data_df.loc[11, 'Mesure 3 Systole'] = mesure_3_systole_jour_6_soir
        data_df.loc[11, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_6_soir
        
        #jour 7 matin
        data_df.loc[12, 'Mesure 1 Systole'] = mesure_1_systole_jour_7_matin
        data_df.loc[12, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_7_matin
        data_df.loc[12, 'Mesure 2 Systole'] = mesure_2_systole_jour_7_matin
        data_df.loc[12, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_7_matin
        data_df.loc[12, 'Mesure 3 Systole'] = mesure_3_systole_jour_7_matin
        data_df.loc[12, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_7_matin
        
        #jour 7 soir
        data_df.loc[13, 'Mesure 1 Systole'] = mesure_1_systole_jour_7_soir
        data_df.loc[13, 'Mesure 1 Diastole'] = mesure_1_diastole_jour_7_soir
        data_df.loc[13, 'Mesure 2 Systole'] = mesure_2_systole_jour_7_soir
        data_df.loc[13, 'Mesure 2 Diastole'] = mesure_2_diastole_jour_7_soir
        data_df.loc[13, 'Mesure 3 Systole'] = mesure_3_systole_jour_7_soir
        data_df.loc[13, 'Mesure 3 Diastole'] = mesure_3_diastole_jour_7_soir   
        
        #calcul des moyennes
        #Moyenne systole jour 1
        if data_df.loc[0, 'Mesure 1 Systole'] != None or data_df.loc[0, 'Mesure 2 Systole'] != None or data_df.loc[0, 'Mesure 3 Systole'] != None or data_df.loc[1, 'Mesure 1 Systole'] != None or data_df.loc[1, 'Mesure 2 Systole'] != None or data_df.loc[1, 'Mesure 3 Systole'] != None:
            moyenne_systole_jour_1 = (data_df.loc[0, 'Mesure 1 Systole'] + data_df.loc[0, 'Mesure 2 Systole'] + data_df.loc[0, 'Mesure 3 Systole'] + data_df.loc[1, 'Mesure 1 Systole'] + data_df.loc[1, 'Mesure 2 Systole'] + data_df.loc[1, 'Mesure 3 Systole']) / 6
        else :
            moyenne_systole_jour_1 = 0
        
        #Moyenne diastole jour 1
        if data_df.loc[0, 'Mesure 1 Diastole'] != None or data_df.loc[0, 'Mesure 2 Diastole'] != None or data_df.loc[0, 'Mesure 3 Diastole'] != None or data_df.loc[1, 'Mesure 1 Diastole'] != None or data_df.loc[1, 'Mesure 2 Diastole'] != None or data_df.loc[1, 'Mesure 3 Diastole'] != None:
            moyenne_diastole_jour_1 = (data_df.loc[0, 'Mesure 1 Diastole'] + data_df.loc[0, 'Mesure 2 Diastole'] + data_df.loc[0, 'Mesure 3 Diastole'] + data_df.loc[1, 'Mesure 1 Diastole'] + data_df.loc[1, 'Mesure 2 Diastole'] + data_df.loc[1, 'Mesure 3 Diastole']) / 6
        else :
            moyenne_diastole_jour_1 = 0
        
        #Moyenne systole jour 2
        if data_df.loc[2, 'Mesure 1 Systole'] != None or data_df.loc[2, 'Mesure 1 Systole'] != None or data_df.loc[2, 'Mesure 1 Systole'] != None or data_df.loc[3, 'Mesure 1 Systole'] != None or data_df.loc[3, 'Mesure 1 Systole'] != None or data_df.loc[3, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_2 = (data_df.loc[2, 'Mesure 1 Systole'] + data_df.loc[2, 'Mesure 2 Systole'] + data_df.loc[2, 'Mesure 3 Systole'] + data_df.loc[3, 'Mesure 1 Systole'] + data_df.loc[3, 'Mesure 2 Systole'] + data_df.loc[3, 'Mesure 3 Systole']) / 6
        else :
            moyenne_systole_jour_2 = 0
        
        #Moyenne diastole jour 2
        if data_df.loc[2, 'Mesure 1 Diastole'] != None or data_df.loc[3, 'Mesure 1 Diastole'] != None or data_df.loc[3, 'Mesure 1 Diastole'] != None or data_df.loc[3, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_2 = (data_df.loc[2, 'Mesure 1 Diastole'] + data_df.loc[2, 'Mesure 2 Diastole'] + data_df.loc[2, 'Mesure 3 Diastole'] + data_df.loc[3, 'Mesure 1 Diastole'] + data_df.loc[3, 'Mesure 2 Diastole'] + data_df.loc[3, 'Mesure 3 Diastole']) / 6
        else :
            moyenne_diastole_jour_2 = 0
        
        #Moyenne systole jour 3
        if data_df.loc[4, 'Mesure 1 Systole'] != None or data_df.loc[5, 'Mesure 1 Systole'] != None or data_df.loc[5, 'Mesure 1 Systole'] != None or data_df.loc[5, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_3 = (data_df.loc[4, 'Mesure 1 Systole'] + data_df.loc[4, 'Mesure 2 Systole'] + data_df.loc[4, 'Mesure 3 Systole'] + data_df.loc[5, 'Mesure 1 Systole'] + data_df.loc[5, 'Mesure 2 Systole'] + data_df.loc[5, 'Mesure 3 Systole']) / 6
        else :
            moyenne_systole_jour_3 = 0
        
        #Moyenne diastole jour 3
        if data_df.loc[4, 'Mesure 1 Diastole'] != None or data_df.loc[5, 'Mesure 1 Diastole'] != None or data_df.loc[5, 'Mesure 1 Diastole'] != None or data_df.loc[5, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_3 = (data_df.loc[4, 'Mesure 1 Diastole'] + data_df.loc[4, 'Mesure 2 Diastole'] + data_df.loc[4, 'Mesure 3 Diastole'] + data_df.loc[5, 'Mesure 1 Diastole'] + data_df.loc[5, 'Mesure 2 Diastole'] + data_df.loc[5, 'Mesure 3 Diastole']) / 6
        else :
            moyenne_diastole_jour_3 = 0
        
        #Moyenne systole jour 4
        if data_df.loc[6, 'Mesure 1 Systole'] != None or data_df.loc[7, 'Mesure 1 Systole'] != None or data_df.loc[7, 'Mesure 1 Systole'] != None or data_df.loc[7, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_4 = (data_df.loc[6, 'Mesure 1 Systole'] + data_df.loc[6, 'Mesure 2 Systole'] + data_df.loc[6, 'Mesure 3 Systole'] + data_df.loc[7, 'Mesure 1 Systole'] + data_df.loc[7, 'Mesure 2 Systole'] + data_df.loc[7, 'Mesure 3 Systole']) / 6
        else :
            moyenne_systole_jour_4 = 0
        
        #Moyenne diastole jour 4
        if data_df.loc[6, 'Mesure 1 Diastole'] != None or data_df.loc[7, 'Mesure 1 Diastole'] != None or data_df.loc[7, 'Mesure 1 Diastole'] != None or data_df.loc[7, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_4 = (data_df.loc[6, 'Mesure 1 Diastole'] + data_df.loc[6, 'Mesure 2 Diastole'] + data_df.loc[6, 'Mesure 3 Diastole'] + data_df.loc[7, 'Mesure 1 Diastole'] + data_df.loc[7, 'Mesure 2 Diastole'] + data_df.loc[7, 'Mesure 3 Diastole']) / 6
        else :
            moyenne_diastole_jour_4 = 0
            
        #Moyenne systole jour 5
        if data_df.loc[8, 'Mesure 1 Systole'] != None or data_df.loc[9, 'Mesure 1 Systole'] != None or data_df.loc[9, 'Mesure 1 Systole'] != None or data_df.loc[9, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_5 = (data_df.loc[8, 'Mesure 1 Systole'] + data_df.loc[8, 'Mesure 2 Systole'] + data_df.loc[8, 'Mesure 3 Systole'] + data_df.loc[9, 'Mesure 1 Systole'] + data_df.loc[9, 'Mesure 2 Systole'] + data_df.loc[9, 'Mesure 3 Systole']) / 6
        else :
            moyenne_systole_jour_5 = 0
        
        #Moyenne diastole jour 5
        if data_df.loc[8, 'Mesure 1 Diastole'] != None or data_df.loc[9, 'Mesure 1 Diastole'] != None or data_df.loc[9, 'Mesure 1 Diastole'] != None or data_df.loc[9, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_5 = (data_df.loc[8, 'Mesure 1 Diastole'] + data_df.loc[8, 'Mesure 2 Diastole'] + data_df.loc[8, 'Mesure 3 Diastole'] + data_df.loc[9, 'Mesure 1 Diastole'] + data_df.loc[9, 'Mesure 2 Diastole'] + data_df.loc[9, 'Mesure 3 Diastole']) / 6
        else :
            moyenne_diastole_jour_5 = 0
        
        #Moyenne systole jour 6
        if data_df.loc[10, 'Mesure 1 Systole'] != None or data_df.loc[11, 'Mesure 1 Systole'] != None or data_df.loc[11, 'Mesure 1 Systole'] != None or data_df.loc[11, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_6 = (data_df.loc[10, 'Mesure 1 Systole'] + data_df.loc[10, 'Mesure 2 Systole'] + data_df.loc[10, 'Mesure 3 Systole'] + data_df.loc[11, 'Mesure 1 Systole'] + data_df.loc[11, 'Mesure 2 Systole'] + data_df.loc[11, 'Mesure 3 Systole']) / 6
        else :
            moyenne_systole_jour_6 = 0
        
        #Moyenne diastole jour 6
        if data_df.loc[10, 'Mesure 1 Diastole'] != None or data_df.loc[11, 'Mesure 1 Diastole'] != None or data_df.loc[11, 'Mesure 1 Diastole'] != None or data_df.loc[11, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_6 = (data_df.loc[10, 'Mesure 1 Diastole'] + data_df.loc[10, 'Mesure 2 Diastole'] + data_df.loc[10, 'Mesure 3 Diastole'] + data_df.loc[11, 'Mesure 1 Diastole'] + data_df.loc[11, 'Mesure 2 Diastole'] + data_df.loc[11, 'Mesure 3 Diastole']) / 6
        else :
            moyenne_diastole_jour_6 = 0
        
        #Moyenne systole jour 7
        if data_df.loc[12, 'Mesure 1 Systole'] != None or data_df.loc[13, 'Mesure 1 Systole'] != None or data_df.loc[13, 'Mesure 1 Systole'] != None or data_df.loc[13, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_7 = (data_df.loc[12, 'Mesure 1 Systole'] + data_df.loc[12, 'Mesure 2 Systole'] + data_df.loc[12, 'Mesure 3 Systole'] + data_df.loc[13, 'Mesure 1 Systole'] + data_df.loc[13, 'Mesure 2 Systole'] + data_df.loc[13, 'Mesure 3 Systole']) / 6
        else :
            moyenne_systole_jour_7 = 0
        
        #Moyenne diastole jour 7
        if data_df.loc[12, 'Mesure 1 Diastole'] != None or data_df.loc[13, 'Mesure 1 Diastole'] != None or data_df.loc[13, 'Mesure 1 Diastole'] != None or data_df.loc[13, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_7 = (data_df.loc[12, 'Mesure 1 Diastole'] + data_df.loc[12, 'Mesure 2 Diastole'] + data_df.loc[12, 'Mesure 3 Diastole'] + data_df.loc[13, 'Mesure 1 Diastole'] + data_df.loc[13, 'Mesure 2 Diastole'] + data_df.loc[13, 'Mesure 3 Diastole']) / 6
        else :
            moyenne_diastole_jour_7 = 0
        chart_data = {
        'x' : ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
        'y_systole' : [moyenne_systole_jour_1, moyenne_systole_jour_2, moyenne_systole_jour_3, moyenne_systole_jour_4, moyenne_systole_jour_5, moyenne_systole_jour_6, moyenne_systole_jour_7],
        'y_diastole' : [moyenne_diastole_jour_1, moyenne_diastole_jour_2, moyenne_diastole_jour_3, moyenne_diastole_jour_4, moyenne_diastole_jour_5, moyenne_diastole_jour_6, moyenne_diastole_jour_7]
    }
        
        chart_data_without_first_measure = {
        'x' : ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
        'y_systole' : [moyenne_systole_jour_1, moyenne_systole_jour_2, moyenne_systole_jour_3, moyenne_systole_jour_4, moyenne_systole_jour_5, moyenne_systole_jour_6, moyenne_systole_jour_7],
        'y_diastole' : [moyenne_diastole_jour_1, moyenne_diastole_jour_2, moyenne_diastole_jour_3, moyenne_diastole_jour_4, moyenne_diastole_jour_5, moyenne_diastole_jour_6, moyenne_diastole_jour_7]
    }
        #draw chart
        st.line_chart(chart_data, x='x', y=['y_systole', 'y_diastole'])
    else:
        st.markdown("Soumettre le formulaire affichera les courbes des valeurs moyennes")

elif page == 'Protocole et règle des 3':
    stb.true_or_false("Test qcm 1, vrai ou faux", 
                      False, 
                      "commentaire si bonne réponse", 
                      "commentaire si mauvaise réponse",
                      "Afficher la réponse")
    stb.single_choice("Test qcm 2, une seule réponse",
                  ["option 1", "option 2", 
                  "option 3", "option 4"],
                  1,
                  "commentaire si bonne réponse", 
                  "commentaire si mauvaise réponse")
    stb.multiple_choice("Test qcm 3, choix multiple",
                    {"1":True,
                     "2":False,
                     "3":False,
                     "4":False,
                     "5":True,
                     "6":True},
                    "commentaire si bonne réponse", 
                    "commentaire si mauvaise réponse"
                   )

