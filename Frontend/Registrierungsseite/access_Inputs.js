function access_Data() {
    var email = document.getElementById("email").value;
    var passwort = document.getElementById("passwort").value;
    var passwort_repeat = document.getElementById("pw_repeat").value;
    var data = {
        "email": email,
        "passwort": passwort,
        "pw_repeat": passwort_repeat
    }
    console.log(data)
    return data
}

/*function compare_pw() {
    access_Data()
    if (access_Data()["passwort"] == access_Data()["pw_repeat"]) {
        var x = "Passwörter stimmen überein"
        document.getElementById("demo").innerHTML = x
    }
}*/