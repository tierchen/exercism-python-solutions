from itertools import permutations

house_numbers = range(5)  # There are five houses.


def solution():
    milk = 2  # Milk is drunk in the middle house.
    norwegian = 0  # The Norwegian lives in the first house.
    for blue, red, green, ivory, yellow in permutations(house_numbers):
        if green - ivory == 1:  # The green house is immediately to the right of the ivory house.
            for englishman, spaniard, ukrainian, japanese in permutations([1, 2, 3, 4]):  # Norwegian excluded
                if (englishman == red  # The Englishman lives in the red house.
                        and abs(norwegian - blue) == 1):  # The Norwegian lives next to the blue house.
                    for dog, snails, fox, horse, zebra in permutations(house_numbers):
                        if dog == spaniard:  # The Spaniard owns the dog.
                            for coffee, tea, orange_juice, water in permutations([0, 1, 3, 4]):  # Milk excluded
                                if (coffee == green  # Coffee is drunk in the green house.
                                        and ukrainian == tea):  # The Ukrainian drinks tea.
                                    for old_gold, kools, chesterfields, lucky_strike, parliaments in permutations(house_numbers):
                                        if (old_gold == snails  # The Old Gold smoker owns snails.
                                                and kools == yellow  # Kools are smoked in the yellow house.
                                                and japanese == parliaments  # The Japanese smokes Parliaments.
                                                and lucky_strike == orange_juice  # The Lucky Strike smoker drinks orange juice.
                                                and abs(kools - horse) == 1  # Kools are smoked in the house next to the house where the horse is kept.
                                                and abs(chesterfields - fox) == 1):  # The man who smokes Chesterfields lives in the house next to the man with the fox.
                                            nations = {englishman: 'Englishman',
                                                       spaniard: 'Spaniard',
                                                       ukrainian: 'Ukrainian',
                                                       norwegian: 'Norwegian',
                                                       japanese: 'Japanese'}
                                            return ("It is the {} who drinks the water.\n"
                                                    "The {} keeps the zebra.").format(nations[water], nations[zebra])
