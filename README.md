[![Build Status](https://travis-ci.org/erichaase/atlassian.svg)](https://travis-ci.org/erichaase/atlassian)

# Description
* Input: a chat message (string)
* Output: JSON describing the message's special content (string)

## Special Content

### Mentions
* Format: @username
* Description: a way to mention a user, always starts with an '@' and ends when hitting a non-word character
* Reference: [How do @mentions work? – Help Center](http://help.hipchat.com/knowledgebase/articles/64429-how-do-mentions-work-)

### Emoticons
* Format: (emoticonname)
* Description: ASCII strings representing 'custom' emoticons, no longer than 15 characters, contained in parenthesis (you can assume that anything matching this format is an emoticon)
* Reference: [HipChat - Emoticons](https://www.hipchat.com/emoticons)

### Links
* Format: http(s)://...
* Description: any URLs contained in the message, along with the page's title

# Examples
See test cases in `test/test_hip_chat.py`

# Test
1. sudo pip install -r requirements.txt
2. py.test
