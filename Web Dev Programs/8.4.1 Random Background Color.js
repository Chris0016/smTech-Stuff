import React from 'react';
import ReactDOM from 'react-dom';

function randint(range) {
    return Math.floor(Math.random() * range)
}

class BackgroundRandomButton extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            red : 255,
            green : 255, 
            blue : 255
        }
    }

    randomize() {
        this.setState({
            red : randint(255),
            green : randint(255),
            blue : randint(255)
        });
    }

    render() {
        return(
            <div style={{
                backgroundColor : `rgb(` + this.state.red + `,` + this.state.green + `,` + this.state.blue + `)`,
                width : '500px',
                height : '500px'
                }}>
                <button onClick={ () => this.randomize() }> 
                    Random!
                </button>
            </div>
        );
    }
}

function App() {
    return (
        <BackgroundRandomButton />
    );
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
);