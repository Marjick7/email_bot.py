import smtplib
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)
except:
    pass


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mohamedmarjick123@gmail.com', 'Barakath1234')
    server.sendmail('mohamedmarjick123@gmail.com',
                    'mohamedmarjick000@gmail.com',
                    'hello World'
                    )
