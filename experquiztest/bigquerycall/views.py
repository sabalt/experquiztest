from django.shortcuts import render
from django.http import HttpResponse
from google.cloud import bigquery



def index(request):
    client = bigquery.Client()
    query = (
    'SELECT licenses.license as license,'
    'count(*) as total '
    'FROM `bigquery-public-data.github_repos.sample_repos` as repo inner join `bigquery-public-data.github_repos.licenses` as licenses on repo.repo_name = licenses.repo_name '
    'GROUP BY license '
    'order by total desc '
    'LIMIT 5'
    )
    results = client.query(query)
    for row in results:
        print("{} : {} views".format(row.license, row.total))
    return render(request, 'bigquerycall/index.html')