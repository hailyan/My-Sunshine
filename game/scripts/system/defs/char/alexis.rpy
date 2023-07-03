define alexis = Character("Alexis", image="alexis", voice_tag="alexis")

image alexis_blink:
    "images/char/alexis/raw_li_assets/eyes_open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/char/alexis/raw_li_assets/eyes_closed.png"
    .15
    repeat

image side alexis = LayeredImageProxy("alexis", Transform(xoffset=-40, zoom=0.55))

layeredimage alexis:
    zoom 1.5

    group hair_back:
        attribute hair_back default:
            "images/char/alexis/raw_li_assets/hair_back.png"
    
    always:
        "images/char/alexis/raw_li_assets/base.png"
    
    group eyes:
        attribute blink default:
            "alexis_blink"
        attribute eyes_open:
            "images/char/alexis/raw_li_assets/eyes_open.png"
        attribute eyes_closed:
            "images/char/alexis/raw_li_assets/eyes_closed.png"
            
    group outfit:
        attribute outfit_work default:
            "images/char/alexis/raw_li_assets/outfit_work.png"
    
    #group hair_side_1:
        #attribute hair_side_1 default:
            #"images/char/alexis/raw_li_assets/hair_side_1.png"
    group hair_side_2:
        attribute hair_side_2 default:
            "images/char/alexis/raw_li_assets/hair_side_2.png"
    
    group hair_front:
        attribute hair_front default:
            "images/char/alexis/raw_li_assets/hair_front.png"
    
    group hair_accessory:
        attribute hair_rose:
            "images/char/alexis/raw_li_assets/hair_rose.png"
    
    group eyebrows:
        attribute eyebrows_normal default:
            "images/char/alexis/raw_li_assets/eyebrows_normal.png"
    
    group mouth:
        attribute mouth_neutral default:
            "images/char/alexis/raw_li_assets/mouth_neutral.png"
        attribute mouth_talk:
            "images/char/alexis/raw_li_assets/mouth_talk.png"
    
    group hands:
        attribute hand_out:
            "images/char/alexis/raw_li_assets/hand_out.png"
        attribute hand_raised:
            "images/char/alexis/raw_li_assets/hand_raised.png"
        attribute hand_touched:
            "images/char/alexis/raw_li_assets/hand_touched.png"
        attribute hand_write:
            "images/char/alexis/raw_li_assets/hand_write.png"