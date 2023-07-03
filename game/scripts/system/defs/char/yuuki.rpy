define yuuki = Character("Yuuki", image="yuuki", voice_tag="yuuki")

image yuuki_blink:
    "images/char/yuuki/raw_li_assets/eyes_open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/char/yuuki/raw_li_assets/eyes_closed.png"
    .15
    repeat

image side yuuki = LayeredImageProxy("yuuki", Transform(xoffset=-40, zoom=0.55))

layeredimage yuuki:
    zoom 1.5

    group hair_back:
        attribute hair_back default:
            "images/char/yuuki/raw_li_assets/hair_back.png"

    always:
        "images/char/yuuki/raw_li_assets/base.png"
    
    group eyes:
        attribute blink default:
            "yuuki_blink"
        attribute eyes_open:
            "images/char/yuuki/raw_li_assets/eyes_open.png"
        attribute eyes_closed:
            "images/char/yuuki/raw_li_assets/eyes_closed.png"
        attribute eyes_closed_happy:
            "images/char/yuuki/raw_li_assets/eyes_closed_happy.png"
    
    group outfit:
        attribute outfit_work default:
            "images/char/yuuki/raw_li_assets/outfit_work.png"
    
    group hair_side:
        attribute hair_side default:
            "images/char/yuuki/raw_li_assets/hair_side.png"
    
    group hair_front:
        attribute hair_front default:
            "images/char/yuuki/raw_li_assets/hair_front.png"

    group hair_accessory:
        attribute hair_moon:
            "images/char/yuuki/raw_li_assets/hair_moon.png"
    
    group eyebrows:
        attribute eyebrows_normal default:
            "images/char/yuuki/raw_li_assets/eyebrows_normal.png"
        attribute eyebrows_raised:
            "images/char/yuuki/raw_li_assets/eyebrows_raised.png"
        attribute eyebrows_mad:
            "images/char/yuuki/raw_li_assets/eyebrows_mad.png"
    
    group mouth:
        attribute mouth_smile default:
            "images/char/yuuki/raw_li_assets/mouth_smile.png"
        attribute mouth_talk:
            "images/char/yuuki/raw_li_assets/mouth_talk.png"
        attribute mouth_sad:
            "images/char/yuuki/raw_li_assets/mouth_sad.png"
        attribute mouth_shout:
            "images/char/yuuki/raw_li_assets/mouth_shout.png"
        attribute mouth_pout:
            "images/char/yuuki/raw_li_assets/mouth_pout.png"
    
    group hands:
        attribute hand_clasped:
            "images/char/yuuki/raw_li_assets/hand_clasped.png"
        attribute hand_wave:
            "images/char/yuuki/raw_li_assets/hand_wave.png"