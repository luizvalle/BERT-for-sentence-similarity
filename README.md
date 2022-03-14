# Instructions
## Description
The program reads from the **standard input** pairs of sentences of the form `<sentence1>[SEP]<sentence2>` on each line. Once the `EOF` character is found, it returns the cosine **distance** between the BERT encodings of each of the sentence pairs given. The cosine distance (1 - cosine similarity) is a real number in the range [0,1], where lower numbers mean the encodings are semantically closer.

## Example (typing into standard input)
```bash
$ python similarity.py
Changed LinkedList to HashMap.[SEP]Fixed issue with HashMap.
Fixed divide by zero bug[SEP]Fixed issue with HashMap.
Fixed syntax error[SEP]Added missing import of math
Fixed syntax error[SEP]Added missing semicolon
0.20660609006881714
0.3534572720527649
0.4152190089225769
0.3391793370246887
```

## Example (piping input)
Suppose you have a file called `commits.txt` with the following content
```txt
Changed LinkedList to HashMap.[SEP]Fixed issue with HashMap.
Fixed divide by zero bug[SEP]Fixed issue with HashMap.
Fixed syntax error[SEP]Added missing import of math
Fixed syntax error[SEP]Added missing semicolon
```
```bash
$ cat commits.txt | python similarity.py
0.20660609006881714
0.3534572720527649
0.4152190089225769
0.3391793370246887
```
The `cat` command could be replaced by a program that produces the sentence pairs and prints them line-by-line to the stadard output.
