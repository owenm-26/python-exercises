# String Manipulation Cheat Sheet

## Special Rules

`str = "She said \"I like python \". Let's go."` == She said "I like python". Let's go.

## Methods

`a[::-1]` - reverses string with a step length of 1

`a.find("o")` - returns first index occurrence of substring. Otherwise -1.w

`a.split(",")` - returns a list of strings split by input string. Defaults to space if not specified 

`"-".join([])` - concatenates string items of list with the desired delimiter between them.

`a.format(x, y)` - replaces `{}` in string with arguments given

`a.strip(".")` - strips designated character from front and back of string. Defaults to space if no arg given

`a.replace("r", "R")` - replaces every occurrence of the first with the second.

## Cases

`a.lower()` - changes every character in string to lowercase

`a.upper()` - changes every character in string to uppercase

`ord("a")` - gets the numerical value of the string. Uppercase is 65-90. Lowercase is 97-122.

`a.title()` - turns string into title case 
ex: "owen mariani" --> "Owen Mariani"