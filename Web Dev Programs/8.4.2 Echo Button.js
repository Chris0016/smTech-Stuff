import React from 'react';
import ReactDOM from 'react-dom';

/* 
    Introduce this in a number of steps in order to explore all the behaviors of React.

    1. First review html forms
    2. Talk about how forms are handled in React - Managed State
    3. Start w/ an empty handleChange and handleSubmit
    4. Fill in handleChange
    5. Fill in console.log in handleSubmit
    6. Finish handleSubmit
*/

class Echo extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            value : ""
        }
    }

    handleSubmit(event) {
        console.log(this.state.value)
        event.preventDefault(); /* use this to stop the form from clearing */
        this.setState({
            value : ""
        });
    }

    handleChange(event) {
        this.setState({
            value : event.target.value
        });
    }

    render() {
        return(
            <form onSubmit={(e)=>this.handleSubmit(e)}>
                <label>
                    Enter some text. &nbsp;
                    <input type="text" value={this.state.value} onChange={(e)=>this.handleChange(e)}/>
                </label>
                <input type="submit" value="Submit"/>
            </form>
        );
    }
}

function App() {
    return (
        <Echo />
    );
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
);