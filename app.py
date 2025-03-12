import gradio as gr
import pandas as pd
import os
import logging
from langchain_community.vectorstores import Chroma
from langchain_experimental.open_clip import OpenCLIPEmbeddings

# ✅ Define Paths
IMAGES_DIR = "images"
LISTINGS_CSV = "listings.csv"
VECTOR_DB_DIR = "chroma_db"  # Directory to store the vector database

# ✅ Load Property Data
try:
    df = pd.read_csv(LISTINGS_CSV, dtype={"price": str, "bedrooms": str, "bathrooms": str, "house_size": str})
    print("✅ Successfully loaded property listings.")
except Exception as e:
    logging.error(f"🚨 Error loading CSV file: {e}")
    exit()

# ✅ Load Vector Database
if not os.path.exists(VECTOR_DB_DIR):
    logging.warning("⚠️ Vector database missing! Ensure data is preprocessed before running the app.")
    exit()

try:
    db = Chroma(persist_directory=VECTOR_DB_DIR, collection_name="listings", embedding_function=OpenCLIPEmbeddings())
    print("✅ Vector database loaded successfully.")
except Exception as e:
    logging.error(f"🚨 Error initializing vector database: {e}")
    exit()

# ✅ Function: Search Listings
def search_listings(budget, bedrooms, neighborhood, features, property_type):
    """ Searches vector database based on user input preferences and returns matched listings. """
    
    query = f"Budget: {budget}, Bedrooms: {bedrooms}, Neighborhood: {neighborhood}, Features: {features}, Type: {property_type}"
    
    search_results = db.similarity_search(query, k=5)
    
    results = []
    for res in search_results:
        prop_id = res.metadata["id"]
        img_path = os.path.join(IMAGES_DIR, f"{prop_id}.png")

        # Handle missing images
        if os.path.exists(img_path):
            results.append((img_path, df.iloc[prop_id]['description']))
        else:
            logging.warning(f"⚠️ Image missing for listing ID {prop_id}")
            results.append(("⚠️ Image Not Found", df.iloc[prop_id]['description']))

    return results if results else [("⚠️ No Listings Found", "No properties match your search criteria.")]

# ✅ Function: Retrieve Personalized Listing Description
def personalize_description(evt: gr.SelectData):
    """ Retrieves personalized listing description when a user selects a listing. """
    try:
        listing_id = int(evt.value.split('/')[-1].split('.')[0])  # Extract listing ID from filename
        return df.iloc[listing_id]["description"]
    except Exception as e:
        logging.error(f"🚨 Error fetching personalized description: {e}")
        return "Error retrieving description."

# ✅ Gradio UI Layout
def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## 🏡 HomeMatch: Your Personalized Real Estate Search")

        with gr.Tabs():
            with gr.TabItem("Buyer's Preferences"):
                with gr.Row():
                    budget = gr.Textbox(label="What is your budget range?")
                    bedrooms = gr.Textbox(label="How many bedrooms do you need?")
                    neighborhood = gr.Textbox(label="Do you prefer a specific neighborhood?")
                    features = gr.Textbox(label="Any must-have features? (e.g., balcony, garden, garage)")
                    property_type = gr.Textbox(label="What type of property do you prefer? (e.g., apartment, villa, townhouse)")

                search_btn = gr.Button("Find My Home 🏠")

            with gr.TabItem("Search Results"):
                with gr.Row():
                    gallery = gr.Gallery(label="Recommended Listings", columns=3, rows=2, allow_preview=True, object_fit="cover")
                with gr.Row():
                    personalized_desc = gr.Textbox(label="Personalized Description", interactive=False)

        # ✅ Event Handlers
        search_btn.click(
            fn=search_listings, 
            inputs=[budget, bedrooms, neighborhood, features, property_type], 
            outputs=gallery
        )

        gallery.select(
            fn=personalize_description, 
            inputs=None, 
            outputs=personalized_desc
        )
        
    return demo

# ✅ Launch Application
if __name__ == "__main__":
    demo = create_ui()
    demo.launch(share=True, debug=True)
