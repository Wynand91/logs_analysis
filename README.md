# PROJECT: Logs Analysis

The _logs_analysis_ script contains a class that is able to create a log output from a database called 'news'.
The three methods  _**most_popular_articles**_, _**most_popular_authors**_ and _**error_log**_ each runs a query to get the relevant
data and stores data in an list. The method called _**write_file**_ writes contents of the list to a file called _log_result.txt_ 
 
**log_result.txt** should contain (in order): 

    1. the most popular articles, 
    2. the most popular authors and 
    3. days on which more than 1% responses were 404 responses.
    
**The example.txt file shows an example of the program's output** 
    
## Installation:

Using vagrant/virtualbox (Recommended):

   1. Download vagrant [here](https://www.vagrantup.com/downloads.html)
   2. Download VirtualBox [here](https://www.virtualbox.org/)
   3. Download VM configurations zip file(FSND-Virtual-Machine) and unzip [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
   4. From your terminal, inside FSND-Virtual-Machine/vagrant run: `vagrant up`
   5. After step 4 is finished run: `vagrant ssh`
   6. Your terminal is now logged into your virtual machine!
   
Installing database data:
    
   1. Download the SQL file [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip to extract
   2. Put this file in the `vagrant` directory inside FSND-Virtual-Machine (File that is shared with virtual machine)
   3. cd into FSND-Virtual-Machine/vagrant and load data with: `psql -d news -f newsdata.sql`
   4. Data is now loaded into database on virtual machine! If an error such as `psql: FATAL: database "news" does not exist` or `psql: could not connect to server: Connection refused` occurs, download
    VM configurations into a new directory and start it from there.

## Requirements/dependencies:

    python 3+
    psycopg2==2.7.7 (pip install psycopg2) 

## How to run:

The following views are used:
(_Please note! There is no need to create the SQL views manually as it is automatically created in the class __init___)

```buildoutcfg
CREATE OR REPLACE VIEW total_article_views AS
            SELECT path, COUNT(*) AS total_views 
            FROM log 
            GROUP BY path 
            ORDER BY total_views DESC 
            OFFSET 1;
            
CREATE OR REPLACE VIEW total_views_with_author AS
            SELECT articles.author, 
                   articles.title, 
                   total_article_views.total_views 
            FROM articles JOIN total_article_views 
            ON total_article_views.path 
            LIKE concat('%', articles.slug) 
            ORDER BY total_views DESC;
            
CREATE OR REPLACE VIEW responses_in_day AS
            SELECT date_trunc('day', log.time) AS day, 
                   count(status) AS responses 
            FROM log 
            GROUP BY day;
            
CREATE OR REPLACE VIEW errors_in_day AS
            SELECT date_trunc('day', log.time) AS date,
                   count(status) as errors
            FROM log
            WHERE status LIKE concat('404','%')
            GROUP BY date;
            
CREATE OR REPLACE VIEW responses_and_errors AS
            SELECT * FROM responses_in_day
            JOIN errors_in_day
            ON responses_in_day.day = errors_in_day.date;
```

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