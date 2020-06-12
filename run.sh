#!/bin/sh

read -r -d '' var << EOF
<!DOCTYPE html>
<html>
    <head>
        <title>
            API Test
        </title>
    </head>
    <body>
        <h1>
            THIS WEBSITE IS FOR AN API!!!
        </h1>
        Endpoint is GET /api?md=MARKDOWNTEXT
    </body>
</html>
EOF

echo $var > index.html