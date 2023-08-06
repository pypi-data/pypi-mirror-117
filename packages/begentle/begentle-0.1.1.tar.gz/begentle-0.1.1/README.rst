========
begentle
========
begentle is a package for detecting toxic language using 
the Perspective API (more info at `PerspectiveAPI.com <https://perspectiveapi.com/>`_).
Google already has a Python module for this, but I think it's 
too complex, so I created my own.

Getting Started
---------------
First you will need a Google Cloud project API key with
the Perspective API enabled. 

Follow these two tutorials:
| `Tutorial 1: Getting Started <https://developers.perspectiveapi.com/s/docs-get-started>`_
| `Tutorial 2: Enable the API <https://developers.perspectiveapi.com/s/docs-enable-the-api>`_

Once you have your API key install the package::

    pip install begentle

and use it like so::
    
    from begentle import CommentAnalyzer
    analyzer = CommentAnalyzer('YOUR_API_KEY')
    comment = 'You suck! I hate you, never come back.'
    print(analyzer.analyze(comment))

You should see something like 0.9543847.
This is a value between 0 and 1 representing toxicity.
Generally toxic phrases return a value above 0.9.
And that's it!