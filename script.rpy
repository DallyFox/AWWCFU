# И мир был создан для нас.
# 2014 Юлия Лопарева
# Lopareva.julia@gmail.com

# Я не знаю, зачем это.
image ctc_blink:
       "ui/dialogue/ctc.png"
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat 
       
# Тут записываются изображения, которые будут фоном.
image bg placeholder = "bgs/placeholder.png"

# А тут уже прописываются персонажи.
define noname = Character('???', color="#c8ffc8", ctc="ctc_blink", ctc_position="nestled")
define me = Character("[myname]", color="#c8ffc8", ctc="ctc_blink", ctc_position="nestled")
define foxy = Character('Фокси', color="#c8ffc8", ctc="ctc_blink", ctc_position="nestled")


# Тут вроде как прописывается картинка, которую видем в начале. 
init:
    image splash = "ui/splash.png"
    
label splashscreen:
        
    $ renpy.pause(0)
    scene black
    with Pause(0.5)
    
    show splash 
    with dissolve
    #play sound "sfx/logo.wav" 
    with Pause(2.0)
     
    scene black 
    with dissolve
    with Pause(1.0)

    return

# А отсюда уже начинаем кодить.
label start:

    scene bg placeholder with fade
    
    "Добро пожаловать в игру."
    foxy "Меня зовут Фокси. Сегодня я буду вашим помошником, чтобы помочь вам разобраться, как пользоваться данной программой."
    foxy "Для начала, я предлагаю вам ввести имя главной героини. Вы можете ввести ей любое имя, но учтите, что вы играете за девушку."
    foxy "Поэтому не стоит писать мужские имена. Хотя...как хотите, я вам разрешаю."

python:
    myname = renpy.input("Какое будет имя у героини?")
    myname = myname.strip()

    if not myname:
         myname = "Эшли"
me "меня зовут [myname]?"
    
scene black with dissolve
    
$renpy.pause(0.3)
    
return
