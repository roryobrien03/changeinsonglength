# Introduction:

As an avid music listener, I have noticed it becoming somewhat a trend for the length of newly released music to be shorter than previous. 

There are multiple causes of this I think, some of the main ones include: 
•	Reduction of attention spans of people due to the new technology world and addiction to smartphones and social media such as Instagram, Snapchat, Tiktok etc.
•	The rise of streaming services such as Spotify, which incentivize artists to try to maximise their streams rather than producing good quality albums/singles. There are now over 20 songs on many albums which was extremely rare of before. 
•	Tiktok in particular is the most viral app in the world and many songs become popular due to short (~ 15 seconds) snippets of songs becoming trendy on it.

I wanted to investigate if this was true or not, so I gathered data from Kaggle (https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year/code ) of the hit songs on Spotify from 2010-2019. I analysed this data and then used both simple linear regression and machine learning to try and predict what future song duration would be.

I also used a 2021 dataset of top songs on Spotify to compare my results and predictions to (https://www.kaggle.com/datasets/equinxx/spotify-top-50-songs-in-2021) .

# Analysis of 2010-2019 dataset:

  
One of my first observations from the data was the mean duration of all the songs in the dataset being 224.68 seconds. This corresponds to 3 minutes and 44 seconds. 
Next, the mean durations of songs is steadily declining from year to year, with a large spike from 2018 to 2019 as can be seen on the graph. This coincides with TikTok becoming very popular from 2019 onwards, which I previously stated as one of the potential causes of the general decline.




  

Above are the 10 lowest duration songs in the dataset. 8 out of 10 are from 2015 onwards. 2015 was chosen as the cut-off point for comparison as it splits the dataset in half.


 

Now we can see the 10 highest duration songs in the dataset. 8 out of 10 are before 2015.
With the longest songs generally being after 2015, and the shortest songs being before, it’s a fairly reasonable assumption that song length of top songs is decreasing.


 

This boxplot of the data is a good indicator of the range of the duration of the songs for each year. The length of the boxplot represents the range of the interquartile range (middle 50% of the data). The larger the box, the greater the range. It can be seen here that as the years increase, the boxes are going lower, representing a general decrease in song length. The diamond shapes show outliers in each year

 

This is a swarmplot. It’s very similar to a boxplot but may be easier on the eye and clearer to some viewers. It shows the data points of each year and indicates the same thing as a boxplot.





# Predictions:

I used 3 different prediction types:
•	Simple Linear Regression (OLS) of all the data (formula below)
 
•	Simple Linear Regression (OLS) of the mean values for each year (formula below)
 
•	Machine Learning model (used a test size of 30% of the data)


The machine learning model had a Mean Absolute Error (MSE) of 26.37 and a Root Mean Squared Error (RMSE) of 36.89. These may appear high, but when you consider the average value for song duration is 224.67 seconds and a standard deviation of 34.13 seconds, this model is actually very good. Average residuals of 36.89 seconds (just over half a minute) can be deemed acceptable.



Comparison to 2021:
    For 2021:
•	The Simple Linear Regression (OLS) of all the data predicted a value of 206.6 seconds for 2021.
•	The Simple Linear Regression (OLS) of the mean values for each year predicted a value of 204.41 seconds for 2021.
•	The Machine Learning model predicted a value of 207.02 seconds.

Using the 2021 dataset, it can be found that the actual mean duration was 197.48 seconds, which is lower than our models predicted (by about 10 seconds for each). However, I feel this could be attributed to the extremity of the speed at which song length has become smaller in the more recent years. 




 

For example, it can be seen here that the lowest duration song in 2021 was 132.78 seconds. This would have been the lowest duration song in our entire dataset from 2010-2019.




Conclusion:

Overall, my preconceptions were confirmed by analysis of the data. However, I may have been biased going into the process as a result of this, so I need to be wary of that also. 

I do think the predictions of the models being off further proved my point in the introduction. 

To take a real world example, SZA is a brilliant artist and one of my favourites. Her 2017 album ‘Ctrl’ had 14 songs with an average song length of 210 seconds. Her 2022 album ‘SOS’ has 23 songs with an average song length of 176.91 seconds. This is a huge contrast and a sign of the times. Luckily with SZA, her new album has been critically acclaimed and the quality hasn’t gone down since her last album, but this cannot be said for every artist. 

Overall, it must be questioned how far this can go. I’m worried for the music industry with this trend as a decrease in length of songs usually means less substance and quality to the music.

