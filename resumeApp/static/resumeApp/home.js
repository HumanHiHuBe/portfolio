document.getElementById('nav-form').addEventListener('submit', function(e) {
    e.preventDefault();
});

function f1(inid) {
    ele = document.getElementById(inid)
    console.log(ele.value)
    //working
}
function f2(spid) {
    ele = document.getElementById(spid)
    ele.click(function f() {
        window.top.close();   
    })
    //working
}

function f3(bid) {
    ele = document.getElementsByTagName('section')
    sValue = document.getElementById('i1').value
    console.log(sValue)
    let dict1 = new Map()
    for(i=0; i<ele.length; i++){
        dict1.set(ele[i], ele[i].textContent)
    }
    for(let [key,value] of dict1){
        if(value.search(/sValue/i)){
            console.log(sValue)
        };
    }

}
