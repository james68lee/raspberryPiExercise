import gradio as gr
import ollama
from gpiozero import LED

led = LED(18)

def get_response(question):
    prompt1 = "Please analyze the semantic meaning of the sentence '"
    prompt2 = "' is ON or OFF. The answer is only on word."
    response = ollama.chat(
    model = "gemma2:2b",      
    messages = [
         {"role": "system", "content": "You are a semantic analysis robot."},
         {"role": "user", "content": prompt1 + question + prompt2}
    ])
    reply_msg = response['message']['content']
    if "ON" in reply_msg:
        led.on()
    else:
        led.off()

    return reply_msg

app = gr.Interface(fn=get_response,
                   inputs="text",
                   outputs="text")
app.launch(server_name="raspberrypi.local")