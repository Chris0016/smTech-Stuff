import React from 'react';
import ReactDOM from 'react-dom';

class Greeting extends React.Component {
    
    render() {
        return (
            <h1> Hello {this.props.firstName} {this.props.lastName} </h1>
        )
    }
}

function App() {
    return (
        <div>
            <Greeting firstName="Jane" lastName="Smith"/>
            <Greeting firstName="Simon" lastName="Shoe"/>
        </div>
    );
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
);
