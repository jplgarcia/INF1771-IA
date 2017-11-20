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
take_action :-
	senses( _,_,_,_,_,Impact,Scream ),
	at(agent,pos( X,Y )),
	(
		(
			(
				at(gold, pos( X,Y )),
				Shine = shine
			);
			(
				\+ at(gold, pos( X,Y )),
				Shine = no
			)
		),
		(
			(
				at(breeze, pos( X,Y )),
				Breeze = breeze
			);
			(
				\+ at(breeze, pos( X,Y )),
				Breeze = no
			)
		),
		(
			(
				at(stench, pos( X,Y )),
				Stench = stench
			);
			(
				\+ at(stench, pos( X,Y )),
				Stench = no
			)
		)
	),
	(
		(
			agentfacing( DXIR,DYIR ),
			NX is X+DXIR, NY is Y+DYIR,
			at(wall, pos( NX,NY )),
			print("Parede a frente"),%%/**
			(
				NX1 is X-DYIR, NY1 is Y+DXIR,
				NX2 is X+DYIR, NY2 is Y-DXIR,
				(
					(	
						%%Tem parede à esquerda, vira pra direita
						at(wall, pos( NX1, NY1 )),
						%print("Parede a esquerda"),
						turn(right)
					);
					(
						%%Tem parede à direita, vira pra esquerda
						at(wall, pos( NX2,NY2 )),
						%print("Parede a direita"),
						turn(left)
					);
					(
						\+ at(wall, pos( NX1,NY1 )),
						\+ at(wall, pos( NX2,NY2 )),
						turn(right)
					)
				)
			)%%*/
			%%turn(left)
		);true
	),
	take_action( X, Y, Stench, Breeze, Shine, Impact, Scream ),
	retract(senses( _, _, _, _, _, _, _ )),
	asserta(senses( X, Y, Stench, Breeze, Shine, no, no)) ,! .

take_action(  X, Y,no, no, no, no, no ) :-
	(
		get_all_should_visit( _,pos( X,Y ),Should_List ),
		(
			(
				\+ length( Should_List,0 ),
				[ Should_Head|_ ] = Should_List,
				pos( DXU,DYU ) = Should_Head,
				NDXIR is DXU-X, NDYIR is DYU-Y,
				turn_to( NDXIR,NDYIR ),
				step,!
			);
			(
				length( Should_List,0 ),
				step,!
			);true
		)
	);true .

%%Decides to pick up gold if seen
take_action( X, Y, _, _, shine, _, _ ) :-
	pick_gold(pos( X,Y )).

%%Treats monster death
take_action( X, Y, _, _, _, _, scream ) :-
	agentfacing( DX,DY ),
	NX is X+DX,NY is Y+DY,
	kill_monster( pos( NX,NY )),!.


%%Decides wheter to step or shoot if smelled stench; prefers to walk to a safe place over steping/shooting an unsafe place
take_action( X, Y, stench, _, _, _, _ ) :-
	get_safe_adjacent_list(_ , pos( X,Y ), Safe_List ),
	get_adjacent_list(_ , pos( X,Y ), [Unsafe_Head|Unsafe_Tail ] ),
	get_all_should_visit(_ , pos( X,Y ),Should_List ),
	(
		(
			%%CASE no safe space
			(
				length( Safe_List,0 );
				length( Should_List,0 )
			),
			(
				(	%%CASE PotentialDanger then step
					at( potential_monster,Unsafe_Head ),
					pos( XU,YU ) = Unsafe_Head,
					DXIR is XU-X, DYIR is YU-Y,
					turn_to( DXIR,DYIR ),
					step,!
				);
				(	%%CASE RealDanger
					at(realMonster,Unsafe_Head ),
					(
						(
							%%If has ammo then shoot
							ammo( QTD ),
							\+ QTD < 1,
							pos( MXU,MYU ) = Unsafe_Head,
							MDXIR is MXU-X, MDYIR is MYU-Y,
							turn_to( MDXIR,MDYIR ),
							shoot,!
						);
						(	%%Has no ammo
							%% If there is no monster, go there
							(
								[Unsafe_Head|Unsafe_Tail ] = Unsafe_Tail,
								\+ at(realMonster,Unsafe_Head ),
								run_from_monster(X,Y,Unsafe_Head ),!
							);
							(
								[Unsafe_Head|Unsafe_Tail ] = Unsafe_Tail,
								\+ at(realMonster,Unsafe_Head ),
								run_from_monster(X,Y,Unsafe_Head ),!
							);
							(
								[Unsafe_Head|Unsafe_Tail ] = Unsafe_Tail,
								\+ at(realMonster,Unsafe_Head ),
								run_from_monster(X,Y,Unsafe_Head ),!
							)
						)
					)
				)
			),!
		);
		(	%%CASE Safe then Step to should_visit
			\+ length( Safe_List,0),
			get_all_should_visit( _,pos( X,Y ),Should_List ),
			(
				(
					\+ length( Should_List,0 ),
					[ Should_Head|_ ] = Should_List,
					Where_to = Should_Head
				);
				(
					length( Should_List,0 ),
					[ Safe_Head|_ ] = Safe_List,
					Where_to = Safe_Head
				)
			),
			pos( DXU,DYU ) = Where_to,
			NDXIR is DXU-X, NDYIR is DYU-Y,
			turn_to( NDXIR,NDYIR ),
			step,!
		),!
	)	.

%%Decides wheter to step  if felt breeze; prefers to walk to a safe place over steping to an unsafe place
take_action( X, Y, _, breeze, _, _, _ ) :-
	get_safe_adjacent_list(_ , pos( X,Y ), Safe_List ),
	get_adjacent_list(_ , pos( X,Y ), [Unsafe_Head|_ ] ),
	(
		(
			%%CAS E no safe space
			length( Safe_List,0),
			(
				at(potential_hole,Unsafe_Head ),
				pos( XU,YU ) is Unsafe_Head,
				DXIR is XU-X, DYIR is YU-Y,
				turn_to( DXIR,DYIR ),
				step,!
			),!
		);
		(	%%CASE Safe then Step to should_visit
			\+ length( Safe_List,0),
			get_all_should_visit( _,pos( X,Y ),Should_List ),
			(
				(
					\+ length( Should_List,0 ),
					[ Should_Head|_ ] = Should_List,
					Where_to = Should_Head
				);
				(
					length( Should_List,0 ),
					[ Safe_Head|_ ] = Safe_List,
					Where_to = Safe_Head
				)
			),
			pos( DXU,DYU ) = Where_to,
			NDXIR is DXU-X, NDYIR is DYU-Y,
			turn_to( NDXIR,NDYIR ),
			step,!
		),!
	)	.
	
turn_to( X,Y ) :-
	PX1 is X, PY1 is Y,
	PX2 is - Y, PY2 is X,
	PX3 is Y, PY3 is - X,
	PX4 is - X, PY4 is - Y,
	(
		(
			agentfacing( PX1,PY1 ),!
		);
		(
			agentfacing(PX2,PY2 ),
			turn(right),!
		);
		(
			agentfacing(PX3,PY3 ),
			turn(left),!
		);
		(
			agentfacing(PX4,PY4 ),
			turn(right),
			turn(right),!
		)
	).
run_from_monster(X,Y,Unsafe_Head ) :-
	pos( XU,YU ) is Unsafe_Head,
	DXIR is XU-X, DYIR is YU-Y,
	turn_to( DXIR,DYIR ),
	step,!.