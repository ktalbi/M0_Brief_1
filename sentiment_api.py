from fastapi import FastAPI,HTTPException
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer
from pydantic import BaseModel 
from loguru import logger


app = FastAPI(title="SentimentAnalyzer", version="1.0.0")

# Inclure les routes
#app.include_router(routes_user.router, prefix="/api/v1/users", tags=["Users"])

# Pydantic
class Texte(BaseModel):
    texte: str

# initialisation de l'analyzer
sia = SentimentIntensityAnalyzer()

# Logs
Path("logs").mkdir(parents=True, exist_ok=True)
logger.remove()
logger.add("logs/sentiment_api.log", rotation="500 MB", level="INFO")


@app.post("/analyse_sentiment/")
async def analyse_sentiment(texte_object: Texte):
    logger.info(f"Analyse du texte: {texte_object.texte}")
    try:
        sentiment = sia.polarity_scores(texte_object.texte)
        logger.info(f"Résultats: {sentiment}")
        # on retourne la réponse
        return {
            "neg": sentiment["neg"],
            "neu": sentiment["neu"],
            "pos": sentiment["pos"],
            "compound": sentiment["compound"],
        }

    except Exception as e:
        logger.error(f"Erreur lors de l'analyse: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/")
async def root():
    return {"message": "OK - POST /analyse_sentiment/ avec {'texte': '...'}"}