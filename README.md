# Professor Oak's Blog

![Professor Oak gif](static/gif/prof-oak.gif)

[Click on this link to visit the blog on Heroku](https://prof-oaks-blog-0421d28e5692.herokuapp.com/)

<br>


# Content

- [Introduction](#introduction)
    * [User experience](#user-experience)
    * [My vision for the game](#my-vision-for-the-game)
- [Features](#features)
- [Future features](#future-features)
- [Design](#design)
- [Technologies used](#technologies-used)
    * [Balsemiq](#balsemiq)
    * [Lucid Flowchart](#lucid-flowchart)
    * [Bootstrap](#bootstrap)
    * [ElephantSQL](#elephantsql)
    * [Cloudinary](#cloudinary)
    * [Libraries](#libraries)
- [Testing](#testing)
    * [HTML validation](#html-validation)
    * [CSS validation](#css-validation)
    * [JavaScript validation](#javascript-validation)
    * [Python validation](#python-validation)
- [Bug fixes](#bug-fixes)
- [Deployment](#deployment)
    * [Github deployment](#github-deployment)
    * [Heroku deployment](#heroku-deployment)
- [Credits](#credits)

<br>


# Introduction

## User experience

## My vision for the blog

<br>


# Features

<br>


# Future features

<br>


# Design

### Colour scheme

I wanted to keep the colours fun and matching with the pokemon theme. The main pages follow the design of a pokeball, red - black - white. Other features like the back up button and the delete modal follow the pokemon logo colours, blue - yellow

<img src="static/images/pokeball.webp" width="200px"><img src="static/images/International_Pokémon_logo.svg.png" width="540px">

<br>

![Colour Palette](static/images/readme/colour-palette.png)

### Images

The images from the posts come from the websites that I got the post content from. They are linked in the credits section.

<details>
<summary>images and gif :</summary>

- [Pokemon logo](https://en.wikipedia.org/wiki/Pok%C3%A9mon)
- [person?](https://9gag.com/gag/aM4wexM)
- [pokemon?](https://www.polygon.com/2017/2/15/14615360/whos-that-pokemon-meme-creator)
- [Ash](https://mynintendonews.com/2023/10/07/pokemon-pays-tribute-to-ash-ketchums-25-year-journey/)
- [Misty](https://gamerant.com/pokemon-misty-anime-full-lore-history/)
- [Brock](https://www.reddit.com/r/MyHeroAcadamia/comments/17840ts/will_they_get_along_brock_pokemon/)
- [Oak](https://screenrant.com/pokemon-things-you-did-not-know-about-professor-oak-willow/)
- [Dennis](https://www.reddit.com/r/cars/comments/6y5a7v/what_year_and_model_range_rover_is_this_dennis/)
- [Dee](https://www.reddit.com/r/IASIP/comments/sl7bjs/sweet_dee_with_her_gorgeous_flojo_nails_10_years/)
- [Frank](https://www.joe.co.uk/entertainment/11-times-frank-reynolds-was-the-most-disgustingly-hilarious-man-on-television-208751)
- [Charlie](https://hellyeahcharlieday.tumblr.com/post/170055955219/charilework-which-charlie-kelly-are-you)
- [Mac](https://www.thewrap.com/rob-mcelhenney-fat-weight-always-sunny/)
- [Rick](https://tvtropes.org/pmwiki/pmwiki.php/Characters/RickAndMortyRickSanchez)
- [Morty](https://tvtropes.org/pmwiki/pmwiki.php/Characters/RickAndMortyMortySmith)
- [Jerry](https://ricksanchez.fandom.com/wiki/Jerry_Smith)
- [Gif](https://www.youtube.com/watch?v=vzCAgHASh_U&list=PLT6LA7qWKxZoJJAUZgXHQ0m6UMP8cPBMX&index=25)

</details>

<br>


# Technologies used

- This project is written in Python
- [ChatGPT](https://chat.openai.com/) helped me with articulating myself better in the readme introduction.
- [Github](https://github.com/) was used to create a repository with the help of The Code Institute template.
- [Heroku](https://heroku.com/) was used to deploy my game.
- [Visual Studio Code](https://code.visualstudio.com/) is where I did all my coding.
- [Favicon](https://favicon.io/) was used to create a unique favicon for this blog.
- [Gif](https://ezgif.com/) was used to create a gif for my README.
- [Pickcoloronline](https://pickcoloronline.com/) was used to get exact colour matches.
- [Coolers](https://coolors.co/) was used to create a colour pallate.
- [Image Resizer](https://imageresizer.com/) was used to change all images to webp files.

## balsemiq

## Lucid Flowchart

## Bootstrap

## ElephantSQL

## Cloudinary

## Libraries

<br>


# Testing

## HTML validation

## CSS validation

## JavaScript validation

## Python validation

<br>


# Bug fixes

- I had accidentally added the path to the post_detail page outside of the urlpatterns brackets.
- There was a bug that would throw an error when the socials page is clicked when a user isn't logged in. That got fixed with an if else statement.
- If a user would comment on a post and then refresh, the comment would duplicate. I had to add HttpResponseRedirect to the comment form.
- After I would update my profile picture it would return me to the incorrect user profile. I had to return the correct user pk.
- The update profile message wans't showing, I had placed the message code in the wrong section.
- The edit comment button stopped working, because I had accidentally deleted the .id in the comment.

<b>I have not noticed any existing bugs.</b>

<br>


# Deployment

## Heroku deployment

To deploy Your App to Heroku, you have to :
- Create a Heroku account.
- From the dashboard select create new app.
- Enter a name for your app, it needs to be unique, and select your region then press create app.
- Select settings at the top of your app page.
- Press reveal config vars.
- If the user is using google sheets in their project, you'll have to name your credentials file in the key input and copy and paste that credential file in the value input.
- Also add PORT in key input and 8000 as value input.
- Scroll down and press the add buildpack button.
- From here press the Python icon and then the add buildpack button.
- Add another builpack and press the Nodejs icon this time and then press add buildpack button again.
- Scroll back up and select Deploy at the top of your app page.
- Choose your deployment method, when choosing Github, you will have to connect to your account.
- Then choose which repo you want to deploy and connect to it.
- Choose if you want to deploy automatic or manual, and press deploy.

## Github deployment

To fork this repository on Github, you have to :
  - Go to my [GitHub repository called PP4](https://github.com/ObiWanBonobi/PP4).
  - In the top-right corner of the page, click Fork.
  - Under "Owner," select the dropdown menu and click an owner for the forked repository.
  - By default, forks are named the same as their upstream repositories. Optionally, to further distinguish your fork, in the "Repository name" field, type a name.
  - Click Create fork.

To clone this repository, you have to :
  - Go to my [GitHub repository called PP4](https://github.com/ObiWanBonobi/PP4).
  - Above the list of files, click  Code.
  - Copy the URL for the repository.
  - Open Git Bash.
  - Change the current working directory to the location where you want the cloned directory.
  - Type git clone, and then paste the URL you copied earlier.
  - Press Enter to create your local clone.

You can see the deployed blog [here](https://prof-oaks-blog-0421d28e5692.herokuapp.com/).

<br>


# Credits

- <b>Inspiration and code</b> : I got most of my code and inspiration from 2 different walkthroughs that I combined, [Code Institute Blog](https://github.com/Code-Institute-Solutions/blog) and [Django Social Network](https://realpython.com/django-social-network-1/).
- <b>Django</b> : I learned a lot from the [official Django website](https://www.djangoproject.com/).
- <b>Json file</b> : I got the pokemon data for my json file, from this [pokemon database on github](https://github.com/sohailpervaiz/pokemon-database).
- <b>Blogs</b> : I got all the blog content from the following websites:
    * https://www.ign.com/articles/palworld-vs-pokmon-comparison-just-how-similar-are-the-designs
    * https://screenrant.com/pokemon-first-created-rhydon-original-design-dinosaur/
    * https://gamerant.com/pokemon-generation-one-popular-rumors-everyone-believed/#mew-under-the-truck
    * https://screenrant.com/pokemon-ash-serena-married-xyz-anime/
    * https://theconversation.com/pokemons-ash-wins-world-championship-after-25-years-heres-why-the-franchise-is-still-capturing-fans-194788
    * https://gamerant.com/best-pokemon-each-type/#fire-ndash-charizard
    * https://gamerant.com/pokemon-ash-ketchum-most-used-types/#flying---13
    * https://www.zavvi.com/blog/gaming/the-top-10-most-powerful-pokemon/#:~:text=Arceus&text=By%20far%20the%20most%20naturally,to%20control%20other%20Legendary%20Pok%C3%A9mon.
    * https://www.zavvi.com/blog/features/pokemon-game-fan-theories/
    * https://www.wikihow.com/Is-Pokemon-Demonic
    * https://gamerant.com/pokemon-worst-type-combinations-ranked/#bug-grass
    * https://gamerant.com/pokemon-trainers-anime-ash-better-worse-beat/#can-39-t-beat-ash-jessie-and-james

- <b>Most of my credit goes to the Code Institute program where I made notes on every section and got most of my ideas and code from there.</b>