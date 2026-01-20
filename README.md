<h2>Messenger_API</h2>
<br>
<div>
<b>This project provides an API for:</b>
<ul>
<li>Creating chats and sending messages between users.</li>
<li>Wide functionality for operating and performing users' data.</li>
<li>Flexible deployment in various environments.</li>
</ul>
</div>
<br>
:eight_spoked_asterisk:<b>Tech Stack</b>:eight_spoked_asterisk:<br>
FastAPI, SQLAlchemy, Alembic, PostgreSQL, Docker, Docker-Compose, Pytest
<br><br>
:eight_pointed_black_star:<b>Essential dependencies</b>:eight_pointed_black_star:<br>
Python 3.10+, Docker 28+ 
<hr> 
<div>
<h3>Docker Deploy</h3>
Open a terminal and run the following command:

```commandline
git clone https://github.com/735Andrew/Messenger_API
```
<br>
Create a <b>.env</b> file in the root directory with the following variables: <br>
<b>/Messenger_API/.env</b>

```commandline 
POSTGRES_USER = <USER_VARIABLE>
POSTGRES_PASSWORD = <PASSWORD_VARIABLE>
POSTGRES_DB = <DB_VARIABLE>
DATABASE_URL = postgresql+asyncpg://<USER_VARIABLE>:<PASSWORD_VARIABLE>@db:5432/<DB_VARIABLE>
```
<br>
Open a terminal in the root directory and execute this command to build the Docker container:

```commandline
docker-compose up -d 
```
</div>
