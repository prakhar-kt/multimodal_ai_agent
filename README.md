# MultiModal AI Agent

A multimodal AI travel assistant that helps users get flight ticket prices and generates destination artwork using OpenAI's GPT-4 and DALL-E 3 models.

## Features

- Interactive chat interface using Gradio
- Provides ticket prices for major cities like London, Paris, Tokyo, etc.
- Generates artistic travel destination images in minimalist pop-art style


## Requirements

The project requires Python 3.11 and the following main dependencies:
- openai
- gradio
- python-dotenv
- Pillow
- torch
- transformers
- langchain

Full dependencies are listed in `environment.yml`.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/multimodal-ai-agent.git
   cd multimodal-ai-agent
   ```

2. Create and activate conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate llms

3. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your API keys:
     ```
     OPENAI_API_KEY="your-openai-api-key"
     ```

4. Run the application:
   ```bash
   gradio multimodal_ai_agent.py
   ```

The application will launch in your default web browser. You can then interact with the AI travel assistant through the chat interface.
