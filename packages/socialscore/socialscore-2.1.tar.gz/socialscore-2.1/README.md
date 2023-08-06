# social_score : Calculate the score of a social media profile and posts on twitter and other social media sites on the internet
This repository contains the opensource implementation of the research  paper titled "Calculate the score of a social media profile and posts on twitter and other social media sites on the internet". 

#### Paper Title: Calculate the score of a social media profile and posts on twitter and other social media sites on the internet

#### Authors: [Pooja Chaudhary](https://pooja-chaudhary.github.io), [Ravin Kumar](https://mr-ravin.github.io)

#### Publication:  23<sup>rd</sup> August, 2021.

#### Publication Journal: [Advances in Computers and Electronics](https://www.syncsci.com/journal/ACE/index).

#### Publication House: [SyncSci Publishing](https://www.syncsci.com).

#### Publication link: https://doi.org/10.25082/ACE.2021.01.003 

#### Cite as:

```
Chaudhary, P., & Kumar, R. (2021). Calculate the score of a social media profile and posts on twitter and other social media sites on the internet. 
Advances in Computers and Electronics, 2(1), 22-24. https://doi.org/10.25082/ACE.2021.01.003
```

#### Doi: [10.25082/ACE.2021.01.003](https://doi.org/10.25082/ACE.2021.01.003)

#### Earlier preprints: 
- OSF Preprints: https://doi.org/10.31219/osf.io/sme2a
- SSRN Preprints: https://ssrn.com/abstract=3861433 

#### Prerequisites 

- [Tweepy Library](https://github.com/tweepy/tweepy)

### Steps for using this library
```python
import socialscore
### pass username , and degree_score along with the login credentials for twitter app.
res=socialscore.social_score(consumer_key,consumer_secret,access_token,access_token_secret,username,degree_score) 
###res contains the social score value.
```

### Installing module using PyPi
```python
pip install socialscore
```

```python
Copyright (c) 2013-2021 Pooja Chaudhary, Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
