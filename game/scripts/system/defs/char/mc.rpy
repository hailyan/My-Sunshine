define mc = Character("MC", image="mc", voice_tag="mc")

image mc_blink:
    "images/char/mc/raw_li_assets/eyes_open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/char/mc/raw_li_assets/eyes_closed.png"
    .15
    repeat

image side mc = LayeredImageProxy("mc", Transform(xoffset=-40, zoom=0.55))

layeredimage mc:
    zoom 1.5

    group hair_back:
        attribute hair_back default:
            "images/char/mc/raw_li_assets/hair_back.png"

    always:
        "images/char/mc/raw_li_assets/base.png"
    
    group eyes:
        attribute blink default:
            "mc_blink"
        attribute eyes_open:
            "images/char/mc/raw_li_assets/eyes_open.png"
        attribute eyes_closed:
            "images/char/mc/raw_li_assets/eyes_closed.png"
        attribute eyes_closed_happy:
            "images/char/mc/raw_li_assets/eyes_closed_happy.png"
    
    group glasses:
        attribute glasses default:
            "images/char/mc/raw_li_assets/glasses.png"

    group hair_side:
        attribute hair_side default:
            "images/char/mc/raw_li_assets/hair_side.png"
    
    group hair_front:
        attribute hair_front default:
            "images/char/mc/raw_li_assets/hair_front.png"

    group hair_accessory:
        attribute hair_bow:
            "images/char/mc/raw_li_assets/hair_bow.png"
    
    group hair_ahoge:
        attribute hair_ahoge default:
            "images/char/mc/raw_li_assets/hair_ahoge.png"

    group eyebrows:
        attribute eyebrows_normal default:
            "images/char/mc/raw_li_assets/eyebrows_normal.png"
        attribute eyebrows_raised:
            "images/char/mc/raw_li_assets/eyebrows_raised.png"
        attribute eyebrows_mad:
            "images/char/mc/raw_li_assets/eyebrows_mad.png"
    
    group mouth:
        attribute mouth_smile default:
            "images/char/mc/raw_li_assets/mouth_smile.png"
        attribute mouth_talk:
            "images/char/mc/raw_li_assets/mouth_talk.png"
        attribute mouth_tongue:
            "images/char/mc/raw_li_assets/mouth_tongue.png"
        attribute mouth_sad:
            "images/char/mc/raw_li_assets/mouth_sad.png"
        attribute mouth_shout:
            "images/char/mc/raw_li_assets/mouth_shout.png"
        attribute mouth_pout:
            "images/char/mc/raw_li_assets/mouth_pout.png"
    
    group outfit:
        attribute outfit_work default:
            "images/char/mc/raw_li_assets/outfit_work.png"