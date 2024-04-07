#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/*Write a C program that creates 5 zombie processes.*/

/**
 * infinite_while - sleeps 1
 * 
 * Return: 0 in success 
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}



int main ()
{
	int child_process;
	int loop = 5;

	for (;loop > 0; loop--)
	{
		child_process = fork();
		if ( child_process == -1)
		{
			printf("fork failed");
		}
		else if (child_process == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}

	}
	infinite_while();
	return (0);
}
