#!/bin/bash

# set variables
url="http://localhost:8000/predict"
age=60
income=40
score=90
male=1
# execute POST request using curl
curl -X POST \
     -H "Content-Type: application/json" \
     -d "{\"male\": $male, \"age\": $age, \"income\": $income, \"score\": $score}" \
     $url
