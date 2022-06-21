# Amharic Sentiment Analysis - Hate Speech Detection Using Machine Learning

The scope of this project is limited to the presence or absence of hate 
speech on Amharic language Twitter posts. In this context, the term 'hate speech' 
refers to abusive or threatening statements or phrases that describe prejudice against 
a particular group in Ethiopia.

## Advisor

- Elefelious Getachew (Ph.D.)


## Members

- [Surafel Kindu](https://github.com/Surafeljava) - ATR/9237/10 - Section-1
- [Samia Abdella](https://github.com/Surafeljava) - ATR/3142/10 - Section-1
- [Daniel Tefera](https://github.com/Surafeljava) - ATR/1145/10 - Section-1
- [Eyob Maru](https://github.com/Surafeljava) - ATR/0121/10 - Section-1
- [Ahlam Muhdin](https://github.com/Surafeljava) - ATR/2923/10 - Section-3

## Amharic sentiment Analysis Backend

The Backend has provides the API Server which is developed using Django and postgresql. The final work is also deployed on heroku.

## How to run the backend server locally

To run this project on, start by cloning the [ASA Backend API Server Repository](https://github.com/danielteferadeti/Amharic_Sentiment_Analysis_Backend)

### Requirements before running the code

The backend server is developed using Django framework and postgresql as a tool. Before running this project make sure the following requirements are met on the machine:

* Download and install Python: [Python 3](https://www.python.org/downloads/)

* Install and prepare the pip and pip virtual environment. [pip environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

* Download and install Django framework: [Django Framework](https://www.djangoproject.com/download/)

* Download and Install Postgres: [Postgresql](https://www.postgresql.org/download/)

After installing the above requirements make the following adjustments to the cloned sourced code:

* Navigate to Amharic_Sentiment_Analysis/settings.py and move to the DATABASES section and fill the requirement of the postgresql database info accordingly.

* run django in pip environment

* Migrate all the database models to the database using the following command
```bash
  python manage.py migrate
```
```bash
  python manage.py makemigrations
```

* Run the django server using the following command

```bash
  python manage.py runserver
```

The runserver command will launch the django server on http://127.0.0.1:8000/



## This API Server is used by

The project Amharic Sentiment Analysis - Hate Speech Detection Using Machine Learning as API server for the web application.


## References
* Docs.djangoproject.com. 2022. Django documentation | Django documentation | Django. [online] Available at: <https://docs.djangoproject.com/en/4.0/> [Accessed 21 June 2022].

* Youtube.com. 2022. [online] Available at: <https://www.youtube.com/watch?v=rHux0gMZ3Eg> [Accessed 21 June 2022].

* Youtube.com. 2022. [online] Available at: <https://www.youtube.com/watch?v=rHux0gMZ3Eg> [Accessed 21 June 2022].

* Youtube.com. 2022. [online] Available at: <https://www.youtube.com/watch?v=rHux0gMZ3Eg> [Accessed 21 June 2022].



