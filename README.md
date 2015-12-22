# IBMWatsonPersonalityInsights
Python integration to the IBM Watson Platform's Personality Insights engine. Execute the script by passing a Twitter handle as the sole argument, and the PI engine will analyze your personality based on your writing. Includes modified sample from https://gist.github.com/yanofsky/5436496 that uses Tweepy to pull last 3,240 tweets from a given account.

See the README at https://github.com/watson-developer-cloud/personality-insights-python to get started with IBM Bluemix.

Sample output from Mac OS X Terminal:
```
Drews-MBP:IBMWatsonPersonalityInsights drewdepriest$ python twitter-personality.py drewdepriest
getting tweets before 654113633606217731
...400 tweets downloaded so far
getting tweets before 637096139838332927
...600 tweets downloaded so far
getting tweets before 613421173884493824
...800 tweets downloaded so far
getting tweets before 593467470616383487
...1000 tweets downloaded so far
getting tweets before 575417366978367487
...1200 tweets downloaded so far
getting tweets before 544974778205880319
...1400 tweets downloaded so far
getting tweets before 488438180060745727
...1600 tweets downloaded so far
getting tweets before 464549715221442559
...1800 tweets downloaded so far
getting tweets before 448615539494363135
...2000 tweets downloaded so far
getting tweets before 428538127842410495
...2200 tweets downloaded so far
getting tweets before 417547084997218304
...2400 tweets downloaded so far
getting tweets before 403928610668441599
...2600 tweets downloaded so far
getting tweets before 393234418589904896
...2800 tweets downloaded so far
getting tweets before 380317557162405887
...3000 tweets downloaded so far
getting tweets before 369825207340367871
...3199 tweets downloaded so far
getting tweets before 362919600792403968
...3219 tweets downloaded so far
getting tweets before 362041545622437887
...3219 tweets downloaded so far

 Analyzing Twitter user @drewdepriest

 *** Personality Traits *** 
79.91% - Openness
-- 82.30% - Adventurousness
-- 39.45% - Artistic interests
-- 12.26% - Emotionality
-- 81.16% - Imagination
-- 83.64% - Intellect
-- 70.45% - Authority-challenging
70.62% - Conscientiousness
-- 79.40% - Achievement striving
-- 79.49% - Cautiousness
-- 66.38% - Dutifulness
-- 20.33% - Orderliness
-- 67.34% - Self-discipline
-- 71.27% - Self-efficacy
25.40% - Extraversion
-- 80.40% - Activity level
-- 49.30% - Assertiveness
-- 19.97% - Cheerfulness
-- 24.07% - Excitement-seeking
-- 31.42% - Outgoing
-- 34.83% - Gregariousness
27.30% - Agreeableness
-- 51.90% - Altruism
-- 73.90% - Cooperation
-- 47.15% - Modesty
-- 44.58% - Uncompromising
-- 66.54% - Sympathy
-- 64.97% - Trust
19.47% - Emotional range
-- 22.76% - Fiery
-- 15.26% - Prone to worry
-- 27.99% - Melancholy
-- 20.52% - Immoderation
-- 30.72% - Self-consciousness
-- 14.39% - Susceptible to stress

 *** Needs *** 
22.16% - Challenge
21.15% - Closeness
17.76% - Curiosity
16.78% - Excitement
26.82% - Harmony
18.42% - Ideal
17.21% - Liberty
23.78% - Love
23.92% - Practicality
24.96% - Self-expression
19.46% - Stability
24.63% - Structure

 *** Values *** 
74.51% - Conservation
24.44% - Openness to change
25.14% - Hedonism
86.66% - Self-enhancement
15.92% - Self-transcendence
```
