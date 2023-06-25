import React from 'react';
import ReactDOM from 'react-dom';

function Clock() {
    var date = new Date();
    return (
        <p> {date.toLocaleTimeString()} </p>
    );
}

ReactDOM.render(
    <Clock />,
    document.getElementById("root")
);