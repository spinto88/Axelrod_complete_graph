#include "active_links.h"

int active_condition(axl_agent a, axl_agent b)
{
	double hab;

	hab = homophily(a,b);

	if((hab > 0.00) && (hab < 1.00))
		return 1;
	else
		return 0;
}

int number_of_active_links(axl_network* mysys)
{
	int i, j;
	int count = 0;

	for(i = 0; i < mysys->nagents; i++)
	{
		for(j = 0; j < mysys->nagents; j++)
		{
			if(active_condition(mysys->agent[i], mysys->agent[j]))
				count++;
		}
	}
	
	return count;
}

int active_links(axl_network mysys)
{
	/* Active links: this function return if an active link is found.
	An active link is a pair of agents which are neighbors and the homophily
        is larger than zero and less than one. */

	int i, j;
        int n = mysys.nagents;

        for(i = 0; i < n; i++)
	{
		for(j = 0; j < n; j++)
		{
			if(active_condition(mysys.agent[i], mysys.agent[j]))
				return 1;
		}
	}

	return 0;	
}
		

