#include <math.h>
#include <stdio.h>

#define PI 3.14159265
// #define total_bus_bars 2

const int CITY = 2;
const int WEEK = 7;

double summation(bus_bar_number_i, total_bus_bars)
{
    int k = 1;
    if (k != bus_bar_number_i)
    {
    }
    else
    {
    }
}

double forming_admittance_matrix()
{
    float matrix[2][2];
    for (int i = 0; i < 2; ++i)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("Enter the elements:");
            scanf("%f", &matrix[i][j]);
        }
    }

    printf("\nDisplaying values: \n\n");
    for (int i = 0; i < 2; ++i)
    {
        for (int j = 0; j < 2; ++j)
        {
            printf("Element %f = %f\n", i + 1, j + 1, matrix[i][j]);
        }
    }
}

int main()
{
    // summation();
    forming_admittance_matrix();

    return 0;
}
