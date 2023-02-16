# CS50 Web Programming with Python and JavaScript

## Project 2
### Spec
Complete the implementation of your auction site. You must fulfill the following requirements:

* ~~**Models**: Your application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.~~
* ~~**Create Listing**: Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).~~
* **Active Listings Page**: The default route of your web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).
* **Listing Page**: Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing.
    * If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.
    * If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.
    * If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
    * If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.
    * Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.
* **Watchlist**: Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.
* **Categories**: Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.
* ~~**Django Admin Interface**: Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.~~

### Hints
* To create a superuser account that can access Django’s admin interface, run `python manage.py createsuperuser`.
* See Django’s Model field reference for possible field types for your Django model.
* You’ll likely need to create some Django forms for various parts of this web application.
* Adding the `@login_required` decorator on top of any view will ensure that only a user who is logged in can access that view.
* You’re welcome to modify the CSS as much as you’d like, to make the website your own! Some sample screenshots are shown at the top of this page. These are meant only to be examples: your application need not be aesthetically the same as the screenshots here (you’re encouraged to be creative!).

### How to Submit
1. Visit [this link](https://submit.cs50.io/invites/89679428401548238ceb022f141b9947), log in with your GitHub account, and click Authorize cs50. Then, check the box indicating that you’d like to grant course staff access to your submissions, and click Join course.
2. Install Git and, optionally, install submit50.
    > When you submit your project, the contents of your web50/projects/2020/x/commerce branch should match the file structure of the unzipped distribution code as originally received. That is to say, your files should not be nested inside of any other directories of your own creation. Your branch should also not contain any code from any other projects, only this one. Failure to adhere to this file structure will likely result in your submission being rejected.
    > 
    > By way of example, for this project that means that if the grading staff visits https://github.com/me50/USERNAME/tree/web50/projects/2020/x/commerce (where USERNAME is your own GitHub username as provided in the form, below) we should see the two subdirectories (auctions, commerce) and the manage.py file. If that’s not how your code is organized when you check, reorganize your repository needed to match this paradigm.
3. If you’ve installed submit50, execute 
   `submit50 web50/projects/2020/x/commerce`
   Otherwise, using Git, push your work to https://github.com/me50/USERNAME.git, where USERNAME is your GitHub username, on a branch called web50/projects/2020/x/commerce.
4. Record a screencast not to exceed 5 minutes in length (and not uploaded more than one month prior to your submission of this project), in which you demonstrate your project’s functionality. Be certain that every element of the specification, above, is demonstrated in your video. There’s no need to show your code in this video, just your application in action; we’ll review your code on GitHub. [Upload that video to YouTube](https://www.youtube.com/upload) (as unlisted or public, but not private) or somewhere else. In your video’s description, you must timestamp where your video demonstrates each of the seven (7) elements of the specification. **This is not optional**, videos without timestamps in their description will be automatically rejected.
5. Submit [this form](https://forms.cs50.io/b87fb5a9-d373-44ba-aa98-94d4ee3eed38).
