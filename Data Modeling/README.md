# ETL pipeline and Data Modeling with PostgreSQL

<p align="left">
  Project in Data Engineer Nanodegree Course by Udacity
 </p>

<br><br>

## Project Introduction

<!-- Short description of the project -->

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming application. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of `JSON` logs on user activity on the application, as well as a directory with `JSON` meta-data on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. The role of this project is to create a database schema with fact and dimension tables and ETL pipeline for this analysis.

The goal is to model the data with Postgres and build an ETL pipeline using Python.

<br><br>

## Datasets

#### Song Dataset

The dataset is a subset of [Million Song Dataset](http://millionsongdataset.com/). Each file in the dataset is in JSON format and contains meta-data about a song and the artist of that song.

Sample :

```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

<br>
#### Log Dataset
Logs dataset containes log files, it was generated using [Event Simulator](https://github.com/Interana/eventsim).  The files are in JSON format and simulate activity logs from a music streaming application based on specified configurations.

Sample:

```
{"artist": null, "auth": "Logged In", "firstName": "Walter", "gender": "M", "itemInSession": 0, "lastName": "Frye", "length": null, "level": "free", "location": "San Francisco-Oakland-Hayward, CA", "method": "GET","page": "Home", "registration": 1540919166796.0, "sessionId": 38, "song": null, "status": 200, "ts": 1541105830796, "userAgent": "\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"", "userId": "39"}
```

<br><br>

## Database Schema Design

### Database Entity Relationship Diagram

In this project we used the Star Schema with Song Plays as a fact table. It contains all the metrics of the events (user actions). The dimension tables contain about the user, artist, songs and time.

The Star Schema is typically used for relational data modeling. If properly designed it allows to find the required information using the minimum number of joins in the queries.
<br><br>

## Project Structure

| Files / Folders  |                          Description                           |
| :--------------: | :------------------------------------------------------------: |
|    test.ipynb    |    Let you check if the database and tables work correctly     |
| create_tables.py |          Drops, creates the database and the tables.           |
|    etl.ipynb     | Transforms the data from JSON format and populates the tables. |
|      etl.py      | Transforms the data from JSON format and populates the tables. |
|  sql_queries.py  |             Contains all sql used in the project.              |
|       data       |        Folder with songs and logs data in JSON format.         |
|      images      |            Folder with images used on the project.             |
|    README.md     |  File with all instructions and descriptions of the project.   |

<br><br>

### Prerequisites

The prerequisites to run the program are:

- python with installed `psycopg2` and `pandas` libraries
- PostgreSQL

<br><br>

### How to run

1. Create the tables by

   ```
   python3 create_tables.py
   ```

2. Run ETL process by

   ```
   python3 etl.py
   ```

3. Executing `test.ipynb` you can check whether the data has been loaded into database properly

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
