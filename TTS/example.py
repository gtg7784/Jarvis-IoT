from gtts import gTTS
text ="송주현님, 오른쪽에 사람이 있습니다."

tts = gTTS(text=text, lang='ko')
tts.save("test.mp3")