
let changeStructure = document.getElementById("change")

function newDiv(){
    const div = document.getElementById("user")
    div.innerHTML = `
    <div>
        <h3>What change have we made?</h3>
        <p>You can see this because the structure of the previous div has been altered</p>
        <p>If you click the button below you will be able to go back to the previous out look</p>
        <button id="changeback">Change back</button>
    </div>
    `
}

changeStructure.addEventListener("click", newDiv)

let changeText = document.getElementById("changeback")

function newText(){
    const paragraph = document.getElementById("text")
    paragraph.innerText = "If you can see this text then the button below has been clicked"
}

changeText.addEventListener("click", newText)
