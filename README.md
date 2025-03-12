# Generative AI – Practice & Exploration Hub

A structured workspace for hands-on learning and experimentation with Generative AI models, techniques, and frameworks.

## Introduction

This repository serves as a comprehensive learning platform for exploring various aspects of Generative AI. It provides a structured approach to understanding, implementing, and experimenting with different generative models - from large language models to diffusion-based image generators. Each project is organized in dedicated branches, allowing focused learning while maintaining a clean workspace.

## Project Structure

- **Main Branch**: Acts as an index and navigation hub, providing an overview of all projects
- **Model-Specific Branches**: Each branch corresponds to a particular generative AI technique or model implementation
- **Isolated Environments**: Every project has its own virtual environment and dependency management to prevent conflicts

## How to Use

### Navigating Projects

```bash
# Clone the repository
git clone https://github.com/yourusername/Generative-AI.git
cd Generative-AI

# List all available branches
git branch -a

# Switch to a specific project branch
git checkout <branch-name>
cd <branch-name>
```

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
# Then refer the README.md which is available on <branch-name> folder

## Learning Path

This repository follows a structured learning path across different branches:

1. **Foundation Models**: Understanding base architectures and capabilities
2. **Fine-Tuning & Adaptation**: Customizing models for specific tasks and domains
3. **Optimization & Inference**: Running models efficiently with various techniques
4. **Multimodal Integration**: Combining text, image, and audio generation
5. **Production Deployment**: Moving from experimentation to usable applications

## Project List

| Branch | Description | Key Technologies |
|--------|-------------|------------------|
| **TinyLlama_Initial_Test** | Implementation of TinyLlama using Hugging Face for efficient chatbot experiences | LangChain  |
| **simple_story_generator** | An simple story generator | LangChain  |

## Getting Started

For beginners, we recommend following this sequence:

1. Start with the `TinyLlama_Initial_Test` branch to understand basic LLM inference

Each branch includes sample notebooks and scripts with detailed comments to guide your learning.


## License

This project is licensed under the MIT License