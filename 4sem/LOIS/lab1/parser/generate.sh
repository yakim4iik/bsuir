#!/bin/bash

java -jar antlr-4.12.0-complete.jar -Dlanguage=Go -no-visitor -package parser *.g4
