# NUSXchange README
### For developer's purposes
##### Log of uncompleted features / details
1. Add University validation cleanup (~~currently using html validation, allows non-image file uploads[fixed]~~; ~~currently also allows duplicate short_name~~[KY will work on it]) 
2. ~~search function [attempted: Working fine]~~
4. remove duplicates for module mapping (low priority)
5. admin version of module mapping page (KY will work on it):~~delete function~~, add module mapping function?
6. allow user to edit own review (YYY will work on it) (half done, not done with module mappings as it requires preventing adding same module mappings. Jquery part not fixed either)
7. ~~allow admin to edit university info, delete university~~ (both done)
8. ~~Fix comments: Currently accepts empty comments, character limit?~~ (both done)
9. Fix reviews: ~~'input should be properly sanitised so as to prevent XSS attacks (see piazza)'~~, ~~WYSIWYG editor (KY will work on it)~~
10. Clean up review formatting, e.g. display double majors, date etc.
11. ~~unregistered user can still add a review but they will encountered an error (try accessing http://www.nusxchange.appspot.com/tosubmitreview?school=MgU without signing in)~~
11. ~~Countries page: not in alphabetical order; when there are many universities, text exceeds box~~, also looks weird on phone screen

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
4. Allowing only alphabets and spaces for form input validation: http://stackoverflow.com/questions/2794162/jquery-validation-plugin-accept-only-alphabetical-characters

##### Notes
1. ~~Delete module mapping does not work immediately, leads to blank page, but is deleted when you check again, similar to AddUniversity~~
2. Changed implementation of module mappings, now each module mapping has a unique id (ie no 2 module mappings within a school have the same id)


## Official README

NUSXchange is a web application that aims to provide NUS students intending to go on an exchange programme with detailed information about the partner universities by collating reviews by seniors, so as to help them make the right decision.

This was done as part of NUS’ Orbital Programme, the School of Computing's self-driven programming summer experience designed to give first-year students the opportunity to self-learn and build something useful. It is designed as a 4 modular credit (MC) module that is taken pass/fail (CS/CU) over the summer.

Links
Our webapp: http://nusxchange.appspot.com/
Our video:  https://www.dropbox.com/s/0hvpia9bvtn9i7q/eval3.wmv

###1. Ideation:
With over 180 partner universities from over 40 countries, it is not an easy task to choose the university to exchange with. Programmes, cost, language, culture, weather, module mappings are just a few among the many factors students have to consider. The experiences provided by the seniors and their reviews of their time overseas would be valuable to students deciding to go on an exchange. Our project thus aims to address these concerns by providing them with the relevant information on the web.

Elevator pitch: https://www.dropbox.com/s/xs4u8bwi68ykpfp/Elevator%20Pitch%20by%20P.O.P.mp4
Prototype: https://docs.google.com/presentation/d/12JED2nKL44JNsl2qB2qh21z-JYBrD4uvzNrWc73A__M/pub?start=false&loop=false&delayms=60000


###2. Features

NUSXchange has 5 main features: 
1.	University page
2.	Reviews and comments
3.	Module mappings
4.	Search function
5.	Login

University page:
The university page provides an overview of each partner university, presenting information such as image of the school, introduction to the school, academic calendar, recommended faculties, modules offered, average rating and average expenditure (based on submitted reviews) in a clean presentation. 

Reviews and comments:
Users can submit, edit and delete reviews for partner universities when logged in using their NUS accounts. Each review consists of course of the student, date of exchange, ratings for the university (overall, accommodation, academic experience, student life, cost), estimated expenditure (accommodation, food, transport, academic expenses, others), approved module mappings and review about the school. 
Logged in users may also submit comments where they can share tips and recommendations or ask seniors questions about their experiences.

Module mappings:
This feature allows students to see which modules offered by partner universities were successfully mapped to modules offered by NUS previously, thus aiding students who are planning their modules for exchange in choosing modules that count towards their graduation requirements while allowing them to make the best out of their time during the exchange. This information is collected as part of reviews submitted by seniors and compiled into a table under the link Module Mappings.

Search Feature:
The search feature filters to narrow down the list of universities for the user according to their preferences. The filters are: Countries, Cost, Course(of NUS students). The search textbox allows users to input university names as well.

Login:
There are two types of login: login via Google account for administrators (accessible only via homepage) and login via NUS OpenID for users. Login is required for posting, editing and deleting of reviews and comments to encourage accountability. Users may only edit and delete their own reviews and comments, while administrators may edit and delete all reviews, comments, module mappings and universities. 

###3. Technical Details/other features
Form inputs (adding universities, submitting reviews): 
* Input sanitisation was implemented using Beautiful Soup, with help from (link). 
* CKEditor was used as a WYSIWYG editor for information about the university and review contents, to make it easier for users to format their input. 
* Form validation was implemented using jQuery validator: 
	* All field are required except module mappings and exchange type.
	* University page:
	School name, state: accepts only alphabets and spaces
	Short name (unique identifier of school): must be unique (i.e. does not exist in current database) and accepts only alphabets (no spaces allowed as it is used as part of the url for school page) [cannot be edited]
	Image of university: accepts only image files
	* Submit review:
	Choice of major depends on faculty selected
	Year: accepts only integers from 2000 to 2050
	Expenditure: accepts only non-negative integers, total expenditure is automatically calculated when all values are filled in
	Module mappings: credits accept only non-negative integers. SEP Module credits, NUS Module and NUS Module MCs are required only if SEP Module is filled in

Alert dialogue to confirm delete of universities in case of accidental pressing of delete button. 

###4. Potential features:
i) Upvote/downvote of reviews
ii) Allow anonymous posting of reviews, possibly with lower ranking for anonymous reviews to provide incentive to submit as a logged in user
iii) Present expenditure information in the form of a pie chart
iv) Allow replies for comments


3. Acknowledgements:

Tools used in NUSXchange:
Google App Engine (Python), NDB Datastore, Blobstore, Beautiful Soup, jQuery Validator, jQuery, Bootstrap, HTML, CSS, ckeditor, jinja 

Learning resources:
We would like to thank Du, our advisor, as well as 




References
Tool to be used to create the web application: Google App Engine
References(Currently)
•	Pictures
Thumbs up: http://openclipart.org/detail/173822/thumbs-up-by-qubodup-173822
Thumbs down: http://openclipart.org/detail/173823/thumbs-down-by-qubodup-173823
Countries image: http://www.ipa-usa.org/resource/resmgr/active_officer_exchange/world_flag.png
NUS Exchange: http://www.nus.edu/iro/images/studentexchange/outgoing.jpg
Tuebingen: http://upload.wikimedia.org/wikipedia/commons/4/42/TuebingenUniNeueAula.jpg
ANU: http://upload.wikimedia.org/wikipedia/commons/f/f9/ANU_College_of_Law.jpg
VUW: http://upload.wikimedia.org/wikipedia/commons/a/a0/VUW-Kelburn.jpg
Korea U: http://upload.wikimedia.org/wikipedia/commons/7/74/Korea_University.jpg
Contact: http://www.tnicom.com/images/contact_icon[1].png
Search: http://iromin.files.wordpress.com/2014/01/search-marketing.jpg
Login: http://www.jointcommission.org/assets/1/6/button-login.jpg
Canada: http://www.acoa-apeca.gc.ca/eng/investment/InvestmentHome/PublishingImages/Canada_flag.jpg
Germany: http://www.mars.com/global/assets/images/center-content/german-flag.jpg
Australia: http://wiki.guildwars2.com/images/b/b9/Flag_of_Australia.svg
China: http://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People's_Republic_of_China.svg/1500px-Flag_of_the_People's_Republic_of_China.svg.png
Hong Kong: http://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Flag_of_Hong_Kong.svg/900px-Flag_of_Hong_Kong.svg.png
•	School Websites
NUS SEP: http://www.nus.edu/iro/sep/out/index.html
http://publish.ust.hk/prog_crs/ugcourse/index.html
http://www.ust.hk/eng/about/index.htm
http://www.handbook.unsw.edu.au/vbook2014/brCoursesByAtoZ.jsp?StudyLevel=Undergraduate&descr=A
http://www.unsw.edu.au/about-us
http://www.unc.edu/ugradbulletin/depts/compsci.html
http://studyabroad.unc.edu/incoming/ch_info.cfm
http://www.comp.nus.edu.sg/undergraduates/beyond_sep.html
http://ev.buaa.edu.cn/about_buaa/buaa_today/70338.htm
http://www.su.se/english/about
http://sisu.it.su.se/search/courses/en?area_id=5
•	Learning resources
http://www.codecademy.com/dashboard
Code in the Cloud Programming Google App Engine by Mark C. Chu-Carroll
https://developers.google.com/appengine/docs/python/
•	Others
Bootstrap: http://getbootstrap.com/
Comment box style: http://codepen.io/magnus16/pen/buGiB
Openid: https://openid.nus.edu.sg/
NUS 2014 Mission Controls
(BeautifulSoup) http://stackoverflow.com/questions/14850853/how-to-include-third-party-python-libraries-in-google-app-engine
(Sanitising)http://stackoverflow.com/questions/16861/sanitising-user-input-using-python
(Deleting module mapping) http://stackoverflow.com/questions/17950774/app-engine-datastore-python-delete-element-within-a-structuredproperty

