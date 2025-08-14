function validation(e){
    e.preventDefault();

    const email=document.getElementById('email').Value;
    const pass=document.getElementById('password').Value;
    const age=document.getElementById('age').Value;
    const msgBox=document.getElementById('message');

    let message='';

    if (email === ''){
        message='please enter an email.';
        msgBox.style.color='red';
    } else if(pass=== ''){
        message='password must be atleast 8 characters.';
        msgBox.style.color='red';
    } else if(age=== ''){
        message='age must be between 12 and 50.';
        msgBox.style.color='red';
    }

     else{
        message='login successfull';
        msgBox.style.color='green';
    }

    msgBox.innerHTML=message;
}