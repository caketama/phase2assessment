function triangle() {
  const output = document.getElementById("output");
  const number = document.getElementById("number").value;
  for (let i = number; i >= 1; i--) {
    let result = "";
    for (let j = i; j >= 1; j--) {
      result += "*";
    }
    output.insertAdjacentHTML("afterend", result + "<br>");
    //    console.log(number);
  }
}
triangle();
