import os
import logging
import joblib
import pandas as pd
from langchain_community.vectorstores import Chroma
from langchain_experimental.open_clip import OpenCLIPEmbeddings

from config import settings


def load_dataframe():
    """Load the property listings DataFrame from CSV or cache.

    Returns a tuple ``(df, df_dict)`` where ``df_dict`` maps IDs to row data.
    """
    try:
        if os.path.exists(settings.cache_file):
            df = joblib.load(settings.cache_file)
            logging.info("✅ Loaded property listings from cache.")
        else:
            df = pd.read_csv(settings.listings_csv, dtype={
                "price": str, 
                "bedrooms": str, 
                "bathrooms": str, 
                "house_size": str
            })
            joblib.dump(df, settings.cache_file)
            logging.info("✅ Successfully loaded and cached property listings.")
        # Also build a dictionary version
        df_dict = df.set_index("id").to_dict(orient="index")
        return df, df_dict
    except Exception as e:
        logging.error(f"🚨 Error loading CSV file: {e}")
        raise RuntimeError("Failed to load property data.")

def load_vector_db():
    """Initializes and returns the Chroma vector store."""
    if not os.path.exists(settings.vector_db_dir):
        msg = "⚠️ Vector database missing! Ensure data is preprocessed."
        logging.warning(msg)
        # Optionally raise an exception or just continue with empty store
        # raise RuntimeError(msg)

    try:
        db = Chroma(
            persist_directory=settings.vector_db_dir,
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
