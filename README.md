# Social Media Analysis using Image Analytics and Topic Modeling

This project aims to analyze the GoPro's Twitter uploads, as they have a large variety of photos with different levels of engagement. Go Pro is a leading action camera manufacturer which also develops its own mobile apps and video-editing software. 

Firstly, we scraped Go Pro's twitter account for all the posts with images including the caption, number of likes, number of comments, and the URL of the image. Next, the images were passed through Google's Cloud Vision AI API to retrieve annotatation for each image. Using the image descriptors, topic modeling was applied to classify the posts in 5-6 themes. Finally, posts for each theme were analyzed for their performance using the engagement metrics. The analysis is particularly extremely useful for the brand as it highlights which specific photo themes create more engagement amongst their audience.
