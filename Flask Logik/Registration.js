let String password;
let String name;


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

    let email = localStorage.getItem('email')
    let vorname = localStorage.getItem('vorname')
    let nachname = localStorage.getItem('nachname')
    let plz = localStorage.getItem('plz')
    let geburtsdatum = localStorage.getItem('geburtsdatum')

}


/*function compare_pw() {
    access_Data()
    if (access_Data()["passwort"] == access_Data()["pw_repeat"]) {
        var x = "gut"
        document.getElementById("demo").innerHTML = x
    }
}*/