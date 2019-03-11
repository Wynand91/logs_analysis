# !/usr/bin/env python3
import psycopg2


class GetLog:

    def __init__(self):
        self.conn = psycopg2.connect('dbname=news')
        self.cursor = self.conn.cursor()
        self.to_be_printed = []

        # create views
        # total views per article
        self.cursor.execute(
            "CREATE VIEW total_article_views AS "
            "SELECT path, COUNT(*) AS total_views "
            "FROM log "
            "GROUP BY path "
            "ORDER BY total_views DESC "
            "OFFSET 1;"
        )

        # total views per article with author of article
        self.cursor.execute(
            "CREATE VIEW total_views_with_author AS "
            "SELECT articles.author, articles.title,"
            "total_article_views.total_views "
            "FROM articles JOIN total_article_views "
            "ON total_article_views.path "
            "LIKE concat('%', articles.slug) "
            "ORDER BY total_views DESC; "
        )

        # total responses per day
        self.cursor.execute(
            "CREATE VIEW responses_in_day AS "
            "SELECT date_trunc('day', log.time) AS day, "
            "       count(status) AS responses "
            "FROM log "
            "GROUP BY day;"
        )

        # total 404 error responses per day
        self.cursor.execute(
            "CREATE VIEW errors_in_day AS "
            "SELECT date_trunc('day', log.time) AS date, "
            "       count(status) as errors "
            "FROM log "
            "WHERE status LIKE concat('404','%') "
            "GROUP BY date;"
        )

        # Joined responses_in_day and errors_in_day
        self.cursor.execute(
            "CREATE VIEW responses_and_errors AS "
            "SELECT * FROM responses_in_day "
            "JOIN errors_in_day "
            "ON responses_in_day.day = errors_in_day.date;"
        )

        self.cursor.execute(
            "CREATE VIEW percentage_errors AS "
            "SELECT day, "
            "       ROUND(errors * 100.0 / responses, 2) AS percent "
            "FROM responses_and_errors;"
        )

    # What are the most popular three articles of all time?
    def most_popular_articles(self):
        self.cursor.execute(
            'SELECT title, total_views '
            'FROM total_views_with_author '
            'LIMIT 3;'
        )
        result = self.cursor.fetchall()

        for article in result:
            self.to_be_printed.append(
                article[0] + ' - ' + str(article[1]) + ' views \n'
            )
        self.to_be_printed.append("-" * 50 + "\n")

    # Who are the most popular article authors of all time?
    def most_popular_authors(self):
        self.cursor.execute(
            'SELECT name, SUM(total_views) AS sum_of_views '
            'FROM authors JOIN total_views_with_author '
            'ON authors.id = total_views_with_author.author '
            'GROUP BY name '
            'ORDER BY sum_of_views DESC; '
        )
        result = self.cursor.fetchall()

        for author in result:
            self.to_be_printed.append(
                author[0] + ' - ' + str(author[1]) + ' views \n'
            )
        self.to_be_printed.append("-"*50 + "\n")

    # On which days were more than 1% of responses 404 responses?
    def error_log(self):
        self.cursor.execute(
            "SELECT * FROM percentage_errors "
            "WHERE percent > 1.00;"
        )
        result = self.cursor.fetchall()

        for res in result:
            self.to_be_printed.append(
                res[0].strftime('%B %d, %Y') + ' - ' + str(res[1]) + '% errors'
            )
        self.to_be_printed.append("\n")

    # Method writes content of to_be_printed list to file
    def write_file(self):
        with open('log_result.txt', 'w') as f:
            for item in self.to_be_printed:
                f.write(item)

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    instance = GetLog()
    instance.most_popular_articles()
    instance.most_popular_authors()
    instance.error_log()
    instance.write_file()
