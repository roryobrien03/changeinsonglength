# songlength

This project aims to inspect if the length of the most popular songs are decreasing. This has been a common public thought for many reasons. Two of the main reasons for this include: 
The rise of social media and most recently Tiktok (became popular in 2019) leading to shorter-attention spans.
The rise of streaming has lead to artists releasing albums with more tracks but a lower song length.

For this project I used two datasets. The first one I used (https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year/code) contained information on the top streamed songs on Spotify in each year from 2010-2019. The second one (https://www.kaggle.com/datasets/equinxx/spotify-top-50-songs-in-2021) contained information on the top streamed songs on Spotify in 2021. 

Using pandas, I imported the data and calculated the average song length (in seconds) in each year from 2010-2019. The results of this can be seen in this plot, created using matplotlib.

<img width="1440" alt="Screenshot 2023-01-14 at 22 41 57" src="https://user-images.githubusercontent.com/122220434/212500271-43b0d9c4-0cc4-44e5-8839-d17f000d236f.png">


It can be seen that there has been a clear decrease over the years. The peak average song length (247.23 seconds) in 2011, compared to the average song length (207.33 seconds) represents a 16.14% decrease, which is pretty substantial when you consider the relatively small range of song lengths.

Another visualisation of the data, through a plot of the moving average (of the last 3 years) can be seen below, and shows further evidence of the steady decrease in song duration. 

<img width="1440" alt="Screenshot 2023-01-16 at 17 52 53" src="https://user-images.githubusercontent.com/122220434/212740388-5adf5849-a9e6-472e-ae27-28bff2343099.png">


After this, I used a similar method in the "songlength2021.py" file to calculate the average song duration of the top 50 songs in 2021. The resulting figure was 197.49 seconds, which shows evidence of this downward trend.

I then used a linear regression model to predict the expected 2021 average song duration using pandas and the sklearn module. I trained the model on 30% of the data and tested it on the other 70%. This predicted value was 206.25 seconds. This is a 8.76 second (4.44%) difference from the actual value in 2021. This higher expected value is likely due to the fact that the decrease in average time was very steady up until 2019 when it took a heavy fall, so the linear regression model's slope isn't that large (in magnitude) as it uses data on all the values. The slope coefficient of -3.42 shows this.

Otherwise, the RMSE (Root Mean Squared Error) of the model was 4.4 which is pretty low, meaning the linear regression model seems to be pretty accurate.


Overall, it is pretty safe to say that the average duration of the top songs has decreased from 2010-2021. The reasons for this are speculative, and are likely to be strongly linked to the reasons aforementioned.

