#!/bin/bash

TOKEN=1234
BASE_URL=http://bestoon.ir

curl --data "token=$TOKEN&amount=$1&text=$2" $BASE_URL/submit/income/
