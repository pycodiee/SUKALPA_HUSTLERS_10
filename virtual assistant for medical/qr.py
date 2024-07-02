import openai

openai.api_key = 'your-openai-api-key'

def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)
openai.api_key = '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'

@app.route("/webhook", methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    # Get AI response
    response = get_response(incoming_msg)
    msg.body(response)

    return str(resp)

def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)



# import pyqrcode
# import time
# import os

# def generate_qr_code():
#     # You need to implement the actual logic to get the QR code data from WhatsApp
#     # For example, you might use Selenium or a similar tool to automate the WhatsApp Web login
#     qr_data = "example data"
#     qr = pyqrcode.create(qr_data)
#     qr.png("qr_code.png", scale=6)

# while True:
#     generate_qr_code()
#     os.system("display qr_code.png")  # This will open the QR code image. Use an appropriate method to display the QR code.
#     time.sleep(5)


# from flask import Flask, render_template, request, jsonify


# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')


# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     return get_Chat_response(input)


# def get_Chat_response(text):

#     # Let's chat for 5 lines
#     for step in range(5):
#         # encode the new user input, add the eos_token and return a tensor in Pytorch
#         new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

#         # append the new user input tokens to the chat history
#         bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

#         # generated a response while limiting the total chat history to 1000 tokens, 
#         chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

#         # pretty print last ouput tokens from bot
#         return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


# if __name__ == '__main__':
#     app.run()