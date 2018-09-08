## Begin Coding Task2

# Definition

You're going to find the shared SEQUENCE of tokens with maximum length.

I want a github repository of a program that takes in a
list of source code files (the list could be in a file or commandline
arguments) and then proceeds to quickly tokenize the tokens from the
source code and report the longest common token subsequences across all
the files.

The report output should be CSV or JSON

For example CSV columns are: CSV: score,tokens,count,"sourcecode"

score = log2(tokens) * log2(count), so a string that appears in only once
ever has a score of 0 (don't report these), but a sequence of tokens
that is 8 tokens long and occurs 4 times

will have a score of log2(8) * log2(4) = 3 * 2 = 6.

for instance:

38.2,14,1040,"for(int i=0;i < length; i++){"
38.1,14,1021,"for(int j=0;j < length; j++){"
21.74,5,659,"foreach(Object e in"
19.7,4,925,"element.toString()"

# Deliverables

* 1 github repo
* 1 example test set (could be on the software itself)
* source code of a program that tokenizes source code read from a list of source code files (using the programming language of your choice)
	** That finds the longest common token sequences across all files.
	** Outputs a report of the longest common token sequences across the files

* A ReadMe file that describes how I can compile and test your program

# Examples

I want it at the token level, the tokenization doesn't have to be
perfect but lexing is pretty easy compared to parsing.

e.g.

tokenize("for (int i=0;") -> ["for","(","int","i","=","0",";"]
tokenize("for (int j=0;") -> ["for","(","int","j","=","0",";"]
tokenize("for (int v=0;") -> ["for","(","int","v","=","0",";"]

Which could produce:

longestCommonSequences([["for","(","int","i","=","0",";"],
   ["for","(","int","j","=","0",";"],
   ["for","(","int","v","=","0",";"]]) ->
[{seq:["for","(","int"],count:3,score:1.6},{seq:["=","0",";"],count:3,score:2.5}]

Some of the test files should probably be similar files (e.g., have a shared function) so you are sure there are common tokens.

Recommendation: try it on 2 files, 10 files, 100 files.

Please make sure you commit to the repository as you are developing the code, and not simply at the end. Seeing your intermediate commits and how you developed the solution over time is as important as the final solution.

### End Coding Task 2
