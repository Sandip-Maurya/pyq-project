function add_script_for_mathml(){
    let src = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"
    let scriptElm = document.createElement('script');
    scriptElm.src = src;
    document.body.appendChild(scriptElm);
}
async function get_data(){
    let response = await fetch('http://localhost:7000/get_paper_data_view', {method: 'POST'});
    let response_json = await response.json();
    let mathml_test_text = await response_json;
    return  mathml_test_text['MATH']['SCQ']
}   

async function test(){
    let test_data = await get_data();
    console.table(test_data)
    console.log('Test')
    // add_script_for_mathml();

}
