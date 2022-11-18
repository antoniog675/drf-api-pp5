# FitnessBlogz - API

* * *

### ABOUT THE WEBSITE -

* * * 

[Live API Link](https://drf-api-pp5.herokuapp.com/)

[Github Repo](https://github.com/antoniog675/drf-api-pp5)

![Image of json of deployed api on heroku](assets/api_deployed-heroku.jpg)

The API that I have is going to be used to assist the 'FitnessBlogz' website with handling posts, profiles, comments, likes and followers.

What is the website? The website is going to be a 'Instagram' like website where users can share their workout routine, exercises, fitness progress and be able to like and comment on others posts to be able to support others on their fitness journey!

## Database
<hr>

![ERD Diagram for model](/assets/PP5-API.jpg)

The User model is going to be the django default model - We will use user (PK) owner which will have a OneToOne relationship and on_delete=models.CASCADE.

User Model ---> id (BigAuto), username (Char) and password (Char)

Profile Model ---> id (BigAuto), owner (OneToOne), created_at (DateTime), updated_at (DateTime), name (Char), content, (Text), image (Image)

Followers Model ---> id (BigAuto), owner-following (ForeignKeyUser), followed (ForeignKeyUser), created_at (DateTime)

Comments Model ---> id (BigAuto), owner (ForeignKey), post(ForeignKey), created_at (DateTime), updated_at(DateTime), content (Text)

Post Model ---> id (BigAuto), owner (ForeignKey), created_at (DateTime), upadted_at(DateTime), title (Char), content(Text), image (Image)

Like Model ---> id (BigAuto), owner (ForeignKey), post (ForeignKey), created_at (DateTime)

<hr>

## Testing

Tested profiles API, created 3 profiles and all three are stored, contains the users profile image, date createdm bio how many posts they have and how many followers they have and how many people they are following. URL link also goes to correct page

![Profiles API with relevant data](/assets/api_profiles.jpg)

Profile 1 URL works, tested that this works for /2 and /3

![Returns data of profile 1 (Antonio)](/assets/api_profile_1.jpg)

All posts that have been created and uploaded are loaded

![Posts API](/assets/api_posts.jpg)

All comments that have been uploaded from most recent to oldest

![Comments API](/assets/api_comments.jpg)

All likes in website

![Likes API](/assets/api_likes.jpg)

Counts the number of profile that are following eachother

![Followers API](/assets/api_followers.jpg)

<ul>
    <li>Deleting posts removes it from the API, edited posts are also reflected in the backend</li>
    <li>Liking and unliking posts are reflected throughout the API, the number of likes on a post in the front end are the same as the number of likes in the backend </li>
</ul>

## PEP8 -

![Warning from the gitpod pycodestyle](/assets/pep8_warnings_manual.jpg)

I have manually gone through each file to check the warnings and have been correcting all of them, currently there are NO warnings