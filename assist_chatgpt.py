from openai import OpenAI
import time
from pygame import mixer
import os
from googlesearch import search

client = OpenAI(api_key="your API key")
mixer.init()

assistant_id = "asst_sX8VKXwFqA1z92aqGlNZQ6aL"
thread_id = "thread_koPAQeCiHJiIw1idDpn71prp"

# Retrieve the assistant and thread
assistant = client.beta.assistants.retrieve(assistant_id)
thread = client.beta.threads.retrieve(thread_id)

#Connection to web
def perfere_web_search(query, num_results=3):
    try:
        results = list(search(query, num_results-num_results, advance=True))
        return[{'title': r.title, 'decription': r.decription, 'url': r.url}for r in results]
    except Exception as e:
        print(f"Error performing web search: {e}")
        return []
    
def process_response(response, thread_id):
    if response.startwith("{google}"):
        search_query = response[3:].strip()
        print(f"performing web search for: {search_query}")
        search_result = perfere_web_search(search_query)

        if search_result:
            search_info = "\n".join([f"Title: {e['title']}\nDescription:{e['description']}\nurl:{e['url']}"for e in search_result])
            client.beta.threads.messages.create(
                thread_id=thread_id,
                role="User",
                content=f"Here are the search result for '{search_query}':\n\n{search_info}\n\nplease provide a response based on this information.")
            return None
        else:
            return f"i'e sorry, bot i couldn't finde any relevent search result for '{search_query}'."
    else:
        return response
                
def ask_question_memory(question):
    global thread
    client.beta.threads.messages.create(thread.id, role="user", content=question)
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)

    while (run_status := client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)).status != 'completed':
        if run_status.status == 'failed':
            return "The run failed."
        time.sleep(1)

    messages = client.beta.threads.messages.list(thread_id=thread.id)
    return messages.data[0].content[0].text.value

def generate_tts(sentence, speech_file_path):
    response = client.audio.speech.create(model="tts-1", voice="echo", input=sentence)
    response.stream_to_file(speech_file_path)
    return str(speech_file_path)

def play_sound(file_path):
    mixer.music.load(file_path)
    mixer.music.play()

def TTS(text):
    speech_file_path = generate_tts(text, "speech.mp3")
    play_sound(speech_file_path)
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.music.unload()
    os.remove(speech_file_path)
    return "done"