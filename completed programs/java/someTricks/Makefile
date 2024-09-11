#hello:
#	@echo "Hello"

# the one below will run all three recipes 
all: compile run clean

#this recipe will compile the two files
compile:
	@javac Main.java person.java

#this recipe will run Main
run: 
	@java Main

#this will remove all the class files to keep it clean
clean:
	@rm Main.class person.class
