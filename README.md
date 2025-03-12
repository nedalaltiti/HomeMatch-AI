# 🏡 HomeMatch-AI

<img width="1503" alt="image" src="https://github.com/user-attachments/assets/ae74ce97-2c0b-4484-90b1-445d1007492e" />

**AI-powered personalized real estate search engine** using LLMs and vector embeddings.


## 🚀 About the Project
HomeMatch is an AI-powered real estate search tool that personalizes property listings based on buyer preferences. By leveraging Large Language Models (LLMs) and vector databases, the application enhances standard real estate listings by tailoring descriptions to match users' unique needs.

![Alt Text](images/my-image.png)

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


