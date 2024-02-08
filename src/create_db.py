import sqlite3

# con = connect to database
# cur = cursor, which enables user to execute commands in the database
con = sqlite3.connect("nba.db")
cur = con.cursor()

# enables the execution of sqlite commands via python
cur.execute(
    """CREATE TABLE IF NOT EXISTS nba_players
                (name, team, position, age)"""
)


cur.execute(
    """INSERT INTO nba_players VALUES
                ('LeBron James', 'Los Angeles Lakers', 'SF', '39')"""
)

con.commit()

# the "*" in this statement means to select all the information listed in the selected table.
# any other instance you would be more specific, such as '''SELECT team FROM nba_players'''.
for row in cur.execute("""SELECT * FROM nba_players"""):
    print(row)
