from django.shortcuts import render
from django.http import JsonResponse
from .models import Movies, Rating
from rest_framework.decorators import api_view
# Create your views here.

# /api/v1/longest-duration-movies
@api_view(['GET'])
def loang_duration_movies(request):
    movies =  Movies.objects.filter().values('tconst', 'primaryTitle', 'runtimeMinutes', 'genres').order_by('runtimeMinutes')[:10]
    allmovies = []
    print(movies)
    for movie in movies:
        u = {
            'tconst' : movie['tconst'],
            'primaryTitle' : movie['primaryTitle'],
            'runtimeMinutes' : movie['runtimeMinutes'],
            'genres' : movie['genres']
        }
        allmovies.append(u)
    
    data = {'movieList': allmovies}
    res = {'success':True, 'data':data}
    return JsonResponse(res, safe=True)


# /api/v1/new-movie
@api_view(['POST'])
def new_movies(request):
    """

    """
    tconst =  request.data.get('tconst')
    titleType = request.data.get('titleType')
    primaryTitle = request.data.get('primaryTitle')
    runtimeMinutes = request.data.get('runtimeMinutes')
    genres = request.data.get('genres')
    averageRating = request.data.get('averageRating') if request.data.get('averageRating') else '0.0'
    numVotes = request.data.get('averageRating') if request.data.get('averageRating') else 0
    
    if tconst and titleType and primaryTitle and runtimeMinutes and genres:
        pass
    else:
        return JsonResponse({'success':False,'data':{'ERROR':'Field Requied Error','DESCRIPTION':'tconst, titleType, primaryTitle, runtimeMinutes and genres Fields are Requied'}})
    try: 
        m = Movies.objects.create(tconst=tconst, titleType=titleType, primaryTitle=primaryTitle, runtimeMinutes=runtimeMinutes, genres=genres)
        print(m,averageRating,numVotes)  
        r = Rating.objects.create(movies=m,averageReting=averageRating,numVotes=numVotes)   
        print(r)
    except Exception as e:
        print(e)
        return JsonResponse({'success':False,'data':{'ERROR':'MovieError','DESCRIPTION':'Somthing wrong in movie object creation.'}})
    return JsonResponse({'success':True,'data':'New movie added successfully'})

# top-rated-movies
@api_view(['GET'])
def top_rated_movies(request):
    movies =  Rating.objects.filter(averageReting__gte=6.0).values('averageReting', 'movies__tconst', 'movies__primaryTitle', 'movies__genres')
    allmovies = []
    print(movies)
    for movie in movies:
        u = {
            'tconst' : movie['movies__tconst'],
            'primaryTitle' : movie['movies__primaryTitle'],
            'averageRating' : movie['averageReting'],
            'genres' : movie['movies__genres']
        }
        allmovies.append(u)
    
    data = {'movieList': allmovies}
    res = {'success':True, 'data':data}
    return JsonResponse(res, safe=True)
