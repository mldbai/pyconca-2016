# Building a real-time image classification web app with Python and MLDB.ai

### [Pycon Canada 2016 Tutorial](https://2016.pycon.ca/fr/schedule/071-francois-maillet/)

> In this tutorial, we will build a real-time machine learning web app using Python and MLDB.ai. We will use MLDB's Tensorflow integration to use a deep learning model to embed images in a high dimensional conceptual space, and use that representation as features to do transfer learning. This will allow us to build a real-time image classification endpoint.

François Maillet - @mailletf - http://blog.francoismaillet.com


November 13, 15h10

## About

This repo contains the built webapp. Slides will be posted here after the tutorial.


### Installing the plugin

```python
from pymldb import Connection
mldb = Connection()

mldb.put("/v1/plugins/pycon", {
    "type": "python",
    "params": {
        "address": "git://github.com/mldbai/pycon-2016"
    }
})
```

You can then browse to `https://<host:port>/v1/plugins/pycon/routes/static/index.html` to access the UI.
