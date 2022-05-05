
var mathml_elms = document.getElementsByClassName('mathml_text');
var sol_elms = document.getElementsByClassName('sol');
var print_btn_elm = document.getElementById('makepdf_id')
var btn_elm = document.getElementById('btn')
var show_all_ans_btn_elm = document.getElementById('show_all_ans_id');

for (let i=0; i < mathml_elms.length; i++){
    var mathml_elm = mathml_elms[i]
    mathml_elm.innerHTML = mathml_elm.innerText;

}

function show_all_ans(){

    show_all_ans_btn_elm.innerText = 'Hide All Answers'
    for (let i=0; i<sol_elms.length; i++){
        var sol_elm = sol_elms[i];
        sol_elm.classList.toggle('hidden');
    }
}

function makePDF(){
    print_btn_elm.setAttribute('style', 'display:none');
    show_all_ans_btn_elm.setAttribute('style', 'display:none');
    window.print();
}