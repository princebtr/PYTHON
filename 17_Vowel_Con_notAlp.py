a = input()
if (a == "a" or a == "e" or a == "i" or a == "o" or a == "u" or a == "A" or a == "E" or a == "I" or a == "O" or a == "U") :
    print("Vowel.")
elif (a >= "a" and a <= "z" or a >= "A" and a <= "Z" ) :
    print("Consonant.")
else :
    print("Not an alphabet.")

    ''' This program will read a character from user and check whether it is VOWEL or CONSONANT if entered character
         was an alphabet using conditional opertors statement.

Input Format

Take a char ch fom the user.
Constraints

If other than alphabet is entered then print "Not an alphabet."
Output Format

If entered character is vowel then print "Vowel."
If entered character is consonant then print "Consonant."
If entered character is not alphabet then print "Not an alphabet.."'''
