#!/usr/bin/env python2

import psycopg2

questions = [
            'What are the most popular three articles of all time?',
            'Who are the most popular article authors of all time?',
            'On which days did more than 1% of requests lead to errors?'
            ]


queries = [
          """
              SELECT title, count(*)
              as num FROM articles
              JOIN log
              ON articles.slug = SUBSTRING(log.path FROM 10)
              WHERE log.path
              LIKE '/article/%'
              GROUP BY log.path, articles.title
              ORDER BY num
              DESC
              LIMIT 3;
          """,
          """
              SELECT authors.name, count(*)
              as num FROM articles
              JOIN authors
              ON articles.author = authors.id
              JOIN log
              ON articles.slug = SUBSTRING(log.path FROM 10)
              WHERE log.path
              LIKE '/article/%'
              GROUP BY authors.name
              ORDER BY num
              DESC;
          """,
          """
              SELECT TO_CHAR(errors.date, 'Mon dd, yyyy'),
              round(100.0*error/total, 2) AS percent
              FROM totals, errors
              WHERE totals.date = errors.date
              AND error > total/100;
          """
          ]


DBNAME = 'news'
y = 0
z = 1


def get_query(x):
    '''
    Get answer

    connect to the news database and execute the queries from the array
    '''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(queries[x])
    answer = c.fetchall()
    return answer
    db.close()


def print_answer_one(y, z):
    '''
    Print the answer

    Print the first answer for the first question from the news database
    '''
    x = 0
    answer = get_query(x)
    print "\n" + questions[x]
    for row in answer:
        print '"' + row[y] + '"' + " - " + str(row[z]) + " errors"


def print_answer_two(y, z):
    '''
    Print the answer

    Print the second answer for the second question from the news database
    '''
    x = 1
    answer = get_query(x)
    print "\n" + questions[x]
    for row in answer:
        print '"' + row[y] + '"' + " - " + str(row[z]) + " views"


def print_answer_three(y, z):
    '''
    Print the answer

    Print the third answer for the third question from the news database
    '''
    x = 2
    answer = get_query(x)
    print "\n" + questions[x]
    for row in answer:
        print str(row[y]) + " - " + str(row[z]) + "% errors"


def main():
    '''
    Main program

    main program that runs all the functions
    '''
    print_answer_one(y, z)
    print_answer_two(y, z)
    print_answer_three(y, z)


main()
