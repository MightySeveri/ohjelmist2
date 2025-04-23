const items = ["First item", "second item", "third item"];
const target   = document.getElementById("target");

items.forEach((text, index) =>{
  const li = document.createElement("li");
  li.textcontent = text;
  if (index === 1) {
    li.classList.add("my item");
  }
  target.appendchild(li);
})
target.classlist.add("my list");