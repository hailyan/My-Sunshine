label start:
    "Welcome to My Sunshine!"
    "This game is currently in {b}Beta{/b} development."
    "The story will be incomplete and maybe broken."
    "Please be patient and report any bugs/errors to me!"
    "You can report anything on the {a=https://github.com/hailyan/MySunshineVN}Github.{/a}"
    "Without further ado, please enjoy!"
    menu volumeselect:
        "Select a Volume."
        "Volume 1":
            jump vol1select
    menu vol1select:
        "{b}Selected: Volume 1.{/b}\nSelect a Chapter."
        "Chapter 1":
            jump vol1chap1select
    menu vol1chap1select:
        "{b}Selected: Volume 1 - Chapter 1.{/b}\nSelect a Page."
        "Page 1":
            jump vol1chap1page1