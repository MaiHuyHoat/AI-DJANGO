
document.addEventListener('DOMContentLoaded',()=>{
    document.getElementById("btnGen").onclick=()=>{
        
        getAnswerApi()
    }
})
const componetLoadingButton=`<img src="/static/assets/img/gif/Spin_white_bg-blue.gif" style="width: 25px ;height:25px"/>`;
async function getAnswerApi(){
    var textModel1= document.getElementById('model-1').value;
    var textModel2= document.getElementById('model-2').value ;
    var strCode1= document.getElementById('code-1').value;
    if(!strCode1 || !textModel1 || !textModel2){

        window.confirm("Bạn phải nhập code vào các ô : \n + Model 1 và 2 (Code miêu tả model) \n + Code mẫu (Code tiền xử lý cho model 1) .");
        return;
    }
    document.querySelector("#btnGen").innerHTML=componetLoadingButton;
    document.getElementById("code-2").innerHTML="";
     document.querySelector("#btnGen").click=()=>{};
  
   
    var content = ["I have code to illustrate and describe model 1 as follows:\n", textModel1, "\nFor model 1, I have the following processing code:\n", strCode1, 
    "\nNow I need you to generate similar processing code but applied to model 2, illustrated as follows:\n", textModel2, "Requirement: You only need to return the code, no further explanation is needed."].join(" ");

    fetch(urlGenCode,{
        method:'post',
        headers: {
            'content-type':'application/json'
        },
        body:JSON.stringify(
            {
                "model":"gpt-3.5-turbo-16k",
                "questions": content,
             
            }
        )
    }).then(res=>res.json())
     .then(data=>{
        document.querySelector("#btnGen").innerHTML="GenCode";
       
        document.getElementById("code-2").innerHTML=data.response;
      
     })

}