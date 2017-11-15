%------------------------------------------------%
% Module: percepts as p                          %
%------------------------------------------------%

%------------------------------------------------%
% Definitions                                    %
%------------------------------------------------%
:- module(p,  [
                sixth_sense/1
                    ] ).

:- use_module(main ).

%------------------------------------------------%
%                                                %
% Exported Predicates                            %
%                                                %
%------------------------------------------------%

%This predicate will infers that agent has lost energy 'cause it's on the same position of a monster or a hole.
%In addition, this predicate retracts the energy of the agent and will set a new energy for the agent through the command asserta.
sixth_sense(asserta(energy(agent, 0 ))):-
  at(agent, Position ),
  at(hole, Position ),
  retract(energy(agent,_ )).

sixth_sense(asserta(energy(agent, NewEnergy  ))):-
	at(agent, Position ),
	( 
		at(damage(monster(01 ),20 ));
		at(damage(monster(02 ),20 )),
		NewEnergy is energy(agent, _  ) - 20,
		retract(energy(agent,_  )),
	);
	(
		at(damage(monster(03 ),50 ));
		at(damage(monster(01 ),50 )),
		NewEnergy is energy(agent, _ - 50 ),
		retract(energy(agent, _  )),
	) .

%This predicate will infers that agent it's on same positon as the gold it's.
sixth_sense(assertz(at(gold, pos(X,Y )))):-
  at(agent, pos(X,Y )),
  at(shine, pos(X,Y )),
  retract(at(shine, pos(X,Y ))).

%This predicate will infers that agent it's on a hole.
sixth_sense(asserta(on_hole )):-
  not(on_hole ),
  at(agent, Position ),
  at(hole, Position ).

sixth_sense(retract(on_hole )):-
  on_hole,
  at(agent, Position ),
  not(at(hole, Position )).

  sixth_sense(check_surrounding_current_position ):-
    at(agent,Position ),
    not(sensed(Position, current )),
    asserta(sensed(Position, current )).

  sixth_sense(correct_as_safe ):-
    at(agent, Position ),
    not(sensed(Position, around )),
    not(at(hole, Position )),
    not(at(noises, Position )),
    not(at(breeze, Position )),
    asserta(sensed(Position, around )).

  sixth_sense(correct_as_unsafe ):-
    at(agent, Position ),
    not(sensed(Posiiton, around )),
    ( at(hole, Position );
      at(noises, Position );
      at(breeze, Position ),
      asserta(sensed(Pos, around ))
       ).
