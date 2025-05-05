import ollama

prompt1 = "Please analyze the semantic meaning of the sentence '"
prompt2 = "' is ON or OFF. The answer is only on word."
question = prompt1 + "Turn on the lights in the room." + prompt2

response = ollama.chat(
    model = "gemma2:2b",      
    messages = [
         {"role": "system", "content": "You are a semantic analysis robot."},
         {"role": "user", "content": question}
    ])
print("Q:", question)
print(response['message']['content'])

