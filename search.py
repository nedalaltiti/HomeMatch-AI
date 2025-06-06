import os
import logging
from typing import Any, List, Tuple

import gradio as gr

from config import IMAGES_DIR, DEFAULT_IMAGE, TOP_K

# We'll assume data_loader has provided us df, df_dict, db
df = None
df_dict = None
db = None

# We'll keep a global for last_search_ids
last_search_ids = []

def init_globals(the_df: Any, the_df_dict: dict[str, Any], the_db: Any) -> None:
    """
    Call this once in app.py after you load the data and DB 
    so we can store them in our module-level variables.
    """
    global df, df_dict, db
    df = the_df
    df_dict = the_df_dict
    db = the_db

def search_listings(
    budget: str,
    bedrooms: str,
    neighborhood: str,
    features: str,
    property_type: str,
) -> list[tuple[str, str]]:
    """
    Searches vector database based on user input preferences and returns matched listings 
    in the form of a list of (image_path, label) tuples for Gradio's Gallery.
    """
    global last_search_ids
    last_search_ids.clear()

    query = (
        f"Budget: {budget}. "
        f"Bedrooms: {bedrooms}. "
        f"Neighborhood: {neighborhood}. "
        f"Features: {features}. "
        f"Property type: {property_type}."
    )
    logging.info(f"Search query: {query}")

    if db is None:
        return [("⚠️ No DB Found", "Please check vector DB initialization")]

    search_results = db.similarity_search(query, k=TOP_K)
    results = []

    for res in search_results:
        prop_id = res.metadata["id"]
        last_search_ids.append(prop_id)

        img_path = os.path.join(IMAGES_DIR, f"{prop_id}.png")
        if not os.path.exists(img_path):
            img_path = DEFAULT_IMAGE

        results.append((img_path, f"Listing ID: {prop_id}"))


    if not results:
        return [("⚠️ No Listings Found", "No properties match your criteria.")]
    return results

def personalize_description(evt: gr.SelectData) -> str:
    """Return the description for the item selected in the gallery."""
    global last_search_ids, df_dict

    try:
        idx = getattr(evt, "index", None)
        if idx is None or idx < 0 or idx >= len(last_search_ids):
            raise ValueError("Index out of range for last_search_ids.")

        listing_id = last_search_ids[idx]
        listing_info = df_dict.get(listing_id, {})
        return listing_info.get("description", "No description available.")
    except Exception as e:
        logging.error(f"🚨 Error fetching personalized description: {e}")
        return "Error retrieving description."
