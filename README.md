# VOTE YOUR MOST FAVORITE SONG OF ARTISTS

#### Video Demo:  https://youtu.be/0UpnfR4E6xE

#### Description:
How the web application works:
1. The web app is implemented with Spotify API.
2. In order to make the program work, need to enter SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET on the terminal.
3. Need to register and login in order to use the web application.
4. Once login, the index page shows your most favorite song of artists you have voted for.
5. Search & vote page allows you to search all song of the artist you enter from spotiy and vote for the most favorite song. You can make a change of your choice through this page too.
6. Ranking page shows the most popular song of the artist you voted for within the user community and link to search the song in Youtube and Spotify.
7. History page shows the history of songs that you voted for and a link to make a change as well.


Code explanation:
1. helper.py
    This python code contains function track_search and login_required.
    login_required makes sure the user has logged in when using the web app.
    track_search function receives input of artist name and search it in Spotify API. It goes through every search result and append the song name to a list called track, and return the list.

2. application.py
    This python code uses SQLites, Flask to build the web app.
    I. route "/":
        execute SQL statement to get the result of aritist and songs that the user voted for from the database. Send the result to index.html to display
    II. route "/search":
        If no artist name entered or incorrect artist name entered, error message will come up. Else, get the artist name that user enters and search using track_search function in helper.py
        Also look up the artist name and user from history table in database to see if the user voted for this artist before, if yes, send the search result to change.html, and if not, send the result to vote.html
    III. route "/vote":
        Vote your most favorite song of the artist you searched for. Record the vote to history table in database and add it to total count of how many times this song was voted by the community in picks table in database.
        I used sqlite3 statement: begin transaction...commit.. roll back to make sure statements are completed as a whole.
        Once the vote is completed successfully, it will redirect to route "/", which display all votes you have made.
    IV. route "/change"
        to change your vote of the most favorite song. Once you submit your new vote. It will reverse the cout of total votes of your prior favorite song in picks table, and update your voting history for corresponding artist.
        Then your vote to new favorite song will be added to to total count of how many times this song was voted by the community in picks table in database.
        I used sqlite3 statement: begin transaction...commit.. roll back to make sure statements are completed as a whole.
        Once the vote is completed successfully, it will redirect to route "/", which display all votes you have made.
    V. route "/rank"
        look up the most voted song of artists you have voted from picks table in databse, in order to show the most popular song of artists you have voted for. Send the info to rank.html, which also have a button to let you search the song in Youtube and Spotify.
    VI. route "/history"
        look up your voting history from history table in database.
    VII. route "/login"
        implement checks to see if username and password both has been entered. and compare password to result looked up from users table in database to help user login. Once login is successful, will redirect to route "/".
    VIII. route "/logout"
        clear session to log user out.
    IX. route "/register"
        search username from users table in datebase to check if user has registers. Also other checks to make sure all fields are entered. Register user by inserting username and password hash into users table in databse. Once register is sucessful, redirect to login page.

3. choice.db
    I. users table
        has id (primary key), username, and hash as table columns. Each column can't be null. It's a collection of user info.
    II. history table
        has id (primary key), user_id, artist, song_name, timestamp (default value current_timestamp) as table columns. Each column can't be null. User_id is referencing to id in users table. It's a collection of voting history.
    III. picks table
        has id (primary key), artist, song_name, vote as table columns. Each column can't be null. It counts how many times a song of an artist has been vote as the most favorite song.

4. templates
    html templates for each pages. layout.html is the common layout of the website.