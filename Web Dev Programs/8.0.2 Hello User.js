import React from 'react';
import ReactDOM from 'react-dom';

var user = {
    firstname: "Joe",
    lastname: "Smith"
}

ReactDOM.render(
    <h1> Hello {user.lastname}, {user.firstname} </h1>, 
    document.getElementById("root")
);