
all: cshell cppshell


c: cshell
	./cshell

cpp: cppshell
	./cppshell


cshell: shell_sort.c
	gcc -o cshell shell_sort.c

cppshell: shell_sort.cpp
	g++ -o cppshell shell_sort.cpp


clean:
	rm -f *.o cshell cppshell
