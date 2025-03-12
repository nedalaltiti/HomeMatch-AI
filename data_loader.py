import os
import logging
import joblib
import pandas as pd
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_experimental.open_clip import OpenCLIPEmbeddings

# Load environment variables from .env
LISTINGS_CSV = os.getenv("LISTINGS_CSV", "listings.csv")  
VECTOR_DB_DIR = os.getenv("VECTOR_DB_DIR", "chroma_db")
IMAGES_DIR = os.getenv("IMAGES_DIR", "images")
CACHE_FILE = os.getenv("CACHE_FILE", "listings_cache.pkl")
DEFAULT_IMAGE = os.getenv("DEFAULT_IMAGE", "default_image.png")

def load_dataframe():
    """Loads the listings DataFrame from CSV or cache, returns df and df_dict."""
    try:
        if os.path.exists(CACHE_FILE):
            df = joblib.load(CACHE_FILE)
            logging.info("✅ Loaded property listings from cache.")
        else:
            df = pd.read_csv(LISTINGS_CSV, dtype={
                "price": str, 
                "bedrooms": str, 
                "bathrooms": str, 
                "house_size": str
            })
            joblib.dump(df, CACHE_FILE)
            logging.info("✅ Successfully loaded and cached property listings.")
        # Also build a dictionary version
        df_dict = df.set_index("id").to_dict(orient="index")
        return df, df_dict
    except Exception as e:
        logging.error(f"🚨 Error loading CSV file: {e}")
        raise RuntimeError("Failed to load property data.")

def load_vector_db():
    """Initializes and returns the Chroma vector store."""
    if not os.path.exists(VECTOR_DB_DIR):
        msg = "⚠️ Vector database missing! Ensure data is preprocessed."
        logging.warning(msg)
        # Optionally raise an exception or just continue with empty store
        # raise RuntimeError(msg)

    try:
        db = Chroma(
            persist_directory=VECTOR_DB_DIR, 
            collection_name="listings",
            embedding_function=OpenCLIPEmbeddings()
        )
        if db._collection.count() == 0:
            logging.warning("🚨 Warning: No data in ChromaDB. Rebuild the vector store.")
        logging.info("✅ Vector database loaded successfully.")
        return db
    except Exception as e:
        logging.error(f"🚨 Error initializing vector database: {e}")
        raise RuntimeError("Vector database initialization failed.")
