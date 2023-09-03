## UTF-8 Explained
- Developed by Ken Thompson & Rob Pike as a scheme for text encoding
    - Designed to be backwards compatible with ASCII
    - No additional overhead for encoding ASCII
        - Anything that is 1 byte in ASCII should be 1 byte in UTF-8
    - Should also encode everything in Unicode
        - Even beyond the multilingual plane (MLP) that can be encoded in 2 bytes
            - This is what we use UTF-16 for in particular
- ASCII Encoding
    - 128 Characters - Encoded in 7 bits
    - Byte representation -> Always has a leading zero
- A with an accent mark
    - 2 Bytes
    - To encode in UTF-8
        - Start with a number of 1 bits to encode how many bytes are needed
            - 110..... (dots are payload bits)
                - 2 1 bits to signify that it represents two bytes of information
        - Second byte 
            - 10...... 
                - 1 on bit to signifyt the "middle"
- Hiragana Character
    - 3 Bytes
    - To encode in UTF-8
        - 1110....
        - 10......
        - 10......
- Furthest range of UTF-8
    - 4 Bytes
    - To encode in UTF-8
        - 1110....
        - 10......
        - 10......
        - 10......
- Encoding a Sandwich (U+1F96A - 17 bits )
    - We need the 4 byte representation, b/c it has > 17 bits of space
        - 3 Byte representation has only 16 bits available
    - 11110...10......10......10......
    - 11110000100111111010010110101010
    - | P|fill| |1| F || 9 |6|fi|6|A  |
    - Final Binary (in bytes)
        - 11110000 10011111 10100101 10101010
    - Hexadecimal representation
        - f0 9f a5 aa
- Piping a hexadecimal byte sequence to be represented as encoding
    - `echo '0: f0 9f a5 aa' | xxd -r`

