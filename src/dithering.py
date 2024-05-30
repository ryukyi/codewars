"""Dithering
https://www.codewars.com/kata/5426006a60d777c556001aad

A pixmap shall be turned from black to white, turning all pixels to white in the process. But for optical reasons this shall not happen linearly, starting at the top and continuing line by line to the bottom:

for y in range(height):
  for x in range(width):
     set_bit(x, y)
Instead it shall be done by a systematic dithering routine which selects the coordinates on which pixels are to be set in a precise pattern so that the geometrical distance between two consecutive pixels is large and a specific optical effect results.

The following diagrams show the order of the coordinates the algorithm shall produce:

2x2:
1 3
4 2

4x4:
 1  9  3 11
13  5 15  7
 4 12  2 10
16  8 14  6

8x8:
 1  33   9  41   3  35  11  43
49  17  57  25  51  19  59  27
13  45   5  37  15  47   7  39
61  29  53  21  63  31  55  23
 4  36  12  44   2  34  10  42
52  20  60  28  50  18  58  26
16  48   8  40  14  46   6  38
64  32  56  24  62  30  54  22
The pattern continues like that for each square pixmap with a width and height of a power of two (16, 32, 64, …).

But the width and the height of the pixmap can be arbitrary positive numbers. If the pixmap's width and/or height are not a power of two, the coordinates the algorithm would produce outside of the pixmap are skipped:

3x3:
1 6 3
8 5 9
4 7 2

6x5:
 1 16  6 21  3 18
25 10 28 13 26 11
 8 23  5 20  9 24
29 14 27 12 30 15
 4 19  7 22  2 17
Write an algorithm which produces the coordinates of the dithering for a given width and height.

To pass the tests, write a generator function dithering which yields coordinate tuples:

dithering(6, 5) -> (0, 0), (4, 4), (4, 0), (0, 4), (2, 2), (2, 0), (2, 4) ..

#################
The provided Python code implements a dithering algorithm using bitwise operations, specifically focusing on a technique called bit interleaving. This technique is used to generate a Morton code (or Z-order curve), which is a method of mapping multidimensional data to one dimension while preserving the locality of the data points. Let's break down the code and explain each part in detail, especially focusing on the bitwise operations:

### Bitwise Operations
Bitwise operations work directly on the binary representations of integers. They are fundamental in low-level programming and are used here to manipulate and interleave bits from two numbers. The main bitwise operations used in the code are:
- **Bitwise AND (`&`)**: This operation takes two bit patterns of equal length and performs the logical AND operation on each pair of corresponding bits. The result in each position is 1 if the first bit is 1 and the second bit is 1; otherwise, it is 0.
- **Bitwise OR (`|`)**: This operation takes two bit patterns of equal length and performs the logical inclusive OR operation on each pair of corresponding bits. The result in each position is 1 if at least one of the bits is 1.
- **Left Shift (`<<`)**: This operation shifts the bits of the first operand left by the number of positions specified by the second operand. New bits on the right are filled with zeros.

### Function: interleave_bits(x, y)
This function interleaves the bits of two integers, `x` and `y`. Interleaving means that the bits of the two numbers are alternated in the resulting integer.

```python
def interleave_bits(x, y):
    result = 0
    for i in range(16):  # Assuming 16 bits for each of x and y
        result |= ((x & (1 << i)) << i) | ((y & (1 << i)) << (i + 1))
    return result
```

- **Loop through each bit position**: The `for` loop iterates through each bit position from 0 to 15 (assuming 16 bits for simplicity). The actual number of bits needed depends on the maximum values of `x` and `y`.
- **Extracting bits**: `(x & (1 << i))` isolates the `i`-th bit of `x`. The expression `(1 << i)` creates a number with a 1 at the `i`-th position and 0s elsewhere. The AND operation then leaves only the `i`-th bit of `x`.
- **Positioning bits**: After isolating the `i`-th bit of `x`, it is shifted left by `i` positions to align it with its final position in the result. Similarly, the `i`-th bit of `y` is shifted left by `i + 1` positions.
- **Combining bits**: The bits extracted and shifted from `x` and `y` are combined using the OR operation and accumulated into the `result` variable.

### Function: dithering(width, height)
This function generates the coordinates for dithering based on the Morton codes of the coordinates.

```python
def dithering(width, height):
    coords = []
    for y in range(height):
        for x in range(width):
            morton_code = interleave_bits(x, y)
            coords.append((morton_code, x, y))

    coords.sort()

    for _, x, y in coords:
        yield (x, y)
```

- **Generating Morton codes**: For each coordinate `(x, y)` in the pixmap, the Morton code is computed using `interleave_bits(x, y)`. This code serves as a single-dimensional value representing the 2D coordinate.
- **Sorting by Morton code**: The list of coordinates is sorted by the Morton code. Sorting by Morton code arranges the coordinates so that spatially close coordinates in the 2D space are also close in the list, which is crucial for preserving locality and achieving the dithering effect.
- **Yielding coordinates**: Finally, the function yields the coordinates in the order determined by their Morton codes. This order is used to set the pixels in a dithered pattern.

This detailed explanation should help someone unfamiliar with bitwise operations understand how they are used in this context to achieve a specific pattern for setting pixels in a dithering algorithm.

#############
Let's walk through an example using the `dithering` function for a small pixmap of size 2x2 to understand how the Morton codes are generated and used to determine the order of setting pixels. We'll go through each step and operation in detail.

### Step 1: Initialize the `dithering` function
We call the function with width and height both set to 2:
```python
dithering(2, 2)
```
This initializes the function, which will generate coordinates for a 2x2 grid.

### Step 2: Generate Morton Codes for Each Coordinate
The function iterates over each pixel coordinate in the grid. Let's break down the operations for each coordinate:

#### Coordinate (0, 0)
- **Calculate Morton Code**:
  - `x = 0`, `y = 0`
  - `interleave_bits(0, 0)` is called.
  - Inside `interleave_bits`, the result starts at 0. The loop runs for 16 iterations, but since both x and y are 0, all bitwise operations result in 0.
  - The final Morton code for (0, 0) is `0`.

#### Coordinate (0, 1)
- **Calculate Morton Code**:
  - `x = 0`, `y = 1`
  - `interleave_bits(0, 1)` is called.
  - The key operation here is when `i = 0`:
    - `(1 & (1 << 0)) << (0 + 1)` evaluates to `1 << 1`, which is `2`.
  - The final Morton code for (0, 1) is `2`.

#### Coordinate (1, 0)
- **Calculate Morton Code**:
  - `x = 1`, `y = 0`
  - `interleave_bits(1, 0)` is called.
  - The key operation here is when `i = 0`:
    - `(1 & (1 << 0)) << 0` evaluates to `1`.
  - The final Morton code for (1, 0) is `1`.

#### Coordinate (1, 1)
- **Calculate Morton Code**:
  - `x = 1`, `y = 1`
  - `interleave_bits(1, 1)` is called.
  - The key operations are:
    - For `i = 0`, `(1 & (1 << 0)) << 0` gives `1` and `(1 & (1 << 0)) << (0 + 1)` gives `2`.
    - The results are combined using OR: `1 | 2` which is `3`.
  - The final Morton code for (1, 1) is `3`.

### Step 3: Sort Coordinates by Morton Code
The coordinates along with their Morton codes are:
- (0, 0, 0)
- (0, 1, 2)
- (1, 0, 1)
- (1, 1, 3)

Sorting these by the Morton code gives:
- (0, 0, 0)
- (1, 0, 1)
- (0, 1, 2)
- (1, 1, 3)

### Step 4: Yield Sorted Coordinates
The function then yields the x and y values in the sorted order:
- (0, 0)
- (1, 0)
- (0, 1)
- (1, 1)

This sequence sets pixels in a pattern that maximizes the distance between consecutively set pixels, achieving the dithering effect.

This detailed walkthrough shows how bitwise operations are used to interleave bits and generate Morton codes, which are then used to sort and determine the order of pixel setting in a dithering algorithm.
"""
