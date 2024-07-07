Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##### working with strings#####
>>> my_text='hello, my name's george'##error
SyntaxError: unterminated string literal (detected at line 1)
>>> my_text="hello , my name's george"
>>> print(my_text)
hello , my name's george
>>> my_text="hello , my name is george"
>>> my_text=my_text.replace("george","John")#string replace
>>> print(my_text)
hello , my name is John
>>> 
>>> 
>>> current_top_album="for all the dogs"
>>> 
>>> ##convert to lowercase ##
>>> current_top_album=current_top_album.lower()
>>> print(current_top_album)
for all the dogs
>>> 
>>> ### change to uppercase
>>> current_top_album=current_top_album.upper()
>>> print(current_top_album)
FOR ALL THE DOGS
>>> review_one=""" I really enjoy the courses,
... and they are easy to fit into my busy schedule. 
... I wish I had started using your platform sooner.
... I'll be recommending you to my friends!! """
>>> print(review_one)
 I really enjoy the courses,
and they are easy to fit into my busy schedule. 
I wish I had started using your platform sooner.
I'll be recommending you to my friends!! 
>>> review_two=""" One year ago I was unsure of how to make progress in my career. 
... Now I work as a Prompt Engineer and I can't thank you enough! 
... Keep up the great work. """#multi line string
>>> review_two
" One year ago I was unsure of how to make progress in my career. \nNow I work as a Prompt Engineer and I can't thank you enough! \nKeep up the great work. "
