from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process the information about each submission
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    # print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dicitonary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
        'writer': response_dict['by'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                        reverse=True)

submission_comments, submission_links, labels = [], [], []
for submission_dict in submission_dicts:
    # Use html to make x-labels clickable links to news articles
    submission_name = submission_dict['title']
    submission_url = submission_dict['hn_link']
    submission_link = f"<a href='{submission_url}'>{submission_name}</a>"

    # Build the label
    submitter = submission_dict['writer']
    label = f"{submitter}<br />{submission_name}"
    
    submission_comment = submission_dict['comments']
    

    submission_links.append(submission_link)
    submission_comments.append(submission_comment)
    labels.append(label)

# Make visualization
data = [{
    'type': 'bar',
    'x': submission_links,
    'y': submission_comments,
    'hovertext': labels
}]

my_layout = {
    'title': 'Most-ative newsfeeds on hacker-news based on comments',
    'xaxis': {'title': 'News articles'},
    'yaxis': {'title': 'Comments'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hackerrank_news.html')



