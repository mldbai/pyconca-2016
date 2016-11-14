# Building a real-time image classification web app with Python and MLDB.ai

### [Pycon Canada 2016 Tutorial](https://2016.pycon.ca/fr/schedule/071-francois-maillet/)

> In this tutorial, we will build a real-time machine learning web app using Python and MLDB.ai. We will use MLDB's Tensorflow integration to use a deep learning model to embed images in a high dimensional conceptual space, and use that representation as features to do transfer learning. This will allow us to build a real-time image classification endpoint.

François Maillet - @mailletf - http://blog.francoismaillet.com


November 13, 15h10

## About

This repo contains the built web app. The slides are available in the `talk` folder of the repository. Check back for a screen cast of the talk to be posted within 2 weeks.

For those who attended the talk, the glitch that caused the built plugin to fail to load is now fixed. The code below will work properly.


### Installing the plugin

```python
from pymldb import Connection
mldb = Connection()

mldb.put("/v1/plugins/pycon", {
    "type": "python",
    "params": {
        "address": "git://github.com/mldbai/pyconca-2016.git"
    }
})
```

You can then browse to `https://<host:port>/v1/plugins/pycon/routes/static/index.html` to access the UI.
