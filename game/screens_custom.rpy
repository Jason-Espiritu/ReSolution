# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

screen name_input():
    modal True
    
    zorder 100
    
    style_prefix "name"
    
    add "gui/overlay/confirm.png"

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            xalign .5
            yalign .5
            spacing 45
            
            label "What is your name?": 
                style "name_prompt"
                #size 40
                xalign 0.5

            input:
                style "input_style"
                length 15
                xalign 0.5
                value VariableInputValue("player")
        
            textbutton "OK":
                xalign 0.5
                action Jump("cont")
                keysym('K_RETURN', 'K_KP_ENTER') #able to press Enter key

style name_frame is gui_frame
style name_prompt is gui_prompt
style name_prompt_text is gui_prompt_text

style name_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
style name_prompt_text:
    text_align 0.5
    layout "subtitle"
    outlines [(absolute(2), "#de3c4f" , absolute(1) , absolute(1))]

style input_style:
    outlines [(absolute(2), "#000000" , absolute(0) , absolute(0))]