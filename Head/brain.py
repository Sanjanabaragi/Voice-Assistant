import webbrowser

from Training_model.model import mind
import wikipedia
import threading
from Head.Mouth import speak
import sys,time
from Training_model.model import mind

def load_qa_data(file_path):
    qa_dict={}
    with open(file_path, "r",encoding="utf-8",errors="replace") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            parts=line.split(":")
            if len(parts)!=2:
                continue
            q,a=parts
            qa_dict[q]=a
    return qa_dict

qa_file_path=r"C:\Users\Sanjana Baragi\PycharmProjects\Voice_assistant\Data\brain_data\qna_data.txt"
qa_dict=load_qa_data(qa_file_path)

def save_qa_data(file_path,qa_dict):
    with open(file_path,"a",encoding="utf-8") as f:
        for q,a in qa_dict.items():
            f.write(f"{q}:{a}\n")

def wiki_search(prompt):
    search_prompt = prompt.replace("jarvis", "")
    search_prompt = search_prompt.replace("wikipedia", "")

    try:
        wiki_summary = wikipedia.summary(search_prompt, sentences=2)

        animate_thread = threading.Thread(target=print_animated_message, args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        # Assuming 'search_prompt' is defined somewhere
        qa_dict[search_prompt] = wiki_summary  # Store in qa_dict
        save_qa_data(qa_file_path, qa_dict)  # Save updated qa_dict

    except wikipedia.exceptions.DisambiguationError as e:
        speak("There is a disambiguation page for the given query. Please provide more specific information.")
        print("There is a disambiguation page for the given query. Please provide more specific information.")
    except wikipedia.exceptions.PageError:
        google_search(search_prompt)


def google_search(query):
    query = query.replace("who is ", "")
    query = query.strip()

    if query:
        url = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(url)
        speak("You can see search results for " + query + " in Google on your screen.")
        # print("You can see search results for " + query + " in Google on your screen.")
    else:
        speak("I didn't catch what you said.")
        # print("I didn't catch what you said.")


def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)  # Adjust the sleep duration for the animation speed
    print()


def brain(text):
    try:
        response=mind(text)

        if not response:
            wiki_search(text)
            return

        animate_thread=threading.Thread(target=print_animated_message,args=(response,))
        speak_thread=threading.Thread(target=speak,args=(response,))

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        qa_dict[text]=response
        save_qa_data(qa_file_path,qa_dict)

    except Exception as e:

        print(f"An error occurred:{str(e)}")
        wiki_search(text)

