# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#call function to change gender

# Character Name Defaults.
define sex = "Male"
define female_name = "Gundou"
define male_name = "Kanda"

define player = male_name

# routing 
define route = ""

#Pronoun used in the game
define his = "his"
define His = "His"
define he = "he"
define him = "him"
define He = "He"
define Sir = "Sir"
define sir = "sir"
define Mr = "Mr."
define guy = "guy"

# Unknown
define unk = Character("???")

# Everyone
define every = Character("EVERYONE")

# Our Main Character
define mc = Character("[player!u]")

# Alfred
define alfred = Character("ALFRED")

# Kazumi
define kazumi = Character("KAZUMI")

# Hideaki
define hideaki = Character("HIDEAKI")

# Tadao
define tadao = Character("TADAO")

#Mamoru
define mamoru = Character("MAMORU")

## SUB CHARACTERS ##

#Student/s in player's class
define student1 = Character("STUDENT A")
define student2 = Character("STUDENT B")
define student3 = Character("STUDENT C")
define student4 = Character("STUDENT D")
define students = Character("STUDENTS")

#Student/s from other classes.
define student = Character("STUDENT")

define UniStu = Character("UNI STUDENT")

# Principal
define principal = Character("PRINCIPAL")

# Teachers
define teacher1 = Character("TEACHER A")
define teacher2 = Character("TEACHER B")
define teacher3 = Character("TEACHER C")
define teacher4 = Character("TEACHER D")
