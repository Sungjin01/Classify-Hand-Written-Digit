let drawing = false;

window.onload = function() {
    //let spawn = require('child_process').spawn;

    document.getElementById('resetButton').addEventListener('click', onResetButtonClick);
    document.getElementById('addDigitCanvasButton1').addEventListener('click', onAddDigitCanvasButtonClick);
    
    var x, y; document.onmousemove=(e)=>{x=e.pageX;y=e.pageY;console.log(x, y);}
    
}

function onResetButtonClick(){

}


function onAddDigitCanvasButtonClick(e){
    const digitCanvasDiv = document.createElement('div');
    digitCanvasDiv.className = 'digitCanvasDiv';
    const digitCanvas = document.createElement('canvas');
    digitCanvas.id = 'digitCanvas' + e.target.parentNode.childElementCount;
    digitCanvas.className = 'digitCanvas';
    digitCanvas.style.width = '15vmin';
    digitCanvas.style.height = '15vmin';
    const ctx = digitCanvas.getContext("2d");
    ctx.lineWidth = 8;
    ctx.lineCap = "round";
    ctx.strokeStyle = 'black';
    const draw = e => {
        const x = e.offsetX;
        const y = e.offsetY;
        console.log(x + ' ' + y + ' find');
        if (!drawing) return;
        ctx.beginPath();
        ctx.moveTo(2*x, y);
        ctx.lineTo(2*x, y);
        ctx.stroke();
    };
    digitCanvas.addEventListener('mouseup', onDrawn);
    digitCanvas.addEventListener('touchend', onDrawn);
    digitCanvas.addEventListener("mousedown", () => (drawing = true));
    digitCanvas.addEventListener("mouseup", () => (drawing = false));
    digitCanvas.addEventListener("mousemove", draw);
    const clearButton = document.createElement('button');
    clearButton.className = 'clearCanvasButton';
    clearButton.addEventListener('onclick', onClearCanvasButtonClick);

    digitCanvasDiv.appendChild(digitCanvas);
    digitCanvasDiv.appendChild(clearButton);

    e.target.parentNode.insertBefore(digitCanvasDiv, e.target);
}

function onDrawn(e){

    calculateResult();
}

function onClearCanvasButtonClick(e){
    let cnvs = e.target.parentNode.firstChild;
    let ctx = cnvs.getContext('2d');

    ctx.clearRect(0, 0, cnvs.width, cnvs.height);
    ctx.beginPath();
}

function calculateResult(){

}
