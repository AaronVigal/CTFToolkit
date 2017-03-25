from re import sub
# TODO
    # Binary (2 char)
    # Hex (0-F)
    # Decimal (0-9)
    # Base 64
    # ROT 13
    # Ceasar Cipher
    # Morse Code (2 char)
    # Atbash Cipher
    # Affine Cipher
    # Rail-fence Cipher
    # Baconian Cipher (2 char)
    # Polybius Cipher
    # Bifid Cipher
cts = []
cts.append(input("Ciphertext: "))
if len(cts[0]) < 3:
    print("Ciphertext is too short.")
    exit(1)
recursive = "y" in input("Recursive? ").lower()
if recursive:
    try:
        depth = int(input("Branch Depth: "))
    except ValueError:
        print("Branch depth must be an integer.")
        exit(1)
else:
    depth = 1
possibilities = []
for i in range(depth):
    for ct in cts:
        unique_chars = set([c for c in ct])
        if len(unique_chars) is 2:
            possibilities.extend([(sub("1?..", lambda m: chr(int(m.group())), str(int("".join(["0" if c == ct[0] else "1" for c in ct]), 2))), "Binary"), (sub("1?..", lambda m: chr(int(m.group())), str(int("".join(["1" if c == ct[0] else "0" for c in ct]), 2))), "Inverted Binary")])
            try:
                possibilities.append(("".join([{"aaaaa":"A","aaaab":"B","aaaba":"C","aaabb":"D","aabaa":"E","aabab":"F","aabba":"G","aabbb":"H","abaaa":"I","abaaa":"J","abaab":"K","ababa":"L","ababb":"M","abbaa":"N","abbab":"O","abbba":"P","abbbb":"Q","baaaa":"R","baaab":"S","baaba":"T","baabb":"U","baabb":"V","babaa":"W","babab":"X","babba":"Y","babbb":"Z"}["".join("b" if x == ct[0] else "a" for x in "".join(group))] for group in list(zip(*(iter([c for c in ct]),) * 5))]).lower(), "Inverted Bacon"))
            except KeyError:
                try:
                    possibilities.append(("".join([{"aaaaa":"A","aaaab":"B","aaaba":"C","aaabb":"D","aabaa":"E","aabab":"F","aabba":"G","aabbb":"H","abaaa":"I","abaaa":"J","abaab":"K","ababa":"L","ababb":"M","abbaa":"N","abbab":"O","abbba":"P","abbbb":"Q","baaaa":"R","baaab":"S","baaba":"T","baabb":"U","baabb":"V","babaa":"W","babab":"X","babba":"Y","babbb":"Z"}["".join("a" if x == ct[0] else "b" for x in "".join(group))] for group in list(zip(*(iter([c for c in ct]),) * 5))]).lower(), "Bacon"))
                except KeyError:
                    pass
            # possibilities.append(decode_morse(ct))
        if all([c in "0123456789ABCDEF" for c in ct]):
            # possibilities.append(decode_hex(ct))
            pass
for possibility in possibilities:
    print(possibility[1], "==>", possibility[0])
