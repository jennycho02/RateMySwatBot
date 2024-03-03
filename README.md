# MySwatBot Project Build

**Collaborators**: Emma Stavis, Jenny Cho, Liv Medeiros-Sakimoto

**Course**: CPSC091R Social and Crowd Computing - Fall 2023 Under the Supervision of Professor Sukrit Venkatagiri

___
## Installation:

1. Install virtualenv:
`pip3 install virtualenv`
   
2. Create your virtual environment:
   `virtualenv venv`

3. Actrive your virtual environment:
   `source venv/bin/activate`

4. Install Mastodon, Flask and its dependencies within your virtual environment:
   `pip3 install Mastodon.py`
   `pip3 install flask`

5. Create a file called "user_token" in the main directory. Add your user authentication token to this file, e.g., "asdf4348sdgaj4r". This will allow you to access your Mastodon account from the app. Note that it is added to the .gitignore file so you don't accidentally push it to GitHub.
   



## Running the app:
`my_app` is the main directory or "application factory" for Flask and `__init__.py`` tells Python that the `my_app` directory should be treated as a package. To run your flask app:

`flask --app my_app run --debug --port 8000`

Note that if you can't access the app on that port, try a different one, like 5000 or 8080.
Also note that it takes a bit to boot up occasionally. 


## Our Structure:
- `my_app` is the main directory or "application factory" for Flask
- `__init__.py` is the main app that handles incoming requests for your web server
- `templates` is the directory that holds all of your HTML files
- `static` is the directory that holds all of your CSS and Javascript files
- `initialize_db.py` is code that defines database tables and has commented-out code that initializes the database entries when run
- `stream.py` listens for DMs on Mastodon


___
Our team chose to pursue the problem surrounding a course-specific review site for a few reasons. First, as Swarthmore students, we experience the problem that every Swattie faces: we don’t have an objective way to learn about courses (regardless of rotating professors?) from other students. We understand what it’s like to register for a class without any context or preconception of what the realistic course expectations are (aside from those made public on course syllabi). This demonstrates our dedication to solving the problem and our interest in finding an effective solution for the Swarthmore community. In comparison to the other two problems we came up with as a group, which focused on 1) Swarthmore’s club events communications issue and 2) the problem of the never-ending stream of depressing global news, this bot targets a more universal Swarthmore and college student experience. Moreover, after conducting more research on the Mastodon API, we also believe that implementing a private Swarthmore course rating bot is a reasonable first challenge for piggyback prototyping on the platform. Building a good news bot would be a fairly simple project, and building an entirely new club communication system is logistically challenging. This is a problem that warrants at least a semester of problem-solving. Given the impact this project could have on the Swarthmore College community, we want to make sure it is built right. With features like opt-in post anonymity and standardized course polls, we hope to help students find the most relevant courses according to their interests at Swarthmore through our Rate My Swat Bot on Mastodon. 

The issues we are trying to address are a common concern across all college campuses: how to decide which courses to take and which professors to study under. While platforms such as ratemyprofessor.com work well in larger academic institutions, smaller colleges like Swarthmore face challenges in replicating that success. RateMyProfessor relies on a high volume of student feedback, and Swarthmore simply cannot keep up with the thousands of reviews other schools accumulate, making it difficult to provide a fair representation of a course or professor. At Swarthmore, there is a constantly changing array of courses with rotating professors, leaving students unsure whether a class will benefit their academic journey or prove detrimental. However, this uncertainty has fostered a culture of open communication among students about their experiences. Swarthmore students have flocked to other platforms such as Facebook and Instagram to create spaces where they can seek and share information about courses and professors. Nevertheless, these social media apps were not designed with the specific needs of course evaluations in mind, such as keeping a record of these reviews over multiple years. Given the diverse focuses of these platforms, which range from photo sharing to content creation, they do not provide a focused and dedicated space for students to exchange valuable insights regarding their academic choices. Thus, in response to this challenge, we would like to take the opportunity to incorporate successful aspects of ratemyprofessor, such as a rating scale assessing basic qualities on difficulty and quality, as well as the inclusion of sections for individual comments, into our project. A study titled “Does ratemyprofessor.com really rate my professor?” by Otto et al. (2008) suggests that online ratings can be valid measures of instructors' abilities to inspire learning, they have the potential to be valuable tools for students in selecting professors and for instructors in improving their teaching methods. However, the study also shows a lack of clarity in determining factors for course reviews, resulting in biased and unclear evaluations from individual interpretations of survey questions. To limit this bias, it also suggests revising the surveys to clarify terms such as easiness, making definitions more prominent and collecting additional information like the level of interest in the course (Otto et al., 2008).

The first component of our proposed solution is a website on which users can search for courses at Swarthmore and then see all previous reviews for that course. If a course does not have any reviews yet, the user can select an option that will “post to Mastodon” to solicit reviews. Moreover, even if a course has reviews, a student can request a boosting post to Mastodon. In this posting step, we would use the API to have a bot post a simple message on Mastodon calling for users to reply with reviews for the course to that post. With the Mastodon API, we will always be listening for replies to our bot’s posts. On these events, we will take the content of the post (the review) and add it to the appropriate course’s review page on the website. Similarly, we will listen for DMs to our bot. If users want to DM us to retain anonymity, they are able to do so as long as they write the course code (e.g. CS41) at the beginning of their message. On these DM events, we will similarly add it to the appropriate course’s review page on our website. 


___
___



