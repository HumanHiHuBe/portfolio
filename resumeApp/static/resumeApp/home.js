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
