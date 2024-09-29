from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import gradio as gr

# Load GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Flask app for handling curl requests
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, do_sample=True, top_k=50, top_p=0.95)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'generated_text': generated_text})

# Gradio interface for UI interaction
def gradio_generate_text(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, do_sample=True, top_k=50, top_p=0.95)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Set up Gradio UI
gr_interface = gr.Interface(fn=gradio_generate_text, inputs="text", outputs="text", title="GPT-2 Text Generator")

if __name__ == "__main__":
    # Launch Gradio in a separate thread
    import threading
    threading.Thread(target=lambda: gr_interface.launch(share=True)).start()
    
    # Start Flask server
    app.run(host="0.0.0.0", port=5000)
