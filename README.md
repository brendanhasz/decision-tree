# Decision Tree
`decision-tree` is a program which uses a decision tree machine learning algorithm to classify data. It constructs and applies decision trees to training and test data files.  The program uses the `ID3` (Interactive Dichotomiser 3) algorithm.


# Useage
[`python`](http://www.python.org/) is required to run the code.  To build a decision tree from training data, run

```bash
$ python builddt.py train_data_filename dt_filename
```

where "train_data_filename" is the name of the file from which to make the decision tree, and "dt_filename" is the name of the file to which you would like to save the constructed decision tree.

To classify data using a constructed decision tree, run

```bash
$ python applydt.py test_data_filename dt_filename
```

where "test_data_filename" is the data you wish to classify, and "dt_filename" is the file where the decision tree was saved by builddt.py.


# Copyright
Copyright (C) 2012 Brendan Hasz

[bhasz@brandeis.edu](mailto:bhasz@brandeis.edu)

[www.cs.brandeis.edu/~bhasz/main.php](http://www.cs.brandeis.edu/~bhasz/main.php)

[Brandeis University](http://www.brandeis.edu/), Waltham, MA, USA

