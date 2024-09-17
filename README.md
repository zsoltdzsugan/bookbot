# "Book Bot"

A _python_ program that can analyze an entire book and print out an interesting statistical report.

## Usage

_required arguments:_
-f FILENAME, --filename FILENAME < Specify the filename to process

```shell
python3 main.py [-h] [-v] -f FILENAME [-cw] [-cc] [-pr]
```

## Options:

-cw, --count-words < Returns the count of the words in the document
-cc, --count-chars < Returns the number of times each character appears in the document
-pr, --print-report < Returns a report of the document

## Example:

```shell
python3 main.py -f <mybook.txt> --cw
```
