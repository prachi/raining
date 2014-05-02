curl "http://0.0.0.0/count_now?pk=url1&dimensions=\{\"amazon\":\{\"music\":\"beyonce\"\}\}&metrics=\{\"hits\":1\}"
curl "http://0.0.0.0/count_now?pk=url1&dimensions=\{\"amazon\":\{\"music\":\"gaga\"\}\}&metrics=\{\"hits\":2\}"
curl "http://0.0.0.0/count_now?pk=url1&dimensions=\{\"amazon\":\{\"books\":\"beyonce\"\}\}&metrics=\{\"hits\":5\}"
curl "http://0.0.0.0/count_now?pk=url1&dimensions=\{\"amazon\":\{\"books\":\"gaga\"\}\}&metrics=\{\"hits\":12\}"
curl "http://0.0.0.0/count_now?pk=url1&dimensions=\{\"bing\":\{\"books\":\"beyonce\"\}\}&metrics=\{\"hits\":100\}"
echo 'done'
echo 'totals'
curl "http://0.0.0.0/totals?pk=url1&dimensions=\{\"amazon\":\{\"music\":\"beyonce\"\}\}" | python -mjson.tool