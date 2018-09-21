<a href="https://farhour.com"><img src="https://farhour.com/img/github/LCS-of-source-codes.gif" title="LCS" alt="LCS"></a>

# Coding Task 2 - LCS of source codes

This repository is mostly an **academic exercise**. This code solves the problem of finding all shared sequences of tokens with the maximum length. The tokens are created from our input source code files by the program. I use **regular expressions** to tokenize the codes and **generalized suffix tree** to find all longest shared sequences of these tokenized codes. The full explanation of the problem can be found in `TASK.md` in this repo. For more details about the time complexity of the problem, see the [FAQ](#faq-about-algorithms) section.

---

## Table of Contents

- [Example](#example)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Syntax of Sample Source Codes](#syntax-of-sample-source-codes)
- [FAQ About Algorithms](#faq-about-algorithms)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

---

## Example

The longest shared sequences of the two below codes are `["*", "0.05", ";", "ENDIF", ";"]` and `["K", ":=", "1", ";", "IF"]`. Their length is five.

```qbasic
K := 1;
IF quantity := 1 THEN
        total := total + price * quantity;
        tax := price * 0.05;
ENDIF;
```
```qbasic
K := 1;
IF var := 1 THEN
        sum := number + test * value;
        ave := summit * 0.05;
ENDIF;
```

---

## Requirements

This project is fully written in **Python 3**. To clone this repo and run the program, you need:
* **Git** (1.7.x or newer)
* **Python** (3.2 or above)

---

## Installation

Just clone this repo to your local machine and use Python 3 to run it!

---

## Usage

**Option 1**: Input the source code files through the command line. The result in `CSV` and `JSON` formats will be created in the output directory.
```shell
$ python run.py input/samples/file-1.txt input/samples/file-2.txt
```
**Option 2**: Specify the directory which have the source code files in the `run.py` file and then run it.
```python
path = 'input/sample/*.txt'
```
```shell
$ python run.py
```
You can create random source code files using `codeGenerator.py` file:
```shell
$ python codeGenerator.py
```
If you need to change the number of files or the repetition of the same code in the files, change these lines in the `codeGenerator.py` file:
```python
numberOfFiles = 100
sameCodeExists = True
```
---

## Features

- Using **generalized suffix tree** (instead of dynamic programming approach) to find the **LCS** of tokens with the least time complexity.
- Using **regular expressions** to tokenize the source codes.
- Reading path of the source code files from the command line or searching all the files in a given directory.
- Generating the result in `CSV` or `JSON` formats.
- Generating random source code files using a simple code generator.

---

## Syntax of Sample Source Codes

The tokenizer of this program tokenizes the source codes using several **regular expressions**. You can change them and add more complex regular expressions to tokenize different types of programming language and detect more distinct tokens. Here are the rules of current tokenizer:
- The **Keywords** of the sample programming language are: `IF`, `THEN`, `ENDIF`, `FOR`, `NEXT`, `GOSUB`, `TO`, `PRINT`, and `RETURN`.
- The other **Tokens** that can be identified by the program are:
  - **Numbers**: Any integer or decimal number.
  - **Assignment Operator**: The assignment operator in our sample programming language is `:=`.
  - **Statement Terminator**: The statement terminator in our sample programming language is `;`.
  - **Identifiers**: An identifier starts with a letter A to Z or a to z and followed by letters. It does not contain any underscore or number.
  - **Arithmetic Operators**: The four arithmetic operators are `+`, `/`, `-`, and `*`.
- **Line Endings**: The tokenizer identifies line endings using a regular expression and skips it.
- **Spaces and Tabs**: The tokenizer recognizes and skips any spaces and tabs in the source codes.

If a token identified by the program as a mismatch, then the tokenizer generates a **runtime error**.

---

## FAQ About Algorithms

- **Why do you NOT use *dynamic programming* to solve this problem?**
    - Dynamic Programming can be used to find the longest common substring in a way that needs less code to write **BUT** when we have a lot of files, the code execution time will be increased. For more details, visit [here](https://www.geeksforgeeks.org/longest-common-substring-dp-29/).
- **What is the *time complexity* of the *dynamic programming* approach?**
    - Dynamic Programming can be used to find the longest common substring in **`O(m*n)`** time For two strings of length **`m`** and **`n`**. The idea is to find the length of the longest common suffix for all substrings of both strings and store these lengths in a table. For more details, visit [here](https://www.geeksforgeeks.org/longest-common-substring-dp-29/).
- **Is there a better approach with less *time complexity* to find the longest common substring?**
    - Fortunately yes! By using a suffix tree and building a generalized suffix tree, we can solve this problem in a faster way for a lot of files.
- **What is a *suffix tree*?**
    - In computer science, a suffix tree (also called PAT tree or, in an earlier form, position tree) is a compressed trie containing all the suffixes of the given text as their keys and positions in the text as their values. Suffix trees allow particularly fast implementations of many essential string operations. For more details, visit [here](https://en.wikipedia.org/wiki/Suffix_tree).
- **What is a *generalized suffix tree*?**
    - In computer science, a generalized suffix tree is a suffix tree for a set of strings. Given the set of strings of total length, it is a Patricia tree containing all suffixes of the strings. It is mostly used in bioinformatics, but we use it in our code to solve the problem efficiently. For more details, visit [here](https://en.wikipedia.org/wiki/Generalized_suffix_tree).
- **What is the *time complexity* of the *generalized suffix tree* approach?**
    - One can find the lengths and starting positions of the longest common substrings of two given strings, **`S`** of length **`m`** and **`T`** of length **`n`**, in **`O(m+n)`** time with the help of a generalized suffix tree. Finding them by dynamic programming costs **`O(m*n)`**. For more details, visit [here](https://www.geeksforgeeks.org/suffix-tree-application-5-longest-common-substring-2/).

---

## Contributing

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine.

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request.

---

## Support

Reach out to me at one of the following places!

- Website at <a href="https://farhour.com" target="_blank">farhour.com</a>
- Twitter at <a href="http://twitter.com/farhour" target="_blank">@farhour</a>

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- This project is licensed under the **[MIT license](http://opensource.org/licenses/mit-license.php)**.
- Copyright © 2018 <a href="https://farhour.com" target="_blank">**Farbod Farhour**</a>

---

This README was written with ❤️.
