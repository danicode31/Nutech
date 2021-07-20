import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone() as micro:
    print("Escuchando...")
    sonido = listener.listen(micro)
    texto = listener.recognize_google(sonido, lenguague='es_ES')
    print(texto)
    


r = sr.Recognizer() 

with sr.Microphone() as source:
    print('Speak Anything : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print('Sorry could not hear')


 
r = sr.Recognizer() 
 
with sr.Microphone() as source:
    print('Speak Anything : ')
    audio = r.listen(source)
 
    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print('Sorry could not hear')