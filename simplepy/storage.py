##########################################################################
#
#   Copyright / License notice 2022
#   --------------------------------
#
#   Permission is hereby granted, free of charge,
#       to any person obtaining a copy of this software
#       and associated documentation files (the “Software”),
#       to deal in the Software without restriction, including
#       without limitation the rights to use, copy, modify, merge,
#       publish, distribute, sublicense, and/or sell copies of the Software,
#       and to permit persons to whom the Software is furnished to do so,
#       subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included
#       in all copies or substantial portions of the Software.
#
##########################################################################

import simplepy
import sqlite3
from pathlib import Path

class Storage:

    def __init__(self):
        pass

    def fileExists(self,fileName): return Path(fileName).is_file()

    def  createStorage(name):
        conn = sqlite3.connect(name+'db')

        c = conn.cursor()
        c.execute("""CREATE TABLE students (
            name TEXT,
            age INTEGER,
            height REAL
        )""")

        c.execute("INSERT INTO students VALUES ('mark', 20, 1.9)")

        all_students = [
            ('john', 21, 1.8),
            ('david', 35, 1.7),
            ('michael', 19, 1.83),
        ]
        c.executemany("INSERT INTO students VALUES (?, ?, ?)", all_students)

        c.execute("SELECT * FROM students")
        print(c.fetchall())

        #import pandas as pd
        #df = pd.read_csv("population_total.csv")
        #df.to_sql("population", con=c)
        #c.execute("SELECT * FROM population").fetchall()

        # commit
        conn.commit()

        # close the connection
        conn.close()