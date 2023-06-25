import React from 'react';
import ReactDOM from 'react-dom';

class Clock extends React.Component {
    
    constructor(props) {
        super(props)

        this.state = {date: new Date()}
    }

    componentDidMount() {
        this.id = setInterval( () => this.update(), 1000);

    }

    componentDidUnmount() {
        clearInterval(this.id);
    }

    update() {
        this.setState({date: new Date()});
    }

    render() {
        return (
            <p> {this.state.date.toLocaleTimeString()} </p>
        );
    }

}

function App() {
    return (
        <Clock />
    );
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
);
