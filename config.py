import os
from dotenv import load_dotenv

load_dotenv()

# Paths and files
LISTINGS_CSV = os.getenv("LISTINGS_CSV", "listings.csv")
VECTOR_DB_DIR = os.getenv("VECTOR_DB_DIR", "chroma_db")
CACHE_FILE = os.getenv("CACHE_FILE", "listings_cache.pkl")
IMAGES_DIR = os.getenv("IMAGES_DIR", "images")
DEFAULT_IMAGE = os.getenv("DEFAULT_IMAGE", "default_image.png")

# Search settings
TOP_K = int(os.getenv("TOP_K", "5"))
