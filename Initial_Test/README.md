# Initial_Test

## Overview
A brief overview of Initial_Test - a generative AI project that initial exploration on generative AI and 
DeepSeek-Prover-V2-671B  model. 

## Project Structure
```
.                  
├── .env                    # file for environment variables  
├── hf_api.py               # main script
├── README.md               # This file
└── requirements.txt        # Python dependencies
```


## Usage

### Setting Up Project Environments

```bash
# Create a virtual environment for the current project
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt
```
### adding environment variables
create .env file and in that place :
```bash
HUGGINGFACEHUB_API_TOKEN='<Your Access Token>'
```
### Basic Usage
```bash
python hf_api.py
```

### possible modifications
```python
result=model.invoke('Your input prompt')
```

## Model Details
 - DeepSeek-Prover-V2-671B 