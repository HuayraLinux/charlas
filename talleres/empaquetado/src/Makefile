CC := gcc
CFLAGS := -O2
.PHONY : clean install

all: hola_huayra

hola_huayra: hola.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f hola.o hola_huayra

install:
	cp test $(DESTDIR)/usr/bin/hola_huayra
