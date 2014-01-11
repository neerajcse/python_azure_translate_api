python_azure_translate_api
==========================
Python module for Microsoft Translator API

Published under BEERWARE LICENSE.

 ----------------------------------------------------------------------------
 "THE BEER-WARE LICENSE" (Revision 43):
 <neerajkumar@outlook.com> wrote this file. As long as you retain this notice you
 can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer in return. 
 If you are reading this in the second half the the 21st century, then I am at 
 an age which won't allow me to metabolize any kind of alcohol, so please
 treat yourself with a beer on my behalf.
 -Neeraj Kumar
 ----------------------------------------------------------------------------

This python module enables you to use the Microsoft Translator API.

It : 
* Has a very simple interface to use.
* Caches the auth token till it times out.
* Gracefully handles network (or other) failures by adding a retry logic

Dependencies:
* Retry module (found in the same repo)
* time
* datetime
* json
* math
* urllib
* urllib2
