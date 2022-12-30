from api.models import Movies, Rating
import csv


def run():
    # filename path
    with open('data\\movies.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Movies.objects.all().delete()

        for row in reader:
            print(row)

            movie = Movies(tconst=row[0],
                        titleType=row[1],
                        primaryTitle=row[2],
                        runtimeMinutes=row[3],
                        genres=row[4])
            movie.save()