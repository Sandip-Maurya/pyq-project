
var mathml_elms = document.getElementsByClassName('mathml_text');
var sol_elms = document.getElementsByClassName('sol');
var print_btn_elm = document.getElementById('makepdf_id')
var btn_elm = document.getElementById('btn')
var show_all_ans_btn_elm = document.getElementById('show_all_ans_id');

for (let i = 0; i < mathml_elms.length; i++) {
    var mathml_elm = mathml_elms[i]
    mathml_elm.innerHTML = mathml_elm.innerText;

}

function show_all_ans() {

    show_all_ans_btn_elm.innerText = 'Hide All Answers'
    for (let i = 0; i < sol_elms.length; i++) {
        var sol_elm = sol_elms[i];
        sol_elm.classList.toggle('hidden');
    }
}

function makePDF() {
    print_btn_elm.setAttribute('style', 'display:none');
    show_all_ans_btn_elm.setAttribute('style', 'display:none');
    window.print();
}


// For app2 
const Exam_elm = document.getElementById('Exam');
const Subject_elm = document.getElementById('Subject');
const select_exam_msg = document.getElementById('select_exam_msg').innerText


function create_options(elm, data){
    let opt_node = document.createElement('option');
    let text_node = document.createTextNode(data)
    opt_node.appendChild(text_node);
    elm.appendChild(opt_node)
    return
}




function get_subjects_from_exam() {
    let exam_val = Exam_elm.value;
    let first_opt_val = Subject_elm.options[0];
    Subject_elm.innerHTML = '';
    Subject_elm.appendChild(first_opt_val);

    if (exam_val != 'Select an Exam') {
        fetch('http://127.0.0.1:5000/get_subjects_from_exam?' + new URLSearchParams({ Exam: exam_val })).then
            (promise_data => {
                promise_data.json().then
                    (subjects => {
                        // console.log(subjects);
                        for (let index in subjects){
                            create_options(Subject_elm, subjects[index]);
                        }
                    })
            })
    } 
    else {

        create_options(Subject_elm, select_exam_msg)
    }

}