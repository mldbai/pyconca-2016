import json

# nice pymldb-style wrapper
mldb = mldb_wrapper.wrap(mldb)

mldb.log("Handling a route!!!")

def handlePredict():
    if len(mldb.plugin.rest_params.rest_params) != 1 or \
            mldb.plugin.rest_params.rest_params[0][0] != "url":
        return ("Bad format", 400)
    
    url = mldb.plugin.rest_params.rest_params[0][1]
    
    res = mldb.query("""
        SELECT * FROM transpose((
            SELECT brand_predictor({url: '%s'})[scores] as *
        ))
        ORDER BY result DESC
        LIMIT 1
    """ % url)
    
    mldb.log(res)
    
    return (res[1][0].replace('"', ''), 200)


# check if we're calling the right route
if mldb.plugin.rest_params.verb == "GET" and mldb.plugin.rest_params.remaining == "/py_predict":
    val, code = handlePredict()
    mldb.plugin.set_return(val, code)
    
