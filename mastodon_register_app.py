from mastodon import Mastodon

Mastodon.create_app(
    'pytooterapp2', #use a different app name
    scopes = ['read', 'write', 'follow', 'push'],
    redirect_uris = 'https://127.0.0.1:8000/user/login/',
    website = 'http://127.0.0.1:8000/',
    api_base_url = 'https://social.cs.swarthmore.edu',
    to_file = 'clientcred.secret'
)
