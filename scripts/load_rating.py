from api.models import Movies, Rating
import csv


def run():
    # filename path
    with open('data\\ratings.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Rating.objects.all().delete()

        for row in reader:
            print(row)
            movie = Movies.objects.get(tconst=row[0])
            r = Rating(movies=movie,
                        averageReting=row[1],
                        numVotes=row[2]
                        )
            r.save()