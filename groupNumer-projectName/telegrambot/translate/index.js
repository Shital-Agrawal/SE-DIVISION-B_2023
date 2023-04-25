const express = require("express");

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get("/", function (req, res) {
  const query = req.query;
  console.log(query);
  res.send(query);
});

app.listen(8080, () => {
  console.log("sever started on port 8080");
});
