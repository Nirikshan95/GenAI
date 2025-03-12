# TinyLlama_Initial_Test

## Overview
A brief overview of TinyLlama_Initial_Test - a generative AI project that initial exploration on generative AI and TinyLlama model. 

## Project Structure
```
.
├── venv/                   
├── .env/                   # file for environment variables  
├── hf_api.py               # main script
├── README.md               # This file
└── requirements.txt        # Python dependencies
```


## Usage

### adding environment variables
create .env file and in that place :
```bash
HUGGINGFACEHUB_ACCESS_TOKEN='<Your Access Token>'
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
 - TinyLlama model