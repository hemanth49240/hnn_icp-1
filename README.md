# hnn_icp-1
Code Video : https://drive.google.com/file/d/1Jn5O4N8L4YFHd90lemlS4s8q7hY5Qvft/view?usp=sharing

1.1 Deletion of charcters and reversing string

The user is prompted to enter a string (m).
The user is prompted to enter the number of characters to be deleted (s).
For each deletion, the user provides a character to be removed from the original string.

The input string is converted into a list of characters (char_list).
A set (characters_to_delete) is created to store the characters to be deleted.
For each deletion, the specified character is added to the set.
List comprehension is used to create a new list (char_list) excluding the characters in the set.
The resulting list is reversed and joined into a single string (result_string).

The resultant string after deletion and reversal is printed.
Example:

Enter a string: python
Enter the number of characters to be deleted: 2
Enter the character to be deleted: h
Enter the character to be deleted: o
Resultant string: ntyp

1.2 Arithmetic Operations:

The code performs basic arithmetic operations on the input numbers.
Input:
The user is prompted to enter two integer numbers (num1 and num2).

Addition: add = num1 + num2
Subtraction: sub = num1 - num2
Multiplication: mul = num1 * num2
Division: div = num1 / num2
The results of these operations are stored in variables.

Output:
The code prints the results of the arithmetic operations.

Example:
Input:
5
3

Output:
addition: 8
subtraction: 2
multiplication: 15
division: 1.6666666666666667

2. String Replace/Modification:
   
Input:
The user is prompted to enter a string (s2).

The code splits the input string into a list of words using the split method with the space character as the delimiter.
For each word in the list, if the word is "python", it is replaced with "pythons". Otherwise, the word is appended to the new string (s1).
The modified string is then printed.

Output:

The modified string with "python" replaced by "pythons" is printed.
Example:

Input: 
I love playing with python
Output: 
I love playing with pythons

3. Marks to Grade calculator

The user is prompted to enter a floating-point number (inpsc), representing a score.

The code checks the value of the input score against predefined ranges.
Based on the range in which the score falls, it prints the corresponding grade ('A', 'B', 'C', 'D', or 'F').

The grade corresponding to the input score is printed.
Example:
Input: 90.5
Output: GRADE A
