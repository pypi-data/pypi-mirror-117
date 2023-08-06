# **Telegram bot just by calling one function.**

### Description:
If you have some functions and you want to **bot them** use **bottem** :wink:  
<br>
Actually, it is just a wrapper for pyrogram and adds a command handler for all of your module functions.

___
### Requirements
* Python3+
* Pyrogram

___
### Usage:
```sh
cp config.init.example config.init
vi config.init
```
```python
from . import my_module
from bottem import Bottem

Bottem(my_module)
```
**my_module.py**:
```python
def hello(*args):
    return "Hello World!"

def echo(*words):
    return " ".join(words)
```  
Then you just need to send commadn to your bot:  
* `/echo This text is echoed.` to receive `This text is echoed.` reply  
* `/hello` to receive `Hello World!` reply.
___
### Config file
* `api_id` from [telegram](https://my.telegram.org/apps)
* `api_hash`
* `bot_token` from [botfather](https://t.me/botfather)

Read [pyrogram](https://docs.pyrogram.org/topics/config-file) for more config info.  
___

PS:  
BTW I've stolen this README.md from this [repo](https://github.com/tamton-aquib)
