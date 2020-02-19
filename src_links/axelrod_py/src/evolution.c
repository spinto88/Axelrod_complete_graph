#include "evolution.h"

void evolution(axl_network *mysys)
{
	int i, j, k, l, r;	
	int step_n;
        double h_ab, random;
	int n_active_links;
	int links_zero = 0;
	int links_ones = 0;
	active_link *active_links;
	int *list_ones;
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
			links_ones = 0;
			for(k = 0; k < mysys->nagents; k++)
			{
				if((homophily(mysys->agent[i], mysys->agent[k]) == (1./mysys->agent[i].f)) && (k != j))
					links_ones++;
			}

			if(links_ones != 0)
			{
				l = 0;
				list_ones = (int *)malloc(sizeof(int) * links_ones);			
				for(k = 0; k < mysys->nagents; k++)
				{
					if((homophily(mysys->agent[i], mysys->agent[k]) == (1./mysys->agent[i].f))  && (k != j))
					{
						list_ones[l] = k;
						l++;
					}
				}
			}
					
			/* Take a random feature */
			r = rand() % mysys->agent[i].f;

			/* If the two agents share this feature, take the closest not equal */
			while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
				r = (r+1) % mysys->agent[i].f;
      	    			        
			/* Agent i copies a feature from agent j */
			mysys->agent[i].feat[r] = mysys->agent[j].feat[r];

			if(links_ones != 0)
			{
				links_zero = 0;
				for(l = 0; l < links_ones; l++)
				{
					if(homophily(mysys->agent[i], mysys->agent[list_ones[l]]) == 0.00)
						links_zero += 1;
				}

				fp = fopen("Links_zero.dat","a");
				fprintf(fp, "%f\n", ((float)links_zero)/links_ones);
				fclose(fp);
				free(list_ones);
			}
		}

		mysys->seed = rand();
	}
	free(active_links);

	return;
}
