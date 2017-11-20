
:- module(deb, [
	what/0
]).
:- dynamic([
	what/0
]).
what :- 
	asserta(at(breeze,pos(2,1))) .
:- use_module(main).
:- use_module(percepts).
:- use_module(actions).