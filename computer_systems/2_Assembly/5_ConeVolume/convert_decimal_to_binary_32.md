## Exercise - Converting pi (3.1415926535) to Binary32
Source: https://en.wikipedia.org/wiki/Single-precision_floating-point_format

### Step 1 - Convert Fractional Part
- Fractional Part -> 0.14159 (i.e. pi % 3)
- Conversion algorithm into binary fraction:
    - Multiply fraction by 2
    - Take fraction part and repeat with the new fraction by 2 until
        - Fraction of zero is found, or
        - Precision limit is reached (23 fraction digits)
- Conversion:
    1. 2 * 0.14159 = 0.28318 = 0 + 0.28318 => 0
    2. 2 * 0.28318 = 0.56636 = 0 + 0.56636 => 0
    3. 2 * 0.56636 = 1.13272 = 1 + 0.13272 => 1
    4. 2 * 0.13272 = 0.26544 = 0 + 0.26544 => 0
    5. 2 * 0.26544 = 0.53088 = 0 + 0.53088 => 0

