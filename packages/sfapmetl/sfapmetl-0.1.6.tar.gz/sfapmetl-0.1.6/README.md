#### Python sfapmetl feature
#### Installation

    $ pip install sfapmetl

#### Usage

    $ sf-apm-etl <config file path>

* Please provide config as mentioned below:

```
key: <profilekey>
tags:
  Name: <name>
  appName: <appName>
  projectName: <projectName>
jobUrl: <job_url> #component url of job table
stageUrl: <stage_url> #component url of stage table
taskUrl: <task_url> #component url of task table
authKey: <authentication_key_for_the_urls>
```
* After this setup, add cronjob into /etc/crontab( Applicable for Linux AWS instance, else run this script as a cron job)
        ex: To run script every 5 minutes
         -  */5 * * * * root sf-apm-etl <config file path>

 * please refer this link for cronjob
        https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804

