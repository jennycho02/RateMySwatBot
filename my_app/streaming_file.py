from mastodon import Mastodon, StreamListener
import mastodon
import time


f = open("./user_token",'r')
access_token = f.readlines()[0]
f = open("./key",'r')
API_KEY = f.readlines()[0]

instance = "https://social.cs.swarthmore.edu"
# Creates an instance of the Masotodon class 
mastodon = Mastodon(
    access_token=access_token,
    api_base_url=instance
)

# Variable to store comment ID and content 
conversation = []
# Define the StreamListener class
class StreamListener(StreamListener): 
    def on_conversation(self, conversation):
        print(conversation)
        client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=API_KEY,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
        )

        analyze_request = {
        'comment': { 'text': conversation },
        'requestedAttributes': {'TOXICITY': {}, 'PROFANITY': {}, 'IDENTITY_ATTACK': {}}
        }
        response = client.comments().analyze(body=analyze_request).execute()
        print(json.dumps(response, indent=2))

        #add threshold if else
        #if ok, add to database


        #else
        # user = conversation['user']
        # content = "Your review was flagged as potentially harmful. Please adjust your message and try again."
        # m = Mastodon(access_token=access_token, api_base_url="https://social.cs.swarthmore.edu")
        # m.toot(content, visility = "direct")



    

# Creates an instance of custom StreamListener 
listener = StreamListener()

# Start streaming with the custom listener
def getDMS(): 
    mastodon.stream_direct(listener, run_async=True, timeout=300, reconnect_async=False, reconnect_async_wait_sec=5)
    return conversation 

