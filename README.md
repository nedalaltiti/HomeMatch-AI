# 🏡 HomeMatch-AI

**AI-powered personalized real estate search engine** using LLMs and vector embeddings.

<img width="1503" alt="image" src="https://github.com/user-attachments/assets/4482856f-4550-4aec-9dd1-0870ee6cd7e6" />
<img width="1503" alt="image" src="https://github.com/user-attachments/assets/3aae8681-4334-48a7-94b6-2b23eaefb44e" />

## 🚀 About the Project
HomeMatch is an AI-powered real estate search tool that personalizes property listings based on buyer preferences. By leveraging Large Language Models (LLMs) and vector databases, the application enhances standard real estate listings by tailoring descriptions to match users' unique needs.

### 🔹 **Core Features**
- 🔍 **Smart Search**: Uses **semantic search** to understand natural language queries for property hunting.
- 📝 **Personalized Listing Descriptions**: AI-generated descriptions that highlight features important to the buyer.
- 🖼️ **Multimodal Search**: Searches **both text and images** to enhance property discovery.
- ⚡ **Real-time Recommendations**: Generates property listings dynamically based on user inputs.
- 🎨 **User-Friendly UI**: Interactive web application built with **Gradio**.

## 🏗️ **Project Structure**
```
HomeMatch-AI/
│── chroma_db
│── images/ 
│── .gitignore 
│── HomeMatch.ipynb
│── data_loader.py
│── search.py
│── ui.py
│── README.md 
│── listings.csv
│── listings_cache.pkl
│── requirements.txt 
```

## 🛠️ **Installation & Setup**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/nedalaltiti/HomeMatch-AI.git
cd HomeMatch-AI

python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install -r requirements.txt
```
Option 1: Run in Jupyter Notebook
```bash
Open HomeMatch.ipynb and run the cells.
```
Option 2: Run Gradio UI
```bash
python app.py
```
This will generate a local URL to access the app.

**Note:** The application falls back to an image named `default_image.png` when
 a listing has no associated photo. Ensure `images/default_image.png` exists or
 set the `DEFAULT_IMAGE` environment variable to point to a custom file.

## ⚙️ Configuration
HomeMatch-AI uses a small [Pydantic](https://docs.pydantic.dev/) settings class for configuration.
Copy the provided `.env.example` to `.env` and adjust any values as needed. These environment variables control paths and search behavior:

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `LISTINGS_CSV` | `listings.csv` | Path to the property CSV file |
| `VECTOR_DB_DIR` | `chroma_db` | Directory holding the vector database |
| `CACHE_FILE` | `listings_cache.pkl` | Pickle file used for caching the dataframe |
| `IMAGES_DIR` | `images` | Directory containing listing images |
| `DEFAULT_IMAGE` | `default_image.png` | Fallback image when a listing photo is missing |
| `TOP_K` | `5` | Number of search results returned from the vector DB |
 
## 📊 How It Works

### 🏡 1. Collect Buyer Preferences  
Users enter their desired budget, number of bedrooms, preferred location, must-have features, and property type.

### 🔎 2. Vector Search in Database  
- The entered preferences are converted into vector embeddings.  
- A vector search is performed on the database to find the closest matching properties.  

### 🎯 3. AI-Generated Personalized Listings  
- LLMs rewrite the property descriptions to highlight features the buyer cares about.  
- Images of the listings are retrieved and displayed along with personalized text.  

## 🎨 Demo UI (Gradio)

The project includes a **Gradio-powered UI** for an interactive real estate search experience.

### 🚀 Run the UI  
```bash
python app.py
```


