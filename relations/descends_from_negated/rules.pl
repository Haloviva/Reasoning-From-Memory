:- module(descends_from_negated, [descends_from_negated/2]).

:- use_module(relations/descends_from/rules, [descends_from/2]).

descends_from_negated(Person1, Person2) :-
  fact_descends_from_negated(Person1, Person2).

descends_from_negated(Person1, Person2) :-
  descends_from(Person2, Person1).

descends_from_negated(Person1, Person2) :-
  descends_from:fact_descends_from(Person1, Person1sAncestor),
  descends_from_negated(Person1sAncestor, Person2),
  Person1 \= Person2.