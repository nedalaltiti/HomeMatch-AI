# 🏡 HomeMatch-AI

**AI-powered personalized real estate search engine** using LLMs and vector embeddings.


## 🚀 About the Project
HomeMatch-AI transforms traditional real estate listings into **personalized** narratives tailored to each buyer’s preferences. Leveraging **LLMs, vector databases, and multimodal embeddings**, it helps buyers find the perfect home by **matching their input preferences with real estate listings.**

### 🔹 **Core Features**
- 🔍 **Smart Search**: Uses **semantic search** to understand natural language queries for property hunting.
- 📝 **Personalized Listing Descriptions**: AI-generated descriptions that highlight features important to the buyer.
- 🖼️ **Multimodal Search**: Searches **both text and images** to enhance property discovery.
- ⚡ **Real-time Recommendations**: Generates property listings dynamically based on user inputs.
- 🎨 **User-Friendly UI**: Interactive web application built with **Gradio**.

## 🏗️ **Project Structure**
```
HomeMatch-AI/
│── images/ 
│── .gitignore 
│── HomeMatch.ipynb 
│── README.md 
│── listings.csv 
│── requirements.txt 
```

## 📦 **Installation & Setup**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/nedalaltiti/HomeMatch-AI.git
cd HomeMatch-AI

python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install -r requirements.txt

🛠️ How to Run
Option 1: Run in Jupyter Notebook

Open HomeMatch.ipynb and run the cells.

Option 2: Run Gradio UI
python app.py
```
Then, open the link shown in the terminal to interact with the UI.

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


