# Jak pisać duże programy komputerowe?

Dr. Magdalena Rother and Dr. Kristian Rother

## Treść:
Nauczyłaś/eś się już pisać proste programy.
Jak zatem kontynuwać i pisać wysokiej jakości programy, które mają więcej niż 100, 1000, lub 10000 linii kodu?
Na tych zajęciach dwoje doświadczonych programistów, umożliwi Tobie wypróbowanie trzech podstawowych technik, używanych praktycznie przez wszytkie większe firy zajmujące się rozwojem oprogramowania na świecie. 

## Purpose

These are materials to conduct a 2-hour tutorial on software development. The main purpose is to give participants who started to learn programming an idea of what professional software development is.

## Target Audience

High School students with a little programming experience in any programming language.

## Core Concepts

* User Stories
* Version Control
* Automated Testing

## Learning Goals

Participants apply basic software development techniques within 90'.

* Participants develop a User Story
* Participants check out code using a version control System
* Participants add code to a version control system
* Participants run automated test code
* Participants write a test on their own
* Participants write code to make a test pass

## Prerequisites

* whiteboard
* git installed on computers
* Python installed on computers
* text editor (e.g. IDLE)


## Lesson Plan

| phase | activity | time |
|-------|----------|------|
| warm-up | welcome, introduce yourself | 5' |
| warm-up | why is writing a big program difficult? | 4' |
| new content | explain concept map  |  5' |
| apply       | exercise : develop User Story  | 10' |
| apply       | exercises: version control    | 20' |
| apply       | exercises: automated testing  | 20' |
| wrap-up     | summary           |  5' |
| wrap-up     | Q & A             | 10' |

## How to conduct this teaching unit?

### 1. Warm-up

We started the course by introducing us and briefly explaining a sample project we have been working on. We explained the main difference between *our* programs and the ones written by the participants so far: *they are big programs*.

We asked participants why they think writing a big program was difficult. They found most of the answers we could think of.

### 2. The concept map

Here we introduce the structure of the course: 3 concrete engineering techniques that stand for all the others that are there. We made the 3 techniques visible as cards on a whiteboard. The main purpose was to give participants something they could remember easily.

You may consider arranging them in a circle (planning, coding, testing) if you want to put an emphasis on iterative development. We wanted to keep things more general and didn't bother doing so.

### 3. The User Story

We started with a simple description on the white board
 
    "generate emoticons"

and asked the participants whether they could start programming. We asked why not. Again, they came up with reasonable questions about input etc. We took the role of a client and helped to formulate a more precise description. Eventually, the User Story converged to something similar to:

    "as the producer of a chat software, 
    I want words in the text to be exchanged by emoticons
    written as ASCII characters, 
    so that chat users automatically see emoticons
    in their messages."

### 4. Using a version control system

At this point, we turned on computers and went through the exercises using `git`. The exercises were interspersed with a few brief explanations what a version control system is and what it is good for.

### 5. Using automated tests

After a break, we continued with the exercises using the Python `unittest` module. The exercises were interspersed with a few brief explanations what a version control system is and what it is good for.

### 6. Wrap-up

In the end we had a short Q & A round with questions related to work as a software developer in general.

## License

(c) 2016 Magdalena Rother and Kristian Rother

The material presented here is distributed under the conditions of the Creative Commons Attribution Share-alike License 4.0
