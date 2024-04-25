import pandas as pd
import numpy as np
import streamlit as st
import streamlit_book as stb

st.set_page_config(layout="wide")

# Titre de l'application
st.header('Suivi Tension Artérielle', divider=True)

# Créer une liste déroulante pour la navigation entre les pages
page = st.sidebar.selectbox('Choisissez une page', ('Accueil - Suivi de la tension', 'Quiz'))

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
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Jour 1", "Jour 2", "Jour 3", "Jour 4", "Jour 5", "Jour 6", "Jour 7"])
        with tab1:
            tab_j_1_matin, tab_j_1_soir = st.tabs(['Matin', 'Soir'])
            with st.expander("Mesures de tension artérielle Jour 1"):
                with tab_j_1_matin:
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
                with tab_j_1_soir:            
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
        with tab2:
            tab_j_2_matin, tab_2_1_soir = st.tabs(['Matin', 'Soir'])    
            with st.expander("Mesures de tension artérielle Jour 2"):
                with tab_j_2_matin:            
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
                with tab_2_1_soir:            
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
        with tab3:
            tab_j_3_matin, tab_j_3_soir = st.tabs(['Matin', 'Soir'])
            with st.expander("Mesures de tension artérielle Jour 3"):
                with tab_j_3_matin:
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
                with tab_j_3_soir:            
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
        with tab4:
            tab_j_4_matin, tab_j_4_soir = st.tabs(['Matin', 'Soir'])
            with st.expander("Mesures de tension artérielle Jour 4"):
                with tab_j_4_matin:
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
                with tab_j_4_soir:
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
        with tab5:
            tab_j_5_matin, tab_j_5_soir = st.tabs(['Matin', 'Soir'])
            with st.expander("Mesures de tension artérielle Jour 5"):
                with tab_j_5_matin:
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
                with tab_j_5_soir:
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
        with tab6:
            tab_j_6_matin, tab_j_6_soir = st.tabs(['Matin', 'Soir'])
            with st.expander("Mesures de tension artérielle Jour 6"):
                with tab_j_6_matin:
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
                with tab_j_6_soir:
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
        with tab7:
            tab_j_7_matin, tab_j_7_soir = st.tabs(['Matin', 'Soir'])
            with st.expander("Mesures de tension artérielle Jour 7"):
                with tab_j_7_matin:
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
                with tab_j_7_soir:
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
        clickSubmit = st.form_submit_button('Soumettre le formulaire')

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
            moyenne_systole_jour_1_sans_premiere_mesure = (data_df.loc[0, 'Mesure 2 Systole'] + data_df.loc[0, 'Mesure 3 Systole'] + data_df.loc[1, 'Mesure 2 Systole'] + data_df.loc[1, 'Mesure 3 Systole']) / 4
        else :
            moyenne_systole_jour_1 = 0
        
        #Moyenne diastole jour 1
        if data_df.loc[0, 'Mesure 1 Diastole'] != None or data_df.loc[0, 'Mesure 2 Diastole'] != None or data_df.loc[0, 'Mesure 3 Diastole'] != None or data_df.loc[1, 'Mesure 1 Diastole'] != None or data_df.loc[1, 'Mesure 2 Diastole'] != None or data_df.loc[1, 'Mesure 3 Diastole'] != None:
            moyenne_diastole_jour_1 = (data_df.loc[0, 'Mesure 1 Diastole'] + data_df.loc[0, 'Mesure 2 Diastole'] + data_df.loc[0, 'Mesure 3 Diastole'] + data_df.loc[1, 'Mesure 1 Diastole'] + data_df.loc[1, 'Mesure 2 Diastole'] + data_df.loc[1, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_1_sans_premiere_mesure = (data_df.loc[0, 'Mesure 2 Diastole'] + data_df.loc[0, 'Mesure 3 Diastole'] + data_df.loc[1, 'Mesure 2 Diastole'] + data_df.loc[1, 'Mesure 3 Diastole']) / 4
        else :
            moyenne_diastole_jour_1 = 0
        
        #Moyenne systole jour 2
        if data_df.loc[2, 'Mesure 1 Systole'] != None or data_df.loc[2, 'Mesure 1 Systole'] != None or data_df.loc[2, 'Mesure 1 Systole'] != None or data_df.loc[3, 'Mesure 1 Systole'] != None or data_df.loc[3, 'Mesure 1 Systole'] != None or data_df.loc[3, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_2 = (data_df.loc[2, 'Mesure 1 Systole'] + data_df.loc[2, 'Mesure 2 Systole'] + data_df.loc[2, 'Mesure 3 Systole'] + data_df.loc[3, 'Mesure 1 Systole'] + data_df.loc[3, 'Mesure 2 Systole'] + data_df.loc[3, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_2_sans_premiere_mesure = (data_df.loc[2, 'Mesure 2 Systole'] + data_df.loc[2, 'Mesure 3 Systole'] + data_df.loc[3, 'Mesure 2 Systole'] + data_df.loc[3, 'Mesure 3 Systole']) / 4
        else :
            moyenne_systole_jour_2 = 0
        
        #Moyenne diastole jour 2
        if data_df.loc[2, 'Mesure 1 Diastole'] != None or data_df.loc[3, 'Mesure 1 Diastole'] != None or data_df.loc[3, 'Mesure 1 Diastole'] != None or data_df.loc[3, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_2 = (data_df.loc[2, 'Mesure 1 Diastole'] + data_df.loc[2, 'Mesure 2 Diastole'] + data_df.loc[2, 'Mesure 3 Diastole'] + data_df.loc[3, 'Mesure 1 Diastole'] + data_df.loc[3, 'Mesure 2 Diastole'] + data_df.loc[3, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_2_sans_premiere_mesure = (data_df.loc[2, 'Mesure 2 Diastole'] + data_df.loc[2, 'Mesure 3 Diastole'] + data_df.loc[3, 'Mesure 2 Diastole'] + data_df.loc[3, 'Mesure 3 Diastole']) / 4
        else :
            moyenne_diastole_jour_2 = 0
        
        #Moyenne systole jour 3
        if data_df.loc[4, 'Mesure 1 Systole'] != None or data_df.loc[5, 'Mesure 1 Systole'] != None or data_df.loc[5, 'Mesure 1 Systole'] != None or data_df.loc[5, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_3 = (data_df.loc[4, 'Mesure 1 Systole'] + data_df.loc[4, 'Mesure 2 Systole'] + data_df.loc[4, 'Mesure 3 Systole'] + data_df.loc[5, 'Mesure 1 Systole'] + data_df.loc[5, 'Mesure 2 Systole'] + data_df.loc[5, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_3_sans_premiere_mesure = (data_df.loc[4, 'Mesure 2 Systole'] + data_df.loc[4, 'Mesure 3 Systole'] + data_df.loc[5, 'Mesure 2 Systole'] + data_df.loc[5, 'Mesure 3 Systole']) / 4
        else :
            moyenne_systole_jour_3 = 0
        
        #Moyenne diastole jour 3
        if data_df.loc[4, 'Mesure 1 Diastole'] != None or data_df.loc[5, 'Mesure 1 Diastole'] != None or data_df.loc[5, 'Mesure 1 Diastole'] != None or data_df.loc[5, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_3 = (data_df.loc[4, 'Mesure 1 Diastole'] + data_df.loc[4, 'Mesure 2 Diastole'] + data_df.loc[4, 'Mesure 3 Diastole'] + data_df.loc[5, 'Mesure 1 Diastole'] + data_df.loc[5, 'Mesure 2 Diastole'] + data_df.loc[5, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_3_sans_premiere_mesure = (data_df.loc[4, 'Mesure 2 Diastole'] + data_df.loc[4, 'Mesure 3 Diastole'] + data_df.loc[5, 'Mesure 2 Diastole'] + data_df.loc[5, 'Mesure 3 Diastole']) / 4
        else :
            moyenne_diastole_jour_3 = 0
        
        #Moyenne systole jour 4
        if data_df.loc[6, 'Mesure 1 Systole'] != None or data_df.loc[7, 'Mesure 1 Systole'] != None or data_df.loc[7, 'Mesure 1 Systole'] != None or data_df.loc[7, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_4 = (data_df.loc[6, 'Mesure 1 Systole'] + data_df.loc[6, 'Mesure 2 Systole'] + data_df.loc[6, 'Mesure 3 Systole'] + data_df.loc[7, 'Mesure 1 Systole'] + data_df.loc[7, 'Mesure 2 Systole'] + data_df.loc[7, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_4_sans_premiere_mesure = (data_df.loc[6, 'Mesure 2 Systole'] + data_df.loc[6, 'Mesure 3 Systole'] + data_df.loc[7, 'Mesure 2 Systole'] + data_df.loc[7, 'Mesure 3 Systole']) / 4
        else :
            moyenne_systole_jour_4 = 0
        
        #Moyenne diastole jour 4
        if data_df.loc[6, 'Mesure 1 Diastole'] != None or data_df.loc[7, 'Mesure 1 Diastole'] != None or data_df.loc[7, 'Mesure 1 Diastole'] != None or data_df.loc[7, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_4 = (data_df.loc[6, 'Mesure 1 Diastole'] + data_df.loc[6, 'Mesure 2 Diastole'] + data_df.loc[6, 'Mesure 3 Diastole'] + data_df.loc[7, 'Mesure 1 Diastole'] + data_df.loc[7, 'Mesure 2 Diastole'] + data_df.loc[7, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_4_sans_premiere_mesure = (data_df.loc[6, 'Mesure 2 Diastole'] + data_df.loc[6, 'Mesure 3 Diastole'] + data_df.loc[7, 'Mesure 2 Diastole'] + data_df.loc[7, 'Mesure 3 Diastole']) / 4
        else :
            moyenne_diastole_jour_4 = 0
            
        #Moyenne systole jour 5
        if data_df.loc[8, 'Mesure 1 Systole'] != None or data_df.loc[9, 'Mesure 1 Systole'] != None or data_df.loc[9, 'Mesure 1 Systole'] != None or data_df.loc[9, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_5 = (data_df.loc[8, 'Mesure 1 Systole'] + data_df.loc[8, 'Mesure 2 Systole'] + data_df.loc[8, 'Mesure 3 Systole'] + data_df.loc[9, 'Mesure 1 Systole'] + data_df.loc[9, 'Mesure 2 Systole'] + data_df.loc[9, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_5_sans_premiere_mesure = (data_df.loc[8, 'Mesure 2 Systole'] + data_df.loc[8, 'Mesure 3 Systole'] + data_df.loc[9, 'Mesure 2 Systole'] + data_df.loc[9, 'Mesure 3 Systole']) / 4
        else :
            moyenne_systole_jour_5 = 0
        
        #Moyenne diastole jour 5
        if data_df.loc[8, 'Mesure 1 Diastole'] != None or data_df.loc[9, 'Mesure 1 Diastole'] != None or data_df.loc[9, 'Mesure 1 Diastole'] != None or data_df.loc[9, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_5 = (data_df.loc[8, 'Mesure 1 Diastole'] + data_df.loc[8, 'Mesure 2 Diastole'] + data_df.loc[8, 'Mesure 3 Diastole'] + data_df.loc[9, 'Mesure 1 Diastole'] + data_df.loc[9, 'Mesure 2 Diastole'] + data_df.loc[9, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_5_sans_premiere_mesure = (data_df.loc[8, 'Mesure 2 Diastole'] + data_df.loc[8, 'Mesure 3 Diastole'] + data_df.loc[9, 'Mesure 2 Diastole'] + data_df.loc[9, 'Mesure 3 Diastole']) / 4
        else :
            moyenne_diastole_jour_5 = 0
        
        #Moyenne systole jour 6
        if data_df.loc[10, 'Mesure 1 Systole'] != None or data_df.loc[11, 'Mesure 1 Systole'] != None or data_df.loc[11, 'Mesure 1 Systole'] != None or data_df.loc[11, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_6 = (data_df.loc[10, 'Mesure 1 Systole'] + data_df.loc[10, 'Mesure 2 Systole'] + data_df.loc[10, 'Mesure 3 Systole'] + data_df.loc[11, 'Mesure 1 Systole'] + data_df.loc[11, 'Mesure 2 Systole'] + data_df.loc[11, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_6_sans_premiere_mesure = (data_df.loc[10, 'Mesure 2 Systole'] + data_df.loc[10, 'Mesure 3 Systole'] + data_df.loc[11, 'Mesure 2 Systole'] + data_df.loc[11, 'Mesure 3 Systole']) / 4
        else :
            moyenne_systole_jour_6 = 0
        
        #Moyenne diastole jour 6
        if data_df.loc[10, 'Mesure 1 Diastole'] != None or data_df.loc[11, 'Mesure 1 Diastole'] != None or data_df.loc[11, 'Mesure 1 Diastole'] != None or data_df.loc[11, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_6 = (data_df.loc[10, 'Mesure 1 Diastole'] + data_df.loc[10, 'Mesure 2 Diastole'] + data_df.loc[10, 'Mesure 3 Diastole'] + data_df.loc[11, 'Mesure 1 Diastole'] + data_df.loc[11, 'Mesure 2 Diastole'] + data_df.loc[11, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_6_sans_premiere_mesure = (data_df.loc[10, 'Mesure 2 Diastole'] + data_df.loc[10, 'Mesure 3 Diastole'] + data_df.loc[11, 'Mesure 2 Diastole'] + data_df.loc[11, 'Mesure 3 Diastole']) / 4
        else :
            moyenne_diastole_jour_6 = 0
        
        #Moyenne systole jour 7
        if data_df.loc[12, 'Mesure 1 Systole'] != None or data_df.loc[13, 'Mesure 1 Systole'] != None or data_df.loc[13, 'Mesure 1 Systole'] != None or data_df.loc[13, 'Mesure 1 Systole'] != None:
            moyenne_systole_jour_7 = (data_df.loc[12, 'Mesure 1 Systole'] + data_df.loc[12, 'Mesure 2 Systole'] + data_df.loc[12, 'Mesure 3 Systole'] + data_df.loc[13, 'Mesure 1 Systole'] + data_df.loc[13, 'Mesure 2 Systole'] + data_df.loc[13, 'Mesure 3 Systole']) / 6
            moyenne_systole_jour_7_sans_premiere_mesure = (data_df.loc[12, 'Mesure 2 Systole'] + data_df.loc[12, 'Mesure 3 Systole'] + data_df.loc[13, 'Mesure 2 Systole'] + data_df.loc[13, 'Mesure 3 Systole']) / 4
        else :
            moyenne_systole_jour_7 = 0
        
        #Moyenne diastole jour 7
        if data_df.loc[12, 'Mesure 1 Diastole'] != None or data_df.loc[13, 'Mesure 1 Diastole'] != None or data_df.loc[13, 'Mesure 1 Diastole'] != None or data_df.loc[13, 'Mesure 1 Diastole'] != None:
            moyenne_diastole_jour_7 = (data_df.loc[12, 'Mesure 1 Diastole'] + data_df.loc[12, 'Mesure 2 Diastole'] + data_df.loc[12, 'Mesure 3 Diastole'] + data_df.loc[13, 'Mesure 1 Diastole'] + data_df.loc[13, 'Mesure 2 Diastole'] + data_df.loc[13, 'Mesure 3 Diastole']) / 6
            moyenne_diastole_jour_7_sans_premiere_mesure = (data_df.loc[12, 'Mesure 2 Diastole'] + data_df.loc[12, 'Mesure 3 Diastole'] + data_df.loc[13, 'Mesure 2 Diastole'] + data_df.loc[13, 'Mesure 3 Diastole']) / 4
        else :
            moyenne_diastole_jour_7 = 0
        chart_data = {
        'Jour' : ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
        'Systole' : [moyenne_systole_jour_1, moyenne_systole_jour_2, moyenne_systole_jour_3, moyenne_systole_jour_4, moyenne_systole_jour_5, moyenne_systole_jour_6, moyenne_systole_jour_7],
        'Diastole' : [moyenne_diastole_jour_1, moyenne_diastole_jour_2, moyenne_diastole_jour_3, moyenne_diastole_jour_4, moyenne_diastole_jour_5, moyenne_diastole_jour_6, moyenne_diastole_jour_7]
    }
        
        chart_data_without_first_measure = {
        'Jour' : ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
        'Systole' : [moyenne_systole_jour_1_sans_premiere_mesure, moyenne_systole_jour_2_sans_premiere_mesure, moyenne_systole_jour_3_sans_premiere_mesure, moyenne_systole_jour_4_sans_premiere_mesure, moyenne_systole_jour_5_sans_premiere_mesure, moyenne_systole_jour_6_sans_premiere_mesure, moyenne_systole_jour_7_sans_premiere_mesure],
        'Diastole' : [moyenne_diastole_jour_1_sans_premiere_mesure, moyenne_diastole_jour_2_sans_premiere_mesure, moyenne_diastole_jour_3_sans_premiere_mesure, moyenne_diastole_jour_4_sans_premiere_mesure, moyenne_diastole_jour_5_sans_premiere_mesure, moyenne_diastole_jour_6_sans_premiere_mesure, moyenne_diastole_jour_7_sans_premiere_mesure]
    }
        chart_data_without_measure_day_1 = {
        'Jour' : ['Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7'],
        'Systole' : [moyenne_systole_jour_2, moyenne_systole_jour_3, moyenne_systole_jour_4, moyenne_systole_jour_5, moyenne_systole_jour_6, moyenne_systole_jour_7],
        'Diastole' : [moyenne_diastole_jour_2, moyenne_diastole_jour_3, moyenne_diastole_jour_4, moyenne_diastole_jour_5, moyenne_diastole_jour_6, moyenne_diastole_jour_7]
    }
        #draw chart
        st.write("")
        st.write("Points des valeurs moyennes de la pression artérielle")
        st.scatter_chart(chart_data, x='Jour', y=['Systole', 'Diastole'], color=['#F90000', '#0095F9'])
        
        st.write("Points des valeurs moyennes de la pression artérielle sans la première mesure")
        st.scatter_chart(chart_data_without_first_measure, x='Jour', y=['Systole', 'Diastole'], color=['#F90000', '#0095F9'])
        
        st.write("Points des valeurs moyennes de la pression artérielle sans les mesures du jour 1")
        st.scatter_chart(chart_data_without_measure_day_1, x='Jour', y=['Systole', 'Diastole'], color=['#F90000', '#0095F9'])
    else:
        st.markdown("Soumettre le formulaire pour afficher les courbes des valeurs moyennes")

elif page == 'Quiz':

    st.subheader('Testez vos connaissances ', divider='red')

    st.subheader("L'hypertension artérielle :anatomical_heart:")

    intro = '''L'HTA est un problème courant mais souvent mal compris, touchant des millions de personnes à travers le monde. 
         Elle se caractérise par une pression sanguine constamment élevée dans les vaisseaux.  
  
  **Pression artérielle** :
    
La pression artérielle, mesurée en deux valeurs (systolique et diastolique), est normalement en dessous de 120/80 mmHg. Au-delà de 140/90 mmHg, on parle généralement d'hypertension.

**Causes et conséquences de l'hypertension** :

Les causes incluent le mode de vie, l'hérédité, l'âge et d'autres facteurs comme l'obésité et le tabagisme.
Les conséquences peuvent être graves, augmentant le risque de maladies cardiovasculaires, de problèmes rénaux et de troubles de la vision.

**Gestion et traitement de l'HTA** :

Heureusement, l'HTA peut souvent être maîtrisée par des changements de mode de vie et, si nécessaire, des médicaments prescrits par un médecin.

**Conclusion et recommandations** :

Comprendre et gérer l'HTA est essentiel pour prévenir les complications graves et maintenir une bonne santé cardiovasculaire. Avec un mode de vie sain et en suivant les conseils médicaux, il est possible de contrôler efficacement la pression artérielle et de réduire les risques associés à cette condition.
    '''

    st.markdown(intro)

    st.divider()

    stb.single_choice("Combien de personnes souffrent d'HTA en France ? ",
                  ["5 Millions", "17 Millions", 
                  "20 Millions", "10 Millions"],
                  1,
                  "En effet ! 17 millions de personnes souffrent d'hypertension en France", 
                  "Essaie encore !", "Afficher la réponse")
    
    stb.single_choice("Combien d'adultes sont touchés par l'hypertension ? ",
                  ["1 adulte sur 3", "1 adulte sur 4", 
                  "1 adulte sur 2", "1 adulte sur 5"],
                  0,
                  "En effet ! 1 adulte sur 3 souffre d'hypertension en France", 
                  "Essaie encore !", "Afficher la réponse")
    stb.true_or_false("L'hypertension artérielle est le premier motif de consultation en médecine générale", 
                      True, 
                      "Et oui, l'hypertension est le premier motif de consultation en médecine générale", 
                      "Essaie encore !",
                      "Afficher la réponse")
    
    stb.multiple_choice("L'hypertension artérielle est le premier motif de consultation en médecine générale", 
                      {"Vrai":True,
                     "Faux":False},
                      "Et oui, l'hypertension est le premier motif de consultation en médecine générale", 
                      "Essaie encore !",
                      "Afficher la réponse")
