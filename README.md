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


#### Code explanation:

1. helper.py
    This python code contains function track_search and login_required. <br />
    login_required makes sure the user has logged in when using the web app. <br />
    track_search function receives input of artist name and search it in Spotify API. It goes through every search result and append the song name to a list called track, and return the list.


2. application.py
    This python code uses SQLites, Flask to build the web app. <br />
    
    I. route "/":  <br />
        Execute SQL statement to get the result of aritist and songs that the user voted for from the database. Send the result to index.html to display. <br />
        
    II. route "/search": <br />
        If no artist name entered or incorrect artist name entered, error message will come up. Else, get the artist name that user enters and search using track_search function in helper.py .<br />
        Also look up the artist name and user from history table in database to see if the user voted for this artist before, if yes, send the search result to change.html, and if not, send the result to vote.html . <br />
        
    III. route "/vote":<br />
        Vote your most favorite song of the artist you searched for. Record the vote to history table in database and add it to total count of how many times this song was voted by the community in picks table in database. <br />
        I used sqlite3 statement: begin transaction...commit.. roll back to make sure statements are completed as a whole. <br />
        Once the vote is completed successfully, it will redirect to route "/", which display all votes you have made. <br />
        
    IV. route "/change" <br />
        To change your vote of the most favorite song. Once you submit your new vote. It will reverse the cout of total votes of your prior favorite song in picks table, and update your voting history for corresponding artist. <br />
        Then your vote to new favorite song will be added to to total count of how many times this song was voted by the community in picks table in database. <br />
        I used sqlite3 statement: begin transaction...commit.. roll back to make sure statements are completed as a whole. <br />
        Once the vote is completed successfully, it will redirect to route "/", which display all votes you have made. <br />
        
    V. route "/rank" <br />
        Look up the most voted song of artists you have voted from picks table in databse, in order to show the most popular song of artists you have voted for. Send the info to rank.html, which also have a button to let you search the song in Youtube and Spotify. <br />
        
    VI. route "/history" <br />
        Look up your voting history from history table in database. <br />
        
    VII. route "/login" <br />
        Implement checks to see if username and password both has been entered. and compare password to result looked up from users table in database to help user login. Once login is successful, will redirect to route "/". <br />
        
    VIII. route "/logout" <br />
        Clear session to log user out. <br />
        
    IX. route "/register" <br />
        Search username from users table in datebase to check if user has registers. Also other checks to make sure all fields are entered. Register user by inserting username and password hash into users table in databse. Once register is sucessful, redirect to login page. <br />


3. choice.db <br />
    I. users table <br />
        Has id (primary key), username, and hash as table columns. Each column can't be null. It's a collection of user info. <br />
        
    II. history table <br />
        Has id (primary key), user_id, artist, song_name, timestamp (default value current_timestamp) as table columns. Each column can't be null. User_id is referencing to id in users table. It's a collection of voting history. <br />
        
    III. picks table <br />
        Has id (primary key), artist, song_name, vote as table columns. Each column can't be null. It counts how many times a song of an artist has been vote as the most favorite song. <br />


4. templates <br />
    Html templates for each pages. layout.html is the common layout of the website. <br />
