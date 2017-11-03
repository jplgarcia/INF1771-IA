:- dynamic position/2.
:- dynamic facing/2.
position(1,1).
facing(1,0).
/
False_Maybe_True é como um booleano com 3 valores
room_is_edge(coordinate(X,Y),False_Maybe_True).
room_has_breeze(coordinate(X,Y),False_Maybe_True).
room_has_hole(coordinate(X,Y),False_Maybe_True).
room_has_stench(coordinate(X,Y),False_Maybe_True).
room_has_wumpus(coordinate(X,Y),False_Maybe_True).
room_has_shine(coordinate(X,Y),False_Maybe_True).
room_has_gold(coordinate(X,Y),False_Maybe_True).
EX.:
room_has_shine(coordinate(X,Y),False_Maybe_True) :-
	room_has_gold(coordinate(X,Y),False_Maybe_True).

room_has_stentch(coordinate(X,Y),false):-
	room_has_wumpus(coordinate(X-1,Y),false),
	room_has_wumpus(coordinate(X+1,Y),false),
	room_has_wumpus(coordinate(X,Y-1),false),
	room_has_wumpus(coordinate(X,Y+1),false).

room_has_stentch(coordinate(X,Y),maybe):-
	assert(room_has_wumpus(coordinate(X-1,Y),maybe)),
	assert(room_has_wumpus(coordinate(X+1,Y),maybe)),
	assert(room_has_wumpus(coordinate(X,Y-1),maybe)),
	assert(room_has_wumpus(coordinate(X,Y+1),maybe)).


/

step() :-
	position(Xaxis,Yaxis),
	facing(Xunit,Yunit),
	X is Xaxis+Xunit,
	Y is Yaxis+Yunit,
	move(X,Y),
	format("position(~a,~a)",[X,Y]).

move(X,Y) :-
	retract(position(_,_)),
	assert(position(X,Y)).

turn(right) :-
	facing(Xunit,Yunit),
	X is Yunit,
	Y is -Xunit,
	retract(facing(_,_)),
	assert(facing(X,Y)),
	format("facing(~a,~a)",[X,Y]).
	
turn(left) :-
	facing(Xunit,Yunit),
	X is -Yunit,
	Y is Xunit,
	retract(facing(_,_)),
	assert(facing(X,Y)),
	format("facing(~a,~a)",[X,Y]).

/turn(X) é para aceitar outras nomenclaturas para left e right/
turn(X) :-
	(
		(
			X==l;
			X==e;
			X==esquerda;
			X==cc;
			X==counter_clockwise),/cc = "counter clockwise"/
		turn(left),!/"!" é para não continuar a avaliação (como um return)/
	);
	(
		(
			X==r;
			X==d;
			X==direita;
			X==c;/c = "clockwise"/
			X==clockwise),
		turn(right),!
	).
