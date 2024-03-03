# MySwatBot Project Build



## Submission Statement

**Collaborators**: Emma Stavis, Jenny Cho, Liv Medeiros-Sakimoto

**Course**: CPSC091R Social and Crowd Computing - Fall 2023

___

# Setting up the Project



## Resources
GitHub refresher: https://coderuse.com/2017/10/A-Short-Refresher-On-Git/

Flask Quick Start Guide: https://flask.palletsprojects.com/en/3.0.x/quickstart/

Intro to HTML Guide: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started

Python refresher: https://code.tutsplus.com/series/a-smooth-refresher-to-python–cms-950

Introduction to Flask: https://pymbook.readthedocs.io/en/latest/flask.html, https://opensource.com/article/18/4/flask

Introduction to Jinja2 template language: https://realpython.com/primer-on-jinja-templating/



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

## Build 2: Write-up Portion


### AI/ML for Content Moderation

For our Swarthmore course review Mastodon bot and web application, the @RateMySwat bot, we’ve decided to leverage AI and ML to perform content moderation as we receive and filter through user-submitted (via DM to our bot) course reviews. There’s some complexity involved with 1) the order of user input through a DM to our bot on Mastodon, 2) the API call to moderate the content of the submitted review, 3) database integration contingent on the API results, and 4) a message notifying the user if the content of their submitted review does not pass our moderation check (outlined by our community guidelines). In other words, if a submitted course review does not pass the content moderation check via the chosen API, we will not add it to our database and will instead let the user know that their submission has not been accepted (try again message from our bot in a DM). Ultimately, we decided to go with Perspective API in order to achieve the necessary level of content moderation.



### Why Perspective API?

In selecting the Perspective API for RateMySwatBot’s content moderation, our considerations were centered around both developer and user criteria. As developers, the crucial factors included the API’s ease of use and customization options, which allowed us to 1) seamlessly integrate content moderation into our workflow with minimal complexity and 2) tailor the entire moderation system to custom levels of toxicity (and other flags) necessary for our specific needs.This individualized detection system could easily align with our community guidelines, which leads us into the user perspective. For our reviewers, the most important feature is the effectiveness and easily communicable nature of the content moderation system, ensuring that submitted course reviews adhered to community standards and could be flagged if certain policies were violated. The API’s free availability was also significant, making it the optimal choice for our project in the end.

### API Comparison Table

Below, we’ve outlined the three different APIs we researched, along with the specific criteria that helped us choose which one to use in our application. 

| **Criteria** | [**Perspective API**](https://developers.perspectiveapi.com/s/docs?language=en_US) | [**OpenAI API**](https://platform.openai.com/docs/api-reference/introduction) | [**Moderation API**](https://docs.moderationapi.com/get-started/quickstart) | 
| -------- | --------------- | ---------- | -------------- |
| Cost     | Free            | Not free   | Not free       | 
| Speed | Fast, does | Fast, depending on length of query | Fast, but also query dependent |
| Ease of use | Easy and perfectly customizable (and testable) for our particular use-case | Easy, straightforward parameters for chat-completion responses but difficult to apply in this use-case | Unclear, but extremely customizable and tailored to account needs |
| Documentation quality | Minimal but straightforward and effective | Extensive | Extensive |
| Sentiment detection quality | Customizable toxicity detectors for content | No standardized sentiment detector | Customizable moderation thresholds |
| Translation functionality | Yes, ability to understand some input from another language | Yes, understands input and can provide output in another language if specified | Yes, also uses AI to translate input and output in specified language if necessary |







___




## Build 2: [Group Thoughts](https://docs.google.com/document/d/1-v4gEQ9IFtPYOGUT0f2MCDkdrRJ4xs-TLDMCWycukB4/edit)

### Notes

- How much of the information on this site can already be inferred by our audience?
- Seasoned Swatties are likely familiar with differences between STEM and SS courses (problem sets versus open dialogue/discussion)
- But freshman (who would most likely benefit the most during their orientation registration), might not have this same context for Swarthmore courses
- What about a discussion page where people can pose questions that people can respond to?

### More Questions 11/16

**Q: How to make our mastodon server/set up user permissions**

- Do not need to address for this project
- Everyone in the class will be the members of our mastodon server
- Address this in theory for the last part of this project


**Q: Best way to listen for new DMs and update our database**

- How do we know when a new DM needs to be read into the database
- OPTION: You could use the streaming function (prof can provide some example code)
- In an ideal world, you should be streaming all the time
- This is when you have your server up and running, then you should be able to handle reading in the message (but if the server is down, you do not need to handle that)


**Q: Database in general**

- It is a file, really - something called instances with a folder
- The larger and larger it gets, you can outsource to aws but this is not necessary for our project
- Create one database of classes and one database of users, and then an other database of reviews (and then link them together with a key, a primary key)

**NOTE: Relational databases**

- Don't need to do this now but eventually the idea could be that you update this like once a semester and run the python script to update the database
- For now, we’ll write the python script that will take all the class info from the csv and put it into the database as a primer (just once)
- And then we have a handler (event handler that handles an event) that when we get a DM, we send it to perspective
- If it passes perspective, we add it to the database, if it’s not, then we send it back to the user with a template message 



### Questions 11/8

- How to make our mastodon server/set up user permissions
- Best way to listen for new DMs and update our database
- Database in general


### Database Search Options

- Database complexity and the information architecture of all the stored review data
- What about an advanced search option to filter? on the website
- On the course display page, being able to filter by professor?


### Mastodon Community

- What about a discussion page where people can pose questions that people can respond to?
(Think of Quora or Stack Overflow)


### Using Perspective

- do not want to duplicate efforts
- we won't even add a review to the database until we have cleared it through Perspective
- if the Perspective moderation does not clear, we send a template message back to the user to notify them





___





## Build 1: Work Delegation 

We decided that working on all of the pieces together would be the most efficient and equal in the end, since each of the three requirements would have very different levels of work. So, all of us worked together on what we have so far!



### Planning for the Flask app 

|   Website Feature      |   Goal    | API Call | 
|   ---------------      | --------- | -------: | 
|   `Home / Search Bar`  |   display fake results (eventually backend database) |  get/post | 
| `Empty Search Results` | request more reviews through a bot post |  post | 
|   `Write a Review`     | redirect user to Mastodon bot homepage |  na | 

**For future reference**: remember the intricacies of fetching data that we'll need to 1) store in a database and 2) retrieve efficiently.



### Logic and User Flow

1. **Search for a review of a specific class**

        if review found
            → display existing reviews

2. **Empty search results**

        if no review found 
            → button to request reviews
                if pressed:
                    → redirect to request form resembling course review form

3. **Write a review**

        button to write a review
            → mastodon authentication
            → direct message to bot template



### Tasks Moving Forward

**"Search" Bar and Display**
- [X] located on the home page
- [X] hard-coded backend for now
- [X] html for search bar and button
- [ ] get and display backend aesthetically

**"Request Reviews" Form**
- [X] located on a separate page/shown when no reviews
- [X] html structure for more form fields
- [X] typeable dropdown (hard-coded database for now)
- [ ] if time: success page?

**"Submit a Review" Form**
- [X] button upper right of home page
- [X] redirect to mastodon code
- [X] look into html template messages (like email lets you write)
- [X] if time: success page?



___
___





# Project Goals Write-up

### Part I
***In one paragraph, describe why you chose this problem among the three. This description should convince the reader that this is a difficult and interesting problem, worth spending a semester considering. State what the problem is and why it is a problem, or describe a new idea and why it will enhance an existing application or practice.***

Our team chose to pursue the problem surrounding a course-specific review site for a few reasons. First, as Swarthmore students, we experience the problem that every Swattie faces: we don’t have an objective way to learn about courses (regardless of rotating professors?) from other students. We understand what it’s like to register for a class without any context or preconception of what the realistic course expectations are (aside from those made public on course syllabi). This demonstrates our dedication to solving the problem and our interest in finding an effective solution for the Swarthmore community. In comparison to the other two problems we came up with as a group, which focused on 1) Swarthmore’s club events communications issue and 2) the problem of the never-ending stream of depressing global news, this bot targets a more universal Swarthmore and college student experience. Moreover, after conducting more research on the Mastodon API, we also believe that implementing a private Swarthmore course rating bot is a reasonable first challenge for piggyback prototyping on the platform. Building a good news bot would be a fairly simple project, and building an entirely new club communication system is logistically challenging. This is a problem that warrants at least a semester of problem-solving. Given the impact this project could have on the Swarthmore College community, we want to make sure it is built right. With features like opt-in post anonymity and standardized course polls, we hope to help students find the most relevant courses according to their interests at Swarthmore through our Rate My Swat Bot on Mastodon. 

### Part II
***In a second paragraph, analyze the problem or idea to give more background and context. Do not just focus on the negative aspects of the current situation, but also identify some positive aspects that may be beneficial to retain. A few salient examples from existing systems or practices could be used to support those claims. If appropriate, you may conduct this analysis by describing a scenario that illustrates how someone might encounter and resolve the problem.***

The issues we are trying to address are a common concern across all college campuses: how to decide which courses to take and which professors to study under. While platforms such as ratemyprofessor.com work well in larger academic institutions, smaller colleges like Swarthmore face challenges in replicating that success. RateMyProfessor relies on a high volume of student feedback, and Swarthmore simply cannot keep up with the thousands of reviews other schools accumulate, making it difficult to provide a fair representation of a course or professor. At Swarthmore, there is a constantly changing array of courses with rotating professors, leaving students unsure whether a class will benefit their academic journey or prove detrimental. However, this uncertainty has fostered a culture of open communication among students about their experiences. Swarthmore students have flocked to other platforms such as Facebook and Instagram to create spaces where they can seek and share information about courses and professors. Nevertheless, these social media apps were not designed with the specific needs of course evaluations in mind, such as keeping a record of these reviews over multiple years. Given the diverse focuses of these platforms, which range from photo sharing to content creation, they do not provide a focused and dedicated space for students to exchange valuable insights regarding their academic choices. Thus, in response to this challenge, we would like to take the opportunity to incorporate successful aspects of ratemyprofessor, such as a rating scale assessing basic qualities on difficulty and quality, as well as the inclusion of sections for individual comments, into our project. A study titled “Does ratemyprofessor.com really rate my professor?” by Otto et al. (2008) suggests that online ratings can be valid measures of instructors' abilities to inspire learning, they have the potential to be valuable tools for students in selecting professors and for instructors in improving their teaching methods. However, the study also shows a lack of clarity in determining factors for course reviews, resulting in biased and unclear evaluations from individual interpretations of survey questions. To limit this bias, it also suggests revising the surveys to clarify terms such as easiness, making definitions more prominent and collecting additional information like the level of interest in the course (Otto et al., 2008).

### Part III
***In a third paragraph, describe your proposed solution using the Mastodon API. It can be a high-level overview about how your proposed solution can be built using the Mastodon API.***

The first component of our proposed solution is a website on which users can search for courses at Swarthmore and then see all previous reviews for that course. If a course does not have any reviews yet, the user can select an option that will “post to Mastodon” to solicit reviews. Moreover, even if a course has reviews, a student can request a boosting post to Mastodon. In this posting step, we would use the API to have a bot post a simple message on Mastodon calling for users to reply with reviews for the course to that post. With the Mastodon API, we will always be listening for replies to our bot’s posts. On these events, we will take the content of the post (the review) and add it to the appropriate course’s review page on the website. Similarly, we will listen for DMs to our bot. If users want to DM us to retain anonymity, they are able to do so as long as they write the course code (e.g. CS41) at the beginning of their message. On these DM events, we will similarly add it to the appropriate course’s review page on our website. 









___
___



