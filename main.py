import os

# nice pymldb-style wrapper
mldb = mldb_wrapper.wrap(mldb)

mldb.log("Hello world!")

mldb.plugin.serve_static_folder("static", "static")


mldb.put('/v1/functions/inception', 
         {
            "type": 'tensorflow.graph',
            "params": {
                "modelFileUrl": 'archive+'+
                'http://public.mldb.ai/models/inception_dec_2015.zip'+
                '#tensorflow_inception_graph.pb',
                "inputs": 'fetcher(url)[content] AS "DecodeJpeg/contents"',
                "outputs": "pool_3"
             }
         })


mldb.put("/v1/functions/scorer", {
    "type": "classifier",
    "params": {
        "modelFileUrl": "file://" + os.path.join(mldb.plugin.get_plugin_dir(), "car_brand_cls.cls")
    }
})

mldb.log(mldb.put("/v1/functions/brand_predictor", {
    "type": "sql.expression",
    "params": {
        "expression": """
            scorer(
                {
                    features: inception({url})
                }) as *
        """
    }
}))


mldb.log("Plugin ready!")