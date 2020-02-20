|pypi|_
|build status|_
|pypi downloads|_
|license|_


About
=====

SlackerToo is a **fork** and continuation of `Slacker`_ library, a full-featured Python interface for the `Slack API
<https://api.slack.com/>`_.

Installation
============

.. code-block:: bash

    $ pip install slacker2

Examples
========
.. code-block:: python

    from slacker2 import Slacker

    slack = Slacker('<your-slack-api-token-goes-here>')

    # Send a message to #general channel
    slack.chat.post_message('#general', 'Hello fellow slackers!')

    # Get users list
    response = slack.users.list()
    users = response.body['members']

    # Upload a file
    slack.files.upload('hello.txt')

    # If you need to proxy the requests
    proxy_endpoint = 'http://myproxy:3128'
    slack = Slacker('<your-slack-api-token-goes-here>',
                    http_proxy=proxy_endpoint,
                    https_proxy=proxy_endpoint)

    # Advanced: Use `request.Session` for connection pooling (reuse)
    from requests.sessions import Session
    with Session() as session:
        slack = Slacker(token, session=session)
        slack.chat.post_message('#general', 'All these requests')
        slack.chat.post_message('#general', 'go through')
        slack.chat.post_message('#general', 'a single https connection')


Documentation
=============

https://api.slack.com/methods


.. |build status| image:: https://apushkarev.visualstudio.com/slacker2/_apis/build/status/slacker2-CI
.. _build status: https://apushkarev.visualstudio.com/slacker2/_build/latest?definitionId=2
.. |pypi downloads| image:: https://img.shields.io/pypi/dm/slacker2.svg
.. _pypi downloads: https://pypi.org/project/slacker2/
.. |pypi| image:: https://img.shields.io/pypi/v/Slacker2.svg
.. _pypi: https://pypi.python.org/pypi/slacker2/
.. |license| image:: https://img.shields.io/github/license/os/slacker.svg
.. _license: https://pypi.org/project/slacker2/
.. _Slacker: https://pypi.org/project/slacker