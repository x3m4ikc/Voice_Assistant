import tkinter as tk
# import pyaudio
import speech_recognition as sr

window = tk.Tk()

window.geometry('650x450')
window.title('Запись с микрофона')
window.resizable(False, False)

# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     print(i, p.get_device_info_by_index(i)['name'])
'''Микрофон индекс 2'''
txt = tk.Text(window)
txt.place(x=0, y=0)

r = sr.Recognizer()

def speech():
    with sr.Microphone(device_index=1) as source:
        txt_label.configure(txt='Говорите...')
        window.update()

        try:
            audio = r.listen(source, phrase_time_limit=5, timeout=7)
            query = r.recognize_google(audio, language='ru-Ru')
        except(sr.WaitTimeoutError, sr.UnknownValueError):
            txt_label.configure(text='Не понятно...Скажите еще раз')
            window.update()
            speech()

        else:
            txt_label.configure(text='Намите на кнопку и говорите')
            return query.capitalize()

def insert_rec():
    recording = speech()
    txt.insert(1.0, recording)

button_rec = tk.Button(window, text='REC', bg='red', font=('Cooper', 16), command=insert_rec)
button_rec.place(x=30, y=400)

txt_label = tk.Label(window, text='Нажмите на кнопку и говорите...', font=('Cooper', 12))
txt_label.place(x=100, y=408)

window.mainloop()