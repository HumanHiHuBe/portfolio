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

// function f3(bid) {
//     ele = document.getElementsByTagName('section')
//     let sValue = document.getElementById('i1').value
//     console.log(sValue)
//     let dict1 = new Map()
//     for(i=0; i<ele.length; i++){
//         dict1.set(ele[i], ele[i].textContent)
//     }
//     for(let [key,value] of dict1){
//         let newBol = "/"+sValue+"/"+"i"
//         console.log(newBol)
//         console.log(key.innerText)
//         let nstr = key.textContent
//         console.log(nstr)
//         let res = nstr.search(RegExp(newBol, "i"))
//         console.log(res)
//         if(res == -1){
//             console.log("Didn't find")
//         }else{
//             console.log(sValue)
//             key.scrollIntoView({ behavior: "smooth", block: "end", inline: "nearest" })
//             console.log(key)
//             console.log(value)
//             break
//         }
        

        // if(key.innerText.search(newBol)){
        //     key.scrollIntoView({ behavior: "smooth", block: "end", inline: "nearest" })
        // }
        



//     }

// }

function f3(bid) {
    let sValue = document.getElementById('i1').value.toLowerCase(); // Convert the search string to lowercase for case-insensitive search
    let sections = document.getElementsByTagName('section');
    
    for (let i = 0; i < sections.length; i++) {
        let sectionText = sections[i].textContent.toLowerCase(); // Convert section text to lowercase
        if (sectionText.includes(sValue)) {
            sections[i].scrollIntoView({ behavior: "smooth", block: "end", inline: "nearest" });
            break; // Stop searching after finding the first match
        }
    }
}

