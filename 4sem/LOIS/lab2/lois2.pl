%Лабараторная работа №2 по дисциплине ЛОИС
%Выполнена студентом группы 121703 БГУИР Якимович Илья Викторович
%Программа содержит описание предикатов, позволяющих расставить на шахматной доске 8 ферзей
%так, чтобы ни один ферзь не находился под боем другого ферзя
%29.05.2023

getSolution(S) :-
    findall(S, solve(S), Solutions),
    writeSolutions(Solutions),
    countSolutions(Solutions, Count),
    write('Number of solutions: '), write(Count), nl.

writeSolutions([]).
writeSolutions([Solution | Rest]) :-
    write(Solution), nl,
    writeSolutions(Rest).

solve([]).
solve([X/Y | Oth]) :- 
    solve(Oth),
    select(Y, [1, 2, 3, 4, 5, 6, 7, 8], _),
    noAttack(X/Y, Oth).
    
noAttack(_, []).
noAttack(X/Y, [X1/Y1 | Oth]) :-
    Y =\= Y1,
    Y1 - Y =\= X1 - X, 
    Y1 - Y =\= X - X1,
    noAttack(X/Y, Oth).

countSolutions([], 0).
countSolutions([_ | Rest], Count) :-
    countSolutions(Rest, RestCount),
    Count is RestCount + 1.
