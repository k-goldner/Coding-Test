const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(express.json());

app.get("/ping", (req, res) => {
  res.send({ Message: "pong" });
});

function convert_data(targetobj, referenceobj) {
  for (const [key, value] of Object.entries(referenceobj)) {
    let str = "{" + key + "}";
    let reg = new RegExp(str, "g");
    targetobj = JSON.parse(JSON.stringify(targetobj).replace(reg, value));
  }
  return targetobj;
}

app.post("/", (req, res) => {
  let payload = req.body.payload;
  let referencedata = req.body.referenceData;
  payload = convert_data(payload, referencedata);
  res.send(payload);
});

app.listen(3000, () => {
  console.log("Server is up on port 3000");
});

module.exports = {
  convert_data: convert_data,
};
