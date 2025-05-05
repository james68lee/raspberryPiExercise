import gradio as gr

def greet(name):
    return "Hello " + name + "!"

inputs = gr.Textbox(lines=2, placeholder="請輸入姓名...", 
                    label="請輸入使用者姓名")
outputs = gr.Label()
examples = ["陳會安", "江小魚"]
app = gr.Interface(fn=greet,
                   inputs=inputs,
                   outputs=outputs,
                   examples=examples, 
                   title = "歡迎使用者",
                   description = "輸入姓名顯示歡迎訊息")
app.launch(server_name="raspberrypi.local")