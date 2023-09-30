#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * infinite_while - creayes an infinite loop
 *
 * Return: 0 on success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0.
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == -1)
			return (1);

		if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %u\n", pid);
	}
	infinite_while();

	return (0);
}
