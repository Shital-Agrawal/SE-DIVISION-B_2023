function main() {
  const intputfield = document.getElementById("file");
  intputfield.onchange = () => {
    const selectedFile = intputfield.files[0];

    const inputDiv = document.getElementsByClassName("input_field")[0];
    const loadingDiv = document.getElementsByClassName("contain_loding")[0];
    const resultDiv = document.getElementsByClassName("result_div")[0];
    const downloadlink = document.getElementById("download");

    inputDiv.style.display = "none";
    loadingDiv.style.display = "block";

    const formdata = new FormData();
    formdata.append("Doc", selectedFile, selectedFile["name"]);

    let requestOptions = {
      method: "POST",
      body: formdata,
      redirect: "follow",
    };

    fetch("http:localhost:8080/compress", requestOptions)
      .then((response) => response.json())
      .then((result) => {
        console.log(result["time"]);
        setInterval(() => {
          loadingDiv.style.display = "none";
          resultDiv.style.display = "block";
        }, 2000);
        const id = result["time"];
        const url = "http:localhost:8080/download/" + id;
        downloadlink.href = url;
      })
      .catch((error) => console.log("error", error));
  };
}

document.addEventListener("DOMContentLoaded", async () => {
  main();
});
