# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu
    
 #   add "ui/dialogue/add_dialogue_overlay.png"
 #   add "ui/dialogue/add_dialogue_badge.png"


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

 
    add "ui/black.png"
    
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 5

            for caption, action, chosen in items:

                if action:

                    button:
                        action action 
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

    
    
init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    
    
    #style.menu_choice_button.yminimum = 30
    #style.menu_choice_button.ymaximum = 35


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:
    
        tag menu
        
        add "ui/menus/gradient.png"
        add "ui/menus/mainmenu/add_logo.png"
        
        imagemap:
            ground "ui/menus/mainmenu/mm_ground.png"
            hover "ui/menus/mainmenu/mm_hover.png"
            cache False
            alpha False
            
            hotspot (88,604,186,53) action (Start) at buttonfade
            hotspot (307,604,188,53) action ShowMenu("load") at buttonfade
            hotspot (526,604,188,53) action ShowMenu("preferences") at buttonfade
            hotspot (747,604,188,53) action Quit(confirm=False) at buttonfade
        

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:

  imagemap:
            ground "ui/menus/saveload/sl_ground.png"
            hover "ui/menus/saveload/sl_hover.png"
            selected_idle "ui/menus/prefs/prefs_hover.png"
            selected_hover "ui/menus/prefs/prefs_hover.png"
        
            add "ui/menus/saveload/add_sl_backdrop.png"
            
            cache False
            alpha False
    
            hotspot (191,342,80,86) at brightbuttonfade action FilePagePrevious() 
            hotspot (736,342,80,86) at brightbuttonfade action FilePageNext(max=25)
            
            hotspot (362,200,285,173) clicked FileAction(1):
                use load_save_slot(number=1)
            hotspot (362,400,285,173) clicked FileAction(2):
                use load_save_slot(number=2)
                
            hotspot (406,632,213,49) action Return() at buttonfade
             
            key "save_delete" action FileDelete(2)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu


    use file_picker
    
    add "ui/menus/saveload/add_sl_savelabel.png"
    
    add "ui/menus/saveload/add_sl_overlay.png"

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu


    use file_picker
    
    add "ui/menus/saveload/add_sl_loadlabel.png"
    add "ui/menus/saveload/add_sl_overlay.png"

 ##############################################
 #############                   ################
##############  LOAD SAVE SLOTS  #################
 #############                   ################
  ##############################################


         
screen load_save_slot:
    $ file_text = "%2s. %s\n  %s" % (
                        FileSlotName(number, 2),
                        FileTime(number, empty=_("Пустая ячейка")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 50 ypos 15
    text file_text xpos 55 ypos 125 size 30 drop_shadow [(1, 2)] font "Fox.ttf"
    
    
init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)
    
    config.thumbnail_width = 190
    config.thumbnail_height = 100



##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu
        
    imagemap:
        alpha False
        cache False
        ground "ui/menus/prefs/prefs_ground.png"
        hover "ui/menus/prefs/prefs_hover.png"
        selected_idle "ui/menus/prefs/prefs_hover.png"
        selected_hover "ui/menus/prefs/prefs_hover.png"

        hotspot (406,632,213,49) action Return() at buttonfade

        hotspot (399,242,41,38) action Preference("display", "window") at buttonfade
        hotspot (326,242,56,38) action Preference("display", "fullscreen") at buttonfade

        hotspot (897,336,41,43) action Preference("transitions", "none") at buttonfade
        hotspot (826,325,56,45) action Preference("transitions", "all") at buttonfade


        bar pos (287,346) value Preference("music volume") style "pref_slider"
        bar pos (287,528) value Preference("sound volume") style "pref_slider"

        bar pos (805,440) value Preference("auto-forward time") style "pref_slider"

        hotspot (326,424,56,45) action Preference("skip", "all") at buttonfade
        hotspot (400,424,40,45) action Preference("skip", "seen") at buttonfade
        
        
        hotspot (898,513,46,50) action Preference("after choices", "stop") at buttonfade
        hotspot (822,517,60,42) action Preference("after choices", "skip") at buttonfade

        bar pos (805,260) value Preference("text speed") style "pref_slider"

init -2 python:
    
    style.pref_slider.left_bar = "ui/menus/prefs/bar_full.png"
    style.pref_slider.right_bar = "ui/menus/prefs/bar_empty.png"
    style.pref_slider.hover_left_bar = "ui/menus/prefs/bar_full.png"
    style.pref_slider.ymaximum = 21
    style.pref_slider.xmaximum = 170
    style.pref_slider.thumb = None

   


##############################################################################
# Yes/No Prompt
    
#screen yesno_prompt:
    #on "show" action With(dissolve)
    
   # modal True

   # add "ui/menus/gradient.png"
    
   # imagemap:
   #     #idle 'ui/menus/yesno/yesno_idle.png' 
   #     hover 'ui/menus/yesno/yesno_hover.png'
   #     cache False
        
   #     hotspot (372,430,112,71) action yes_action at buttonfade
   #     hotspot (555,442,65,51) action no_action at buttonfade

   # #text _(message):
        #xalign 0.5
        #yalign 0.5

   # if message == layout.ARE_YOU_SURE:
   #     add "ui/menus/yesno/yesno_are_you_sure.png"
        
   # elif message == layout.DELETE_SAVE:
   #     add "ui/menus/yesno/yesno_delete_save.png"
        
  #  elif message == layout.OVERWRITE_SAVE:
   #     add "ui/menus/yesno/yesno_overwrite_save.png"
        
  #  elif message == layout.LOADING:
  #      add "ui/menus/yesno/yesno_loading.png"
        
  #  elif message == layout.QUIT:
  #      add "ui/menus/yesno/yesno_quit.png"
        
   # elif message == layout.MAIN_MENU:
   #     add "ui/menus/yesno/yesno_main_menu.png" 


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:
    
    imagemap:
        alpha False
        cache False
        ground "ui/menus/quickmenu/qm_ground.png"
        hover "ui/menus/quickmenu/qm_hover.png"
        selected_idle "ui/menus/quickmenu/qm_hover.png"
        selected_hover "ui/menus/quickmenu/qm_hover.png"   

        hotspot (581,734,60,27) action ShowMenu('save') at buttonfade
        hotspot (446,734,66,27) action ShowMenu('load') at buttonfade
        hotspot (718,734,61,27) action Preference("auto-forward", "toggle") at buttonfade
        hotspot (848,734,73,27) action ShowMenu('preferences') at buttonfade
        

    
    #######################################################################
 ########################                       #############################
#########################    TRANSFORMATONS     ##############################
 ########################                       #############################
    #######################################################################
 



transform buttonfade:

    on idle:
        alpha 1.0
    on hover:
            alpha 0.0
            linear 0.2 alpha 1.0
    on selected_hover:
            alpha 0.0
            linear 0.2 alpha 1.0



transform brightbuttonfade:

    on idle:
        alpha 1.0
    on hover:
            alpha 1.0
            linear 0.2 alpha 1.2
    on selected_hover:
         alpha 1.0
         linear 0.2 alpha 1.2