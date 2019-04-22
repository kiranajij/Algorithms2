all: heapsort.c heap_main.c
	gcc heapsort.c heap_main.c -o main

clean:
	rm main
