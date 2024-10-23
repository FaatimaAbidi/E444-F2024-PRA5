import requests
import time
import matplotlib.pyplot as plt
import csv

strings = ["hello world","this_is_awesome:)","Joe Biden won the election.","ECE444 has a final this year."]
api_url = "http://ece444-final-environment-env.eba-iasmjqbh.ca-central-1.elasticbeanstalk.com/"

def test_100():
  with open('results.csv', 'w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(["test string", "iteration", "timestamp", "status code", "response"])
    for index, string in enumerate(strings):
      new_str = string.replace(" ", "%20")
      results = []
      for i in range(100):
        url = api_url + new_str
        response = requests.get(url)
        csvWriter.writerow([new_str, i, time.time(), response.status_code, response.text])
        results.append(response.text)
      plt.plot(results)
      plt.xlabel("Iteration")
      plt.ylabel("Prediction Returned by API")
      plt.title("Results for test of string: " + string)
      plt.show()

test_100()