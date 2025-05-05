import gradio as gr
from openai import OpenAI
from gpiozero import LED

api_key = "<API-KEY>"
client = OpenAI(api_key=api_key)
led = LED(18)

def get_response(prompt):
    input_msg = "請分析下列文字內容的語意是開啟或關閉燈光, 開啟回答ON; 關閉回答OFF"
    response = client.chat.completions.create(
      model = "gpt-3.5-turbo",      
      messages = [
            {"role": "system", "content": "你是一位語意分析機器人"},
            {"role": "user", "content": input_msg + "\n" + prompt}
                 ]
    )
    reply_msg = response.choices[0].message.content
    if reply_msg =="ON":
        led.on()
    else:
        led.off()

    return reply_msg

app = gr.Interface(fn=get_response,
                   inputs="text",
                   outputs="text")
app.launch(server_name="raspberrypi.local")