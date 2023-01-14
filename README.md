# songlength

This project aims to inspect if the length of the most popular songs are decreasing. This has been a common public thought for many reasons. Two of the main reasons for this include: 
The rise of social media and most recently Tiktok (became popular in 2019) leading to shorter-attention spans.
The rise of streaming has lead to artists releasing albums with more tracks but a lower song length.

For this project I used two datasets. The first one I used (https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year/code) contained information on the top streamed songs on Spotify in each year from 2010-2019. The second one (https://www.kaggle.com/datasets/equinxx/spotify-top-50-songs-in-2021) contained information on the top streamed songs on Spotify in 2021. 

Using pandas, I imported the data and calculated the average song length (in seconds) in each year from 2010-2019. The results of this can be seen in this plot, created using matplotlib.

<img width="1440" alt="Screenshot 2023-01-14 at 22 41 57" src="https://user-images.githubusercontent.com/122220434/212500271-43b0d9c4-0cc4-44e5-8839-d17f000d236f.png">

It can be seen that there has been a clear decrease over the years. The peak average song length (247.23 seconds) in 2011, compared to the average song length (207.33 seconds) represents a 16.14% decrease, which is pretty substantial when you consider the relatively small range of song lengths.

