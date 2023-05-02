#!/bin/bash
# Takes in a URL, sends a GET request to the URL, displays the body of the response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
