# Task
- Implement the `varint` encoding in Protocol Buffers

## Notes
- Protocol Buffers
    - A wire format - encoding of bytes to transmit over the network
    - Compact & allows us to encode schemas
    - Faster than JSON
    - Similar to Thrift & Avro
- Varint
    - Allow encoding unsigned 64 bit integers (8 bytes)
    - Variable encoding that can use between 1-10 bytes

## Planning
- Read the test files correctly
    - Hexdump
    - Interpret as int
- Implement basic varint encoder
- Implement decoder
    - Not in scope of exercise
    - But then we can take any integer and test that we got the right integer back
        - Roundtrip test
            - Not foolproof -> you could have a symmetric bug in encoder & decoder
        - Other type of test
            - Test all 4 billion 32 bit floats
- Refactor/Cleanup


## Explainer Notes
### What does it mean for a value to "be" a certain number of bits?
- [Link](https://csprimer.com/watch/fixed-width/)
- Fundamental concept
- In most contexts
    - If we want to operate over some data (i.e. int) - we need to specify how many bits it should have
    - Tightly coupled to the hardware
        - CPU expects the numbers to reside in registers (each with 64 bits)
- Example: 4 Bit Integers (Positive - Unsigned)
    - `[X][X][X][X]`
    - Each X can represent 0 or 1
        - If you exceed the memory allocated, you get overflow
        - Which means that it will evaluate to 0
- Classic example overflow causing realworld impact
    - [Ariane flight V88](https://en.wikipedia.org/wiki/Ariane_flight_V88)
    - Tried to squeeze a number into a 16 bit register
        - Were using code from the Ariane 4
        - Caused an overflow leading to the rocket exploding
- Overflow in Postgres
    - People get confused when Postgres works fine up until 4 billion transactions
    - B/c there's a transaction ID used for the MVCC concurrency control system that postgres uses
        - It's a 32 bit integer
    - Postgres decides whether a transaction is in the future or past via this transaction ID
    - So after 4 billion transactions (2^32) - it overflows
- Why hasn't someone created a solution for this if it's such a problem?
    - Python
        - Shifting bits
            - You are taking the binary representation of a number and shifting the bits either to the left (<<) or the right (>>)
            - Examples
                - 1 << 1 (shifting by 1 bit) -> 2
                    - 1 -> 10
                - 1 << 2 (shifting by 2 bits) -> 4
                    - 1 -> 100
                - 4 << 2 (shifting by 2 bits) -> 16
                    - 100 -> 10000
        - Decided that large numbers should be well handled so that users don't need to care about overflow
        - If in JS you were to shift the bit 1 by 65 places you get two
            - It has 33 bit integers
        - In python this doesn't happen
            - You can shift the bit why as many places as you like until you hit a MemoryError
            - Why?
                - Python implements numbers such that it stores an array of integers
                    - Parts of your large number
                - When you do an operation it can in software decide how to add parts of the numbers together 
                    - Generally the right most part of one number is added to the right most part of the other number
                    - If there is an overflow, it is well defined (i.e. you can identify what the resulting number should have been) and you can carry that over to the next number
                - This is a lot slower than a single machine addition
                    - B/c it is using far more machine additions to get the addition right
                
    
### What are signed & unsigned integers?
- [Link](https://csprimer.com/watch/signed-integers/)
- For the bits that we have
    - Are we allocating bits to just encoding positive integers?
    - Or do we have an encoding that represents negative integers as well
        - Takes a particular scheme to represent this
- Example: 4 bit integer
    - If unsigned, our range is 0 (0000) to 15 (1111)
    - You need a scheme to represent the negative integers
    - Example Scheme: The first bit to indicate the sign (Signed bit)
        - 0 -> Positive, 1 -> Minimum
        - Positive:
            - Min -> 0000 -> 0
            - Max -> 0111 -> 7
        - Negative:
            - Min -> 1000 -> -0
            - Max -> 1111 -> -7
        - Not the worst scheme
            - Floating points use signed bits
            - It's awkward working with negative zero 
                - B/c otherwise you have overhead of checking against zero and neg zero
        - Also
            - You can't take two numbers and add them independently of whether they're positive or negative
            - Ideally you want a scheme where you can use the grade school algorithm
                - Take 7 (0111) and -1 (1001)
                - Adding them together via this algo leads to 0000 (1 remainder)
                - We wanted 6, but overflowed to 0
            - If you had such a scheme, you could use the same adder for signed and unsigned integers
    - Signed Integer Scheme (two's complement)
        - Idea: By adding any numbers together via the GSA will lead to the right answer
        - What we need -> Adding numbers together always makes progress forwards
            - In the previous scheme: large negative numbers lead to larger binary numbers leading to overflow
        - Scheme:
            - Consider a 4 bit integer, where leading bit is an indicator bit
            - 0000 -> 0111 to represent 0 -> 7
            - If leading bit is 1, it signifies that you're adding the negative value of the highest value integer you can achieve at that bit location (a large negative weight)
                - 1111 -> -1 (0111 -> 7, with leading bit == 1, signifies adding -8 to it)
                - 1110 -> -2 (0110 -> 6, with leading bit == 1, signifies adding -8 to it)
                - 1000 -> -8 (0000 -> 0, with leading bit == 1, signifiesa dding -8 to it)
            - 3 bit integers
                - 111 -> -1 (011 -> 3, with leading bit ==1, signifies adding -4 to it)
            - Note about this scheme -> Adding more bits to it increases the magnitude of the integer
            - Example: Adding 4 bit integers:
                - 5 (0101) and -2 (1100)
                - Applying GSA
                    - 0011 -> (-3)
            
### What do "big-endian" and "little-endian" mean?
- [Link](https://csprimer.com/watch/byte-ordering/)
- Why can't we agree on one convention? No idea, we can't come to agreement
    - So we need to live with arbitrary decisions
- 123
    - Interpreted as 123, not 321 by historical convention
    - The further to the left the higher the value
        - In contrast to our left-to-right writing system
        - This is right-to-left - makes sense since we got them from Arabic
- Let's say you have a TCP/UDP port 
    - Port is a value from 0 to 2^16
        - You need two bytes to store the port
    - Example, you wrote [01], [02] in hex (?)
        - Left to Right (Big Endian)
            - 01 -> 256
            - 02 -> 2
        - Right to Left (Little Endian -> Low order left)
            - 01 -> 1
            - 02 -> 512
    - Representation of multibyte values will differ depending on hardward
        - Intel Machines are Little Endian
        - AMD machines are Big Endian
    - If you create a PDF on one machine and upload it to a server where the representation differs, you could have an issue in poor software
        - Whether a multibyte integer is represented as BE or LE will generally be communicated
- Origin
    - From Gulliver's Travels 
    - Little Endian -> Eat eggs from the little end
    - Big Endian -> Eat egg from the big end
            


## Why does one byte correspond to hexidecimal digits?
- [Link](https://csprimer.com/watch/hex-byte/)
- Two hex digits side by side is usually a representation of a byte
    - B/c you can represent 8 bits with these 2 digits
    - Killer app of hex digits
- Example: 8 Bit sequence (11110011)
    - Take first 4 bits (1111) (16 possible representations, 0-9-a-f)
        - Highest is f
    - Last 4 bits (0011)
        - 3
- One byte has 256 possible states (2^8)
    - 2 hexadecimal digits (2^4 * 2^4)


## How do I read a hexdump?
- [Link](https://csprimer.com/watch/reading-hexdump/)
- `hexdump` bash command
    - `hexdump -C /bin/ls | head` (-C is for canonical, the common representation of hex)
        - `xxd` another hexdump command has a different format
    - Output is represented in four columns
        - Left-Hand Column
            - Represents which byte the next byte is
            - First row ->  000000000 (0th Byte)
            - Second Row -> 000000010 (16th byte) -> This is represented in hexadecimal
        - Middle Columns
            - Each row of a column represents 8 bytes, with 2 hex integers (which represent 1 byte)
        - Last Column
            - The ASCII guess of the content
                - Direct ASCII repreesentation of byte values
            - '.' can either be an ASCII dot or something ASCII can't represent
                - We don't really care about these
            - 2 is in ASCII, but it is not an ASCII printable character (so gets represented as a .)
            - Can be helpful to get some sort of overview 
    - Asterisk in the index column
        - Indicates a continuous repetition of the previous row of bytes until the row that follows the asterisk
