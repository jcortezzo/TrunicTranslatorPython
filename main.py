import eng_to_ipa as ipa
from turtle import Turtle, Screen
from trunic.trunic_character import TrunicCharacter
from rendering.draw import draw

def main():
    input_word = input(f"Input a word: ")
    print(f"Phonetic breakdown: {ipa.convert(input_word)}") 

    pen = Turtle(visible=False)
    draw(pen, TrunicCharacter("æ"), scale=100)
    Screen().exitonclick()

if __name__ == "__main__":
    main()