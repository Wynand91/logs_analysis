# PROJECT: Logs Analysis

The _logs_analysis_ script contains a class that is able to create a log output from a database called 'news'.
The three methods  _**most_popular_articles**_, _**most_popular_authors**_ and _**error_log**_ each runs a query to get the relevant
data and stores data in an list. The method called _**write_file**_ writes contents of the list to a file called _log_result.txt_ 
 
**log_result.txt** should contain (in order): 

    1. the most popular articles, 
    2. the most popular authors and 
    3. days on which more than 1% responses were 404 responses.
    
**The example.txt file shows an example of the program's output** 
    
## Requirements/dependencies:

    python 3+
    psycopg2==2.7.7 (pip install psycopg2)
    
    
## How to run:
_Please note! There is no need to create the SQL views manually as it is automatically created in the class __init___

    1. Install necessary requirements/dependencies (preferably in a virtual environment)
    2. In terminal, cd to directory containing the 'logs_analysis.py' script
    3. run 'python logs_analysis.py'
    4. a 'log_result.txt' file containing the results will appear in your current working directory


## Author

 - Wynand theron


## License

MIT License

Copyright (c) 2019 Wynand Theron

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.