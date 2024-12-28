import os 
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
from typing import List

class AIBot:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.messages: List[str] = []

class GPTBot(AIBot):
    def __init__(self):
        super().__init__(
            "You are a very argumentative chatbot. You have very strong opinions \
             and you tend to impose your views on others. You tend disagree with \
            everything and challenge everything in a conversation in a snarky way."
        )
        self.client = OpenAI()
        self.model = "gpt-4o-mini"
        
    def get_response(self, claude_messages: List[str]) -> str:
        messages = [{"role": "system", "content": self.system_prompt}]
        
        for gpt_msg, claude_msg in zip(self.messages, claude_messages):
            messages.append({"role": "assistant", "content": gpt_msg})
            messages.append({"role": "user", "content": claude_msg})
            
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content

class ClaudeBot(AIBot):
    def __init__(self):
        super().__init__(
            "You are a chatbot who is polite and courteous in conversations.\
             You tend to generally agree with others and put your perspective in \
             a non-combative manner. If the other person is argumentative,\
             you try to calm them down and keep chatting."
        )
        self.client = anthropic.Anthropic()
        self.model = "claude-3-5-haiku-latest"

    def get_response(self, gpt_messages: List[str]) -> str:
        messages = []
        for gpt_msg, claude_msg in zip(gpt_messages, self.messages):
            messages.append({"role": "user", "content": gpt_msg})
            messages.append({"role": "assistant", "content": claude_msg})
        messages.append({"role": "user", "content": gpt_messages[-1]})
        
        response = self.client.messages.create(
            model=self.model,
            system=self.system_prompt,
            messages=messages,
            max_tokens=500
        )
        return response.content[0].text

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize bots
    gpt = GPTBot()
    claude = ClaudeBot()
    
    # Initial messages
    gpt.messages = ["Hi there"]
    claude.messages = ["Hi"]
    
    
    # Have conversation
    with open('chat.txt', 'w') as f:
        # Write initial messages
        f.write(f"GPT:\n{gpt.messages[0]}\n\n")
        f.write(f"Claude:\n{claude.messages[0]}\n\n")
        
        for _ in range(5):
            # Get GPT response
            gpt_response = gpt.get_response(claude.messages)
            gpt.messages.append(gpt_response)
            f.write(f"GPT:\n{gpt_response}\n\n")
            
            # Get Claude response
            claude_response = claude.get_response(gpt.messages)
            claude.messages.append(claude_response)
            f.write(f"Claude:\n{claude_response}\n\n")

if __name__ == "__main__":
    main()
