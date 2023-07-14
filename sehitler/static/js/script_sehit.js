const text_box_sehit = document.querySelector(".text_box_sehit");
const sehits = document.querySelector(".sehits");
const sehits_children = [...sehits.children];



const txt_changed = () =>{
    console.clear()
    value_temp = text_box_sehit.value.toUpperCase()

    sehits_children.forEach(elements => {
        div_card = [...elements.children]
        if (value_temp != "") {
            span_sehit = div_card[1].getElementsByTagName("span");
            let iT = span_sehit[0].innerText
            if(!iT.includes(value_temp)){
                elements.classList.add("dont-disp")
            }else{
                elements.classList.remove("dont-disp")
            }
        }
        else{
            elements.classList.remove("dont-disp")
        }
        
    });

   

    
    
    
};

text_box_sehit.addEventListener("keyup", txt_changed);
