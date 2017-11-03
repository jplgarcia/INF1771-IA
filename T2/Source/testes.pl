:- dynamic position/2.
:- dynamic facing/2.
position(1,1).
facing(1,0).

step() :-
	position(Xaxis,Yaxis),
	facing(Xunit,Yunit),
	X is Xaxis+Xunit,
	Y is Yaxis+Yunit,
	retract(position(_,_)),
	assert(position(X,Y)),
	format("position(~a,~a)",[X,Y]).
	

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
