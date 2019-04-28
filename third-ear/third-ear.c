#include "inttypes.h"
#include "libpruio/pruio.h"
#include "stdio.h"
#include "time.h"

int CHANNEL_0[50000];
int CHANNEL_1[50000];
int CHANNEL_2[50000];
int CHANNEL_3[50000];

int main()
{
	pruIo *io = pruio_new(PRUIO_DEF_ACTIVE, 0, 0, 0);
	if(io -> Errr)
	{
		printf("constructor failed (%s)\n", io->Errr);
		return 1;
	}
	uint32 mask = 30;
	if(pruio_config(io, 50000, mask, 20001, 0))
	{
		printf("config failed (%s)\n", io->Errr);
		return 1;
	}
	clock_t t;
	t = clock();
	if(pruio_mm_start(io, 0, 0, 0, 0))
	{
		printf("mm_start failed (%s)\n", io->Errr);
		return 1;
	}
	uint16 *AdcV = io->Adc->Value;
	t = clock() - t;
	double time_taken = ((double)t)/CLOCKS_PER_SEC;
	//printf("%f", time_taken);
	for(int i = 0; i < 50000; i++)
	{
		//printf("%" PRIu16 ,AdcV[i]);
		CHANNEL_0[i] = AdcV[(i * 4)];
		CHANNEL_1[i] = AdcV[(i * 4) + 1];
		CHANNEL_2[i] = AdcV[(i * 4) + 2];
		CHANNEL_3[i] = AdcV[(i * 4) + 3];
		printf("%d %d %d %d\n", CHANNEL_0[i], CHANNEL_1[i], CHANNEL_2[i], CHANNEL_3[i]);
	}
	pruio_destroy(io);
	return 0;	
}
