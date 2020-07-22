﻿# The script of the game goes in this file.

#define effect and transitions
define persistent.dialogueBoxOpacity = 0.75 #opacity of dialogue box
define dissolve = Dissolve(0.2) #transition between similar scenes
define fade_to_black = Fade(0.5,1.5,0.5) #transition between distinct scenes


# Declare characters used by this game. The color argument colorizes the
# name of the character.
define placeholder = Character("",window_background="eka_talking_normal.png", window_xpos=2000, window_ypos=2000)
define eka_thinking_normal = Character("Eka",window_xpos= 650, window_ypos = 1500, window_background= Transform("eka_thinking_normal.png", alpha=persistent.dialogueBoxOpacity), who_xpos = -60, who_ypos = 160, who_color="#38379d",what_xpos=150, what_ypos = 230)
define eka_thinking_shaking = Character(kind=eka_thinking_normal, window_background=Transform("eka_thinking_shaking.png", alpha=persistent.dialogueBoxOpacity))
define eka_talking_normal = Character(kind=eka_thinking_normal, window_xpos= 650, window_ypos = 650, window_background=Transform("eka_talking_normal.png",alpha=persistent.dialogueBoxOpacity), who_xpos = -60, who_ypos = 150, what_xpos=150, what_ypos = 230)
define eka_talking_normal_intro_kelas = Character(kind=eka_talking_normal, window_xpos = 650, window_ypos = 1500)
define eka_talking_budi_intro_kelas = Character(kind=eka_talking_normal, window_xpos = 800, window_ypos = 200)
define eka_talking_nerd = Character(kind=eka_talking_normal_intro_kelas, window_background=Transform("eka_talking_normal_flipped.png", alpha=persistent.dialogueBoxOpacity))
define eka_talking_bully = Character(kind=eka_talking_normal_intro_kelas)
define eka_talking_simon = Character(kind=eka_talking_normal_intro_kelas)
define eka_talking_seated_down = Character(kind=eka_talking_nerd)
define eka_talking_shaking = Character(kind=eka_talking_normal, window_background=Transform("eka_talking_shaking.png",alpha=persistent.dialogueBoxOpacity))
define budi = Character("Mr. Budi", window_xpos= 750, window_ypos = 300, window_background=Transform("talking_normal_flipped.png",alpha=persistent.dialogueBoxOpacity),who_xpos = -60, who_ypos = 150, who_color="#717171",what_xpos=150, what_ypos = 230, what_color="#000000")
define budi_depan_papan_tulis = Character(kind=budi, window_xpos = 500, window_ypos = 150)
define budi_blur = Character(kind=budi, window_ypos = 300)
define kelas = Character("Class", window_xpos= 650, window_ypos = 200, window_background=Transform("class talking in unison.png",alpha=persistent.dialogueBoxOpacity),who_xpos = -60, who_ypos = 150, who_color="#717171",what_xpos=150, what_ypos = 230, what_color="#000000")
define kelas1 = Character(kind=kelas, window_xpos = 1100, window_ypos = 200)
define kelas2 = Character(kind=kelas, window_xpos = 1150, window_ypos = 800)
define kelas3 = Character(kind=kelas, window_xpos = 650, window_ypos = 600)
define nerd = Character("???", window_xpos = 530, window_ypos = 200, window_background=Transform("talking_normal_flipped.png",alpha=persistent.dialogueBoxOpacity), who_xpos = -60, who_ypos = 150, who_color="#717171", what_xpos=150, what_ypos = 230, what_color="#000000")
define bully = Character(kind=nerd, window_ypos = 150, who_xpos = -60, who_ypos = 150, what_xpos=150, what_ypos = 230 )
define budi_blur = Character(kind=budi, window_ypos = 300)
define simon_unknown = Character("???", window_xpos = 850, window_ypos = 200, window_background=Transform("talking_normal.png",alpha=persistent.dialogueBoxOpacity), who_xpos = -60, who_ypos = 150, who_color = "#c43730",what_xpos=150, what_ypos = 230, what_color="#000000")
define simon = Character("Simon", kind=simon_unknown)
define simon_not_seen = Character("Simon", kind=simon, window_xpos=550, window_ypos= 700)
define simon_andrea_nando = Character("Simon", kind=simon_unknown, window_xpos = 800, window_ypos = 1300 ,window_background=Transform("talking_normal_rotate.png",alpha=persistent.dialogueBoxOpacity))
define andrea_unknown = Character("???", window_xpos = 850, window_ypos = 150, window_background=Transform("talking_normal.png",alpha=persistent.dialogueBoxOpacity), who_xpos = -60, who_ypos = 150, who_color = "#e44fca", what_xpos=150, what_ypos = 230, what_color="#000000")
define andrea = Character("Andrea", kind=andrea_unknown)
define nando_unknown = Character("???", window_xpos = 600, window_ypos = 200, window_background =Transform("talking_normal.png",alpha=persistent.dialogueBoxOpacity), who_xpos = -60, who_ypos = 150, who_color = "#40a03f", what_xpos=150, what_ypos = 230, what_color="#000000")
define nando = Character("Nando", kind=nando_unknown)
define eka_andrea_nando = Character(kind=eka_talking_normal, window_xpos=800, window_ypos = 1400, window_background = Transform("eka_talking_normal_rotate.png", alpha=persistent.dialogueBoxOpacity))
define eka_canteen = Character(kind=eka_andrea_nando)
define simon_canteen = Character("Simon", window_xpos = 600, window_ypos = 1350, kind=simon_unknown, window_background = Transform("talking_normal_rotate.png",alpha=persistent.dialogueBoxOpacity))
define nando_canteen = Character("Nando", kind=nando_unknown, window_ypos = 500, window_xpos=650, window_background = Transform("talking_normal.png",alpha=persistent.dialogueBoxOpacity))
define andrea_canteen = Character(kind=andrea, window_ypos= 550)
define eka_thinking_normal_room = Character(kind=eka_thinking_normal, window_background=Transform("eka_thinking_normal_small.png", alpha=persistent.dialogueBoxOpacity),window_xpos= 600, window_ypos = 1300, who_xpos = -110, what_xpos=100)
define eka_talking_normal_room = Character(kind=eka_talking_normal, window_xpos =600, window_ypos= 1000, window_background = Transform("eka_talking_normal_flipped.png",alpha=persistent.dialogueBoxOpacity))

#chapter variables
default is_chapter1_played = False
#define variables
default point = 0
default simon_second = False
default whiteboard_interaction_point = 0
default is_choose_seat_showed_1st_time = False #flag to control whether choose seat has been showed / not
default is_convo_simon_seated_down = False
default is_nerd_interacted = False
default is_bully_interacted = False
default is_bag_interacted = False

#phone variables
default is_door_interacted_day_1 = False
default is_dailynote_interacted_day_1 = False
default is_chatnow_interacted_day_1 = False
default is_todolist_interacted_day_1 = False
default is_browser_interacted_day_1 = False

#define images
#Chapter 1 scenes
image eka_luar_kelas_normal = "otw_introduksi_normal.jpg"
image eka_luar_kelas_tutupin_muka = "OTW INTRODUKSI - nutupin muka di tas.jpg"
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
image seated_down_hand_into_bag = "SEATED DOWN - hand into bag.jpg"
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
image eka_guling = "EKAS ROOM - eka guling2 di kasur, mukaknya ditempelin di bantal.jpg"
image eka_kasur_megang_hp = "EKAS ROOM - eka tiduran di kasur, megang hp.jpg"
image eka_hp = "EKAS ROOM - eka ngangkat kepalanya, hp di tangan.jpg"
image eka_deket_dispenser = "EKAS ROOM - grab water - deket dispenser.jpg"
image eka_minum_air = "EKAS ROOM - grab water - minum aer.jpg"
image eka_taro_gelas = "EKAS ROOM - grab water - gelas kosong ditaro.jpg"
image eka_depan_kaca = "EKAS ROOM - WASH FACE - depan kaca 1.jpg"
image eka_splashing_face = "EKAS ROOM - WASH FACE - splashing face with water.jpg"
image eka_depan_kaca_2 = "EKAS ROOM - WASH FACE - depan kaca 2.jpg"
image light_switch_on = "EKAS ROOM - LIGHT SWITCH on.jpg"
image light_switch_off = "EKAS ROOM - LIGHT SWITCH off.jpg"
image eka_sleep = "EKAS ROOM - lights off, ada lampu tumblr nyala.jpg"

#gyrate screens
label transition:
    $ renpy.movie_cutscene('video/SPLASH_SCREEN_ZOOMING.webm')

label main_menu_sc:
    show screen main_menu_select
    placeholder "Published@2020"
# The game starts here.
#Chapter 1
label chapter1:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    hide screen main_menu_select
    hide screen chapter_selection
    $ renpy.movie_cutscene('video/splash-chap-6-JANUARY-1_1.webm')
    show screen chapter1_splash
    placeholder "hmmm"
    hide screen chapter1_splash
    scene eka_luar_kelas_normal with dissolve
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
    eka_thinking_normal "Ugh, how do people even introduce themselves for \nthe first time…"
    eka_thinking_normal "…"
    eka_thinking_normal "sigh…"

    scene eka_luar_kelas_tutupin_muka with dissolve
    eka_thinking_normal "I hate transfering school… \nwhat if I don’t have friends…."

    scene eka_buka_tas with dissolve
    eka_thinking_normal "…"
    eka_thinking_normal "wait..."
    eka_thinking_shaking "I didn't forget something, \ndid I?!" with hpunch

    scene eka_luar_kelas_normal with dissolve
    eka_thinking_normal "Um- phone, my phone…"

    scene hand_into_bag with fade_to_black
    eka_thinking_normal "where is it…"

    scene eka_ngeluarin_hp with dissolve
    eka_thinking_normal "Ah! Thank god!"
    eka_thinking_normal "…"

    scene hand_into_bag with dissolve
    eka_thinking_shaking "Please, please tell me I \nput my wallet inside my \nbag and not at home…" with hpunch
    eka_thinking_shaking "oh my god, where is it!?" with hpunch
    eka_thinking_shaking "!!!" with hpunch

    scene ngeluarin_dompet with dissolve
    eka_thinking_normal "THANK GOD."
    budi "Eka? What are you doing \noutside?"
    eka_thinking_normal "!!!"

    scene mr_budi_looking_at_player with fade_to_black
    eka_talking_normal "O-oh! Um-"
    eka_talking_normal "I- sorry, sir, I was just…"
    eka_thinking_normal "…anxious, I'm anxious…"
    eka_thinking_normal "I'm not prepared to face new peers…"
    eka_talking_normal "…"

    scene mr_budi_smiles with dissolve
    budi "It's okay."
    budi "Come, let's go inside."
    eka_talking_normal "um… okay, sir."

    scene black
    #insert audio

    scene full_fokus_kelas with fade_to_black
    eka_thinking_normal "…"
    eka_thinking_shaking "..." with hpunch
    eka_thinking_shaking "…they're all looking at me…" with hpunch
    eka_thinking_shaking "am I…" with hpunch
    eka_thinking_shaking "do I… look weird?" with hpunch
    eka_thinking_shaking "why is it so quiet…" with hpunch
    jump walk_interface

label walk_interface:
    show screen walk_button
    placeholder "hmmm"
    jump walk_interface

label after_walk:
    hide screen walk_button
    scene tangan_garuk2 with dissolve
    budi "Good morning class!"
    budi "It's a new term, surely your \nbreak was fun?"
    kelas "We want more! We want \nmore!"
    budi "hahaha, what a lively class."
    budi_blur "where's your new year spirit? \nNew year new me!"
    show screen tangan_garuk2_shaking
    eka_thinking_shaking "worm… how will I introduce myself…" with hpunch
    eka_thinking_shaking "hello, guys?" with hpunch
    eka_thinking_shaking "hey, nice to meet yall?" with hpunch
    eka_thinking_shaking "good morning?" with hpunch

    hide screen tangan_garuk2_shaking
    show screen clenching_hand
    eka_thinking_shaking "im not ready at all-" with hpunch
    hide screen clenching_hand
    scene clenching_hands with dissolve
    budi "Okay! Enough chit-chat! \nToday we have a new addition \nto this class!"
    show screen clenching_hand
    eka_thinking_shaking "Oh. My. God." with hpunch

    hide screen clenching_hand
    scene looking_at_mr_budi with dissolve
    budi "Go ahead now, Eka. Introduce yourself!"
    eka_thinking_normal "I'm going to die."

    menu:
        "Deep Breath":
            $ point += 5
            call .deep_breath from _call_after_walk_deep_breath
        "Introduce":
            call .introduce from _call_after_walk_introduce

    scene 1st_person_depan_kelas with fade_to_black
    eka_thinking_normal "...there are several empty \nseats tho"

    jump chapter1_choosing_seat
label .deep_breath:
    scene 1st_person_depan_kelas with fade_to_black
    eka_thinking_normal "It's okay, Eka… you can do \nthis…"
    eka_thinking_normal "It's only a simple introduction..."
    eka_thinking_normal "you can do this…!"
    eka_talking_normal_intro_kelas "Uh- hello! My name's Eka, I'm a transfer student from St. Bernadicus High School."
    eka_talking_normal_intro_kelas "Uhhh-"
    eka_talking_normal_intro_kelas "Nice to meet you all!"
    eka_talking_normal_intro_kelas "Nice to meet you all!" (multiple=5)
    kelas "they're cute…"
    kelas "hehe"
    kelas "nice to meet you too!"
    kelas "hi!"
    eka_thinking_shaking "OH MY GOD I DID IT." with hpunch

    scene looking_at_mr_budi_hes_smiling with fade_to_black
    budi "Well done! Now you may sit."
    budi "Feel free to choose your own \nseat."

    return
label .introduce:
    scene 1st_person_depan_kelas with fade_to_black
    eka_talking_normal_intro_kelas "He-"
    eka_thinking_normal "...everyone is staring-"
    eka_thinking_shaking "I want to make a great first impression-" with hpunch
    eka_thinking_shaking "but-" with hpunch
    eka_thinking_shaking "should I really say hello? \nIs it too formal? Should I say \ngood morning instead?" with hpunch
    eka_thinking_shaking "do I look stupid? Why is \neveryone staring at me \nlike that…" with hpunch
    eka_talking_normal_intro_kelas "…"
    eka_talking_normal_intro_kelas "…" (multiple=2)
    kelas "…" (multiple=2)
    budi "…"

    scene looking_at_mr_budi with fade_to_black
    budi "Well! So class, here's Eka, \nthey're the new transfer \nstudent from St. Bernadicus \nHigh School!"
    eka_talking_budi_intro_kelas "…!"

    scene looking_at_mr_budi_hes_smiling with dissolve
    budi "You just moved here with your family, right?"
    eka_talking_budi_intro_kelas "um… yes, sir…"
    budi "Great! Now that you've \nintroduced yourself, feel free \nto choose a seat!"
    eka_talking_budi_intro_kelas "uh… okay…"
    eka_thinking_normal "ah… I missed my chance…"
    eka_thinking_normal "everyone must've think I'm weird…"

    return

label chapter1_choosing_seat:
    scene 1st_person_depan_kelas
    show screen choose_seat
    if not(is_choose_seat_showed_1st_time):
        $ is_choose_seat_showed_1st_time = True
        eka_thinking_normal "where should I sit..."
    else:
        placeholder "hmmm"
    jump chapter1_choosing_seat

label chapter1_choosing_seat_simon_scene:
    scene 1st_person_depan_kelas
    show screen choose_seat_simon_scene
    if not(is_choose_seat_showed_1st_time):
        $ is_choose_seat_showed_1st_time = True
        eka_thinking_normal "where should I sit..."
    else:
        placeholder "hmmm"
    jump chapter1_choosing_seat_simon_scene

label nerdy_scene:
    hide screen choose_seat
    hide screen choose_seat_simon_scene
    scene muka_nerd_shook with fade_to_black
    $ is_nerd_interacted = True
    eka_talking_nerd "um, hello"

    scene muka_nerd_tidak_senang with dissolve
    nerd "…"
    eka_thinking_normal "Well… doesn't she look \nfriendly…"
    menu:
        "Doubt":
            eka_thinking_normal "well… let's just… find another seat…"
            if not(simon_second):
                jump chapter1_choosing_seat
            else :
                jump chapter1_choosing_seat_simon_scene
        "I don't mind":
            eka_thinking_normal "well, maybe it's just me…"
            eka_thinking_normal "I'm sure she wouldn't mind!"
            eka_talking_nerd "Hello… um, do you mind if I sit here?"

            scene muka_nerd_shook_even_more with dissolve
            eka_thinking_normal "…well, she certainly looks \nsuper uncomfortable right \nnow… worm."

            scene muka_nerd_nunduk with dissolve
            nerd "Uh… um…"
            nerd "Actually, I… I already have a seatmate, but she's sick today \nso…"
            nerd "…yeah, you can't sit here."

            scene muka_nerd_senyum_sopan with dissolve
            nerd "I'm really sorry!"
            eka_talking_nerd "U-uh, it's okay, really!"
            eka_talking_nerd "Sorry for bothering you!"
            eka_thinking_normal "(sigh) crap…"
            if not(simon_second):
                jump chapter1_choosing_seat
            else:
                jump chapter1_choosing_seat_simon_scene

    jump nerdy_scene

label bully_scene:
    hide screen choose_seat
    hide screen choose_seat_simon_scene
    scene muka_bully_seram with fade_to_black
    $ is_bully_interacted = True
    eka_talking_bully "…"
    bully "…"
    eka_talking_bully "…"

    scene muka_bully_makin_melototin with dissolve
    bully "…"
    eka_talking_bully "Uh, I'm- I'm sorry…"
    eka_thinking_normal "WHAT AM I THINKING…"

    if not(simon_second):
        jump chapter1_choosing_seat
    else:
        jump chapter1_choosing_seat_simon_scene

label simon_scene:
    hide screen choose_seat
    hide screen choose_seat_simon_scene
    scene simon_ngeliatin with fade_to_black
    eka_talking_simon "Hello…"
    simon_unknown "oh, hello! You wanna sit here?"
    menu:
        "Look around":
            $ simon_second = True
            jump chapter1_choosing_seat_simon_scene
        "Sure":
            scene choosing_seat_simon_senyum with dissolve
            eka_talking_simon "yeah… hehe…"
            eka_talking_simon "This seat is empty, right?"
            simon_unknown "yep! My seatmate move to \nthe front, tsk tsk, she \nabandoned me…"

            scene simon_pura2_sedih with dissolve
            simon_unknown "sigh…"

            scene simon_nyengir with dissolve
            simon_unknown "anyway, yes feel free to sit \nhere!"
            eka_talking_simon "O-oh, well then, I will sit here!"
            simon "Yes, totally! By the way, my name's Simon."
            eka_talking_simon "Ah, nice meeting you Simon!"
            jump seated_down

    jump simon_scene

label simon_scene_second:
    hide screen choose_seat
    hide screen choose_seat_simon_scene
    scene simon_nyengir with fade_to_black
    simon_unknown "Just sit here, I don't mind, \nreally!"
    eka_talking_simon "ah, thank you so much!"
    simon "Yes, totally! By the way, my name's Simon."
    eka_talking_simon "Ah, nice meeting you Simon!"
    jump seated_down

label seated_down:
    scene guru_beres_buku with fade_to_black
    eka_thinking_normal "sigh…"
    eka_thinking_normal "well, not a bad start"
    eka_thinking_normal "certainly CAN go worse…"
    jump seated_down_interaction_scene


label seated_down_interaction_scene:
    scene guru_beres_buku
    show screen seated_down_interaction
    placeholder "hmmm..."
    jump seated_down_interaction_scene

label seated_down_simon_convo:
    hide screen seated_down_interaction
    if not(is_convo_simon_seated_down):
        $ point += 5
        $ is_convo_simon_seated_down = True
        $ whiteboard_interaction_point += 1
    scene simon_normal with fade_to_black
    eka_talking_seated_down "um…"

    scene simon_ngeliat_player with dissolve
    simon "yeah?"
    menu:
        "About school":
            eka_talking_seated_down "so… um…"
            eka_talking_seated_down "do you like… going to this \nschool?"

            scene simon_surprised with dissolve
            eka_thinking_normal "oh- oh, is that a weird \nquestion-"
            eka_talking_seated_down "Um- wait, neverm-"

            scene seated_down_simon_senyum with dissolve
            simon "it's great, I think, going to this school."
            simon "I mean, I might be biased, \nall of my siblings also go to this school, so…"
            simon "but! The canteen food is nice, \nthe library is awesome, and \noverall it's a great school!"
            eka_talking_seated_down "Ah, I see.."
            eka_thinking_normal "…is this the part where \nI ask to-"
            simon "I can show you around, after school?"
            eka_talking_seated_down "!!!"
            eka_talking_seated_down "Uh, yes, yes that's awesome! Wow!"
            eka_thinking_normal "…"
            eka_thinking_normal "WHY DID I SAY WOW… I WANT TO BURY MYSELF UNDERGROUND…"
            jump seated_down_interaction_scene

        "About seatmate":
            scene simon_ngeliat_player with dissolve
            eka_talking_seated_down "so… um…"
            eka_talking_seated_down "which one is your former seatmate?"

            scene simon_surprised with dissolve
            eka_thinking_normal "oh- oh, is that a weird \nquestion-"

            scene simon_senyum_nunjuk_depan with dissolve
            if is_nerd_interacted:
                simon "well, funny you said it, she's actually the one you talked to earlier, the girl with glasses?"
            else:
                simon "well, she's the one with the glasses, seated at front."
                eka_talking_seated_down "Oh- um… why did she move?"
                simon "that, I don't really know."
                simon "probably thinking we're too \nloud, anyway."
                eka_thinking_normal "We?"

            jump seated_down_interaction_scene

label notebook_bag_scene:
    hide screen seated_down_interaction
    if not(is_bag_interacted):
        $ is_bag_interacted = True
        $ whiteboard_interaction_point += 1
    scene seated_down_hand_into_bag with dissolve
    eka_thinking_normal "now that I'm seated, where's \nmy notebook…"
    eka_thinking_normal "…"
    eka_thinking_normal "…"
    eka_thinking_normal "well, it should be HERE… but… but…"
    eka_thinking_normal "…"
    eka_thinking_shaking "I didn't bring my notebook… \nOh my god… I want to… \nUgh…" with hpunch
    eka_thinking_shaking "…" with hpunch
    eka_thinking_shaking "…no, no, I remember putting \nit inside the bag…" with hpunch
    eka_thinking_shaking "Ah, crap where is it…" with hpunch
    eka_thinking_normal "!!!"
    eka_thinking_normal "I BRING IT!!!"
    simon_not_seen "you okay?"
    eka_talking_seated_down "Ah- um-"

    scene seated_down_simon_senyum with fade_to_black
    eka_talking_seated_down "it's fine, I thought I didn't \nbring my notebook…"

    scene seated_down_simon_concerned with dissolve
    simon "Oof, lucky you. Usually Mr. \nBudi is pretty strict with notes \nand books, sooo…"
    eka_thinking_normal "I almost die at my first day of school... Great."
    eka_talking_seated_down "oh, well…"
    simon "…"
    jump seated_down_interaction_scene

label whiteboard_scene:
    if whiteboard_interaction_point < 2:
        eka_thinking_normal "Hmmm...I should know more about school and check my notebook first"
        jump seated_down_interaction_scene
    else:
        scene guru_depan_papan_tulis with dissolve
        hide screen seated_down_interaction
        budi_depan_papan_tulis "Okay, now that everyone and everything's settled, let's start with the lesson!"
        kelas "groans…"
        budi_depan_papan_tulis "Now, now, everyone bring out your pen and paper.."
        kelas "(disaproving noises)"
        budi_depan_papan_tulis  "Just kidding! Hahah, I gotta go, actually… to deal with stuffs, so instead I shoud give you guys assignment to do."
        budi_depan_papan_tulis "But anyway, since this is the \nfirst day as well, I will let you \nguys off without assignment! Anyway, behave well, okay!"
        kelas "yeah!"
        kelas "wow, thank you so much, sir!"
        kelas "we will!"
        kelas "yeehaw!"
        budi_depan_papan_tulis "well then, I should go now. Remember, don't cause ruckus \nor you will get in trouble!"
        kelas "no worries sir!"
        jump andrea_nando_scene

label andrea_nando_scene:
    scene andrea_nando_normal with fade_to_black
    andrea_unknown "hey, y'all wanna go to the canteen?"
    nando_unknown "isn't it too soon to be hungry?"
    andrea_unknown "well, it's better than doing \nnothing in here. Mr. Budi said nothing about going to the canteen."
    simon_andrea_nando "well, I don't see anything wrong with that, actually."

    scene andrea_shrugging with dissolve
    nando_unknown "Well now it's two to one, \nI guess I gotta join."

    scene andrea_nyengir with dissolve
    andrea_unknown "YO! Well then, it's settled, \nlet's go!"

    scene andrea_nengok_player with dissolve
    andrea_unknown "oh, feel free to join us!"
    eka_andrea_nando "M-me?"
    eka_andrea_nando "To the canteen?"
    simon_andrea_nando "Yeah, why not?"
    andrea "anyway, my name's Andrea, \njust remembered we haven't \ntold our names yet!"
    nando "Ah- yes!"

    scene nando_nyengir with dissolve
    nando "I'm Nando, nice to meet you, hehe."
    eka_andrea_nando "Oh, um, same goes! Hehe..."
    eka_thinking_normal "keep smiling… keep smiling…"
    andrea "So, you wanna join?"
    nando "It's better tho, than being here doing absolutely nothing."
    eka_andrea_nando "Uh… um..."

    menu:
        "Think":
            eka_thinking_normal "Well… I can't guarantee \nI won't be awkward…"
            menu:
                "Think":
                    eka_thinking_normal "And… what if I only become a burden…"
                    menu:
                        "Think":
                            eka_thinking_normal "What if… i-"
                            simon_andrea_nando "Eka? Um, something's in your mind?"
                            eka_andrea_nando "Ah- eee not really, haha-"
                            andrea "Chiiill, it's free period, it's not a crime to go to the canteen in a \nfree period."

                            scene simon_angkat_alis_nyengir with dissolve
                            simon_andrea_nando "Well, she's right. Sooo..?"
                            eka_thinking_normal "…well, now it's only polite if \nI join, right…"
                            eka_andrea_nando "Okay, then… let's go…?"
                            nando "great! Let's go!"
                            jump canteen_scene
        "Agree":
            $ point += 5
            eka_thinking_normal "well, it doesn't hurt to try to… \njoin, I guess…"
            eka_andrea_nando "Are you sure it's okay for me to join?"
            andrea "wh- of course it is! Let's go \nthen!"
            eka_andrea_nando "O-okay!"
            jump canteen_scene
    jump andrea_nando_scene

label canteen_scene:
    scene minus_andrea with fade_to_black
    simon_canteen "You didn't order food?"
    eka_canteen "N-nah, I'm too...stuffed to \norder anything…"
    eka_thinking_normal "the fact I'm too anxious to \ndrink or eat anything… this \nsucks…"
    simon_canteen "Em… how about drink? Juice?"
    eka_canteen "um… I'm fine, really, thank \nyou…"
    nando_canteen "How about some snacks?"
    eka_canteen "I'm fine, really!"
    eka_canteen "Eh, um…"
    eka_canteen "is that too harsh- I didn't mean \nto…"
    nando_canteen "well, I'm gonna dig in, then!"

    scene andrea_duduk with dissolve
    andrea_canteen "oh. My. God."
    nando_canteen "hwat… munch… what \nhappened…"
    andrea_canteen "I saw Billy??"
    nando_canteen "wh?? (gulp) Really? He's at \nschool?"
    nando_canteen "wow, at first day at school too!"
    andrea_canteen "I KNOW RIGHT."
    simon_canteen "after a whole half semester \ngone? Well, good thing he's \nback on track!"
    eka_canteen "…Billy?"
    nando_canteen "PSH! I'd be surprised if he's \nhere for midterms."
    nando_canteen "he's literally gone half the semester! God knows where \nhe was."
    eka_thinking_normal "…am I getting ignored…"
    andrea_canteen "Sources say he's going to \nschool tho, but he doesn't go \nto class…"
    nando_canteen "wh-?? What is he doing then?"
    eka_thinking_normal "…I'm curious but they really ignored me so I will just \nshut up…"
    eka_thinking_normal "or…"
    menu:
        "Just ask":
            $ point += 5
            jump canteen_just_ask_scene

        "Just listen":
            jump canteen_just_listen_scene

    jump canteen_scene

label canteen_just_ask_scene:
    eka_canteen "Is Billy our classmate..?"
    eka_thinking_normal "WHEW THERE I ASKED IT."
    simon_canteen "Eh, no. he's from another class."
    andrea_canteen "he's a quiet kid. Too quiet \neven!"
    andrea_canteen "I think he got some creepy \nvibes…"
    nando_canteen "Yooo, don't say that. Hahah! \nBut I gotta say he's weird in general, but not on the creepy level yet."
    andrea_canteen "YET."
    eka_thinking_normal "Oof…"
    simon_canteen "Isn't he got bullied..? That's \nwhy he's not going to classes, right?"
    andrea_canteen "well, he looks like a bullied person…"
    nando_canteen "he looks fucked up"
    andrea_canteen "oh my god Nando."
    andrea_canteen "but also he's right, he does \nlook a bit fucked up…"
    andrea_canteen "but also he worsens it by not \ngoing to school!"

    jump canteen_just_listen_scene

label canteen_just_listen_scene:
    nando_canteen "…I also heard he refused his classmate's help?"
    nando_canteen "he really just… ignore them."
    nando_canteen "or you could say he's quite annoyed to be helped, tho."
    andrea_canteen "…wow, people can do that?"

    scene nando_surprised with dissolve
    nando_canteen "Oh shoot, I see him!"

    scene semua_orang_nengok with dissolve
    eka_thinking_normal "Oh??"

    scene eka_balik_badan with dissolve
    nando_canteen "Aaand, he goes. Wow he really don't waste any time at the canteen."
    eka_thinking_normal "I missed the moment! Ah..."

    scene andrea_duduk with dissolve
    eka_thinking_normal "Now I only know vague \ndescription of Billy…"
    eka_thinking_normal "I can only hope I won't be like that…"
    eka_thinking_normal "well, not that it's possible… \nI will not drive people away, \nwon’t I…"
    eka_thinking_normal "right?"

    jump eka_room #later replace with jump eka_room

label eka_room:
    scene eka_kasur_megang_hp with fade_to_black
    eka_talking_normal_room "..."
    eka_talking_normal_room "sigh..."
    eka_thinking_normal_room "well, there we go… my \nfirst day at the new school\n…"
    eka_thinking_normal_room "I don't really know if I \nshould be glad or not…"
    eka_thinking_normal_room "…I should be, right?"
    eka_thinking_normal_room "It's not that bad… I think…"
    scene eka_guling with dissolve
    eka_talking_normal_room "Ughh… it's okay, you did your best, Eka…"
    eka_talking_normal_room "…"
    jump eka_room_select

label eka_room_select:
    hide screen phone_screen
    scene eka_hp with dissolve
    show screen room_interaction
    if is_door_interacted_day_1 and is_dailynote_interacted_day_1:
        placeholder "hmmm"
    else:
        eka_thinking_normal_room "I'm bored…"
    jump eka_room_select

label phone_interface:
    hide screen room_interaction
    hide screen note_bg
    hide screen note_bg_static
    hide screen day_one_note_title
    hide screen day_one_high_point_seq_1
    hide screen day_one_high_point_seq_2
    hide screen day_one_high_point_seq_3
    hide screen day_one_high_point_seq_4
    hide screen day_one_high_point_seq_5
    hide screen day_one_low_point_seq_1
    hide screen day_one_low_point_seq_2
    hide screen day_one_low_point_seq_3
    hide screen day_one_low_point_seq_4
    hide screen day_one_low_point_seq_5
    hide screen day_one_low_point_seq_6

    hide screen chatnow_screen
    hide screen todolist_screen
    hide screen browser_screen
    hide screen music_screen

    show screen phone_screen
    if is_dailynote_interacted_day_1 and is_chatnow_interacted_day_1 and is_todolist_interacted_day_1 and is_browser_interacted_day_1:
        eka_thinking_normal "Well then, I guess I have no \nother thing to do in this \nphone…"
        eka_thinking_normal "…or do i…."
        eka_thinking_normal "…no no, I didn't."
        eka_thinking_normal "Okay then, let's go back."

    placeholder "Published@2020"
    jump phone_interface

image day_one_low_point_seq_1_0 = Text("exhausted..and out of place",color="#000000",size=40,xalign=0.2,yalign=0.2)
label daily_note_interface:
    hide screen phone_screen
    if not(is_dailynote_interacted_day_1):
        show screen note_bg
        placeholder "Published@2020"
        show screen day_one_note_title
        placeholder "Published@2020"
        if point < 15:
            $ is_dailynote_interacted_day_1 = True
            show screen day_one_low_point_seq_1
            placeholder "Published@2020"
            show screen day_one_low_point_seq_2
            placeholder "Published@2020"
            show screen day_one_low_point_seq_3
            placeholder "Published@2020"
            show screen day_one_low_point_seq_4
            placeholder "Published@2020"
            show screen day_one_low_point_seq_5
            placeholder "Published@2020"
            show screen day_one_low_point_seq_6
            placeholder "Published@2020"
        else:
            $ is_dailynote_interacted_day_1 = True
            show screen day_one_high_point_seq_1
            placeholder "Published@2020"
            show screen day_one_high_point_seq_2
            placeholder "Published@2020"
            show screen day_one_high_point_seq_3
            placeholder "Published@2020"
            show screen day_one_high_point_seq_4
            placeholder "Published@2020"
            show screen day_one_high_point_seq_5
            placeholder "Published@2020"
    else:
        hide screen note_bg
        show screen note_bg_static
        show screen day_one_note_title
        if point < 15:
            hide screen day_one_low_point_seq_1
            hide screen day_one_low_point_seq_2
            hide screen day_one_low_point_seq_3
            hide screen day_one_low_point_seq_4
            hide screen day_one_low_point_seq_5
            hide screen day_one_low_point_seq_6
            show screen day_one_low_point_seq_1
            show screen day_one_low_point_seq_2
            show screen day_one_low_point_seq_3
            show screen day_one_low_point_seq_4
            show screen day_one_low_point_seq_5
            show screen day_one_low_point_seq_6
        else:
            hide screen day_one_high_point_seq_1
            hide screen day_one_high_point_seq_2
            hide screen day_one_high_point_seq_3
            hide screen day_one_high_point_seq_4
            hide screen day_one_high_point_seq_5
            show screen day_one_high_point_seq_1
            show screen day_one_high_point_seq_2
            show screen day_one_high_point_seq_3
            show screen day_one_high_point_seq_4
            show screen day_one_high_point_seq_5
        placeholder "Published@2020"
    jump daily_note_interface

label inactive_note:
    hide screen note_bg
    show screen note_bg_static
    show screen day_one_note_title
    if point < 15:
        hide screen day_one_low_point_seq_1
        hide screen day_one_low_point_seq_2
        hide screen day_one_low_point_seq_3
        hide screen day_one_low_point_seq_4
        hide screen day_one_low_point_seq_5
        hide screen day_one_low_point_seq_6
        show screen day_one_low_point_seq_1
        show screen day_one_low_point_seq_2
        show screen day_one_low_point_seq_3
        show screen day_one_low_point_seq_4
        show screen day_one_low_point_seq_5
        show screen day_one_low_point_seq_6
    else:
        hide screen day_one_high_point_seq_1
        hide screen day_one_high_point_seq_2
        hide screen day_one_high_point_seq_3
        hide screen day_one_high_point_seq_4
        hide screen day_one_high_point_seq_5
        show screen day_one_high_point_seq_1
        show screen day_one_high_point_seq_2
        show screen day_one_high_point_seq_3
        show screen day_one_high_point_seq_4
        show screen day_one_high_point_seq_5
    eka_thinking_normal "W-what am I doing here again"
    eka_thinking_normal "I already write today's entry"
    eka_thinking_normal "I'm sleepy tho…"
    jump phone_interface

label chatnow_interface:
    hide screen phone_screen
    show screen chatnow_screen
    $ is_chatnow_interacted_day_1 = True
    eka_thinking_normal "…I don't have any new chats."
    jump phone_interface

label todolist_interface:
    hide screen phone_screen
    show screen todolist_screen
    $ is_todolist_interacted_day_1 = True
    eka_thinking_normal "wow good as new."
    eka_thinking_normal "I don't have any new to do \nlist…"
    eka_thinking_normal "But maybe I should start \nputting homework list here…"
    eka_thinking_normal "Oh well, as long as we don't \nhave any homeworks…"
    jump phone_interface

label browser_interface:
    hide screen phone_screen
    show screen browser_screen
    $ is_browser_interacted_day_1  = True
    if is_dailynote_interacted_day_1:
        eka_thinking_normal "I'm actually already sleepy..."
        eka_thinking_normal "maybe later when I need something to search on the internet?"
    else:
        eka_thinking_normal "I don't feel like browsing internet..."
        eka_thinking_normal "maybe later when I need something to search on the internet?"
        eka_thinking_normal "I do feel like I have to do something on my phone tho…."
    jump phone_interface

label phone_interface_with_music:
    hide screen room_interaction
    hide screen note_bg
    hide screen note_bg_static
    hide screen day_one_note_title
    hide screen day_one_high_point_seq_1
    hide screen day_one_high_point_seq_2
    hide screen day_one_high_point_seq_3
    hide screen day_one_high_point_seq_4
    hide screen day_one_high_point_seq_5
    hide screen day_one_low_point_seq_1
    hide screen day_one_low_point_seq_2
    hide screen day_one_low_point_seq_3
    hide screen day_one_low_point_seq_4
    hide screen day_one_low_point_seq_5
    hide screen day_one_low_point_seq_6

    hide screen chatnow_screen
    hide screen todolist_screen
    hide screen browser_screen

    hide screen phone_screen
    show screen music_screen
    placeholder "hmmm"
    jump phone_interface_with_music

label door_option:
    $ is_door_interacted_day_1 = True
    menu:
        "Grab water":
            jump grab_water

        "Wash face":
            jump wash_face

label grab_water:
    hide screen room_interaction
    scene eka_deket_dispenser with fade_to_black
    eka_thinking_normal "I didn't realize I was thirsty… \ngood thing I remember."
    scene eka_minum_air with dissolve
    eka_thinking_normal "drinking cold water always \nmakes me calmer"
    scene eka_taro_gelas with dissolve
    eka_thinking_normal "Well, let's go back to bed \nthen…"
    jump eka_room_select

label wash_face:
    hide screen room_interaction
    scene eka_depan_kaca with fade_to_black
    eka_thinking_normal "Almost forgot to wash my \nface…"
    scene eka_splashing_face with dissolve
    eka_thinking_normal "phew, I'm fresh again… I feel lighter."
    scene eka_depan_kaca_2 with dissolve
    eka_thinking_normal "Well, let's go back to bed \nthen…"
    jump eka_room_select

label light_scene:
    hide screen room_interaction
    scene light_switch_on with fade_to_black
    eka_thinking_normal "the light switch…"
    if is_dailynote_interacted_day_1:
        scene light_switch_off with dissolve
        eka_thinking_normal "Well, let's turn the lights off"
        jump final_chapter1
    else:
        eka_thinking_normal "but I'm not sleepy yet…"
        jump eka_room_select

label final_chapter1:
    scene eka_sleep with fade_to_black
    eka_thinking_normal "alright then… let's go to sleep."
    eka_thinking_normal "good night…"
    stop music
    jump transition_chapter2

label transition_chapter2:
    $ is_chapter1_played = True
    $ renpy.movie_cutscene('video/splash-chap-7-JANUARY-1_1.webm')
    show screen chapter2_splash 
    placeholder "hmmm"
    hide screen chapter2_splash
    return
