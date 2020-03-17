from source.methods_json import (
    load_json,
)
from source.class_web3 import (
    Web3Connection,
)

if __name__ == '__main__':



    # newcharacter = w3c.create_character(
    #     name = "Destroyers", 
    #     unit = "Sea Guards", 
    #     race = "High Elves",
    # )
    # print("New character: " + str(newcharacter))

    characters = w3c.get_characters()
    print("Character data: " + str(characters))

    # newevent = w3c.create_event(
    #     characterId = 0,
    #     description = "Victory against 0xd04bAcA7ac336EadE692Fd8EDF1a66e4A7d74919",
    # )

    history = w3c.get_events(
        characterId = 0,
    )
    print("history: " + str(history))