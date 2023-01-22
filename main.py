import cmudict
import turtle
from trunic.trunic_character import TrunicCharacter
from trunic.trunic_word import TrunicWord
import draw
import language

def main():
    # cmu_dictionary = cmudict.dict()
    # input_word = input(f"Input a word: ")
    # pronunciation = cmu_dictionary[input_word]
    # print(f"Phonetic breakdown: {pronunciation}") 
    # print(f"{cmudict.dict()}")

    pen: turtle.Turtle = turtle.Turtle(visible=False)
    # draw.draw(pen, TrunicCharacter("AE"), scale=100)
    draw.draw_word(pen, TrunicWord([TrunicCharacter("S") + TrunicCharacter("AE")]), scale=100)
    # draw.draw_word(pen, language.get_trunic_word_from_phones_list(["S", "AE"]), scale=100)
    turtle.Screen().exitonclick()

if __name__ == "__main__":
    main()