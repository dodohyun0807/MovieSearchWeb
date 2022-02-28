import requests
import json

Movie = []


def index():
    api_key = '?api_key=10caf64b13f658a3221fba1405c5813c'
    
    for page_idx in range(1, 401):
        url = f'https://api.themoviedb.org/3/movie/top_rated{api_key}&language=ko-KR&page={page_idx}'
        r = requests.get(url)
        data = json.loads(r.text)
        
        for movie_idx in range(20):
            movie = {'model':'movies.movie', 'fields': {'movie_id':'', 'title':'', 'genres':'', 'overview':'', 'poster_path':'', 'release_date':'', 'popularity':''}}
            movie['fields']['movie_id'] = data['results'][movie_idx]['id']
            movie['fields']['title'] = data['results'][movie_idx]['title']
            movie['fields']['genres'] = data['results'][movie_idx]['genre_ids']
            movie['fields']['overview'] = data['results'][movie_idx]['overview']
            movie['fields']['poster_path'] = data['results'][movie_idx]['backdrop_path']
            movie['fields']['release_date'] = data['results'][movie_idx]['release_date']
            movie['fields']['popularity'] = data['results'][movie_idx]['popularity']
            Movie.append(movie)

index()

file = open('movies.json', 'w+', encoding='utf-8')
file.write(json.dumps(Movie, ensure_ascii=False))
