"""
begentle is a package for detecting toxic
language using the Perspective API.
(more info at https://perspectiveapi.com).
Google already has a Python module for
this, but I think it's too complex, so
I created my own.
"""
__version__ = '0.1.1' # set version
__description__ = "A module for detecting text with profanity using Google's Perspective API."
__author__ = "Rahul Wavare <rahulrakida@gmail.com>"
from googleapiclient import discovery
import typing
import os

class CommentAnalyzer():
    """Comment analyzer class.

    Arguments:
    google_api_key -- A Google Cloud API key with the Perspective API enabled.
    """
    def __init__(self, google_api_key: str):
        self.client = discovery.build(
            "commentanalyzer",
            "v1alpha1",
            developerKey=google_api_key,
            discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            static_discovery=False
        )
    
    def analyze(self, comment: str) -> float:
        """Analyze a comment.

        Find a comment's TOXICITY value and return it.
        Returns a float from 0 to 1 representing toxicity.
        """
        request = {
            'comment': {'text': comment},
            'requestedAttributes': {'TOXICITY': {}}
        }
        response = self.client.comments().analyze(body=request).execute()
        toxicity = response['attributeScores']['TOXICITY']['summaryScore']['value']
        return toxicity
"""
client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False
)

def comment_toxicity(message: str):
    
    # Returns a tuple containing if the comment
    # is toxic, and a value from `0` to `1` representing
    # toxicity. Toxicity is defined by a value
    # above `0.9`.
    # Sample: `(True, 0.97173126)`
    
    request = {
        'comment': { 'text': message },
        'requestedAttributes': {'TOXICITY': {}}
    }

    response = client.comments().analyze(body=request).execute()
    toxicity = response['attributeScores']['TOXICITY']['summaryScore']['value']
    if toxicity >= 0.9:
        is_toxic = True
    else:
        is_toxic = False

    return (is_toxic, toxicity)
"""