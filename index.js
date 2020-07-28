const {
  spawn
} = require("child_process");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.set("view engine", "ejs")

app.use(bodyParser.urlencoded({
  extended: true
}));

app.get("/", function(req, res) {
  res.sendFile(__dirname + "/index.html");
});

app.post("/", function(req, res) {
  var spamMessage = req.body.spamTextBox.replace(/\n/g, '')

  const process = spawn("python3", ["./spamPrediction.py", spamMessage]);

  process.stdout.on("data", data => {
    res.render("result", {
      spamResults: data.toString(),
      spamMessage: spamMessage
    })
  })
});

app.post("/result", function(req, res) {
  var result = req.body.result.toString();

  if (result !==""){
    const process = spawn("python3", ["./inputToFile.py", result]);

    process.stdout.on("data", data => {
      data.toString()
    })
  }




  res.redirect("/");

})



app.listen(5000, function() {
  console.log("server started");
});
