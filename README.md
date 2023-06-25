# Content Aggregator
Content Aggregator built using Django. Runs on Django's ap-scheduler to fetch RSS feeds and consolidates all results into one site.

With so much content coming out online daily, it can be time consuming to go to multiple sites and sources to consume information about your favorite subjects. That's what I experienced, so I decided to kill two birds with one stone and learn how to make my own content aggregator.

Runs automatically using scheduler and updates every few minutes

## How To Run
1. Run `python manage.py migrate`
2. Run `python manage.py makemigrations`
3. Run `python manage.py startjobs`
4. Run `python manage.py runserver`