# Tennis Re-factor

This directory contains a basic re-factoring Kata I wrote to accompany the book ["Clean Code"](https://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) by Robert Martin - specifically as an exercise for the 3rd Chapter on Functions.

The kata is a very simple score tracker for tennis, and keeps track of the points and sets won by two imaginary players. A basic understanding of the [tennis scoring system](https://www.sportingnews.com/us/tennis/news/tennis-scoring-explained-rules-system-points-terms/7uzp2evdhbd11obdd59p3p1cx) is probably useful before tackling the kata, but not essential.

In the [challenge] directory is the original code. It is deliberately designed to exhibit several of the deficiencies called out in Chapter 3 of clean code. The challenge is to carry out a re-factor of the code based on the principles explored in the book without changing the behaviour of the code at all from the user's point of view.

The [solution] directory contains a possible re-factor of the code. Taste in style will vary, but I think most people would agree that it is much cleaner than the original. The solution folder also contains tests which exercise the solution code (note these are deliberately absent from the challenge code).

## Running the Code
The code is written in Python 3.6 and can be run directly in the python interpreter (e.g `python3 tennis.py`) without the need for installing any dependencies.

The unit tests can be run from the [solution] directly using the following command:

`python3 -m unittest discover`.
