import requests
import streamlit as st
from loguru import logger
from pathlib import Path

#  Config Streamlit 
st.set_page_config(page_title="Analyse de sentiment",  layout="centered")
st.title("🧠 Analyse de sentiment (VADER)")
st.caption("Client Streamlit pour l'API FastAPI /analyse_sentiment/")

#  Logger 
Path("logs").mkdir(parents=True, exist_ok=True)
logger.remove()
logger.add("logs/streamlit_app.log", rotation="500 MB", level="INFO")

#  UI 
with st.sidebar:
    st.header("Paramètres")
    api_base_url = st.text_input(
        "URL de l'API",
        value="http://127.0.0.1:9000",
    )

st.subheader("Entrez un texte à analyser")
texte = st.text_area("Texte", height=180, placeholder="Saisis ici le texte à analyser…")


if st.button("Analyser"):
    if texte and texte.strip():
        logger.info(f"Texte à analyser: {texte[:300]}{'...' if len(texte) > 300 else ''}")
        try:
            # Envoi à l'API
            url = f"{api_base_url.rstrip('/')}/analyse_sentiment/"
            with st.spinner("Analyse en cours…"):
                response = requests.post(url, json={"texte": texte})
                # Lève une exception pour les codes HTTP d'erreur
                response.raise_for_status()
                sentiment = response.json()

            # Affichage des résultats
            st.success("Analyse réussie ✅")
            st.write("### Résultats de l'analyse :")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Négatif", f"{sentiment['neg']:.3f}")
            col2.metric("Neutre", f"{sentiment['neu']:.3f}")
            col3.metric("Positif", f"{sentiment['pos']:.3f}")
            col4.metric("Composé", f"{sentiment['compound']:.3f}")

            # Interprétation du score composé
            if sentiment["compound"] >= 0.05:
                st.write("**Sentiment global : Positif 😀**")
            elif sentiment["compound"] <= -0.05:
                st.write("**Sentiment global : Négatif 🙁**")
            else:
                st.write("**Sentiment global : Neutre 😐**")

            logger.info(f"Résultats affichés: {sentiment}")

        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de connexion à l'API : {e}")
            logger.error(f"Erreur de connexion à l'API : {e}")
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")
            logger.error(f"Une erreur est survenue : {e}")
    else:
        st.warning("Veuillez entrer du texte pour l'analyse.")