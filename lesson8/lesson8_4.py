import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown(
        """
        "## 歡迎使用 Gradio"
        請輸入文字，會即時顯示輸入內容
        """)
    input_box = gr.Textbox(label="輸入文字", placeholder="請輸入文字", lines=2, max_lines=4)
    output_box = gr.Textbox(label="輸出文字", placeholder="輸入內容會顯示在這裡", interactive=False)   

    @input_box.change(
        #fn=lambda text: text,  # 回傳輸入的文字
        inputs=[input_box],
        outputs=[output_box]
    )
    def update_output(text):
        return text

demo.launch()