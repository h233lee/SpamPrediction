# SPAM Prediction

This is a simple app created with HTML, NodeJS and Python that utilizes the **Multinomial Naive Bayes** methodology to predict Spam.

It is recommended to use short messages such as SMS texts or e-mail titles to test this app out as it already takes around *10-25* seconds.

It is also important to note that there is a feedback option which appends your results into the list of examples *(SMSSpamCollection)* and helps the model to predict more accurately.

## Challenges:
I wanted to host this using EC2, but I was on a budget and the free-tier AWS provided kept maxing out on CPU memory. I decided that it is best to let users pull this repo and try it out themselves.


### Make sure to install the necessary packages:

```shell
$ pip3 install pandas

$ pip3 install regex

$ npm install

```

To run the app, use the following command

```shell
$ node index.js
```

then enter **[http://localhost:3000/](http://localhost:3000/)**
