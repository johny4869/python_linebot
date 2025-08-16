import gradio as gr

def greet(name): #greet variables according to numbers of inputs 
    if name:
        return f"Hello, {name}! Nice to meet you!"
    else:
        return "Hello! Please enter your name."

with gr.Blocks() as demo:
    name_textbox = gr.Textbox(label="Name", placeholder="Enter your name")
    output_textbox = gr.Textbox(label="Output", interactive=False, placeholder="Output will appear here")
    greet_button = gr.Button("Greet")
    greet_button.click(fn=greet, 
                       inputs=[name_textbox], 
                       outputs=[output_textbox])

demo.launch()