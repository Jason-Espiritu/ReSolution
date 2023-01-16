# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

## SCENE IMAGES ##
#images
image black = "#000"

# Home
image home = "backgrounds/home.png"

image home_afternoon = "backgrounds/home_afternoon.png"

image home_night = "backgrounds/home_night.png"

# School
image school = "backgrounds/school_front.png"

image school_back = "backgrounds/school_back.png"

image classroom = "backgrounds/school_classroom.png"

image faculty = "backgrounds/school_faculty.png"

image office = "backgrounds/school_office.png"

image hallway = "backgrounds/school_hall.png"

image roof = "backgrounds/school_roof.png"

# City
image city = "backgrounds/city.png"

## CHARACTER IMAGES ##
# Player / MC

# Alfred
define alf_width = 489.0
define alf_height = 1552
image alfred happy = im.Scale("images/Alfred/alfred_happy.png", alf_width, alf_height)
image alfred smug = im.Scale("images/Alfred/alfred_smug.png", alf_width, alf_height)
image alfred laugh = im.Scale("images/Alfred/alfred_laugh.png", alf_width, alf_height)
image alfred serious = im.Scale("images/Alfred/alfred_serious.png", alf_width, alf_height)
image alfred gloom = im.Scale("images/Alfred/alfred_gloom.png", alf_width, alf_height)
image alfred sigh = im.Scale("images/Alfred/alfred_sigh.png", alf_width, alf_height)

# Kazumi
define kaz_width = 417.0
define kaz_height = 1338
image kazumi happy = im.Scale("images/Kazumi/kazumi_happy.png", kaz_width, kaz_height)
image kazumi happy_away = im.Scale("images/Kazumi/kazumi_happy_away.png", kaz_width, kaz_height)
image kazumi surprise = im.Scale("images/Kazumi/kazumi_surprise.png", kaz_width, kaz_height)
image kazumi sad = im.Scale("images/Kazumi/kazumi_sad.png", kaz_width, kaz_height)
image kazumi sad_away = im.Scale("images/Kazumi/kazumi_sad_away.png", kaz_width, kaz_height)
image kazumi fluster = im.Scale("images/Kazumi/kazumi_fluster.png", kaz_width, kaz_height)
image kazumi laugh = im.Scale("images/Kazumi/kazumi_laugh.png", kaz_width, kaz_height)
image kazumi crying = im.Scale("images/Kazumi/kazumi_cry.png", kaz_width, kaz_height)
image kazumi angry = im.Scale("images/Kazumi/kazumi_angry.png", kaz_width, kaz_height)

# Hideaki
define hide_width = 439.0
define hide_height = 1459
image hideaki serious = im.Scale("images/Hideaki/hideaki_serious.png", hide_width, hide_height)
image hideaki serious_away = im.Scale("images/Hideaki/hideaki_serious_away.png", hide_width, hide_height)
image hideaki happy = im.Scale("images/Hideaki/hideaki_grins.png", hide_width, hide_height)
image hideaki surprise = im.Scale("images/Hideaki/hideaki_surprise.png", hide_width, hide_height)
image hideaki sad = im.Scale("images/Hideaki/hideaki_sad.png", hide_width, hide_height)
image hideaki smile = im.Scale("images/Hideaki/hideaki_smile.png", hide_width, hide_height)


# Mamoru
define mam_width = 415
define mam_height = 1590
image mamoru serious = im.Scale("images/Mamoru/mamoru_serious.png", mam_width, mam_height)
image mamoru serious_away = im.Scale("images/Mamoru/mamoru_serious_away.png", mam_width, mam_height)

# Tadao
define tad_width = 445
define tad_height = 1537
image tadao happy = im.Scale("images/Tadao/tadao_happy.png", tad_width, tad_height)
image tadao angry = im.Scale("images/Tadao/tadao_angry.png", tad_width, tad_height)
image tadao sarc = im.Scale("images/Tadao/tadao_smirk.png", tad_width, tad_height)
image tadao surprise = im.Scale("images/Tadao/tadao_surprise.png", tad_width, tad_height)
image tadao happy_away = im.Scale("images/Tadao/tadao_happy_away.png", tad_width, tad_height)
image tadao serious = im.Scale("images/Tadao/tadao_serious.png", tad_width, tad_height)
image tadao grin = im.Scale("images/Tadao/tadao_grin.png", tad_width, tad_height)

# Positioning
init:
    $correct_pos_alfred = Position(xpos = 0.5, xanchor=0.5, ypos=1.0, yanchor=0.65)
    $correct_pos_kazumi = Position(xpos = 0.5, xanchor=0.5, ypos=1.0, yanchor=0.65)
    $correct_pos_hideaki = Position(xpos = 0.5, xanchor=0.5, ypos=1.0, yanchor=0.65)
    $correct_pos_tadao = Position(xpos = 0.5, xanchor=0.5, ypos=1.0, yanchor=0.65)
    $correct_pos_mamoru = Position(xpos = 0.5, xanchor=0.5, ypos=1.0, yanchor=0.65)

# DICT TRANSITIONS
init:
    $ dis = { "master" : Dissolve(0.3)}