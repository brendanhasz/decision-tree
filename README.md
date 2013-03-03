# Decision Tree
`decision-tree` is a program which uses a decision tree machine learning algorithm to classify data. It constructs and applies decision trees to training and test data files.  The program uses the `ID3` (Interactive Dichotomiser 3) algorithm.


# Usage
[`python`](http://www.python.org/) is required to run the code.  

## Input format
`builddt` and `applydt` take CSV (Comma Separated Value) formatted files.  The first column in the training file is the class, and the other columns are the attributes.  The test file should be the same, just without the first column of class data.  `applydt` outputs a file in the same format as the training data file.

Some converters are supplied in `/parsers`.  For example, to convert training gene sequence data which has no comma separators, run

```bash
$ python parsers/gene_seq.py -train train_data_filename train_CSV_filename
```

And to convert test gene sequence data, run

```bash
$ python parsers/gene_seq.py -test test_data_filename train_CSV_filename
## Building a Decision Tree from training data
To build a decision tree from training data, run

```bash
$ python builddt.py train_data_filename dt_filename
```

where "train_data_filename" is the name of the file from which to make the decision tree, and "dt_filename" is the name of the file to which you would like to save the constructed decision tree.

## Classifying test data
To classify data using a constructed decision tree, run

```bash
$ python applydt.py test_data_filename dt_filename output_filename
```

where "test_data_filename" is the data you wish to classify, "dt_filename" is the file where the decision tree was saved by builddt.py, and "output_filename" is the file to which you wish to output the classified results.


# Copyright
Copyright (C) 2012 Brendan Hasz

[bhasz@brandeis.edu](mailto:bhasz@brandeis.edu)

[www.cs.brandeis.edu/~bhasz/main.php](http://www.cs.brandeis.edu/~bhasz/main.php)

[Brandeis University](http://www.brandeis.edu/), Waltham, MA, USA

