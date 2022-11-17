


function access_Password() {
    localStorage.setItem('email', document.getElementById("email").value);
    localStorage.setItem('password', document.getElementById("password").value);
    localStorage.setItem('passwordRep', document.getElementById("passwordRep").value);
}

function access_Name() {
    localStorage.setItem('vorname', document.getElementById("vorname").value);
    localStorage.setItem('nachname', document.getElementById("nachname").value);
}

function access_PLZ() {
    localStorage.setItem('plz', document.getElementById("plz").value);
}

function access_Geburtsdatum() {
    localStorage.setItem('geburtsdatum', document.getElementById("geburtsdatum").value);
}

function writeStorage(key){
    document.write(localStorage.getItem('key'))
}

function sendData(){

    email = localStorage.getItem('email')
    vorname = localStorage.getItem('vorname')
    nachname = localStorage.getItem('nachname')
    plz = localStorage.getItem('plz')
    geburtsdatum = localStorage.getItem('geburtsdatum')
    const data = { username: 'example' };

    fetch('https://pate.pythonanywhere.com/server', {
    method: 'POST', // or 'PUT'
    headers: {
    'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((data) => {
    console.log('Success:', data);
    })
    .catch((error) => {
    console.error('Error:', error);
});





/*function compare_pw() {
    access_Data()
    if (access_Data()["passwort"] == access_Data()["pw_repeat"]) {
        var x = "gut"
        document.getElementById("demo").innerHTML = x
    }
}*/