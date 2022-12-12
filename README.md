# Thesis

## Installation

To install and test the project, you need to follow these steps:

### Create skill interface

Using Amazon account log into the [Developer Console](https://developer.amazon.com/alexa/console/ask) and create new
skill. Then in the `Build` tab click on the `Intents` button and select `JSON Editor`. Then paste the content of the 
`skill-interface.json` file to the editor. 

From the `Build.Endpoint` tab, copy the `skill id`. It is needed to complete the installation.

### Deploy skill service

Fill in the ./thesis/.env file according to the template (./thesis/.env.template) using the `skill id` from earlier.

Deploy the Lambda function found in ./thesis directory:

Run the following command:

```
$ serverless deploy --verbose
```

Then run:

```
$ serverless info
```

to gather info about deployed function's `endpoint`.

### Connect service to the interface

Go to the `Build.Endpoint` tab and put the `endpoint` address in the proper field. Build the skill.