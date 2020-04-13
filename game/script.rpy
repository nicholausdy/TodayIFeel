# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define eka_thinking_normal = Character("Eka",window_xpos= 700, window_ypos = 950, window_background="eka_thinking_normal.png",who_xpos = -100, who_ypos = 80, who_color="#38379d",what_xpos=110, what_ypos = 150)
define eka_thinking_shaking = Character(kind=eka_thinking_normal, window_background="eka_thinking_shaking.png")
define eka_talking_normal = Character(kind=eka_thinking_normal, window_background="eka_talking_normal.png")
define eka_talking_shaking = Character(kind=eka_talking_normal, window_backgrounf="eka_talking_shaking.png")
define budi = Character("Mr. Budi", window_xpos= 850, window_ypos = 900, window_background="talking_normal_flipped.png",who_xpos = -100, who_ypos = 80, who_color="#717171",what_xpos=110, what_ypos = 150, what_color="#717171")
define budi_blur = Character(kind=budi, window_ypos = 300)
define kelas = Character("Class", window_xpos = 600, window_ypos = 250, window_background="talking_normal.png",who_xpos = -100, who_ypos = 80, who_color="#717171",what_xpos=110, what_ypos = 150, what_color="#717171")
define kelas1 = Character(kind=kelas, window_xpos = 1100, window_ypos = 200)
define kelas2 = Character(kind=kelas, window_xpos = 1150, window_ypos = 800)
define kelas3 = Character(kind=kelas, window_xpos = 650, window_ypos = 600)
define nerd = Character("???", window_xpos = 550, window_ypos = 900, window_background="talking_normal_flipped.png", who_xpos = -100, who_ypos = 80, who_color="#717171",what_xpos=110, what_ypos = 150, what_color="#717171")
define bully = Character(kind=nerd, window_ypos = 600)
define budi_blur = Character(kind=budi, window_ypos = 300)
define simon_unknown = Character("???", window_xpos = 1000, window_ypos = 500, window_background="talking_normal.png", who_xpos = -100, who_ypos = 80, who_color = "#c43730", what_xpos=110, what_ypos = 150, what_color="#c43730")
define simon = Character("Simon", kind=simon_unknown)
define simon_andrea_nando = Character("Simon", kind=simon_unknown, window_xpos = 1000, window_ypos = 600 ,window_background="talking_normal_flipped.png")
define andrea_unknown = Character("???(a)", window_xpos = 1100, window_ypos = 500, window_background="talking_normal.png", who_xpos = -100, who_ypos = 80, who_color = "#e44fca", what_xpos=110, what_ypos = 150, what_color="#e44fca")
define andrea = Character("Andrea", kind=andrea_unknown)
define nando_unknown = Character("???(n)", window_xpos = 600, window_ypos = 500, window_background = "talking_normal.png", who_xpos = -100, who_ypos = 80, who_color = "#40a03f", what_xpos=110, what_ypos = 150, what_color="#40a03f")
define nando = Character("Nando", kind=nando_unknown)
define simon_canteen = Character("Simon", kind=simon_unknown, window_background = "talking_normal.png")
define nando_canteen = Character("Nando", kind=nando_unknown, window_background = "talking_normal_flipped.png")

#define variables
default point = 0
default simon_second = False
default whiteboard_interaction_point = 0
default is_convo_simon_seated_down = False
default is_nerd_interacted = False
default is_bag_interacted = False

#define images
#Chapter 1 scenes
image eka_luar_kelas_normal = "otw_introduksi_normal.jpg"
image eka_luar_kelas_tutupin_muka = "otw_introduksi_tutupin_muka.jpg"
image eka_buka_tas = "OTW INTRODUKSI - otw buka tas.jpg"
image eka_ngeluarin_hp = "OTW INTRODUKSI - NGELUARIN HP.jpg"
image hand_into_bag = "OTW INTRODUKSI - HAND INTO BAG.jpg"
image ngeluarin_dompet = "OTW INTRODUKSI - NGELUARIN DOMPET.jpg"
image mr_budi_looking_at_player = "OTW INTRODUKSI - Mr. Budi looking at player.jpg"
image mr_budi_smiles = "OTW INTRODUKSI - Mr. Budi smiles.jpg"
image black = "#000"
image full_fokus_kelas = "INTRODUCTION - 3rd pov depan kelas - full fokus kelas.jpg"
image tangan_garuk2 = "INTRODUCTION - 3rd pov depan kelas - tangan garuk2.jpg"
image clenching_hands = "INTRODUCTION - 3rd pov depan kelas - clenching hands.jpg"
image looking_at_mr_budi = "INTRODUCTION - 3rd pov depan kelas - looking at Mr. Budi.jpg"
image 1st_person_depan_kelas = "INTRODUCTION - 1st person POV depan kelas.jpg"
image looking_at_mr_budi_hes_smiling = "INTRODUCTION - 3rd pov depan kelas - looking at Mr. Budi hes smiling.jpg"
image muka_nerd_shook = "CHOOSING SEAT - NERD - muka nerd shook.jpg"
image muka_nerd_tidak_senang = "CHOOSING SEAT - NERD - muka nerd tidak senang.jpg"
image muka_nerd_shook_even_more = "CHOOSING SEAT - NERD - muka nerd shook even more ngeliat player.jpg"
image muka_nerd_nunduk = "CHOOSING SEAT - NERD - nerd memalingkan muka nunduk ke bawah.jpg"
image muka_nerd_senyum_sopan = "CHOOSING SEAT - NERD - nerd senyum sopan.jpg"
image muka_bully_seram = "CHOOSING SEAT - BULLY - muka bully seram melototin.jpg"
image muka_bully_makin_melototin = "CHOOSING SEAT - BULLY - BULLY MAKIN MELOTOTIN.jpg"
image simon_ngeliatin = "CHOOSING SEAT - SIMON - SIMON ngeliatin.jpg"
image choosing_seat_simon_senyum = "CHOOSING SEAT - SIMON - SIMON senyum.jpg"
image simon_pura2_sedih = "CHOOSING SEAT - SIMON - SIMON pura2 sedih.jpg"
image simon_nyengir = "CHOOSING SEAT - SIMON - SIMON nyengir.jpg"
image guru_beres_buku ="SEATED DOWN - guru di depan lagi beres2 buku.jpg"
image simon_normal = "SEATED DOWN - SIMON - NORMAL.jpg"
image simon_ngeliat_player = "SEATED DOWN - SIMON - SIMON ngeliat player.jpg"
image simon_surprised = "SEATED DOWN - SIMON - muka simon surprised.jpg"
image seated_down_simon_senyum = "SEATED DOWN - SIMON - muka simon senyum.jpg"
image simon_senyum_nunjuk_depan = "SEATED DOWN - SIMON - muka simon senyum nunjuk depan.jpg"
image seated_down_simon_concerned = "SEATED DOWN - SIMON - simon concerned.jpg"
image guru_depan_papan_tulis = "SEATED DOWN - guru di depan bawa buku dokumen berdiri di depan papan tulis.jpg"
image andrea_nando_normal = "ANDREA NANDO SHOT -NORMAL.jpg"
image andrea_shrugging = "ANDREA NANDO SHOT -Nando shrugging.jpg"
image andrea_nyengir = "ANDREA NANDO SHOT -andrea nyengir.jpg"
image andrea_nengok_player = "ANDREA NANDO SHOT - andrea nengok ke player.jpg"
image nando_nyengir = "ANDREA NANDO SHOT - nando nyengir.jpg"
image simon_angkat_alis_nyengir = "ANDREA NANDO SHOT - simon ngangkat alis nyengir.jpg"
image minus_andrea = "TO CANTEEN - minus andrea.jpg"
image andrea_duduk = "TO CANTEEN - andrea duduk bawa mi ayam juge.jpg"
image nando_surprised = "TO CANTEEN - nando surprissed.jpg"
image semua_orang_nengok = "TO CANTEEN - semua orang nengok ke arah yang diliat nando kecuali eka.jpg"
image eka_balik_badan = "TO CANTEEN - eka balik badan.jpg"

# The game starts here.
#Chapter 1
label chapter1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene eka_luar_kelas_normal

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show navigation

    # These display lines of dialogue.
    # Scene: Luar kelas
    eka_thinking_normal "Hello… good morning…"
    eka_thinking_normal "ah, is it too stiff…?"
    eka_thinking_normal "hey guys!"
    eka_thinking_normal "Ah, do I sound too excited?"
    eka_thinking_normal "Ugh, how do people even \n introduce themselves \n for the first time…"
    eka_thinking_normal "…"
    eka_thinking_normal "sigh…"

    scene eka_luar_kelas_tutupin_muka
    eka_thinking_normal "I hate transfering school… \n what if I don’t have \n friends…."

    scene eka_buka_tas
    eka_thinking_normal "…"
    eka_thinking_normal "wait..."
    eka_thinking_shaking "I didn't forget something, \n did I?!" with hpunch

    scene eka_luar_kelas_normal
    eka_thinking_normal "Um- phone, my phone…"

    scene hand_into_bag
    eka_thinking_normal "where is it…"

    scene eka_ngeluarin_hp
    eka_thinking_normal "Ah! Thank god!"
    eka_thinking_normal "…"

    scene hand_into_bag
    eka_thinking_shaking "Please, please tell me \n I put my wallet inside \n my bag and not at home…" with hpunch
    eka_thinking_shaking "oh my god, where is it" with hpunch
    eka_thinking_shaking "!!!" with hpunch

    scene ngeluarin_dompet
    eka_thinking_normal "THANK GOD."
    budi "Eka? What are you doing \n outside?"
    eka_thinking_normal "!!!"

    scene mr_budi_looking_at_player
    eka_talking_normal "O-oh! Um-"
    eka_talking_normal "I- sorry, sir, I was just…"
    eka_thinking_normal "…anxious, I'm anxious…"
    eka_thinking_normal "I'm not prepared to face \n new peers…"
    eka_talking_normal "…"

    scene mr_budi_smiles
    budi "It's okay."
    budi "Come, let's go inside."
    eka_talking_normal "um… okay, sir."

    scene black
    #insert audio

    scene full_fokus_kelas
    eka_thinking_normal "…"
    eka_thinking_shaking "..." with hpunch
    eka_thinking_shaking "…they're all looking at me…" with hpunch
    eka_thinking_shaking "am I…" with hpunch
    eka_thinking_shaking "do I… look weird?" with hpunch
    eka_thinking_shaking "why is it so quiet…" with hpunch

    menu:
        "(walk) Stand in front of class":
            pass

    scene tangan_garuk2
    budi "Good morning class!"
    budi "It's a new term, surely \n your break was fun?"
    kelas "We want more! \n We want more!"
    budi "hahaha, what a lively class."
    budi_blur "{alpha=-0.7} where's your new year \n spirit? New year new me! {=blur_text}" (multiple=2)
    eka_thinking_shaking "worm… how will I introduce \n myself…" (multiple=2) with hpunch
    budi_blur "{alpha=-0.7} where's your new year \n spirit? New year new me! {=blur_text}" (multiple=2)
    eka_thinking_shaking "hello, guys?" (multiple=2) with hpunch
    budi_blur "{alpha=-0.7} where's your new year \n spirit? New year new me! {=blur_text}" (multiple=2)
    eka_thinking_shaking "hey, nice to meet yall?" (multiple=2) with hpunch
    budi_blur "{alpha=-0.7} where's your new year \n spirit? New year new me! {=blur_text}" (multiple=2)
    eka_thinking_shaking "good morning?" (multiple=2) with hpunch

    scene clenching_hands
    eka_thinking_shaking "im not ready at all-" with hpunch
    budi "Okay! Enough chit-chat! \n Today we have a new \n addition to this class!"
    eka_thinking_shaking "Oh. My. God." with hpunch

    scene looking_at_mr_budi
    budi "Go ahead now, Eka. \n Introduce yourself!"
    eka_thinking_normal "I'm going to die."

    menu:
        "Deep Breath":
            $ point += 5
            call .deep_breath
        "Introduce":
            call .introduce

    scene 1st_person_depan_kelas
    eka_thinking_normal "...there are several empty \n seats tho"

    jump chapter1_choosing_seat
label .deep_breath:
    scene 1st_person_depan_kelas
    eka_thinking_normal "It's okay, Eka… you can do \n this…"
    eka_thinking_normal "It's only a simple \n introduction..."
    eka_thinking_normal "you can do this…!"
    eka_talking_normal "Uh- hello! My name's Eka, \n I'm a transfer student \n from St. Bernadicus \n High School."
    eka_talking_normal "Uhhh-"
    eka_talking_normal "Nice to meet you all!"
    eka_talking_normal "Nice to meet you all!" (multiple=5)
    kelas "they're cute…" (multiple=5)
    kelas1 "hehe" (multiple=5)
    kelas2 "nice to meet you too!" (multiple=5)
    kelas3 "hi!" (multiple=5)
    eka_thinking_shaking "OH MY GOD I DID IT." with hpunch

    scene looking_at_mr_budi_hes_smiling
    budi "Well done! Now you may \n sit."
    budi "Feel free to choose your \n own seat."

    return
label .introduce:
    scene 1st_person_depan_kelas
    eka_talking_normal "He-"
    eka_thinking_normal "...everyone is staring-"
    eka_thinking_shaking "I want to make a great \n first impression-" with hpunch
    eka_thinking_shaking "but-" with hpunch
    eka_thinking_shaking "should I really say hello? \n Is it too formal? \n Should I say good morning \n instead?" with hpunch
    eka_thinking_shaking "do I look stupid? \n Why is everyone staring \n at me like that…" with hpunch
    eka_talking_normal "…"
    eka_talking_normal "…" (multiple=2)
    kelas "…" (multiple=2)
    budi "…"

    scene looking_at_mr_budi
    budi "Well! So class, here's Eka, \n they're the new transfer \n student from St. \n  Bernadicus High School!"
    eka_talking_normal "…!"

    scene looking_at_mr_budi_hes_smiling
    budi "You just moved here with \n your family, right?"
    eka_talking_normal "um… yes, sir…"
    budi "Great! Now that you've \n introduced yourself, feel \n free to choose a seat!"
    eka_talking_normal "uh… okay…"
    eka_thinking_normal "ah… I missed my chance…"
    eka_thinking_normal "everyone must've \n think I'm weird…"

    return

label chapter1_choosing_seat:
    scene 1st_person_depan_kelas
    show screen choose_seat
    eka_thinking_normal "where should I sit..."
    jump chapter1_choosing_seat

label chapter1_choosing_seat_simon_scene:
    scene 1st_person_depan_kelas
    show screen choose_seat_simon_scene
    eka_thinking_normal "where should I sit..."
    jump chapter1_choosing_seat_simon_scene

label nerdy_scene:
    scene muka_nerd_shook
    hide screen choose_seat
    hide screen choose_seat_simon_scene
    $ is_nerd_interacted = True
    eka_talking_normal "um, hello"

    scene muka_nerd_tidak_senang
    nerd "…"
    eka_thinking_normal "Well… doesn't she look \n friendly…"
    menu:
        "Doubt":
            eka_thinking_normal "well… let's just… find \n another seat…"
            if not(simon_second):
                jump chapter1_choosing_seat
            else :
                jump chapter1_choosing_seat_simon_scene
        "I don't mind":
            eka_thinking_normal "well, maybe it's just me…"
            eka_thinking_normal "I'm sure she wouldn't \n mind!"
            eka_talking_normal "Hello… um, do you mind \n if I sit here?"

            scene muka_nerd_shook_even_more
            eka_thinking_normal "…well, she certainly looks \n super uncomfortable \n right now… worm."

            scene muka_nerd_nunduk
            nerd "Uh… um…"
            nerd "Actually, I… I already have \n a seatmate, but she's \n sick today so…"
            nerd "…yeah, you can't sit here."

            scene muka_nerd_senyum_sopan
            nerd "I'm really sorry!"
            eka_talking_normal "U-uh, it's okay, really!"
            eka_talking_normal "Sorry for bothering you!"
            eka_thinking_normal "(sigh) crap…"
            if not(simon_second):
                jump chapter1_choosing_seat
            else:
                jump chapter1_choosing_seat_simon_scene

    jump nerdy_scene

label bully_scene:
    scene muka_bully_seram
    hide screen choose_seat
    hide screen choose_seat_simon_scene
    eka_talking_normal "…"
    bully "…"
    eka_talking_normal "…"

    scene muka_bully_makin_melototin
    bully "…"
    eka_talking_normal "Uh, I'm- I'm sorry…"
    eka_thinking_normal "WHAT AM I THINKING…"

    if not(simon_second):
        jump chapter1_choosing_seat
    else:
        jump chapter1_choosing_seat_simon_scene

label simon_scene:
    scene simon_ngeliatin
    hide screen choose_seat
    eka_talking_normal "Hello…"
    simon_unknown "oh, hello! You wanna sit \n here?"
    menu:
        "Look around":
            $ simon_second = True
            jump chapter1_choosing_seat_simon_scene
        "Sure":
            scene choosing_seat_simon_senyum
            eka_talking_normal "yeah… hehe…"
            eka_talking_normal "This seat is empty, right?"
            simon_unknown "yep! My seatmate move \n to the front, tsk tsk, \n she abandoned me…"

            scene simon_pura2_sedih
            simon_unknown "sigh…"

            scene simon_nyengir
            simon_unknown "anyway, yes feel free to \n sit here!"
            eka_talking_normal "O-oh, well then, I will \n sit here!"
            simon "Yes, totally! By the way, \n my name's Simon."
            eka_talking_normal "Ah, nice meeting you \n Simon!"
            jump seated_down

    jump simon_scene

label simon_scene_second:
    scene simon_nyengir
    hide screen choose_seat_simon_scene
    simon_unknown "Just sit here, I don't mind,  \n really!"
    eka_talking_normal "ah, thank you so much!"
    simon "Yes, totally! By the way, \n my name's Simon."
    eka_talking_normal "Ah, nice meeting you \n Simon!"
    jump seated_down

label seated_down:
    scene guru_beres_buku
    eka_thinking_normal "sigh…"
    eka_thinking_normal "well, not a bad start"
    eka_thinking_normal "certainly CAN go worse…"
    jump seated_down_interaction_scene


label seated_down_interaction_scene:
    scene guru_beres_buku
    show screen seated_down_interaction
    eka_thinking_normal "hmmm..."
    jump seated_down_interaction_scene

label seated_down_simon_convo:
    if not(is_convo_simon_seated_down):
        $ point += 5
        $ is_convo_simon_seated_down = True
        $ whiteboard_interaction_point += 1
    scene simon_normal
    hide screen seated_down_interaction
    eka_talking_normal "um…"

    scene simon_ngeliat_player
    simon "yeah?"
    menu:
        "About school":
            eka_talking_normal "so… um…"
            eka_talking_normal "do you like… going to this \n school?"

            scene simon_surprised
            eka_thinking_normal "oh- oh, is that a weird \n question-"
            eka_talking_normal "Um- wait, neverm-"

            scene seated_down_simon_senyum
            simon "it's great, I think, going to \n this school."
            simon "I mean, I might be biased, \n all of my siblings \n also go to this school, so…"
            simon "but! The canteen food is \n nice, the library is \n awesome, and overall \n it's a great school!"
            eka_talking_normal "Ah, I see.."
            eka_thinking_normal "…is this the part where \n I ask to-"
            simon "I can show you around, \n after school?"
            eka_talking_normal "!!!"
            eka_talking_normal "Uh, yes, yes that's \n awesome! Wow!"
            eka_thinking_normal "…"
            eka_thinking_normal "WHY DID I SAY WOW… \n I WANT TO BURY MYSELF UNDERGROUND…"
            jump seated_down_interaction_scene

        "About seatmate":
            scene simon_ngeliat_player
            eka_talking_normal "so… um…"
            eka_talking_normal "which one is your former \n seatmate?"

            scene simon_surprised
            eka_thinking_normal "oh- oh, is that a weird \n question-"

            scene simon_senyum_nunjuk_depan
            if is_nerd_interacted:
                simon "well, funny you said it, \n she's actually the one \n you talked to earlier, \n the girl with glasses?"
            else:
                simon "well, she's the one with \n the glasses, seated at \n front."
                eka_talking_normal "Oh- um… why did she \n move?"
                simon "that, I don't really know."
                simon "probably thinking we're \n too loud, anyway."
                eka_thinking_normal "We?"

            jump seated_down_interaction_scene

label notebook_bag_scene:
    if not(is_bag_interacted):
        $ is_bag_interacted = True
        $ whiteboard_interaction_point += 1
    scene hand_into_bag
    hide screen seated_down_interaction
    eka_thinking_normal "now that I'm seated, \n where's my notebook…"
    eka_thinking_normal "…"
    eka_thinking_normal "…"
    eka_thinking_normal "well, it should be HERE… \n but… but…"
    eka_thinking_normal "…"
    eka_thinking_shaking "I didn't bring my notebook… \n Oh my god… I want to… \n Ugh…" with hpunch
    eka_thinking_shaking "…" with hpunch
    eka_thinking_shaking "…no, no, I remember \n putting it inside the bag…" with hpunch
    eka_thinking_shaking "Ah, crap where is it…" with hpunch
    eka_thinking_normal "!!!"
    eka_thinking_normal "I BRING IT!!!"
    simon "you okay?"
    eka_talking_normal "Ah- um-"

    scene seated_down_simon_senyum
    eka_talking_normal "it's fine, I thought I didn't \n bring my notebook…"

    scene seated_down_simon_concerned
    simon "Oof, lucky you. Usually \n Mr. Budi is pretty strict \n with notes and books, \n sooo…"
    eka_thinking_normal "I almost die at my first day \n of school... Great."
    eka_talking_normal "oh, well…"
    simon "…"
    jump seated_down_interaction_scene

label whiteboard_scene:
    if whiteboard_interaction_point < 2:
        eka_thinking_normal "Hmmm...I should know more \n about school and check \n my notebook first"
        jump seated_down_interaction_scene
    else:
        scene guru_depan_papan_tulis
        hide screen seated_down_interaction
        budi "Okay, now that everyone \n and everything's settled, \n let's start with the \n lesson!"
        kelas "groans…"
        budi "Now, now, everyone bring \n out your pen and paper.."
        kelas "(disaproving noises)"
        budi  "Just kidding! Hahah, I gotta \n go, actually… to deal with \n stuffs, so instead I shoud \n give you guys assignment \n to do."
        budi "But anyway, since this is the \n first day as well, I will let \n you guys off without \n assignment! Anyway, behave \n well, okay!"
        kelas "yeah!" (multiple = 4)
        kelas1 "wow, thank you so much, \n sir!" (multiple = 4)
        kelas2 "we will!" (multiple = 4)
        kelas3 "yeehaw!" (multiple = 4)
        budi "well then, I should go now. \n Remember, don't cause \n ruckus or you will get in \n trouble!"
        kelas3 "no worries sir!"
        jump andrea_nando_scene

label andrea_nando_scene:
    scene andrea_nando_normal
    andrea_unknown "hey, y'all wanna go to the \n canteen?"
    nando_unknown "isn't it too soon to be \n hungry?"
    andrea_unknown "well, it's better than doing \n nothing in here. Mr. Budi \n said nothing about \n going to the canteen."
    simon_andrea_nando "well, I don't see anything \n wrong with that, actually."

    scene andrea_shrugging
    nando_unknown "Well now it's two to one, \n I guess I gotta join."

    scene andrea_nyengir
    andrea_unknown "YO! Well then, it's \n settled, let's go!"

    scene andrea_nengok_player
    andrea_unknown "oh, feel free to join us!"
    eka_talking_normal "M-me?"
    eka_talking_normal "To the canteen?"
    simon_andrea_nando "Yeah, why not?"
    andrea "anyway, my name's \n Andrea, just remembered \n we haven't told \n our names yet!"
    nando "Ah- yes!"

    scene nando_nyengir
    nando "I'm Nando, nice to meet \n you, hehe."
    eka_talking_normal "Oh, um, same goes! \n Hehe..."
    eka_thinking_normal "keep smiling… keep smiling…"
    andrea "So, you wanna join?"
    nando "It's better tho, than being \n here doing absolutely \n nothing."
    eka_talking_normal "Uh… um..."

    menu:
        "Think":
            eka_thinking_normal "Well… I can't guarantee \n I won't be awkward…"
            menu:
                "Think":
                    eka_thinking_normal "And… what if I only \n become a burden…"
                    menu:
                        "Think":
                            eka_thinking_normal "What if… i-"
                            simon_andrea_nando "Eka? Um, something's in \n your mind?"
                            eka_talking_normal "Ah- eee not really, haha-"
                            andrea "Chiiill, it's free period, \n it's not a crime to go to the \n canteen in a free period."

                            scene simon_angkat_alis_nyengir
                            simon_andrea_nando "Well, she's right. Sooo..?"
                            eka_thinking_normal "…well, now it's only polite \n if I join, right…"
                            eka_talking_normal "Okay, then… let's go…?"
                            nando "great! Let's go!"
                            jump canteen_scene
        "Agree":
            $ point += 5
            eka_thinking_normal "well, it doesn't hurt to \n try to… join, I guess…"
            eka_talking_normal "Are you sure it's okay \n for me to join?"
            andrea "wh- of course it is! Let's \n go then!"
            eka_talking_normal "O-okay!"
            jump canteen_scene
    jump andrea_nando_scene

label canteen_scene:
    scene minus_andrea
    simon_canteen "You didn't order food?"
    eka_talking_normal "N-nah, I'm too...stuffed \n to order anything…"
    eka_thinking_normal "the fact I'm too anxious \n to drink or eat anything… \n this sucks…"
    simon_canteen "Em… how about drink? \n Juice?"
    eka_talking_normal "um… I'm fine, really, \n thank you…"
    nando_canteen "How about some snacks?"
    eka_talking_normal "I'm fine, really!"
    eka_talking_normal "Eh, um…"
    eka_talking_normal "is that too harsh- I didn't \n mean to…"
    nando_canteen "well, I'm gonna dig in, then!"

    scene andrea_duduk
    andrea "oh. My. God."
    nando_canteen "hwat… munch… what \n happened…"
    andrea "I saw Billy??"
    nando_canteen "wh?? (gulp) Really? He's at \n school?"
    nando_canteen "wow, at first day at school \n too!"
    andrea "I KNOW RIGHT."
    simon_canteen "after a whole half \n semester gone? Well, \n good thing he's back on \n track!"
    eka_talking_normal "…Billy?"
    nando_canteen "PSH! I'd be surprised if he's \n here for midterms."
    nando_canteen "he's literally gone half the \n semester! God knows \n where he was."
    eka_thinking_normal "…am I getting ignored…"
    andrea "Sources say he's going \n to school tho, but he \n doesn't go to class…"
    nando_canteen "wh-?? What is he doing \n then?"
    eka_thinking_normal "…I'm curious but they \n really ignored me so I \n will just shut up…"
    eka_thinking_normal "or…"
    menu:
        "Just ask":
            $ point += 5
            jump canteen_just_ask_scene

        "Just listen":
            jump canteen_just_listen_scene

    jump canteen_scene

label canteen_just_ask_scene:
    eka_talking_normal "Is Billy our classmate..?"
    eka_thinking_normal "WHEW THERE I ASKED IT."
    simon_canteen "Eh, no. he's from another \n class."
    andrea "he's a quiet kid. Too quiet \n even!"
    andrea "I think he got some \n creepy vibes…"
    nando_canteen "Yooo, don't say that. Hahah! \n But I gotta say he's weird in \n general, but not on the \n creepy level yet."
    andrea "YET."
    eka_thinking_normal "Oof…"
    simon_canteen "Isn't he got bullied..? \n That's why he's not \n going to classes, right?"
    andrea "well, he looks like a \n bullied person…"
    nando_canteen "he looks fucked up"
    andrea "oh my god Nando."
    andrea "but also he's right, he \n does look a bit fucked up…"
    andrea "but also he worsens it by \n not going to school!"

    jump canteen_just_listen_scene

label canteen_just_listen_scene:
    nando_canteen "…I also heard he refused his \n classmate's help?"
    nando_canteen "he really just… ignore them."
    nando_canteen "or you could say he's quite \n annoyed to be helped, tho."
    andrea "…wow, people can do \n that?"

    scene nando_surprised
    nando_canteen "Oh shoot, I see him!"

    scene semua_orang_nengok
    eka_thinking_normal "Oh??"

    scene eka_balik_badan
    nando_canteen "Aaand, he goes. Wow he \n really don't waste any time \n at the canteen."
    eka_thinking_normal "I missed the moment! Ah..."

    scene andrea_duduk
    eka_thinking_normal "Now I only know vague \n description of Billy…"
    eka_thinking_normal "I can only hope I won't be \n like that…"
    eka_thinking_normal "well, not that it's possible… \n I will not drive people \n away, won’t I…"
    eka_thinking_normal "right?"

    jump canteen_just_listen_scene #later replace with jump eka_room
