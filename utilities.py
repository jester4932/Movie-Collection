from database import MovieCollection, db_connection


# Builds the first three feature suggestions
def database_build(sqlconn):
    movies_table = [MovieCollection(Title='Star Wars IV', Format='Streaming', Length='121',
                                    Release_Year=1977, Rating=1),
                    MovieCollection(Title='Star Trek 2', Format='VHS', Length='113',
                                    Release_Year=1982, Rating=2),
                    MovieCollection(Title='Die Hard', Format='DVD', Length='132',
                                    Release_Year=1988, Rating=3)]
    sqlconn.add_all(movies_table)
    sqlconn.commit()


# This only for this app. this so the database_build function doesn't continue to add 3 entries every time the app is
# restarted. it will delete all entries and reset back to the original 3 entries above
def database_reset():
    sqlconn = db_connection()
    sqlconn.query(MovieCollection).delete()
    database_build(sqlconn)
    sqlconn.close()


# Select query to get all the current feature suggestions in the database
def db_call():
    sqlconn = db_connection()
    data = []
    for row in sqlconn.query(MovieCollection).order_by(MovieCollection.Rating):
        data.append(row)
    chart = make_chart(data)
    sqlconn.close()
    return data, chart


# Inserts new feature suggestions into the database
def db_insert(rows):
    sqlconn = db_connection()
    rating = check_rating(int(rows['Rating']))
    if rating:
        rating_update(rating)
    movie = MovieCollection(Title=rows['Title'], Format=rows['Format'], Length=rows['Length'],
                         Release_Year=int(rows['Release_Year']), Rating=rows['Rating'])
    sqlconn.add(movie)
    sqlconn.commit()
    sqlconn.close()
    return True


def de_delete(rows):
    sqlconn = db_connection()
    movie = MovieCollection(Title=rows['Title'], Format=rows['Format'], Length=rows['Length'],
                         Release_Year=int(rows['Release_Year']), Rating=rows['Rating'])
    sqlconn.delete(movie)
    sqlconn.commit()
    sqlconn.close()


# check if rating of new movie is higher than existing movies
def check_rating(rating):
    sqlconn = db_connection()
    info = []
    for data in sqlconn.query(MovieCollection).filter(MovieCollection.Rating >= rating):
        info.append(data)
    sqlconn.close()
    return info


# Updates rating if rating of new movie is higher than any movies already in database
def rating_update(data):
    sqlconn = db_connection()
    for info in data:
        x = str(info).split(',')
        row = sqlconn.query(MovieCollection).filter(MovieCollection.id == int(x[0])).first()
        row.Rating = int(x[4])+1
        sqlconn.commit()
    sqlconn.close()


# Makes the table on the web page of current movies in DB
def make_chart(data):
    chart = ''
    for row in data:
        info = str(row).split(',')
        chart += '''<tr>
        <td align="left" style="border-bottom: 1px solid #d8d8d8">%s</td>
        <td align="left" style="border-bottom: 1px solid #d8d8d8">%s</td>
        <td align="left" style="border-bottom: 1px solid #d8d8d8">%s</td>
        <td align="left" style="border-bottom: 1px solid #d8d8d8">%s</td>
        <td align="left" style="border-bottom: 1px solid #d8d8d8">%s</td>
    </tr >'''%(info[1], info[2], info[3], info[4], info[5])
    return chart
