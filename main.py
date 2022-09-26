import random
import webbrowser
import wikipediaapi
import pyttsx3
import speech_recognition as sp
engine = pyttsx3.init()
sr = sp.Recognizer()
sr.pause_threshold = 0.5

commands_list = [['Привет', 'Приветсвую'],
                 ['Добавить задачу', 'Создать задачу', 'Заметка', 'Создать заметку', 'Добавить заметку'],
                 ['Салам', 'Салам алейкум'],
                 ['Найди в интернете'],
                 ['Найди видос'],
                 ['Определение'],
                 ['Подбрось монетку', 'Монетка', 'Орёл или решка', 'Орёл и решка']]

def listen_command():
    '''Func returns the recognized command'''

    try:
        with sp.Microphone(2) as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').capitalize()

        return query
    except (sp.UnknownValueError, sp.WaitTimeoutError, sp.WaitTimeoutError):
        return "Damn... Не понял ни слова :/"

def greetings():
    '''Greeting func'''
    engine.say('Привет господин')
    engine.runAndWait()

def salam():
    engine.say('Салам алейкум, брат мой! Мир тебе и твоей семье!')
    engine.runAndWait()

def create_task():
    '''Create a todo task'''
    engine.say('Что добавим в список дел?')
    engine.runAndWait()

    query = listen_command()

    with open('todo-list.txt', 'a') as file:
        file.write(f'! {query}\n')
    engine.say(f'Задача {query} добавлена в todo-list')
    engine.runAndWait()
    return

def search_on_google():
    engine.say('Что будем искать?')
    engine.runAndWait()

    query = listen_command()
    url = 'https://google.com/search?q=' + query
    engine.say(f'По вашему запросу {query} открываю страничку')
    engine.runAndWait()
    webbrowser.get().open(url)
    return

def search_on_youtube():
    engine.say('Что будем искать?')
    engine.runAndWait()

    query = listen_command()
    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.get().open(url)
    return

def seach_on_wikipedia():
    engine.say('Что будем искать?')
    engine.runAndWait()
    wiki = wikipediaapi.Wikipedia(language='ru')
    query = listen_command()
    wiki_page = wiki.page(query)
    try:
        if wiki_page.exists():
            engine.say(f'Вот что я нашла по запросу {query}')
            engine.runAndWait()
            webbrowser.get().open(wiki_page.fullurl)
        else:
            url = 'https://google.com/search?q=' + query
            engine.say(f'В википедии не нашла, но нашла в гугле по запросу {query}')
            engine.runAndWait()
            webbrowser.get().open(url)
    except:
        engine.say('Похоже у нас возникли ошибки, Хьюстон!')
        engine.runAndWait()
    return

def flip_a_coin():
    a = ['Орел', 'Решка']
    engine.say(f'У нас выпадает {random.choice(a)}')
    engine.runAndWait()

def main():
    engine.say('Готова слушать комманду')
    engine.runAndWait()
    query = listen_command()

    if query in commands_list[0]:
        greetings()
    elif query in commands_list[1]:
        create_task()
    elif query in commands_list[2]:
        salam()
    elif query in commands_list[3]:
        search_on_google()
    elif query in commands_list[4]:
        search_on_youtube()
    elif query in commands_list[5]:
        seach_on_wikipedia()
    elif query in commands_list[6]:
        flip_a_coin()
    else:
        engine.say('Не знаю такой комманды, повторите пожалуйста комманду')
        engine.runAndWait()
        main()

if __name__ == '__main__':
    main()