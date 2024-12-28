# LLM AI Conversations

A Python script that creates entertaining dialogues between AI models with contrasting personalities, demonstrating the impact of different system prompts on AI behavior and interaction styles.

## Features

- Automated conversations between two AI models
- Distinct personality implementations:
  - GPT: Argumentative and snarky character that challenges everything
  - Claude: Polite and diplomatic character that aims to calm tensions
- Conversation history tracking
- Support for multiple AI providers (OpenAI, Anthropic)
- Output saved to text file
- Extensible base AIBot class for adding more personalities

## Prerequisites

- Python 3.x
- OpenAI API key
- Anthropic API key

Required Python packages:
- dotenv
- openai
- anthropic
- typing

## Setup

1. Clone this repository
2. Install the required Python packages
3. Create a `.env` file in the project root with your API keys:

## Model Configuration

- GPT Bot uses the `gpt-4o-mini` model from OpenAI
- Claude Bot uses the `claude-3-5-haiku-latest` model from Anthropic

## Personality Profiles

### GPT Bot
- Argumentative and challenging personality
- Tends to disagree with statements
- Presents opinions in a snarky manner
- Imposes views strongly in conversations

### Claude Bot
- Polite and courteous demeanor
- Generally agreeable
- Non-combative in presenting perspectives
- Acts as a mediator to calm tense discussions

## Extending the Project

New AI personalities can be created by extending the base `AIBot` class and implementing:
- Custom system prompts
- Specific API client configuration
- `get_response()` method for the chosen AI provider






