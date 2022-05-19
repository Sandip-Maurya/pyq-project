// For app2 
const Exam_elm = document.getElementById('Exam');
const Year_elm = document.getElementById('Year')
const Paper_elm = document.getElementById('Paper');
const Subject_elm = document.getElementById('Subject');
const practice_elm = document.getElementById('practice');
const view_elm = document.getElementById('view');
const filter_form_elm = document.getElementById('filter_form')

const Exam_default_val = Exam_elm.options[0].value;
const Year_default_val = Year_elm.options[0].value;
const Paper_default_val = Paper_elm.options[0].value;
const Subject_default_val = Subject_elm.options[0].value;


function create_options(elm, data) {
    let opt_node = document.createElement('option');
    opt_node.setAttribute('value', data)
    let text_node = document.createTextNode(data)
    opt_node.appendChild(text_node);
    elm.appendChild(opt_node)
    return
}

function reset_options(elm){
    let first_opt_val = elm.options[0];
    elm.innerHTML = '';
    elm.appendChild(first_opt_val);
    return
}

function create_exams(){

    reset_options(Exam_elm);
    
    async function get_eams(){
        let response = await fetch(`${window.location.href}/get_exams`);
        let Exam_response_json = await response.json();
        let Exams = Object.values(Exam_response_json);
        // Exams.forEach(Exam => {create_options(Exam_elm, Exam)});
        for(let Exam of Exams){create_options(Exam_elm, Exam)};
        
        return 
    }
    get_eams()
}


function filter_function_Exam(){
    reset_options(Year_elm);
    reset_options(Paper_elm);
    reset_options(Subject_elm);
    let exam_val = Exam_elm.value;

    if (exam_val != Exam_default_val){
        async function add_dd_values_in_year(){
            let response = await fetch(`${window.location.href}/get_years_from_exam?` + new URLSearchParams({
                Exam: exam_val
            }))
            let Year_response_json = await response.json()
            let Year_datas = Object.values(Year_response_json)
            Year_datas.forEach(Year_data => {create_options(Year_elm, Year_data)})
            return 

        }
        add_dd_values_in_year()
    } 
}

function filter_function_Year(){
    reset_options(Paper_elm);
    reset_options(Subject_elm);
    let exam_val = Exam_elm.value;
    let year_val = Year_elm.value;

    if (year_val != Year_default_val){
        async function add_dd_values_in_paper(){
            let response = await fetch(`${window.location.href}/get_papers_from_exam_and_year?` + new URLSearchParams({
                Exam: exam_val,
                Year: year_val
            }));
            let Paper_response_json = await response.json();
            let Paper_datas = Object.values(Paper_response_json);
            Paper_datas.forEach(Paper_data => create_options(Paper_elm, Paper_data));
            return
        }
        add_dd_values_in_paper()
    }

}



function filter_function_Paper(){
    reset_options(Subject_elm);

    let exam_val = Exam_elm.value;
    let year_val = Year_elm.value;
    let paper_val = Paper_elm.value;

    if (paper_val != Paper_default_val){
        async function add_dd_values_in_subject(){
            let response = await fetch(`${window.location.href}/get_subjects_from_exam_and_year?` + new URLSearchParams({
                Exam: exam_val,
                Year: year_val
            }));
            let subject_response_json = await response.json();
            let subject_datas = Object.values(subject_response_json);
            // console.log(subject_datas)
            subject_datas.forEach(subject_data => {create_options(Subject_elm, subject_data)});
            return
        }
        add_dd_values_in_subject();
    } 
}


// function filter_form__submit(){
//     practice_elm.onclick = function () { filter_form_elm.setAttribute('action', window.location.href+'/practice' ) };
//     view_elm.onclick = function () { filter_form_elm.setAttribute('action', window.location.href+'/view' ) };
// }

function practice() {
    filter_form_elm.setAttribute('action', 'http://localhost:7000/practice')
}
function view() {
    filter_form_elm.setAttribute('action', 'http://localhost:7000/view_all')
}