# LLM AI Conversations

A Python-based tool that creates entertaining dialogues between AI models with contrasting personalities, demonstrating the impact of different system prompts on AI behavior and interaction styles.

## Features

- Interactive conversations between multiple AI models
- Distinct personality implementations:
  - GPT-4: Argumentative and snarky character
  - Claude: Polite and diplomatic character
- Conversation context maintenance
- Support for multiple AI providers (OpenAI, Anthropic, Google)
- Jupyter notebook implementation
- Extensible design for adding more AI personalities

## Prerequisites

- Python 3.11+
- OpenAI API key
- Anthropic API key
- Google Generative AI API key (optional)
- Required Python packages:
  - python-dotenv
  - openai
  - IPython
  - anthropic
  - google.generativeai

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



