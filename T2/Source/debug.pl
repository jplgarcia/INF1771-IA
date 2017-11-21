
:- module(deb, [
	what/0
]).
:- dynamic([
	what/0
]).
what :- 
	asserta(at(stench,pos(1,2))),
	asserta(at(monster(01),pos(1,3))),
	check_surrounding_and_current_position,
	trace,
	take_action.
:- use_module(main).
:- use_module(percepts).
:- use_module(actions).