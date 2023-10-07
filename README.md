
# moviesapi
Backend Assignment from Onefin

Below API are as follows:

1. POST https://deployapi.pythonanywhere.com/register/
   {
“username”: <desired username>,
“password”: <desired password>
  }
2. GET https://deployapi.pythonanywhere.com/movies/
3. GET https://deployapi.pythonanywhere.com/collection/
4. POST https://deployapi.pythonanywhere.com/collection/
   Request payload:
      {
      “title”: “<Title of the collection>”,
      “description”: “<Description of the collection>”,
      “movies”: [
      {
      “title”: <title of the movie>,
      “description”: <description of the movie>,
      “genres”: <generes>,
      “uuid”: <uuid>
      }, ...
      ]
      }
5. PUT https://deployapi.pythonanywhere.com/collection/<collection_uuid>/
   {
“title”: <Optional updated title>,
“description”: <Optional updated description>,
“movies”: <Optional movie list to be updated>,
}
6. GET https://deployapi.pythonanywhere.com/<collection_uuid>/
7. DELETE https://deployapi.pythonanywhere.com/collection/<collection_uuid>/
8. GET https://deployapi.pythonanywhere.com/request-count/
