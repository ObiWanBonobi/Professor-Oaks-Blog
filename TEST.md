# Professor Oak's Tests

Click [here](README.md) to go back to the README.md file.

## Content

- [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript experience](#javascript-validation)
    * [Python Validation](#css-validation)
    * [CSS Validation](#css-validation)

<br>


# Validation

## HTML Validation

[W3C validator](https://validator.w3.org/) was used to check the HTML files. I had placed buttons inside of anchor elements that came up as an error, they got changed into div's. I had also accidentally left an extra </script> endtag, that also got deleted. The other errors that were shown, are related to Django.

| **File** | **Template** | **Result** |
|---|---|---|
| templates | base.html | &#10004; |
| templates | login.html | &#10004; |
| templates | logout.html | &#10004; |
| templates | signup.html | &#10004; |
|-|-|-|
| blog | index.html | &#10004; |
| blog | post_detail.html | &#10004; |
|-|-|-|
| database | database.html | &#10004; |
|-|-|-|
| user_profile | socials.html | &#10004; |
| user_profile | profile.html | &#10004; |
| user_profile | update_profile.html | &#10004; |

## CSS Validation

[Jigsaw W3C validator](https://jigsaw.w3.org/css-validator/) was used to check the CSS file. No errors were found.

| **Parent File** | **File** | **Result** |
|---|---|---|
| static | style.css | &#10004; |

## JavaScript Validation

[JShint](https://jshint.com/) was used to check my JavaScript files. I had missed one semicolon and that was it.

| **Parent File** | **File** | **Result** |
|---|---|---|
| static | comments.js | &#10004; |
| static | delete_profile.js | &#10004; |
| static | top_button.js | &#10004; |

## Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check every python file. I fixed all the lines that were too long

| **App** | **File** | **Result** |
|---|---|---|
| profoak | settings.py | &#10004; |
| profoak | urls.py | &#10004; |
|-|-|-|
| blog | admin.py | &#10004; |
| blog | forms.py | &#10004; |
| blog | models.py | &#10004; |
| blog | urls.py | &#10004; |
| blog | views.py | &#10004; |
|-|-|-|
| database | admin.py | &#10004; |
| database | models.py | &#10004; |
| database | urls.py | &#10004; |
| database | views.py | &#10004; |
|-|-|-|
| user_profile | admin.py | &#10004; |
| user_profile | models.py | &#10004; |
| user_profile | urls.py | &#10004; |
| user_profile | views.py | &#10004; |