EXECUTABLE := matrix-svd
OBJS := matrix-svd.o

CC := gcc
CFLAGS := -O3 -std=c99 -mkl

INCLUDES :=
LIBLOCS :=
LDFLAGS :=

%.o: %.c %.h
	$(CC) $(CFLAGS) $(DEFS) $(INCLUDES) -c $< -o $@

$(EXECUTABLE): $(OBJS)
	$(CC) $(CFLAGS) $(DEFS) $(INCLUDES) $(OBJS) -o $@ $(LIBLOCS) $(LDFLAGS)

clean:
	-rm -f *.o $(EXECUTABLE)

