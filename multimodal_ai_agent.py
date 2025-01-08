from dotenv import load_dotenv
import json
import os
from openai import OpenAI
import gradio as gr
import base64
from io import BytesIO
from PIL import Image 

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"
openai = OpenAI()

SYSTEM_MESSAGE = "You are an helpful assistant for an Airline called FlightAI. "
SYSTEM_MESSAGE += "Give short and courteous answers, no more than one sentence"
SYSTEM_MESSAGE += "Always be accurate. If you do not know the answer, say so."

ticket_prices = {"london": "$899", 
                 "paris": "$999", 
                 "tokyo": "$1511",
                 "berlin": "$699",
                 "new york": "$1620",
                 "singapore": "$349",
                 "los angeles": "$1729",
                 "prague": "$769"}

def get_ticket_price(city):
    print(f"Tool get_ticket_price called for {city}")
    city = city.lower()
    return ticket_prices.get(city, "Unknown")

price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city. \
                    Call this whenever you need to know the ticket price, \
                    for example when a customer asks 'How much is the ticket \
                    to this city?' ",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["city"],
        "additionalProperties": False
    }
}

tools = [{"type": "function", "function": price_function}]

def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    city = arguments.get("city")
    price = get_ticket_price(city)
    response = {
        "role": "tool",
        "content": json.dumps({"city": city, "price": price}),
        "tool_call_id": tool_call.id
    }

    return response, city

def artist(city):
    image_response = openai.images.generate(
                    model ="dall-e-3",
                    prompt =f"An image representing a vacation in {city}, \
                             showing tourists spots and unique things about the {city}, \
                             in a minimalistic pop-art style",
                    size ="1024x1024",
                    n=1,
                    response_format="b64_json"
    )

    image_base64 = image_response.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    return Image.open(BytesIO(image_data))

def chat(history):
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + history
    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools
    )
    image=None
    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        image=artist(city)
        response = openai.chat.completions.create(
            model=MODEL,
            messages=messages
        )
    reply = response.choices[0].message.content
    history += [{"role": "assistant", "content": reply}]

    return history, image

with gr.Blocks() as demo:
    with gr.Row():
        chatbot = gr.Chatbot(height=500, type="messages")
        image_output = gr.Image(height=500)
    with gr.Row():
        entry = gr.Textbox(label="Chat with our AI Assistant:")
    with gr.Row():
        clear = gr.Button("Clear")
    
    def do_entry(message, history):
        history += [{"role": "user", "content": message}]
        return "", history
    
    entry.submit(
        do_entry,
        inputs=[entry, chatbot],
        outputs=[entry, chatbot]
    ).then(
        chat,
        inputs=chatbot,
        outputs=[chatbot, image_output]
    )

    clear.click(
        lambda: None,
        inputs=None,
        outputs=chatbot,
        queue=False
    )

demo.launch(inbrowser=True)


