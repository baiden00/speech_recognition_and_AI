import pyaudio,wave
import  speech_recognition as sr
import subprocess
import webbrowser

#function to play audio
def play(file_name):
    chunk = 1024
    wf = wave.open(file_name, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True

    )

    data_str = wf.readframes(chunk)

    while data_str:
        stream.write(data_str)
        data_str = wf.readframes(chunk)

    stream.close()
    pa.terminate()




#instantiating microphone and recognizer to listen, record and parse commands
recognize = sr.Recognizer()
microphone = sr.Microphone()



def Speech():
    #to signify the beginning of the recording
    play("/Users/baidench/Documents/GitHub/speech_recognition_and_AI/confident.wav")

    #listening from the user's microphone
    with microphone as source:
        print("Say Something")
        audio = recognize.listen(source)

    #to signify the end of the recording
    play("/Users/baidench/Documents/GitHub/speech_recognition_and_AI/case-closed.wav")
    print("Recorded")

    command = ""

    #Lrecognizing speech
    try:
        command = recognize.recognize_google(audio)
    except:
        print("could't understand")

    print("Your command: " + command)


    if command == "search Google":
        subprocess.call('wsay "Okay, what should I search for?" ')
        print("Say Something ")
        to_search = ""

        with microphone as source:
            audio = recognize.listen(source)

        to_search = recognize.recognize_google(audio)
        webbrowser.get().open('http://www.google.com/search?q=' + to_search)


    elif "what" in command and "your name" in command:
        subprocess.call('wsay "My name is Baidens Artificial Intelligence" ')

    elif command == "what is my favorite sport":
        subprocess.call('wsay "Charles, your favorite Sport is Soccer" ')

    elif command == "what is my name":
        subprocess.call('wsay "Your name is Charles" ')

    elif command == "hello" or command== "hi":
        subprocess.call('wsay "hey there" ')



Speech()
