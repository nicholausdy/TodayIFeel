﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
##Gyrate screens
screen eka_luar_kelas_normal_view():
    sensitive True
    side "c b r":
        area(0,0,1080,1920)
        viewport id "vp_1":
            draggable True
            add "otw_introduksi_normal.jpg"
        bar value XScrollValue("vp_1")
        vbar value YScrollValue("vp_1")

screen eka_luar_kelas_tutupin_muka_view():
    sensitive True
    side "c b r":
        area(0,0,1080,1920)
        viewport id "vp_1":
            draggable True
            add "otw_introduksi_tutupin_muka.jpg"
        bar value XScrollValue("vp_1")
        vbar value YScrollValue("vp_1")

screen eka_buka_tas_view():
    sensitive True
    side "c b r":
        area(0,0,1080,1920)
        viewport id "vp_1":
            draggable True
            add "OTW INTRODUKSI - otw buka tas.jpg"
        bar value XScrollValue("vp_1")
        vbar value YScrollValue("vp_1")


################################################################################
## In-game screens
################################################################################
image tangan_garuk2_shaking_movie = Movie(play="video/INTRODUCTION-3rd-pov-depan-kelas-tangan-garuk2-SHAKING-FONTS.webm", channel="test")
image clenching_hand_movie = Movie(play="video/INTRODUCTION-3rd-pov-depan-kelas-clenching-hands-SHAKING-FONT.webm", channel="test")
screen walk_button():
    vbox:
        imagebutton id "walk_button":
            idle "buttons/walk button.png"
            hover "buttons/walk button pressed.png"
            xpos 500
            ypos 1300
            action Jump("after_walk")

screen tangan_garuk2_shaking():
    add "tangan_garuk2_shaking_movie"

screen clenching_hand():
    add "clenching_hand_movie"
## Next button screen ##########################################################
screen next_button():
    vbox:
        imagebutton id "next_button":
            idle "buttons/next_button.png"
            #hover "hover_see_button"
            xpos 500
            ypos 1700
            action Return()
image idle_see_button = "buttons/see button.png"
image hover_see_button = "buttons/see button PRESSED.png"
image idle_see_button_small = "buttons/see button small.png"
image hover_see_button_small = "buttons/see button PRESSED small.png"
## Choosing seat screen ########################################################
screen choose_seat():
    showif not(is_bully_interacted):
        imagebutton id "bully_seat":
            idle "idle_see_button_small"
            hover "hover_see_button_small"
            xpos 560
            ypos 560
            action Jump("bully_scene")

    imagebutton id "simon_seat":
        idle "idle_see_button"
        hover "hover_see_button"
        xpos 670
        ypos 630
        action Jump("simon_scene")

    showif not(is_nerd_interacted):
        imagebutton id "nerdy_seat":
            idle "idle_see_button"
            hover "hover_see_button"
            xpos 70
            ypos 630
            action Jump("nerdy_scene")


screen choose_seat_simon_scene():
    showif not(is_bully_interacted):
        imagebutton id "bully_seat":
            idle "idle_see_button_small"
            hover "hover_see_button_small"
            xpos 560
            ypos 560
            action Jump("bully_scene")

    imagebutton id "simon_seat":
        idle "idle_see_button"
        hover "hover_see_button"
        xpos 670
        ypos 630
        action Jump("simon_scene_second")

    showif not(is_nerd_interacted):
        imagebutton id "nerdy_seat":
            idle "idle_see_button"
            hover "hover_see_button"
            xpos 70
            ypos 630
            action Jump("nerdy_scene")

image idle_poke_right_button = "buttons/poke button.png"
image hover_poke_right_button = "buttons/poke button PRESSED.png"
image idle_poke_left_button = "buttons/poke button left.png"
image hover_poke_left_button = "buttons/poke button left PRESSED.png"
image idle_grab_button = "buttons/grab button.png"
image hover_grab_button = "buttons/grab button PRESSED.png"

screen seated_down_interaction():
    showif not(is_convo_simon_seated_down):
        imagebutton id "poke_simon":
            idle "idle_poke_left_button"
            hover "hover_poke_left_button"
            xpos 100
            ypos 1400
            action Jump("seated_down_simon_convo")

    showif not(is_bag_interacted):
        imagebutton id "grab_bag":
            idle "idle_grab_button"
            hover "hover_grab_button"
            xpos 800
            ypos 1500
            action Jump("notebook_bag_scene")


    imagebutton id "see_whiteboard":
        idle "idle_see_button_small"
        hover "hover_see_button_small"
        xpos 800
        ypos 300
        action Jump("whiteboard_scene")

screen room_interaction():
    imagebutton id "light_switch":
        idle "idle_grab_button"
        hover "hover_grab_button"
        xpos 450
        ypos 400
        action Jump("light_scene")
    showif not(is_door_interacted_day_1):
        imagebutton id "door":
            idle "idle_grab_button"
            hover "hover_grab_button"
            xpos 300
            ypos 550
            action Jump("door_option")
    showif not(is_dailynote_interacted_day_1 and is_chatnow_interacted_day_1 and is_todolist_interacted_day_1 and is_browser_interacted_day_1):
        imagebutton id "phone":
            idle "idle_see_button"
            hover "hover_see_button"
            xpos 770
            ypos 1500
            action Jump("phone_interface")


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    sensitive True
    style_prefix "say"
    window:
        id "window"
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    #if not renpy.variant("small"):
    #    add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    #xsize gui.textbox_width
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action:
                text_size 60
                at choice_opacity

transform choice_opacity:
    alpha 0.75

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is choice_button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback():
                text_size 40
                text_color "#000000"
            textbutton _("History") action ShowMenu('history'):
                text_size 40
                text_color "#000000"
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True):
                text_size 40
                text_color "#000000"
            textbutton _("Auto") action Preference("auto-forward", "toggle"):
                text_size 40
                text_color "#000000"
            textbutton _("Save") action ShowMenu('save'):
                text_size 40
                text_color "#000000"
            textbutton _("Q.Save") action QuickSave():
                text_size 40
                text_color "#000000"
            textbutton _("Q.Load") action QuickLoad():
                text_size 40
                text_color "#000000"
            textbutton _("Prefs") action ShowMenu('preferences'):
                text_size 40
                text_color "#000000"


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

style main_menu_text_style:
    color "#ffffff"
    hover_color "#66e0c1"
    size 50


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
image splash_screen = Movie(play="video/SPLASH_SCREEN.webm", channel="test")
image lockbutton = "gui/overlay/lockbutton.png"
image lockbutton_pressed = "gui/overlay/lockbutton_pressed.png"
image main_menu_bg = "gui/overlay/main_menu_bg.png"

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"
    add "splash_screen"
    imagebutton id "start_button":
        idle "lockbutton"
        hover "lockbutton_pressed"
        xpos 575
        ypos 810
        action Start("transition")
    #add "main_menu_bg" xpos 500 ypos 500
    #add gui.main_menu_background

    ## This empty frame darkens the main menu.
    #frame:
    #    pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    #if gui.show_name:

    #    vbox:
    #        text "[config.name!t]":
    #            style "main_menu_title"

    #        text "[config.version]":
    #            style "main_menu_version"

    #add "gui/overlay/main_menu_title.png" xalign 0.5 yalign 0.45

    #vbox xalign 0.5 yalign 0.7:
    #    imagebutton id "load_game_button":
    #        idle "gui/overlay/main_menu_button.png"
    #        xpos 0
    #        ypos 240
    #        xsize 600
    #        ysize 150
    #        action ToggleScreen("chapter_selection")
    #    textbutton "LOAD GAME":
    #        xpos 160
    #        text_style "main_menu_text_style"
            #add this action line to make the button responsive to hover action
    #        action ToggleScreen("chapter_selection")

    #    imagebutton id "new_game_button":
    #        idle "gui/overlay/main_menu_button.png"
    #        xpos 0
    #        ypos 250
    #        xsize 600
    #        ysize 150
    #        action Start("chapter1")
    #    textbutton "NEW GAME" :
    #        xpos 160
    #        ypos 150
    #        text_style "main_menu_text_style"
            #add this action line to make the button responsive to hover action
    #        action Start("chapter1")

image bg_loop = Movie(play="video/mainmenu_BG_loop.webm", channel="test")
screen main_menu_select():
    tag menu
    add "bg_loop"
    vbox xalign 0.45 yalign 0.5:
        imagebutton id "load_game_button":
            idle "gui/overlay/LOAD_GAME_BUTTON.png"
            hover "gui/overlay/LOAD_GAME_BUTTON_pressed.png"
            xpos 120
            ypos 240
            action ToggleScreen("chapter_selection")
        imagebutton id "new_game_button":
            idle "gui/overlay/NEW_GAME_BUTTON.png"
            hover "gui/overlay/NEW_GAME_BUTTON_pressed.png"
            xpos 120
            ypos 260
            action Jump("chapter1")
        imagebutton id "exit_game_button":
            idle "gui/overlay/EXIT_GAME_BUTTON.png"
            hover "gui/overlay/EXIT_GAME_BUTTON_pressed.png"
            xpos 120
            ypos 280
            action Quit(confirm=True)

style chapter_box_day:
    color "#000000"
    size 30
    bold True
    xpos 170
    ypos 30

style chapter_box_title:
    color "#808080"
    size 60
    xpos 150
    ypos 130

#chapter selection screen
screen chapter_selection():
    tag menu

    add "gui/overlay/chap_select_header.png"
    add "gui/overlay/chap_select_bg.png" ypos 217
    side "c r":
        area (0,235,1080,1680)
        viewport id "vp_chap_select":
            draggable True
            mousewheel True
            vbox :
                spacing 50
                fixed:
                    xmaximum 914
                    ymaximum 338
                    text "MONDAY, JANUARY 6" style "chapter_box_day"
                    text "NEW KID AT SCHOOL" style "chapter_box_title"
                    imagebutton id "chapter1_select_box":
                        xpos 80
                        idle "gui/overlay/chap_select_box.png"
                        hover "gui/overlay/chap_select_box_pressed.png"
                        action Jump("chapter1")
                    showif is_chapter1_played:
                        image "gui/overlay/chapsel LAST PLAYED CHAPTER.png":
                            xpos 120
                            ypos 45

                fixed:
                    xmaximum 914
                    ymaximum 338
                    text "TUESDAY, JANUARY 7" style "chapter_box_day"
                    text "ABOUT ADAPTING" style "chapter_box_title"
                    imagebutton :
                        xpos 80
                        idle "gui/overlay/chap_select_box.png"
                        hover "gui/overlay/chap_select_box_pressed.png"
                        action NullAction()

                fixed:
                    xmaximum 914
                    ymaximum 338
                    text "WEDNESDAY, JANUARY 15" style "chapter_box_day"
                    text "CAN I SURVIVE..." style "chapter_box_title"
                    imagebutton :
                        xpos 80
                        idle "gui/overlay/chap_select_box.png"
                        hover "gui/overlay/chap_select_box_pressed.png"
                        action NullAction()

                imagebutton:
                    xpos 80
                    idle "gui/overlay/chap_select_locked.png"
                    #hover "gui/overlay/chap_select_box_pressed.png"
                    action NullAction()
                imagebutton :
                    xpos 80
                    idle "gui/overlay/chap_select_locked.png"
                    #hover "gui/overlay/chap_select_box_pressed.png"
                    action NullAction()
                imagebutton :
                    xpos 80
                    idle "gui/overlay/chap_select_locked.png"
                    #hover "gui/overlay/chap_select_box_pressed.png"
                    action NullAction()
                imagebutton :
                    xpos 80
                    idle "gui/overlay/chap_select_locked.png"
                    #hover "gui/overlay/chap_select_box_pressed.png"
                    action NullAction()
                imagebutton :
                    xpos 80
                    idle "gui/overlay/chap_select_locked.png"
                    #hover "gui/overlay/chap_select_box_pressed.png"
                    action NullAction()
        vbar value YScrollValue("vp_chap_select")

    add "gui/overlay/texture_overlay.png"

    button id "back_to_main_menu" :
        xpos 20
        ypos 70
        xsize 140
        ysize 100
        action ToggleScreen("main_menu_select")
    imagebutton id "back_to_main_menu_button" :
        idle  "gui/overlay/chaps_select_back.png"
        xpos 150
        ypos 120
        action ToggleScreen("main_menu_select")

style phone_hour:
    color "#FFFFFF"
    size 140
    xpos 50
    ypos 100

style pm:
    color "#FFFFFF"
    size 50
    xpos 90
    ypos 140

style date:
    color "#FFFFFF"
    size 50
    xpos 15
    ypos 190

image loop_splash_chap1 = Movie(play="video/splash-chap-6-JANUARY-2-LOOP_1.webm", channel="test")
image loop_splash_chap2 = Movie(play="video/splash-chap-7-JANUARY-2-LOOP_1.webm", channel="test")

screen chapter1_splash():
    add "loop_splash_chap1"
screen chapter2_splash():
    add "loop_splash_chap2"

screen phone_screen():
    add "gui/overlay/homephone_BG.jpg"
    hbox:
        text "06.52" style "phone_hour"
        text "PM" style "pm"
        text "MON, 6 JAN" style "date"
    hbox:
        imagebutton id "daily_note":
            idle "gui/overlay/homephone_dailynote.png"
            hover "gui/overlay/homephone_dailynote_PRESSED.png"
            xpos 50
            ypos 340
            action If(is_dailynote_interacted_day_1, false=Jump("daily_note_interface"), true=Jump("inactive_note"))

        imagebutton id "chat_now":
            idle "gui/overlay/homephone_chatnow.png"
            hover "gui/overlay/homephone_chatnow_PRESSED.png"
            xpos 120
            ypos 347
            action Jump("chatnow_interface")

        imagebutton id "to_do_list":
            idle "gui/overlay/homephone_todolist.png"
            hover "gui/overlay/homephone_todolist_PRESSED.png"
            xpos 190
            ypos 335
            action Jump("todolist_interface")

        imagebutton id "browser":
            idle "gui/overlay/homephone_browser.png"
            hover "gui/overlay/homephone_browser_PRESSED.png"
            xpos 260
            ypos 350
            action Jump("browser_interface")

    hbox yalign 0.95:
        imagebutton id "music":
            idle "gui/overlay/homephone_MUSIC.png"
            hover "gui/overlay/homephone_MUSIC_PRESSED.png"
            xpos 50
            action Jump("phone_interface_with_music")

        imagebutton id "back":
            idle "gui/overlay/homephone_BACK.png"
            hover "gui/overlay/homephone_BACK_PRESSED.png"
            xpos 780
            action Jump("eka_room_select")

#screen2 nguli bwt note and keyboard
image keyboard_vid = Movie(play="gui/overlay/keyboard.webm", channel="test")
screen note_bg():
    imagebutton:
        idle "gui/overlay/dailynote_BG.jpg"
    #add "keyboard_vid" yalign 0.9
    imagebutton:
        idle "gui/overlay/KEYBOARD normal.jpg"
        yalign 0.9
    hbox yalign 0.05 xalign 0.7:
        imagebutton:
            idle "gui/overlay/dailynote_save_NO_PRESS.png"
            action NullAction()
    text " {b} Monday, January 6 {/b} " style "date_title"
    text "Today I feel" style "diary_title"
screen note_bg_static():
    imagebutton:
        idle "gui/overlay/dailynote_BG.jpg"
    hbox yalign 0.05 xalign 0.7:
        imagebutton:
            idle "gui/overlay/dailynote_save.png"
            action Jump("phone_interface")
    text " {b} Monday, January 6 {/b} " style "date_title"
    text "Today I feel" style "diary_title"

style date_title:
    color "#000000"
    size 40
    xpos 50
    ypos 250
style diary_title:
    color "#000000"
    size 40
    xpos 77
    ypos 320
style seq_1:
    color "#000000"
    size 40
    xpos 300
    ypos 320
style seq_2:
    color "#000000"
    size 40
    xpos 620
    ypos 320
style seq_3:
    color "#000000"
    size 40
    xpos 77
    ypos 380
style seq_4:
    color "#000000"
    size 40
    xpos 77
    ypos 440
style seq_5:
    color "#000000"
    size 40
    xpos 77
    ypos 500

style low_seq_2:
    color "#000000"
    size 40
    xpos 77
    ypos 380
style low_seq_3:
    color "#000000"
    size 40
    xpos 670
    ypos 380
style low_seq_4:
    color "#000000"
    size 40
    xpos 77
    ypos 440
style low_seq_5:
    color "#000000"
    size 40
    xpos 530
    ypos 440
style low_seq_6:
    color "#000000"
    size 40
    xpos 77
    ypos 500


screen day_one_note_title():
    text " {b} Monday, January 6 {/b} " style "date_title"
    text "Today I feel" style "diary_title"
screen day_one_low_point_seq_1():
    text "{cps=2}exhausted..and out of place.{/cps}" style "seq_1"
screen day_one_low_point_seq_2():
    text "First day of school is not really..." style "low_seq_2"
screen day_one_low_point_seq_3():
    text "great" style "low_seq_3"
screen day_one_low_point_seq_4():
    text "I feel like I can do better," style "low_seq_4"
screen day_one_low_point_seq_5():
    text "especially in socialising…." style "low_seq_5"
screen day_one_low_point_seq_6():
    text "I hope I can do better in the future, and not worry so \n much." style "low_seq_6"
    hbox yalign 0.05 xalign 0.7:
        imagebutton:
            idle "gui/overlay/dailynote_save.png"
            action Jump("phone_interface")


screen day_one_high_point_seq_1():
    text "{cps=2}strangely relieved.{/cps}" style "seq_1"
screen day_one_high_point_seq_2():
    text " Or not strange after all." style "seq_2"
screen day_one_high_point_seq_3():
    text "I'm exhausted, but I'm glad I can make several friends." style "seq_3"
screen day_one_high_point_seq_4():
    text "I hope I can stay friends with them." style "seq_4"
screen day_one_high_point_seq_5():
    text "And also… for me to not worry too much." style "seq_5"
    hbox yalign 0.05 xalign 0.7:
        imagebutton:
            idle "gui/overlay/dailynote_save.png"
            action Jump("phone_interface")

    #button id "start_chapter_1":
    #    xalign 0.5
    #    yalign 0.35
    #    xsize 600
    #    ysize 150
    #    action Start("chapter1")

style chat_title:
    color "#ffffff"
    size 50
    xpos 450
    ypos 100
style chat_list_mom:
    color "#000000"
    size 40
    xpos 65
    ypos 270
style chat_list_dad:
    color "#000000"
    size 40
    xpos 65
    ypos 320

screen chatnow_screen:
    imagebutton:
        idle "gui/overlay/chatnow_BG.jpg"
    text "Chats" style "chat_title"
    vbox:
        hbox:
            imagebutton:
                idle "gui/overlay/PP_MOM.png"
                xpos 30
                ypos 250
            text "MOM" style "chat_list_mom"
        hbox:
            imagebutton:
                idle "gui/overlay/PP_DAD.png"
                xpos 30
                ypos 300
            text "DAD" style "chat_list_dad"

screen todolist_screen:
    imagebutton:
        idle "gui/overlay/layout to do list.jpg"

screen browser_screen:
    imagebutton:
        idle "gui/overlay/LAYOUT browser.jpg"

screen music_screen:
    imagebutton:
        idle "gui/overlay/bg MUSIC PLAYER.png"
    imagebutton:
        idle "gui/overlay/MUSIC PLAYER back button.png"
        xpos 950
        ypos 120
        action Jump("phone_interface")
    vbox yalign 0.45 xalign 0.1:
        imagebutton:
            idle "gui/overlay/MUSIC PLAYER JAZZ BUTTON.png"
            hover "gui/overlay/MUSIC PLAYER JAZZ BUTTON selected.png"
            ypos 60
            action Play("music",["audio/jazz music 1.mp3","audio/jazz music 2.mp3"])
        imagebutton:
            idle "gui/overlay/MUSIC PLAYER ROCK BUTTON.png"
            hover "gui/overlay/MUSIC PLAYER ROCK BUTTON selected.png"
            ypos 90
            action Play("music",["audio/rock music 1.mp3","audio/rock music 2.mp3"])
        imagebutton:
            idle "gui/overlay/MUSIC PLAYER POP BUTTON.png"
            hover "gui/overlay/MUSIC PLAYER POP BUTTON selected.png"
            ypos 120
            action Play("music",["audio/pop music 1.mp3","audio/pop music 2.mp3"])
        imagebutton:
            idle "gui/overlay/MUSIC PLAYER LO-FI BUTTON.png"
            hover "gui/overlay/MUSIC PLAYER LO-FI BUTTON selected.png"
            ypos 150
            action Play("music",["audio/lofi music 1.mp3","audio/lofi music 2.mp3"])


#template default
#######################################################################################
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 237
    yfill True
    #edit here to change main menu background image
    #background "gui/overlay/main_menu_bg.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -16
    xmaximum 675
    yalign 1.0
    yoffset -16

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 26
    top_padding 102

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 237
    yfill True

style game_menu_content_frame:
    left_margin 34
    right_margin 17
    top_margin 9

style game_menu_viewport:
    xsize 777

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 9

style game_menu_label:
    xpos 43
    ysize 102

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -25


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 43
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 190

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 296

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 9

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 380


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 13

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 7

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 211
    right_padding 17

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 26

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 85

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 380

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 287

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 338

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 507
