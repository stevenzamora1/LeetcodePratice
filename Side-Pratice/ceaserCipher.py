def encode(s: str, shift: int) -> str:
    output = ""
    for n in s:
        shift_base = ord('a')  # Default to lowercase 'a'

        if n.isalpha():  # Only shift letters
            if n.isupper():  # If uppercase, change base to 'A'
                shift_base = ord('A')

            # (ord(n) - shift_base) makes the letters 0 based so between 0 - 25.
            # This makes it easier to shift around when we need to shift around Z
            new_char = chr((ord(n) - shift_base + shift) % 26 + shift_base)
            output += new_char
        else:
            output += n

    return output


def decode(s: str,  shift: int) -> str:
    # Decoding is just encoding with a negative shift
    return encode(s, -shift)


# Create a caesar cipher
def caesar_cipher(s: str, shift: int, mode: str) -> str:

    if mode == "encode":
        return encode(s, shift)

    if mode == "decode":
        return decode(s, shift)
    return "error with mode"


print(caesar_cipher("opx mfut ubml jo dpef", 25, "encode"))
print(caesar_cipher("now lets talk in code", 25, "decode"))
