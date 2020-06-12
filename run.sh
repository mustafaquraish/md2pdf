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

sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
