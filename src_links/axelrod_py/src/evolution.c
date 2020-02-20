#include "evolution.h"

void evolution(axl_network *mysys)
{
	int i, j, k, lo, lz, r;	
	int step_n;
        double h_ab, random;
	int n_active_links;
	active_link *active_links;
	int *list_ones, *list_zero;
	int links_ones, links_zero;
	FILE *fp;

	/* Set the random seed */
	srand(mysys->seed);

	/* Look for active links */
	n_active_links = number_of_active_links(mysys);

	active_links = (active_link *)malloc(n_active_links * sizeof(active_link));

	k = 0;
	for(i = 0; i < mysys->nagents; i++)
	{
		for(j = 0; j < mysys->nagents; j++)
		{
			if(active_condition(mysys->agent[i], mysys->agent[j]))
			{
				active_links[k].source = i;
				active_links[k].target = j;
				k++;
			}
		}
	}
	
	for(step_n = 0; step_n < n_active_links; step_n++)
	{
		/* Choose a random agent */
		k = rand() % n_active_links;

		i = active_links[k].source;
		j = active_links[k].target;

		/* Compute the homophily */
		h_ab = homophily(mysys->agent[i], mysys->agent[j]);
					   
		/* Take a random number */ 
    		random = (((double)rand())/RAND_MAX);

		/* If the interaction takes place, go into the next if */
	 	if((random < h_ab) && (active_condition(mysys->agent[i], mysys->agent[j])))
		{
			mysys->links_destroyed = 0;
			mysys->links_created = 0;

			links_ones = 0;
			links_zero = 0;
			for(k = 0; k < mysys->nagents; k++)
			{
				if(homophily(mysys->agent[i], mysys->agent[k]) == 1.0/mysys->agent[i].f)
					links_ones++;	
				if(homophily(mysys->agent[i], mysys->agent[k]) == 0.00)
					links_zero++;	
			}

			list_ones = (int *)malloc(sizeof(int) * links_ones);
			list_zero = (int *)malloc(sizeof(int) * links_zero);

			lo = 0;
			lz = 0;
			for(k = 0; k < mysys->nagents; k++)
			{
				if(homophily(mysys->agent[i], mysys->agent[k]) == 1.0/mysys->agent[i].f)
				{
					list_ones[lo] = k;
					lo++;	
				}
				else if(homophily(mysys->agent[i], mysys->agent[k]) == 0.00)
				{
					list_zero[lz] = k;
					lz++;	
				}
			}
			/* Take a random feature */
			r = rand() % mysys->agent[i].f;

			/* If the two agents share this feature, take the closest not equal */
			while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
				r = (r+1) % mysys->agent[i].f;
      	    			        
			/* Agent i copies a feature from agent j */
			mysys->agent[i].feat[r] = mysys->agent[j].feat[r];

			for(k = 0; k < links_ones; k++)
			{
				if(homophily(mysys->agent[i], mysys->agent[list_ones[k]]) == 0.00)
					mysys->links_destroyed++;
			}
			for(k = 0; k < links_zero; k++)
			{
				if(homophily(mysys->agent[i], mysys->agent[list_zero[k]]) == 1.0/mysys->agent[i].f)
					mysys->links_created++;
			}

			fp = fopen("Links_created_destroyed","a");
			fprintf(fp, "%d,%d\n", mysys->links_created, mysys->links_destroyed);
			fclose(fp);

			free(list_ones);
			free(list_zero);
		}

		mysys->seed = rand();
	}
	free(active_links);

	return;
}
