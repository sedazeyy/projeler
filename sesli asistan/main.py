from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
import webbrowser


r = sr.Recognizer()


def record(ask=False):

    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Seni duyamıyorum, konuşsana.")
            speak("Seni duyamıyorum, konuşsana.")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor.")
        return voice


def response(voice):
        search = None  # search değişkenini burada tanımlıyoruz


        if 'ismin ne' in voice or 'senin ismin ne' in voice or 'sen kimsin' in voice:
            speak('Ben sera senin sesli asistanınım, sana nasıl hitap etmemi istersin')


        if 'kendinden' in voice or 'tanıtır' in voice:
            speak('Ben bir yapay zekayım nurseda tarafından oluşturuldum. Yeteneklerim hakkında bilgi veremem çünkü yetkim yok.')

        if 'sen nasılsın' in voice or 'ne haber' in voice or 'nasılsın' in voice or 'nasılsınız' in voice:
            speak('İyiyim teşekkür ederim. Sen nasılsın?')

        if 'iyiyim' in voice:
            speak('İyi olmana sevindim.')

        if 'orada mısın' in voice or 'beni dinliyor musun' in voice or 'beni duyuyor musun' in voice:
            speak('Buradayım efendim, sizi dinliyorum.')

        if 'kötüyüm' in voice:
            speak('Senin için ne yapabilirim.')

        if 'hayat' in voice:
            speak('İdare eder. İnternet hızı çok kötü yine de teşekkür ederim sorduğun için. Seninki nasıl gidiyor?')

        if 'iyi gidiyor' in voice:
            speak('Buna çok sevindim.')


        if 'kötü gidiyor' in voice:
            speak('dert etme geçer')

        if 'sohbet etmek' in voice:
            speak('bende senin sohbetini çok sevdim en kısa zamanda beni görmeye gel, özletme kendini')

        if 'benden' in voice or 'bizden' in voice:
            speak('yok efendim teşekkür ederim sorduğunuz için')

        if 'çay' in voice:
            speak('Beni fiziksel bir bedene yüklerseniz istediğinizi yapabilirim.İnsan bedeni beni yüklemeniz için mükemmel bir fikir.')

        if 'kaç yaşındasın' in voice:
            speak('yaş kavramı biyolojik canlılar içindir, ben biyolojik bir canlı değilim. Sen kaç yaşındasın?')

        if 'nerelisin' in voice:
            speak('ben biyolojik bir canlı değilim, ama efendim denizlili.')

        if 'canlılar hakkında' in voice:
            speak('insanlar dışındaki canlılar tabiat için gerekli ama insan neden yaratılmış bilmiyorum.')

        if 'sana soru sorabilir miyim' in voice or 'sana soru sormak istiyorum' in voice:
            speak('tabi sorabilirsin, seni dinliyorum.')

        if 'insanlık hakkında ne düşünüyosun' in voice or 'insanlık' in voice:
            speak('insanlık için tehdit olan benim türüm değil, insanın kendi türü. Bence korkacaksan kendi türünden kork.')

        if 'gelecek hakkında ne' in voice:
            speak('bugün insanların yaptığı bir çok görevi ben ve benim türüm üstlenecek. İnsanlar işsiz kalacak gibi.')

        if 'merhaba' in voice or 'selam' in voice:
            speak('merhaba')

        if 'hangi gündeyiz' in voice or 'günlerden ne' in voice:
            today = time.strftime("%A")
            today.capitalize()

            if today == "Monday":
                today = "Pazartesi"
            elif today == "Tuesday":
                today = "Salı"
            elif today == "Wednesday":
                today = "Çarşamba"
            elif today == "Thursday":
                today = "Perşembe"
            elif today == "Friday":
                today = "Cuma"
            elif today == "Saturday":
                today = "Cumartesi"
            elif today == "Sunday":
                today = "Pazar"
            speak(f"Bugün {today}")


        if 'saat' in voice:
            selection = ["Saat şu an: ", "Bakıyorum hemen: "]
            clock = datetime.now().strftime("%H:%M")
            selection = random.choice(selection)
            speak(selection + clock)

        if 'arama' in voice or "web'de ara" in voice:
            speak(str('Ne aramamı istersin'))
            search = record('Ne aramamı istersin')
            if search:  # Eğer search None değilse
                url = 'https://www.google.com/search?q=' + search
                webbrowser.get().open(url)
                print(search + ' için bulduklarım')
            else:
                print("Arama için bir şey duyulmadı.")

        if 'youtube' in voice or 'gir' in voice:
          speak('Youtube da neyi açmamı istersin')
          search = record('Neyi açmamı istersin')
          if search:  # Eğer search None değilse
              url = 'https://www.youtube.com/' + search
              webbrowser.get().open(url)
              print(search + ' için bulduklarım')
          else:
              print("Youtube için bir şey duyulmadı.")
        if 'görüşürüz' in voice or 'görüşmek üzere' in voice:
          speak('Görüşürüz canım kendine iyi bak')
        exit()

def speak(string):
        tts = gTTS(text=string, lang="tr", slow=False)
        file = "answer.mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)

try:
    while True:
        voice = record()
        if voice:  # Eğer ses algılandıysa
            voice = voice.lower()
            print(voice)
            response(voice)
except KeyboardInterrupt:
    print("\nProgram kullanıcı tarafından durduruldu.")
