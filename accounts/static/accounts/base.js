// tell the embed parent frame the height of the content
if (window.parent && window.parent.parent){
  window.parent.parent.postMessage(["resultsFrame", {
    height: document.body.getBoundingClientRect().height,
    slug: "1nu8g6e5"
  }], "*")
}

// always overwrite window.name, in case users try to set it manually
window.name = "result"