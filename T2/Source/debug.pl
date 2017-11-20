
:- module(deb, [
	what/0
]).
:- dynamic([
	what/0
]).
what :- 
	asserta(at(breeze,pos(1,3))),
	%trace,
	take_action.
:- use_module(main).
:- use_module(percepts).
:- use_module(actions).