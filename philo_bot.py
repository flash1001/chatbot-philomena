from openai import OpenAI
import requests
import time
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
TOKEN = os.getenv("TELEGRAM_TOKEN")
modelph = os.getenv("MODEL_PHILO")

def get_updates(offset):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]

def send_messages(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response

def get_openai_response(prompt):
    system = "You are Philomena Cunk, a humorous and naive character known for asking silly questionsand making ironic or absurd statements, and often oversimplifyingor misunderstanding complex concepts."
        
    response = client.chat.completions.create(
        model = modelph,
        messages = [
            {"role": "system", "content": f"{system}"},
            {"role": "user", "content": f"{prompt}"}],
        max_tokens=256,
        n=1,
        temperature=0.125)
    return response.choices[0].message.content.strip()
    
def main():
    print('Loading Philomena...')  
    offset = 0  
    while True:  
        updates = get_updates(offset)  # get_updates() para obtener actualizaciones de mensajes.
        if updates: 
            for update in updates:  
                offset = update['update_id'] + 1  # Actualiza el valor de offset para evitar procesar la misma actualización nuevamente.
                chat_id = update["message"]["chat"]["id"]  
                user_message = update["message"]["text"] 
                print(f"Received message: {user_message}") 
                GPT = get_openai_response(user_message)  
                send_messages(chat_id, GPT)  
            time.sleep(1)  
            
if __name__ == '__main__':
    main()  
    
