import pickle
import warnings
import pandas as pd
from transformers import pipeline
import streamlit as st
import clipboard

warnings.filterwarnings("ignore")



# Fonction de traduction

def translation(text, trad):
    
    translator = pipeline(trad)
    outputs = translator(text, clean_up_tokenization_spaces = True, max_length = 100000)
   
    return(outputs[0]["translation_text"])
    
# Fonction resumé d'un texte    
    
def summarizer(text):
    summarizer = pipeline("summarization")
    outputs = summarizer(text, clean_up_tokenization_spaces = True)
    return outputs[0]["summary_text"]
    
# Fonction de classification

def classification(text):
    classifier = pipeline("text-classification")
    outputs = classifier(text)
    return pd.DataFrame(outputs)

# Fonction d'identification

def identificateur(text):
    ner_tagger = pipeline("ner", aggregation_strategy = "simple")
    outputs = ner_tagger(text)
    return pd.DataFrame(outputs)

# Fonction réponse aux questions

def quest_ans(text, questions):
    reader = pipeline("question-answering")
    results = []

    for question in questions:
        outputs = reader(question = question, context = text)
        results.append(outputs)
    
    return pd.DataFrame(results)




# Personnaliser le style des boutons    
style = """
<style>
    div[data-testid="stButton"] button {
        background-color: blue;
        color: white;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        cursor: pointer;
    }
</style>
"""
st.markdown(style, unsafe_allow_html=True)
col1, col2 =  st.columns(2)
def page_traduction():
    st.title('Page de traduction de texte')
    st.markdown("**Page de traduction de Texte Anglais en Francais, Allemand et Romain**") 


    # Liste des options de réponse
    traducteurs = ['Anglais-Francais', 'Anglais-Allemand', 'Anglais-Romain']

    # selectbox pour choisir parmi les traducteurs
    traducteur = st.selectbox('Choisissez le traducteur:', traducteurs)

    if(traducteur == "Anglais-Francais"):
        text1 = st.text_area("Entrez le texte à traduire en Francais", height=200, help="Taper votre Texte ici")

                
        if st.button("Traduire") and not text1:
            st.warning("La zone de texte est obligatoire. Veuillez saisir du texte avant de traduire.")
        elif text1:
            if(len(text1) > 300) :
                split_text = text1.split(".")
                traduit1 = [translation(sentence, "translation_en_to_fr") for  sentence in split_text]
                traduit = " ".join(traduit1)
                    
            else :
                traduit = translation(text1, "translation_en_to_fr")
                
            st.subheader('Résultat de la traduction')
            
            st.success(traduit)

            if st.button("Copier Résultat"):
                    clipboard.copy(traduit)
                    st.info("Résultat copié")
                        
    if(traducteur == "Anglais-Romain"):
        text1 = st.text_area("Entrez le texte à traduire en Romain", height=200, help="Taper votre Texte ici")


        if st.button("Traduire") and not text1:
            st.warning("La zone de texte est obligatoire. Veuillez saisir du texte avant de traduire.")
        elif text1:
            if(len(text1) > 300) :
                split_text = text1.split(".")
                traduit1 = [translation(sentence, "translation_en_to_ro") for  sentence in split_text]
                traduit = " ".join(traduit1)
                    
            else :
                traduit = translation(text1, "translation_en_to_ro")
                
            st.subheader('Résultat de la traduction')
            
            st.success(traduit)

            if st.button("Copier Résultat"):
                    clipboard.copy(traduit)
                    st.info("Résultat copié")
                        
    if(traducteur == "Anglais-Allemand"):
        text1 = st.text_area("Entrez le texte à traduire en Allemand", height=200, help="Taper votre Texte ici")


        if st.button("Traduire") and not text1:
            st.warning("La zone de texte est obligatoire. Veuillez saisir du texte avant de traduire.")
        elif text1:
            if(len(text1) > 300) :
                split_text = text1.split(".")
                traduit1 = [translation(sentence, "translation_en_to_de") for  sentence in split_text]
                traduit = " ".join(traduit1)
                    
            else :
                traduit = translation(text1, "translation_en_to_de")
                
            st.subheader('Résultat de la traduction')
            
            st.success(traduit)

            if st.button("Copier Résultat"):
                    clipboard.copy(traduit)
                    st.info("Résultat copié")
                    

                

        

def page_accueil():
    st.title("Natural Language Processing with Transformers Application")

    
    
def page_resumer():
    st.title("Page de resumé de textes")

    text2 = st.text_area("Entrer le texte à resumé", height=200, help="Taper votre Texte ici")
    
    if st.button("Resumé") and not text2:
        st.warning("La zone de texte est obligatoire. Veuillez saisir du texte avant de traduire.")
    elif text2:
        resumer = summarizer(text2)
        st.subheader("Voici votre resumé")
        
        st.success(resumer)
        
        if st.button("Copier Résultat"):
                    clipboard.copy(traduit)
                    st.info("Résultat copié")
                    
def page_identificateur():
    st.title("Page d'identificateur")

    text3 = st.text_area("Entrer le texte ", height=200, help="Taper votre Texte ici")
    
    if st.button("Identificateur") and not text3:
        st.warning("La zone de texte est obligatoire. Veuillez saisir du texte avant de traduire.")
    elif text3:
        Ident = identificateur(text3)
        st.subheader("identificateur")
        
        st.success(Ident)
        
        if st.button("Copier Résultat"):
                    clipboard.copy(traduit)
                    st.info("Résultat copié")

def page_classification():
    st.title("Page de classification")

    text3 = st.text_area("Entrer le texte ", height=200, help="Taper votre Texte ici")
    
    if st.button("Classifier") and not text3:
        st.warning("La zone de texte est obligatoire. Veuillez saisir du texte avant de traduire.")
    elif text3:
        Ident = classification(text3)
        st.subheader("Resultat de la classification")
        
        st.success(Ident)
        
        if st.button("Copier Résultat"):
                    clipboard.copy(traduit)
                    st.info("Résultat copié")
    
def page_quest_ans():
    st.title("Page de question-Reponse")
    
    text3 = st.text_area("Entrer le texte ", height=200, help="Taper votre Texte ici")
    quest = st.text_area("Entrer la question ", height=100, help="Taper votre question ici")
    
    if st.button("Question") and (not text3 or not quest ):
        st.warning("La zone de texte est obligatoire. Veuillez saisir du texte avant de traduire.")
    elif text3 and quest:
        Ident = quest_ans(text3, quest)
        st.subheader("La réponse de votre question")
        
        st.success(Ident)
        
        if st.button("Copier Résultat"):
                    clipboard.copy(traduit)
                    st.info("Résultat copié")

def main():
    st.sidebar.title("Navigation")

    # Ajouter des liens dans la barre latérale pour naviguer entre les pages
    selection = st.sidebar.radio("Sélectionnez une page", ["Accueil", "Traduction", "Resumer","Classification","Identificateur","Question-Reponse"])
    # Personnaliser la mise en forme du radio bouton

    # Afficher la page sélectionnée
    if selection == "Accueil":
        page_accueil()
    elif selection == "Traduction":
        page_traduction()
    elif selection == "Resumer":
        page_resumer()
    elif selection == "Classification":
        page_classification()
    elif selection == "Identificateur":
        page_identificateur()
    elif selection == "Question-Reponse":
        page_quest_ans()

if __name__ == "__main__":
    main()


