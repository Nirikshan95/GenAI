# Story Generator Project

## Overview
A simple story generator application that creates customized stories based on user-selected story types. This project demonstrates the integration of TinyLlama model with a Streamlit interface, leveraging the power of generative AI to create original stories on demand.

## Project Structure
```
.
├── venv/                   
├── .env                    # File for environment variables  
├── story_gen.py            # Main application script
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

## Usage
### Adding Environment Variables
Create a `.env` file in the project directory and add your Hugging Face access token:
```bash
HUGGINGFACEHUB_ACCESS_TOKEN='<Your Access Token>'
```

### Running the Application
To run the Streamlit application:
```bash
streamlit run story_gen.py --server.fileWatcherType none
```

### User Interaction
1. Launch the Streamlit app using the command above
2. Enter your desired story type from the available options
3. The application will generate a unique story based on your selection

## Model Details
- The application currently uses the TinyLlama model from Hugging Face
- PromptTemplate from LangChain is utilized to format user inputs into appropriate prompts