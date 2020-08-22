# chirp-machine
I want a bot to tweet for me because my lazy ass can't remember to do it on a schedule.

### TODO:
- write a ChirpMachine class that can...
1. post a tweet
2. pull content from google sheets

- set up google sheets integration somehow
- post content to google sheets in bulk
- write a cron job to automate the pulling of a tweet

### The Big Plan
1. Spend dedicated time writing out good tweets and putting them into a google sheet
2. Have the cron job run the chirp machine at optimal tweeting times and remove used tweets from the google sheet
3. Maybe dockerize and run on the GPU box?

### Update plan
Google sheets makes it difficult for a headless machine to query things because you'd need a web browser to sign in for OAuth.
I'm sure there's a way around it but I'm not interested in making my life this hard.
Writing will be a sprint-time task where i put all of my effort into it. I can update a table on my GPU box with tweets.

NEW TODO:
- write a script that adds tweets to a table
that way you can write locally, and essentially "push" to the table once you're ready
- write script that pulls from table, posts, updates table, writes to disk
- write cron job to automate that script
- add logic to notify me when tweets are low?
- add logic to run analytics on tweets, send report via email?
