import requests
import time
import pytest
import csv

from pytest_benchmark.plugin import benchmark

strings = ["hello world","this_is_awesome:)","Joe Biden won the election.","ECE444 has a final this year."]
api_url = "http://ece444-final-environment-env.eba-iasmjqbh.ca-central-1.elasticbeanstalk.com/"

def test_strings_expected_response():
    for index,string in enumerate(strings):
        new_string = string.replace(" ", "%20")
        url = api_url + new_string
        response = requests.get(url)
        assert response.status_code == 200
        if index < 2:
            assert response.text == 'FAKE'
        else:
            assert response.text == 'REAL'

def test_one_string(string, writer):
    url = api_url + string.replace(" ", "%20")
    old_time = time.time()
    response = requests.get(url)
    new_time = time.time()
    writer.writerow([string, new_time - old_time, response.status_code, response.text])

@pytest.mark.benchmark(
    min_rounds=100
)
def test_string_1_100_times(benchmark):
    with open('results1.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["test string", "timestamp", "status code", "response"])
        benchmark(test_one_string, strings[0], writer)

@pytest.mark.benchmark(
    min_rounds=100
)
def test_string_2_100_times(benchmark):
    with open('results2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["test string", "timestamp", "status code", "response"])
        benchmark(test_one_string, strings[1], writer)

@pytest.mark.benchmark(
    min_rounds=100
)
def test_string_3_100_times(benchmark):
    with open('results3.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["test string", "timestamp", "status code", "response"])
        benchmark(test_one_string, strings[2], writer)

@pytest.mark.benchmark(
    min_rounds=100
)
def test_string_4_100_times(benchmark):
    with open('results4.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["test string", "timestamp", "status code", "response"])
        benchmark(test_one_string, strings[3], writer)


