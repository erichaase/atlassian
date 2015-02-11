import json
from atlassian.hip_chat import get_properties

def test_mention ():
    message  = "@chris you around?"
    result   = get_properties(message)
    expected = json.dumps({
        "mentions" : [
            "chris"
        ]
    })
    assert result == expected

def test_emoticon ():
    message = "Good morning! (megusta) (coffee)"
    result   = get_properties(message)
    expected = json.dumps({
        "emoticons" : [
            "megusta",
            "coffee"
        ]
    })
    assert result == expected

def test_link ():
    message = "Olympics are starting soon; http://www.nbcolympics.com"
    result   = get_properties(message)
    expected = json.dumps({
        "links" : [
            {
                "url"   : "http://www.nbcolympics.com",
                "title" : "NBC Olympics | Home of the 2016 Olympic Games in Rio"
            }
        ]
    })
    assert result == expected

def test_all ():
    message = "@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016"
    result   = get_properties(message)
    expected = json.dumps({
        "mentions" : [
            "bob",
            "john"
        ],
        "emoticons" : [
            "success"
        ],
        "links" : [
            {
                "url"   : "https://twitter.com/jdorfman/status/430511497475670016",
                "title" : "Justin Dorfman on Twitter: \"nice @littlebigdetail from @HipChat (shows hex colors when pasted in chat). http://t.co/7cI6Gjy5pq\""
            }
        ]
    })
    assert result == expected
