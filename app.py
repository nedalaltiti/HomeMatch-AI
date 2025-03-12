import logging
from dotenv import load_dotenv
from data_loader import load_dataframe, load_vector_db
from search import init_globals
from ui import create_ui

def main():
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler("app.log")]
    )

    # Load environment
    load_dotenv()

    # Load data
    df, df_dict = load_dataframe()
    db = load_vector_db()

    # Initialize search module's globals
    init_globals(df, df_dict, db)

    # Create the UI
    demo = create_ui()
    # Launch
    demo.launch(share=True, debug=True)

if __name__ == "__main__":
    main()
