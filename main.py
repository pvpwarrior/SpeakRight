#created by Parasa V. Prajwal 20/11/2022

import speech_recognition as sr
from sapling import SaplingClient
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

api_key ='KQ5SY11V64H8MI36ZSMKKP6DQHV6F96F'
client = SaplingClient(api_key=api_key)
a = sr.Recognizer()
mixer.init()


with sr.Microphone() as source:
    print("speak now")
    audio = a.listen(source)
    data = a.recognize_google(audio)
    print("USER INPUT: ", data)
    edits = client.edits(str(data), session_id='test_session')
    print("SAPLING API RESPONSE: ", edits)
    crct = str(data)
    if edits == []:
        print("no grammar mistakes")
        tts = gTTS('no mistakes were found')
    else:
        for i in edits:
            print("error_type: ", i['general_error_type'])
            print("sentence: ", i['sentence'])
            print("replacement: ", i['replacement'])
            y = (i['replacement'])
            k = i['start']
            crct = crct[:k] + y + crct[i['end']:]
            print('corrected string: ', crct)
            tts = gTTS("the corrected sentence is "+crct , lang='en')
    mp3_fp=BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    #mp3_fp.close()
    #tts.save("tts.mp3")
    #mixer.music.load("tts.mp3")
    #mixer.music.load(mp3_fp);
    #mixer.music.play()
    song=AudioSegment.from_file(mp3_fp,format="mp3")
    play(song)
    
    
