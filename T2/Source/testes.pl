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