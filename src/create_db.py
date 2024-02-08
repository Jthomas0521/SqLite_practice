import sqlite3

# con = connect to database
# cur = cursor, which enables user to execute commands in the database
con = sqlite3.connect("nba.db")
cur = con.cursor()

# enables the execution of sqlite commands via python
# if the table is not created already, it is now created
cur.execute(
    """CREATE TABLE IF NOT EXISTS nba_players
                (name, team, position, age)"""
)

# primary key is a feature that prevents the insertion of specified (unique) duplicate data.
# EX: """CREATE TABLE IF NOT EXISTS nba_players
#                (name PRIMARY KEY, team, position, age)"""
# )

# inserts data into the table. be sure to enter the data in the order that tables are so that
# the data aligns correctly. You don't Lebron's name where his position should go.
cur.execute(
    """INSERT INTO nba_players VALUES
                ('LeBron James', 'Los Angeles Lakers', 'SF', '39')"""
)

# you can also ignore the attempts of inserting duplicate data by doing this:
# """INSERT OR IGNORE INTO nba_players VALUES
#               ('LeBron James', 'Los Angeles Lakers', 'SF', '39')"""
# )

con.commit()

# the "*" in this statement means to select all the information listed in the selected table.
# any other instance you would be more specific, such as '''SELECT team FROM nba_players'''.
for row in cur.execute("""SELECT * FROM nba_players"""):
    print(row)
