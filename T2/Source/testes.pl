:- dynamic position/2.
:- dynamic facing/2.
position(1,1) .
facing(1,0) .

%% /**
action_weight(action(grab),1000) .
action_weight(action(pitfall),-1000) .
action_weight(action(die),-1000) .
action_weight(action(shoot),-10) .
action_weight(action( X ),-1) :-
	X \= grab,
	X \= pitfall,
	X \= die,
	X \= shoot,
	X \= take_damage .

 
/** 
	Garantem a integridade do conhecimento:
		se já sabemos q algo é verdade ou não, não sobreescrevemos com um maybe.
		também fica de olho em paradoxos (true E false), mas isso pode dificultar se, quando matarmos um wumpus, o fedor desaparecer.
*/
%% /** 
enter_room_has_breeze(coordinate ( X,Y ) , K )) :-
	room_has_breeze ( coordinate( X, Y ), Known ),
	(
		(
			Known == maybe,
			\+ K == maybe
		),
		retract ( room_has_breeze ( coordinate( X, Y ), _ ) ),
		assertz  ( room_has_breeze ( coordinate( X, Y ), K ) ),
		!
	);
	(
		(
			\+ Known == maybe,
			\+ K == maybe,
			K == Known
		),
		format ("Paradoxo: brisa no quarto [~a,~a]", X , Y ),
		!
	).
	
enter_room_has_pit(coordinate ( X,Y ) , K )) :-
	room_has_pit ( coordinate( X, Y ), Known ),
	(
		(
			Known == maybe,
			\+ K == maybe
		),
		retract ( room_has_pit ( coordinate( X, Y ), _ ) ),
		assertz  ( room_has_pit ( coordinate( X, Y ), K ) ),
		!
	);
	(
		(
			\+ Known == maybe,
			\+ K == maybe,
			K == Known
		),
		format ("Paradoxo: poço no quarto [~a,~a]", X , Y ),
		!
	).
	
enter_room_has_stench(coordinate ( X,Y ) , K )) :-
	room_has_stench ( coordinate( X, Y ), Known ),
	(
		(
			Known == maybe,
			\+ K == maybe
		),
		retract ( room_has_stench ( coordinate( X, Y ), _ ) ),
		assertz  ( room_has_stench ( coordinate( X, Y ), K ) ),
		!
	);
	(
		(
			\+ Known == maybe,
			\+ K == maybe,
			K == Known
		),
		format ("Paradoxo: fedor no quarto [~a,~a]", X , Y ),
		!
	).
	
enter_room_has_wumpus(coordinate ( X,Y ) , K )) :-
	room_has_wumpus ( coordinate( X, Y ), Known ),
	(
		(
			Known == maybe,
			\+ K == maybe
		),
		retract ( room_has_wumpus ( coordinate( X, Y ), _ ) ),
		assertz  ( room_has_wumpus ( coordinate( X, Y ), K ) ),
		!
	);
	(
		(
			\+ Known == maybe,
			\+ K == maybe,
			K == Known
		),
		format ("Paradoxo: wumpus no quarto [~a,~a]", X , Y ),
		!
	).
	
enter_room_has_shine(coordinate ( X,Y ) , K )) :-
	room_has_shine ( coordinate( X, Y ), Known ),
	(
		(
			Known == maybe,
			\+ K == maybe
		),
		retract ( room_has_shine ( coordinate( X, Y ), _ ) ),
		assertz  ( room_has_shine ( coordinate( X, Y ), K ) ),
		!
	);
	(
		(
			\+ Known == maybe,
			\+ K == maybe,
			K == Known
		),
		format ("Paradoxo: brilho no quarto [~a,~a]", X , Y ),
		!
	).
	
enter_room_has_gold(coordinate ( X,Y ) , K )) :-
	room_has_gold ( coordinate( X, Y ), Known ),
	(
		(
			Known == maybe,
			\+ K == maybe
		),
		retract ( room_has_gold ( coordinate( X, Y ), _ ) ),
		assertz  ( room_has_gold ( coordinate( X, Y ), K ) ),
		!
	);
	(
		(
			\+ Known == maybe,
			\+ K == maybe,
			K == Known
		),
		format ("Paradoxo: ouro no quarto [~a,~a]", X , Y ),
		!
	).
%% */
/**
	Regras básicas
*/
%% False_Maybe_True é como um booleano com 3 valores
room_is_edge(coordinate( X,Y ),true) :-
	enter_room_has_breeze (room_has_breeze(coordinate( X,Y ),false)),
	enter_room_has_pit (room_has_pit(coordinate( X,Y ),false)),
	enter_room_has_stench (room_has_stentch(coordinate( X,Y ),false)),
	enter_room_has_wumpus (room_has_wumpus(coordinate( X,Y ),false)),
	enter_room_has_shine (room_has_shine(coordinate( X,Y ),false)),
	enter_room_has_gold (room_has_gold(coordinate( X,Y ),false)).
	
room_has_breeze(coordinate( X,Y ),False_Maybe_True ).
room_has_breeze(coordinate( X,Y ),false):-
	enter_room_has_pit (room_has_pit(coordinate( X-1,Y ),false),
	enter_room_has_pit (room_has_pit(coordinate( X+1,Y ),false),
	enter_room_has_pit (room_has_pit(coordinate( X,Y-1),false),
	enter_room_has_pit (room_has_pit(coordinate( X,Y+1 ),false).
	
room_has_pit(coordinate( X,Y ),False_Maybe_True ).
room_has_pit(coordinate( X,Y ),true):-
	enter_room_has_breeze (room_has_breeze(coordinate( X-1,Y ),true),
	enter_room_has_breeze (room_has_breeze(coordinate( X+1,Y ),true),
	enter_room_has_breeze (room_has_breeze(coordinate( X,Y-1),true),
	enter_room_has_breeze (room_has_breeze(coordinate( X,Y+1 ),true).

room_has_stentch(coordinate( X,Y ),False_Maybe_True ).
room_has_stentch(coordinate( X,Y ),false):-
	enter_room_has_wumpus (room_has_wumpus(coordinate( X-1,Y ),false),
	enter_room_has_wumpus (room_has_wumpus(coordinate( X+1,Y ),false),
	enter_room_has_wumpus (room_has_wumpus(coordinate( X,Y-1 ),false),
	enter_room_has_wumpus (room_has_wumpus(coordinate( X,Y+1 ),false).
room_has_stentch(coordinate( X,Y ),maybe):-
	enter_room_has_wumpus (room_has_wumpus(coordinate( X-1,Y ),maybe)),
	enter_room_has_wumpus (room_has_wumpus(coordinate( X+1,Y ),maybe)),
	enter_room_has_wumpus (room_has_wumpus(coordinate( X,Y-1 ),maybe)),
	enter_room_has_wumpus (room_has_wumpus(coordinate( X,Y+1 ),maybe)).
	
room_has_wumpus(coordinate( X,Y ),False_Maybe_True ).
room_has_wumpus(coordinate( X,Y ),true):-
	enter_room_has_stentch (room_has_stentch(coordinate( X-1,Y ),true)),
	enter_room_has_stentch (room_has_stentch(coordinate( X+1,Y ),true)),
	enter_room_has_stentch (room_has_stentch(coordinate( X,Y-1 ),true)),
	enter_room_has_stentch (room_has_stentch(coordinate( X,Y+1 ),true)).

room_has_shine(coordinate( X,Y ),False_Maybe_True ).

room_has_shine(coordinate( X,Y ),False_Maybe_True ) :-
	enter_room_has_gold (room_has_gold(coordinate( X,Y ),False_Maybe_True ).
room_has_gold(coordinate( X,Y ),False_Maybe_True ).



%% */


step() :-
	position( Xaxis,Yaxis ),
	facing( Xunit,Yunit ),
	X is Xaxis + Xunit,
	Y is Yaxis + Yunit,
	move( X,Y ),
	format("position(~a,~a)",[ X,Y ]).

move( X,Y ) :-
	retract (position( _,_ ) ),
	assertz (position( X,Y )).

turn(right) :-
	facing( Xunit,Yunit ),
	X is Yunit,
	Y is -Xunit,
	retract (facing( _,_ )),
	assertz (facing( X,Y )),
	format("facing(~a,~a)",[ X,Y ]).
	
turn(left) :-
	facing( Xunit,Yunit ),
	X is - Yunit,
	Y is Xunit,
	retract (facing( _,_ )),
	assertz (facing( X,Y )),
	format("facing(~a,~a)",[ X,Y ]).

%%	turn( X) é para aceitar outras nomenclaturas para left e right
turn( X ) :-
	(
		(
			X == l;
			X == e;
			X == esquerda;
			X == cc;
			X == counter_clockwise),	%% cc = "counter clockwise"
		turn(left),!				%% "!" é para não continuar a avaliação (como um return)
	);
	(
		(
			X == r;
			X == d;
			X == direita;
			X == c;					%% c = "clockwise"
			X == clockwise),
		turn(right),!
	).
