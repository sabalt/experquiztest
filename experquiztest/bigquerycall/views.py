from django.shortcuts import render
from django.http import HttpResponse
from google.cloud import bigquery
import json



def index(request):
    return render(request, 'bigquerycall/index.html')

def licenses(request):
    if request.is_ajax():
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
        licenses = []
        totals = []
        for row in results:
            licenses.append(row.license)
            totals.append(row.total)
        context = {
            'licenses': licenses,
            'totals': totals
        }
        return HttpResponse(json.dumps(context),
            content_type='application/json')

    return render(request, 'index.html', {'user': ''})