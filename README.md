# **StrawTarget**
![Photo of StrawTarget](https://github.com/TechnicSmile/StrawTarget/blob/master/strawtarget.PNG)
What is StrawTarget?
StrawTarget is easy to use and well designed https://strawpoll.me vote botting app created to showcase how easy webpage botting is. Strawtarget can launch votes quickly and accurately and even bypass strawpolls with captcha.
## Setup
>Setting up strawpoll is simple but you just need to follow all of the steps. :)
1. First off make sure you have [python](https://www.python.org/) installed and make sure you set it up with path variables.
2. Once you have python installed go to your cmd and type "pip install -r requirements.txt" (This will install all the required python libraries for this project.
3. You will next have to make sure you have selenium fully [setup](https://selenium-python.readthedocs.io/installation.html)4.Note:
    - This project is using chromium so make sure that you install that and setup up all the path variables.
4. For this project you can either use the proxies provide your own(This is the best solution by far), just stick all proxies in the proxies.txt file.
5. Launch the python file and input all the correct inputs.
6. There you go thats it, it should fully work if there any issues I reccomend you either make an issue request or check troubleshoot.
## Options
There are 2 main options with StrawTarget
### Normal
Normal means that there is no captcha, this will solve strawpoll quickly and efficently. It bots whatever vote you want fairly quickly saying you have a decent proxy list. This one will likely be what you encounter with most strawpolls.
### Captcha Bypass
This option is the second option of StrawTarget, it will try and beat the captcha (which has a 1/1000) chance and it will repeat untill it gets a working one. This all comes down to luck with the captcha option but still works pretty constistantly.
## TroubleShoot
If you are having any issue they could be related to a number of reasons:
- You did not setup the selenium chromedriver correctly(Most likely path variables).
- You failed to input the correct input type, StrawTarget requires all user inputs to be lowercase and have dashes isntead of spaces.
- Python isn't installed correctly.
- The proxies are outdated, if this is the case you will need to find some fresh https proxies.
## ToDoList
- [ ] Speed up voting proccess (Not allow the page to fully load ads(Heavily slows down slowtarget))
- [ ] Make it more user friendly.
- [ ] Change the captcha do have a higher bypass rate.
## Legal
By using this you do not hold the creator responsible for creating this bot. This bot was mainly created to demonstrate for eductational purposes security vunerabilities and the accesibility of faking user inputs. This bot is supposed to showcase all of this in a smooth, clean way and educational way. Please do not break the tos if you have questions about the tos check [here](https://www.fandom.com/curse-terms-of-service)
