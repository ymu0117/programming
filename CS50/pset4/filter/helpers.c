#include "helpers.h"
#include <math.h>
#include <stdlib.h>
#include <stdio.h>


void swap(int width, RGBTRIPLE image[width]);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < width; i++)
    {
        for(int j = 0; j < height; j++)
        {
            int rgbtGray = floor(image[j][i].rgbtBlue + image[j][i].rgbtGreen + image[j][i].rgbtRed)/3;
            image[j][i].rgbtBlue = rgbtGray;
            image[j][i].rgbtGreen = rgbtGray;
            image[j][i].rgbtRed = rgbtGray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < width; i++)
    {
        for(int j = 0; j < height; j++)
        {
            int sepiaRed = floor(.393 * image[j][i].rgbtRed + .769 * image[j][i].rgbtGreen + .189 * image[j][i].rgbtBlue);
            int sepiaGreen = floor(.349 * image[j][i].rgbtRed + .686 * image[j][i].rgbtGreen + .168 * image[j][i].rgbtBlue);
            int sepiaBlue = floor(.272 * image[j][i].rgbtRed + .534 * image[j][i].rgbtGreen + .131 * image[j][i].rgbtBlue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[j][i].rgbtRed = sepiaRed;
            image[j][i].rgbtGreen = sepiaGreen;
            image[j][i].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        swap(width, image[i]);
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE(*blured)[width] = calloc(height, width * sizeof(RGBTRIPLE));

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            //printf("%d\n", j);
            if (i == 0)
            {
                if (j == 0)
                {
                    blured[i][j].rgbtRed = floor((image[i][j].rgbtRed + image[i][j+1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed)/4);
                    blured[i][j].rgbtBlue = floor((image[i][j].rgbtBlue + image[i][j+1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue)/4);
                    blured[i][j].rgbtGreen = floor((image[i][j].rgbtGreen + image[i][j+1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen)/4);
                }
                else if (j == (width-1))
                {
                    blured[i][j].rgbtRed = floor((image[i][j-1].rgbtRed + image[i][j].rgbtRed + image[i+1][j-1].rgbtRed + image[i+1][j].rgbtRed)/4);
                    blured[i][j].rgbtBlue = floor((image[i][j-1].rgbtBlue + image[i][j].rgbtBlue + image[i+1][j-1].rgbtBlue + image[i+1][j].rgbtBlue)/4);
                    blured[i][j].rgbtGreen = floor((image[i][j-1].rgbtGreen + image[i][j].rgbtGreen + image[i+1][j-1].rgbtGreen + image[i+1][j].rgbtGreen)/4);
                }
                else
                {
                    blured[i][j].rgbtRed = floor((image[i][j-1].rgbtRed + image[i][j].rgbtRed + image[i][j+1].rgbtRed + image[i+1][j-1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed)/6);
                    blured[i][j].rgbtBlue = floor((image[i][j-1].rgbtBlue + image[i][j].rgbtBlue + image[i][j+1].rgbtBlue + image[i+1][j-1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue)/6);
                    blured[i][j].rgbtGreen = floor((image[i][j-1].rgbtGreen + image[i][j].rgbtGreen + image[i][j+1].rgbtGreen + image[i+1][j-1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen)/6);
                }
            }
            else if (i == (height-1))
            {
                if (j == 0)
                {
                    blured[i][j].rgbtRed = floor((image[i][j].rgbtRed + image[i][j+1].rgbtRed + image[i-1][j].rgbtRed + image[i-1][j+1].rgbtRed)/4);
                    blured[i][j].rgbtBlue = floor((image[i][j].rgbtBlue + image[i][j+1].rgbtBlue + image[i-1][j].rgbtBlue + image[i-1][j+1].rgbtBlue)/4);
                    blured[i][j].rgbtGreen = floor((image[i][j].rgbtGreen + image[i][j+1].rgbtGreen + image[i-1][j].rgbtGreen + image[i-1][j+1].rgbtGreen)/4);
                }
                else if (j == width-1)
                {
                    blured[i][j].rgbtRed = floor((image[i][j-1].rgbtRed + image[i][j].rgbtRed + image[i-1][j].rgbtRed + image[i-1][j-1].rgbtRed)/4);
                    blured[i][j].rgbtBlue = floor((image[i][j-1].rgbtBlue + image[i][j].rgbtBlue + image[i-1][j].rgbtBlue + image[i-1][j-1].rgbtBlue)/4);
                    blured[i][j].rgbtGreen = floor((image[i][j-1].rgbtGreen + image[i][j].rgbtGreen + image[i-1][j].rgbtGreen + image[i-1][j-1].rgbtGreen)/4);
                }
            }
            else if (j == 0 && i > 0 && i < height-1)
            {
                blured[i][j].rgbtRed = floor((image[i-1][j].rgbtRed + image[i-1][j+1].rgbtRed + image[i][j].rgbtRed + image[i][j+1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed)/6);
                blured[i][j].rgbtBlue = floor((image[i-1][j].rgbtBlue + image[i-1][j+1].rgbtBlue + image[i][j].rgbtBlue + image[i][j+1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue)/6);
                blured[i][j].rgbtGreen = floor((image[i-1][j].rgbtGreen + image[i-1][j+1].rgbtGreen + image[i][j].rgbtGreen + image[i][j+1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen)/6);
            }
            else if (j == width-1 && i > 0 && i < height-1)
            {
                blured[i][j].rgbtRed = floor((image[i-1][j].rgbtRed + image[i-1][j-1].rgbtRed + image[i][j].rgbtRed + image[i][j-1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j-1].rgbtRed)/6);
                blured[i][j].rgbtBlue = floor((image[i-1][j].rgbtBlue + image[i-1][j-1].rgbtBlue + image[i][j].rgbtBlue + image[i][j-1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j-1].rgbtBlue)/6);
                blured[i][j].rgbtGreen = floor((image[i-1][j].rgbtGreen + image[i-1][j-1].rgbtGreen + image[i][j].rgbtGreen + image[i][j-1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j-1].rgbtGreen)/6);
            }
            else
            {
                blured[i][j].rgbtRed = floor((image[i-1][j-1].rgbtRed + image[i-1][j].rgbtRed + image[i-1][j+1].rgbtRed +
                         image[i][j-1].rgbtRed + image[i][j].rgbtRed + image[i][j+1].rgbtRed +
                         image[i+1][j-1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed)/9);
                blured[i][j].rgbtBlue = floor((image[i-1][j-1].rgbtBlue + image[i-1][j].rgbtBlue + image[i-1][j+1].rgbtBlue +
                         image[i][j-1].rgbtBlue + image[i][j].rgbtBlue + image[i][j+1].rgbtBlue +
                         image[i+1][j-1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue)/9);
                blured[i][j].rgbtGreen = floor((image[i-1][j-1].rgbtGreen + image[i-1][j].rgbtGreen + image[i-1][j+1].rgbtGreen +
                         image[i][j-1].rgbtGreen + image[i][j].rgbtGreen + image[i][j+1].rgbtGreen +
                         image[i+1][j-1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen)/9);
            }
        }
    }

    // copy blured to image
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            image[i][j] = blured[i][j];
        }
    }

    free(blured); 
    
    return;
}

void swap(int width, RGBTRIPLE image[width])
{
    for(int i = 0; i < floor(width/2); i++)
    {
        RGBTRIPLE tmp = image[i];
        image[i] = image[width-i];
        image[width-i] = tmp;
    }
    return;
}
