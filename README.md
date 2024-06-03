## Design: Newsfeed for Kids Application using Flask

### HTML Files
- **index.html**: This will be the main newsfeed page, displaying a list of kid-friendly articles.
- **article.html**: This will display the content of an individual article when a user clicks on its title from the newsfeed.

### Routes
- **@app.route('/')**: This route will display the main newsfeed page (`index.html`).
- **@app.route('/article/<article_id>'):** This route will display the content of the article with the specified `article_id`.
- **@app.route('/api/articles'):** This route will provide a JSON response containing a list of all the articles. This API endpoint can be consumed by a frontend component to dynamically display the newsfeed.