from typing import List, NamedTuple

import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


class QuestionInfo(NamedTuple):
    question_text: str
    votes: int
    views: int


def get_question_info(url: str) -> List[QuestionInfo]:
    page_content = requests.get(url).text
    soup = BeautifulSoup(page_content, "html.parser")
    question_divs = soup.find_all(class_="question-summary")
    questions_info = list()
    for question in question_divs:
        question_text = "".join(question.find(
            class_="question-hyperlink").stripped_strings)
        votes = int("".join(question.find(
            class_="vote-count-post").stripped_strings))
        views = int(question.find(class_="views")[
            "title"].split()[0].replace(",", ""))
        questions_info.append(QuestionInfo(question_text, votes, views))
    return questions_info


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    questions = get_question_info(url)
    questions = [
        question for question in questions if question.views >= 1_000_000]
    return [(question.question_text, question.votes) for question in sorted(questions, key=lambda x: x.votes, reverse=True)]


if __name__ == "__main__":
    from pprint import pprint
    pprint(top_python_questions())
