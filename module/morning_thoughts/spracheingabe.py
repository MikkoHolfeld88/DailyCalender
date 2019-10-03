import speech_recognition as sr

def OnSpeak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Text eingesprochen: ")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        # print("Verstanden:" + eingesprochener_Text)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        eingesprochener_Text = r.recognize_google(audio,language="DE-de") # show_all gibt alle möglich verstandenen Ergebenisse zurück
        print(eingesprochener_Text)
    except sr.UnknownValueError:
        print("Google Speech Recognition konnte nichts verstehen.")
        eingesprochener_Text = "Ich konnte dich leider nicht verstehen :-("
    except sr.RequestError as e:
        print("Konnte keine Ergebnisse von Google Speech Recognition service liefern; {0}".format(e))
        eingesprochener_Text = "Konnte keine Ergebnisse liefern; {0}".format(e)
    return eingesprochener_Text
