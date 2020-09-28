# NLP Chatbot

## About

This is my implementation of a basic NLP Chatbot, which was assigned as a homework problem for my course in Natural Language Processing.\n
Based on ELIZA, the Rogerian psychotherapist, (http://psych.fullerton.edu/mbirnbaum/psych101/Eliza.htm), the chatbot uses Regular Expressions to mimic back the input to the user.\n
It replaces all first person parts of speech to second person and vice versa,
however this was implemented without any grammatical analysis, just regex. Therefore,
the responses will not be perfect. The main problem it encounters so far is the ambiguity
of the pronoun "you" - this can either be the subject or the object of the sentence.\n
It uses a rule-based approach to solving this problem.\n
Additionally, I've implemented evaluation of basic mathematical expressions (addition, subtraction, multiplication, division). When the regex recognizes one of these phrases,
the output will respond as usual, but with the expression evaluated.

## Prerequisites

Python3 is required to run this program. There are no packages required to run this program, save for two libraries inside of Python Core. These are 'regex' and 'operator'.

## How to Install

Clone the repository and run the script as the main module. In the Terminal:

    git clone git@github.com:yuvaltimen/NLP_chatbot.git\n
    python3 chatbot.py
