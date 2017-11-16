%------------------------------------------------%
% Module: actions as acts                          %
%------------------------------------------------%

%------------------------------------------------%
% Definitions                                    %
%------------------------------------------------%
:- module(acts,  [
                take_action/7
                    ]).

:- use_module(main).
:- use_module(percepts).

:- dynamic([
              take_action/7
                  ]).

pick_gold( POS ) :-
	at(gold, POS ),
	adjust_score(1000),
	retract(at(gold, POS )),
	retract(at(shine, POS )).

%generic take_action
take_action() :-
	senses( _,_,_,_,_,Impact,Scream ),
	Shine = no,Breeze = no,Stench = no,
	at(agent,pos( X,Y )),
	(
		(
			at(gold, pos( X,Y )),
			Shine = shine
		);
		(
			at(breeze, pos( X,Y )),
			(Breeze = breeze)
		);
		(
			at(stench, pos( X,Y )),
			Stench = stench
		)
	),
	take_action( X, Y, Stench, Breeze, Shine, Impact, Scream ),
	retract(senses( _, _, _, _, _, _, _ )),
	asserta(senses( X, Y, Stench, Breeze, Shine, no, no)) .

take_action( X, Y,no, no, no, no, no ) :-
	step().

%%Decides to pick up gold if seen
take_action( X, Y, Stench, Breeze, shine, Impact, Scream ) :-
	pick_gold(pos( X,Y ) ).

%%Marks a position as a wall
take_action( X, Y, Stench, Breeze, Shine, impact, Scream ) :-
	agentfacing( DX,DY ),
	NX is X+DX,NY is Y+DY,
	(
		(
			at(wall,pos( NX,NY )),!
		);
		(
			assertz(at(wall,pos( NX,NY ))),!
		)
	) .
%%Treats monster death
take_action( X, Y, Stench, Breeze, Shine, Impact, scream ) :-
	agentfacing( DX,DY ),
	NX is X+DX,NY is Y+DY,
	kill_monster( pos( NX,NY )),!.

turn_to( DXIR,DYIR ) :-
	(
		agentfacing(DXIR,DYIR ),!
	);
	(
		agentfacing(-DYIR,DXIR ),
		turn(left),!
	);
	(
		agentfacing(DYIR,-DXIR ),
		turn(right),!
	);
	(
		agentfacing(-DXIR,-DYIR ),
		turn(right),
		turn(right),!
	).
%%Decides wheter to step or shoot if smelled stench; prefers to walk to a safe place over steping/shooting an unsafe place
take_action( X, Y, stench, Breeze, Shine, Impact, Scream ) :-
	get_safe_adjacent_list(_ , Position, [Safe_Head|Safe_Tail ] ),
	get_safe_adjacent_list(_ , Position, [Unsafe_Head|Unsafe_Tail ] ),
	(
		%%CASE no safe space
		length([Safe_Head|Safe_Tail ], 0),
		(
			(	%%CASE PotentialDanger then step
				at(PotentialDanger,Unsafe_Head ),
				pos( XU,YU ) = Unsafe_Head,
				DXIR = XU-X, DYIR = YU-Y,
				turn_to( DXIR,DYIR ),
				step(),!
			);
			(	%%CASE RealDanger
				at(RealDanger,Unsafe_Head ),
				(
					(
						%%If has ammo then shoot
						ammo( QTD ),
						\+ QTD < 1,
						at(monster(_),Unsafe_Head ),
						pos( XU,YU ) = Unsafe_Head,
						DXIR = XU-X, DYIR = YU-Y,
						turn_to( DXIR,DYIR ),
						shoot(),!
					)/**;
					(%%Has no ammo
						%%Q FAREMOS SE N TIVER MUNIÇÃO? #EDITING
					)*/
				)
			)
		),!
	);
	(	%%CASE Safe then Step
		pos( XU,YU ) = Safe_Head,
		DXIR = XU-X, DYIR = YU-Y,
		turn_to( DXIR,DYIR ),
		step(),!
	),! .

%%Decides wheter to step  if felt breeze; prefers to walk to a safe place over steping to an unsafe place
take_action( X, Y, Stench, breeze, Shine, Impact, Scream ) :-
	get_safe_adjacent_list(_ , Position, [Safe_Head|Safe_Tail ] ),
	get_safe_adjacent_list(_ , Position, [Unsafe_Head|Unsafe_Tail ] ),
	(
		%%CASE no safe space
		length([Safe_Head|Safe_Tail ], 0),
		(
			at(PotentialDanger,Unsafe_Head ),
			pos( XU,YU ) = Unsafe_Head,
			DXIR = XU-X, DYIR = YU-Y,
			turn_to( DXIR,DYIR ),
			step(),!
		),!
	);
	(	%%CASE Safe then Step
		pos( XU,YU ) = Safe_Head,
		DXIR = XU-X, DYIR = YU-Y,
		turn_to( DXIR,DYIR ),
		step(),!
	),! .
