#!/bin/bash

# set variables
url="http://localhost:8000/predict"
age=66
income=13
score=21
male=0
# execute POST request using curl
curl -X POST \
     -H "Content-Type: application/json" \
     -d "{\"male\": $male, \"age\": $age, \"income\": $income, \"score\": $score}" \
     $url
