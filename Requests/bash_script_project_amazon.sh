#!/bin/bash

python ~/Project/public-amazon-crawler/amazon.py
gdrive upload -r ~/Project/public-amazon-crawler/results

exit