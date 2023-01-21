import eng_to_ipa as ipa
import turtle
from trunic.trunic_character import TrunicCharacter
import draw

def main():
    input_word = input(f"Input a word: ")
    print(f"Phonetic breakdown: {ipa.convert(input_word)}") 

    pen: turtle.Turtle = turtle.Turtle(visible=False)
    draw.draw(pen, TrunicCharacter("æ"), scale=100)
    turtle.Screen().exitonclick()

if __name__ == "__main__":
    main()