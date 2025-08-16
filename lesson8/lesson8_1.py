import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"], #text:  ,slider:bar
    outputs=["text"],#輸出:文字
)
demo.launch(share=True)