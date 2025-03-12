import gradio as gr
import logging
from search import search_listings, personalize_description

def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## 🏡 HomeMatch: Your Personalized Real Estate Search")

        with gr.Tabs():
            with gr.TabItem("Buyer's Preferences"):
                with gr.Row():
                    budget = gr.Textbox(label="What is your budget range?")
                    bedrooms = gr.Dropdown(
                        choices=["Studio", "1", "2", "3+", "Any"], 
                        label="How many bedrooms do you need?"
                    )
                    neighborhood = gr.Textbox(label="Do you prefer a specific neighborhood?")
                    features = gr.Textbox(label="Any must-have features? (e.g., balcony, garden, garage)")
                    property_type = gr.Dropdown(
                        choices=["Apartment", "Villa", "Townhouse", "Any"], 
                        label="What type of property do you prefer?"
                    )

                search_btn = gr.Button("Find My Home 🏠")

            with gr.TabItem("Search Results"):
                with gr.Row():
                    gallery = gr.Gallery(
                        label="Recommended Listings", 
                        columns=3, rows=2, 
                        allow_preview=True, 
                        object_fit="cover"
                    )
                with gr.Row():
                    personalized_desc = gr.Textbox(label="Personalized Description", interactive=False)

        # Event Handlers
        search_btn.click(
            fn=search_listings,
            inputs=[budget, bedrooms, neighborhood, features, property_type],
            outputs=gallery
        )

        gallery.select(
            fn=personalize_description,
            inputs=None,  # Gradio automatically passes the event object
            outputs=personalized_desc
        )

    return demo
