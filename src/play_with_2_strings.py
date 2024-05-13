"""https://www.codewars.com/kata/56c30ad8585d9ab99b000c54/train/python

By the way you don't have to check errors or incorrect input values, everything is ok without bad tricks, only two input strings and as result one output string;-)...

And here's the rule:
Input Strings a and b: For every character in string a swap the casing of every occurrence of the same character in string b. Then do the same casing swap with the inputs reversed. Return a single string consisting of the changed version of a followed by the changed version of b. A char of a is in b regardless if it's in upper or lower case - see the testcases too.
I think that's all;-)...

Some easy examples:

Input: "abc" and "cde"      => Output: "abCCde" 
Input: "ab" and "aba"       => Output: "aBABA"
Input: "abab" and "bababa"  => Output: "ABABbababa"
Once again for the last example - description from KenKamau, see discourse;-):

a) swap the case of characters in string b for every occurrence of that character in string a
char 'a' occurs twice in string a, so we swap all 'a' in string b twice. This means we start with "bababa" then "bAbAbA" => "bababa"
char 'b' occurs twice in string a and so string b moves as follows: start with "bababa" then "BaBaBa" => "bababa"

b) then, swap the case of characters in string a for every occurrence in string b
char 'a' occurs 3 times in string b. So string a swaps cases as follows: start with "abab" then => "AbAb" => "abab" => "AbAb"
char 'b' occurs 3 times in string b. So string a swaps as follow: start with "AbAb" then => "ABAB" => "AbAb" => "ABAB".

c) merge new strings a and b
return "ABABbababa"

There are some static tests at the beginning and many random tests if you submit your solution."""


# Function to transform string b based on occurrences in string a
def transform(a: str, b: str) -> str:
    # Count occurrences in a case-insensitive manner and determine if odd or even
    counts = {
        char.lower(): a.lower().count(char.lower()) % 2 for char in set(a.lower())
    }
    # Transform b based on the counts
    transformed_b = "".join(
        char.swapcase() if counts.get(char.lower(), 0) else char for char in b
    )
    return transformed_b


# Main function to work on strings a and b
def work_on_strings(a: str, b: str) -> str:
    # Transform both strings
    transformed_a = transform(b, a)
    transformed_b = transform(a, b)
    return transformed_a + transformed_b


if __name__ == "__main__":
    result = work_on_strings("abc", "cde")
    print(result)
