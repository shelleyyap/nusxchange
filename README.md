# NUSXchange README
### For developer's purposes
##### Log of uncompleted features / details
1. Add University validation cleanup (~~currently using html validation, allows non-image file uploads[fixed]~~; ~~currently also allows duplicate short_name~~[KY will work on it]) 
2. search function [attempted- mostly working fine. Need to do reindexing when submitting/editing review]
4. remove duplicates for module mapping (low priority)
5. admin version of module mapping page (KY will work on it):~~delete function~~, add module mapping function?
6. allow user to edit own review (YYY will work on it) (half done, not done with module mappings as it requires preventing adding same module mappings. Jquery part not fixed either)
7. ~~allow admin to edit university info, delete university~~ (both done)
8. ~~Fix comments: Currently accepts empty comments, character limit?~~ (both done)
9. Fix reviews: ~~'input should be properly sanitised so as to prevent XSS attacks (see piazza)'~~, WYSIWYG editor (KY will work on it)
10. Clean up review formatting, e.g. display double majors, date etc.
11. unregistered user can still add a review but they will encountered an error (try accessing http://www.nusxchange.appspot.com/tosubmitreview?school=MgU without signing in)
11. Countries page: not in alphabetical order; when there are many universities, text exceeds box, also looks weird on phone screen

##### Possible features to work on
1. Allow anonymous posting of reviews and comments
2. Upvote, downvote for reviews. Anonymous reviews lower ranking
3. Pie chart for expenditure
4. Use IVLE API?
5. Web crawler to add universities
6. Search reviews by majors
7. Allow replies for comments
8. More accessible submit review button? (must scroll all the way down, troublesome if there are many reviews)

##### References
1. Including third-party python libraries in GAE (BeautifulSoup): http://stackoverflow.com/questions/14850853/how-to-include-third-party-python-libraries-in-google-app-engine
2. Sanitising user input: http://stackoverflow.com/questions/16861/sanitising-user-input-using-python
3. Deleting a module mapping: http://stackoverflow.com/questions/17950774/app-engine-datastore-python-delete-element-within-a-structuredproperty

##### Notes
1. Delete module mapping does not work immediately, leads to blank page, but is deleted when you check again, similar to AddUniversity
2. Changed implementation of module mappings, now each module mapping has a unique id (ie no 2 module mappings within a school have the same id)
