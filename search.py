import os
import logging
import gradio as gr

# We'll assume data_loader has provided us df, df_dict, db
df = None
df_dict = None
db = None

# We'll keep a global for last_search_ids
last_search_ids = []

def init_globals(the_df, the_df_dict, the_db):
    """
    Call this once in app.py after you load the data and DB 
    so we can store them in our module-level variables.
    """
    global df, df_dict, db
    df = the_df
    df_dict = the_df_dict
    db = the_db

def search_listings(budget, bedrooms, neighborhood, features, property_type):
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

    search_results = db.similarity_search(query, k=5)
    results = []

    for res in search_results:
        prop_id = res.metadata["id"]
        last_search_ids.append(prop_id)

        # Check if there's an image
        images_dir = os.getenv("IMAGES_DIR", "images")
        default_image = os.getenv("DEFAULT_IMAGE", "default_image.png")
        img_path = os.path.join(images_dir, f"{prop_id}.png")
        if not os.path.exists(img_path):
            img_path = default_image

        # Retrieve the row from df_dict (avoid slow df lookups)
        row_data = df_dict.get(prop_id, {})
        description = row_data.get("description", "No description available.")

        results.append((img_path, f"Listing ID: {prop_id}"))


    if not results:
        return [("⚠️ No Listings Found", "No properties match your criteria.")]
    return results

def personalize_description(evt):
    """
    Retrieves the personalized listing description when a user selects a gallery item.
    Expects evt to be a dict with an "index" key.
    """
    try:
        # Check that the event data contains an "index"
        if evt is None or "index" not in evt:
            raise ValueError("Invalid event data received.")
        
        selected_index = evt["index"]
        if selected_index < 0 or selected_index >= len(last_search_ids):
            raise ValueError("Index out of range for last_search_ids.")
        
        listing_id = last_search_ids[selected_index]
        listing_info = df_dict.get(listing_id, {})
        return listing_info.get("description", "No description available.")
    except Exception as e:
        logging.error(f"🚨 Error fetching personalized description: {e}")
        return "Error retrieving description."
    
def personalize_description(evt: gr.SelectData):
    """
    evt.value: content of the selected gallery item
    evt.index: the 0-based index of the selection
    """
    import logging
    global last_search_ids, df_dict

    try:
        if evt.index < 0 or evt.index >= len(last_search_ids):
            raise ValueError("Index out of range for last_search_ids.")

        listing_id = last_search_ids[evt.index]
        listing_info = df_dict.get(listing_id, {})
        return listing_info.get("description", "No description available.")
    except Exception as e:
        logging.error(f"🚨 Error fetching personalized description: {e}")
        return "Error retrieving description."
