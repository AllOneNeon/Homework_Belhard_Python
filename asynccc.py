import httpx

users = httpx.get('https://jsonplaceholder.typicode.com/users')
posts = httpx.get('https://jsonplaceholder.typicode.com/users/posts')
todos = httpx.get('https://jsonplaceholder.typicode.com/users/todos')
albums = httpx.get('https://jsonplaceholder.typicode.com/users/albums')
comments = httpx.get('https://jsonplaceholder.typicode.com/posts/comments')
photos = httpx.get('https://jsonplaceholder.typicode.com/albums/photos')
print(users.text)
print(posts.text)
print(todos.text)
print(albums.text)
print(comments.text)
print(photos.text)