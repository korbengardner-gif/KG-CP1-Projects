#Korben Gardner, Madlib assignment


adjective1 = input("Give me an Adjective: ")
noun1 = input("Give me a Noun: ")
noun2 = input("Give another Noun: ")
verb1 = input("Give me a Verb that DOESN'T end in ING: ")
adjective2 = input("Give me another Adjective: ")
color = input("Give me a Color: ")
exclamation = input("Give an exclamation/something yu would shout: ")
noun3 = input("Give another Noun: ")
verb2 = input("Give me a Verb that DOES end in ING: ")

message = "Princess Zelda sent Link on a(n) " + adjective1 + " quest across the kingdom of Hyrule. To prepare, Link packed his trusty Master Sword, a shield, and a mysterious " + noun1 + ". While hiking through Hyrule Field, a pack of wild " + noun2 + " jumped out of the grass to " + verb1 + "] him! Link easily defeated them, noting that they smelled strongly of " + noun3 + ".Link kept moving and ran into a(n) " + adjective2 + " shrine glowing with " + color + " light. As he stepped inside, his arms accidentally triggered a heavy stone trapdoor. '" + exclamation + "!' Link yelled as he slipped into a secret chamber completely flooded with " + noun3 + ". To his surprise, guarding the exit was an even bigger, angrier group of " + noun2 + "! Fortunately, his paraglider saved him, and he spent the rest of the afternoon " + verb2 + " safely toward the Temple of Time."

print(message)