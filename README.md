# LLM Web Parser

A Python-based tool that combines web scraping and AI-powered summarization to generate concise, markdown-formatted summaries of web content.

## Features

- Web scraping using BeautifulSoup4
- Content cleaning and preprocessing
- AI-powered summarization using OpenAI's GPT models / Local Ollama models
- Markdown-formatted output
- Jupyter notebook implementation

## Prerequisites

- Python 3.11+
- OpenAI API key
- Required Python packages:
  - requests
  - beautifulsoup4
  - python-dotenv
  - openai
  - IPython
  - ollama

## Setup

1. Clone this repository
2. Create a conda env using `conda env create -f environment.yml`.
3. Activate the env using `conda activate llms`.
4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your-openai-api-key-here
ANTHROPIC_API_KEY=your-anthropic-api-key-here
```

## Usage

The main functionality is implemented in `ai-conversations.ipynb`. 
The notebooks provides a fun conversation between a snarky Openai chatbot and
a polite Claude chatbot



