# Python-Intern

Solutions of two recruitment tasks.

## Task 1 "Hacking 101"

Program calculates the power of hacks and returns the value.

### Usage

To calculate the power use the file hack_power.py . Main function hack_calculator(hack: str) allows to calculate the power. Function hack_calculator could get also two more arguments: letters (dictionary) and phrases (dictionary). The default values of these parameters are:
```
letters = {'a': 1, 'b': 2, 'c': 3}

phrases = {'ba': 10, 'baa': 20}
```
Basic argument of hack_caclulator function should be a string. The same with keys in both of additional parameters.

Example of usage:
```
hack_calculator('aabacabaaaca')
```
and the result is:
```
81
```
## Task 2 "Traffic report"

Script lists the number of views of each URL provided in the log file.

### Usage

Each log file, which is to be checked, should has one entry on one row, which should look like:

```
10.10.110.222 [10/Feb/205:14:01:12 +0400] "GET http://google.com HTTP/1.1" 200 1024
```

After checking all rows script prints results in the form:

```
google.com , 1
```


### saving into .csv file

To save the result, from the 'today.log' file, into csv file use the command (into the command line):
```
python page_report.py today.log > report.csv
```

## Author
Filip Zdrzewielski
