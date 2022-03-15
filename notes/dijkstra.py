from tkinter import N


L = [[]];
P =[];
D = [];

def dijkstra(L,P,n):
    D = list(n);
    C = list(range(2,n+1));
