import gradio as gr
import pandas as pd
import os
from PIL import Image
from langchain.vectorstores import Chroma
from langchain_experimental.open_clip import OpenCLIPEmbeddings

# ✅ Define Paths
IMAGES_DIR = "images"
LISTINGS_CSV = "listings.csv"

# ✅ Load Property Data
try:
    df = pd.read_csv(LISTINGS_CSV, dtype={"price": str, "bedrooms": str, "bathrooms": str, "house_size": str})
except Exception as e:
    print(f"🚨 Error loading CSV file: {e}")
    exit()

# ✅ Load Vector Database
try:
    db = Chroma(collection_name="listings", embedding_function=OpenCLIPEmbeddings())
except Exception as e:
    print(f"🚨 Error initializing vector database: {e}")
    exit()

# ✅ Function: Search Listings
def search_listings(budget, bedrooms, neighborhood, features, property_type):
    """ Searches vector database based on user input preferences and returns matched listings. """

    # Build a query string from user inputs
    query = f"Budget: {budget}, Bedrooms: {bedrooms}, Neighborhood: {neighborhood}, Features: {features}, Type: {property_type}"
    
    # Perform similarity search
    search_results = db.similarity_search(query, k=5)
    
    # Extract results
    results = []
    for res in search_results:
        prop_id = res.metadata["id"]
        img_path = os.path.join(IMAGES_DIR, f"{prop_id}.png")

        # Ensure the image exists before displaying
        if os.path.exists(img_path):
            results.append((img_path, df.iloc[prop_id]['description']))
        else:
            results.append(("⚠️ Image Not Found", df.iloc[prop_id]['description']))

    return results

# ✅ Function: Personalize Listing Description
def personalize_description(evt: gr.SelectData):
    """ Retrieves personalized listing description when a user selects a listing. """
    listing_id = int(evt.value.split('/')[-1].split('.')[0])  # Extract ID from filename
    return df.iloc[listing_id]["description"]

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
                    gallery = gr.Gallery(label="Recommended Listings", columns=3, rows=2, allow_preview=True)
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
    demo.launch()
