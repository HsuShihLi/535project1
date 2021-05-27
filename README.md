CPSC535-SP21-Project1
Rewrite greeting cards by reusing most of the text for another occasion

ClassNumber:

535-01

Team members:

Jing Feng: jingfeng@csu.fullerton.edu

Hsushi Li: hsushihli@csu.fullerton.edu

Jingzhi Su: Jingzhi_Su@csu.fullerton.edu

Description of the project:

Briefly, we need to rewrite greeting cards by reusing most of the rext for another occasion. For example, a congratulation email on a new car may be similar to a congratulation email on a new house. One can copy and paste parts of the previous greeting to make it into a new greeting.

The problem can be formulated as follows: Given a string S of length N>0, and a list of M pairs of strings LS, each pair representing a string to be replaced and the second being the actual replacement, display the new string R that is obtained by replacing every occurrence of the first string in each pair with the corresponding second string in the pair. The string matching must be case sensitive.

We would like to develop a software that does it for us.

Example:

Input:

S[] = “My dear Anna, let me congratulate you on the beautiful car that you purchased today. It looks very posh. I hope you got a good deal. Cars are expensive but much needed. Best regards, Naomi.”

LS[] = {{“Anna”, “Jovi and Victor”} , {“car”, “house”}, {“today”, “last week”}, {“posh”, “well built”}}

Output:

R[] = “My dear Jovi and Victor, let me congratulate you on the beautiful house that you purchased last week. It looks very well built. I hope you got a good deal. Cars are expensive but much needed. Best regards, Naomi.”

Features:

Python3; string match.
