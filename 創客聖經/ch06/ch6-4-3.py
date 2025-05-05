import gradio as gr

def greet(name):
    return "你好: " + name + "!"

app = gr.Interface(fn=greet,
                   inputs="text",
                   outputs="text")
app.launch(server_name="raspberrypi.local")