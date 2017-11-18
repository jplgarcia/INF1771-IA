%------------------------------------------------%
% Module: actions as acts                          %
%------------------------------------------------%

%------------------------------------------------%
% Definitions                                    %
%------------------------------------------------%
:- module(acts,  [
                take_action/7,
				take_action/0
                    ]).

:- use_module(main).
:- use_module(percepts).

:- dynamic([
              take_action/7,
				take_action/0
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
			Breeze = breeze
		);
		(
			at(stench, pos( X,Y )),
			Stench = stench
		);true
	),
	(
		(
			agentfacing( DXIR,DYIR ),
			at(wall, pos( X+DXIR,Y+DYIR )),
			(
				(	
					%%Tem parede à esquerda, vira pra direita
					at(wall, pos( X-DYIR,Y+DXIR )),
					turn(r)
				);
				(
					%%Tem parede à direita, vira pra esquerda
					at(wall, pos( X+DYIR,Y-DXIR )),
					turn(l)
				)
			)
		);true
	),
	take_action( X, Y, Stench, Breeze, Shine, Impact, Scream ),
	retract(senses( _, _, _, _, _, _, _ )),
	asserta(senses( X, Y, Stench, Breeze, Shine, no, no)) .

take_action( _, _,no, no, no, no, no ) :-
	step().

%%Decides to pick up gold if seen
take_action( X, Y, _, _, shine, _, _ ) :-
	pick_gold(pos( X,Y ) ).

%%Marks a position as a wall
take_action( X, Y, _, _, _, impact, _ ) :-
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
take_action( X, Y, _, _, _, _, scream ) :-
	agentfacing( DX,DY ),
	NX is X+DX,NY is Y+DY,
	kill_monster( pos( NX,NY )),!.


%%Decides wheter to step or shoot if smelled stench; prefers to walk to a safe place over steping/shooting an unsafe place
take_action( X, Y, stench, _, _, _, _ ) :-
	get_safe_adjacent_list(_ , pos( X,Y ), [Safe_Head|Safe_Tail ] ),
	get_safe_adjacent_list(_ , pos( X,Y ), [Unsafe_Head|Unsafe_Tail ] ),
	(
		%%CASE no safe space
		length([Safe_Head|Safe_Tail ], 0),
		(
			(	%%CASE PotentialDanger then step
				at( potential_monster,Unsafe_Head ),
				pos( XU,YU ) = Unsafe_Head,
				DXIR = XU-X, DYIR = YU-Y,
				turn_to( DXIR,DYIR ),
				step(),!
			);
			(	%%CASE RealDanger
				at(realMonster,Unsafe_Head ),
				(
					(
						%%If has ammo then shoot
						ammo( QTD ),
						\+ QTD < 1,
						pos( XU,YU ) = Unsafe_Head,
						DXIR = XU-X, DYIR = YU-Y,
						turn_to( DXIR,DYIR ),
						shoot(),!
					);
					(	%%Has no ammo
						%% If there is no monster, go there
						(
							[Unsafe_Head|Unsafe_Tail ] = Unsafe_Tail,
							\+at(realMonster,Unsafe_Head ),
							run_from_monster(X,Y,Unsafe_Head ),!
						);
						(
							[Unsafe_Head|Unsafe_Tail ] = Unsafe_Tail,
							\+at(realMonster,Unsafe_Head ),
							run_from_monster(X,Y,Unsafe_Head ),!
						);
						(
							[Unsafe_Head|Unsafe_Tail ] = Unsafe_Tail,
							\+at(realMonster,Unsafe_Head ),
							run_from_monster(X,Y,Unsafe_Head ),!
						)
					)
				)
			)
		),!
	);
	(	%%CASE Safe then Step to should_visit
		get_all_should_visit( _,pos( X,Y ),Should_List ),
		(
			(
				\+ lenght( Should_List,0 ),
				[ Should_Head|Should_Tail ] = Should_List,
				Where_to = Should_Head
			);
			(
				lenght( Should_List,0 ),
				Where_to = Safe_Head
			)
		),
		pos( XU,YU ) = Where_to,
		DXIR = XU-X, DYIR = YU-Y,
		turn_to( DXIR,DYIR ),
		step(),!
	),! .

%%Decides wheter to step  if felt breeze; prefers to walk to a safe place over steping to an unsafe place
take_action( X, Y, _, breeze, _, _, _ ) :-
	get_safe_adjacent_list(_ , pos( X,Y ), [ Safe_Head|Safe_Tail ] ),
	get_safe_adjacent_list(_ , pos( X,Y ), [Unsafe_Head|_ ] ),
	(
		%%CASE no safe space
		length([Safe_Head|Safe_Tail ], 0),
		(
			at(potential_hole,Unsafe_Head ),
			pos( XU,YU ) = Unsafe_Head,
			DXIR = XU-X, DYIR = YU-Y,
			turn_to( DXIR,DYIR ),
			step(),!
		),!
	);
	(	%%CASE Safe then Step to should_visit
		get_all_should_visit( _,pos( X,Y ),Should_List ),
		(
			(
				\+ lenght( Should_List,0 ),
				[ Should_Head|Should_Tail ] = Should_List,
				Where_to = Should_Head
			);
			(
				lenght( Should_List,0 ),
				Where_to = Safe_Head
			)
		),
		pos( XU,YU ) = Where_to,
		DXIR = XU-X, DYIR = YU-Y,
		turn_to( DXIR,DYIR ),
		step(),!
	),! .
	
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
run_from_monster(X,Y,Unsafe_Head ) :-
	pos( XU,YU ) = Unsafe_Head,
	DXIR = XU-X, DYIR = YU-Y,
	turn_to( DXIR,DYIR ),
	step(),!.