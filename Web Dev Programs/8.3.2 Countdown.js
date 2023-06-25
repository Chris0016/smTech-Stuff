import React from 'react';
import ReactDOM from 'react-dom';

/* Define some constants for the subsequent operations */
var dayInMilli = 86400000
var hourInMilli = 3600000
var minuteInMilli = 60000
var secondInMilli = 1000

class Countdown extends React.Component {

    constructor(props) {
        super(props);

        var date = new Date();
        var target = new Date(date.getFullYear() + 1, 0, 1);

        this.state = {
            date : date,
            target : target,
            days : 0,
            hours : 0,
            minutes : 0, 
            seconds : 0
        }
    }

    componentDidMount() {

        this.update();

        this.id = setInterval( () => this.update(), 1000);
    }

    componentDidUnmount() {
        clearInterval(this.id);
    }

    update() {
        var date = new Date();
        var dt = this.state.target.getTime() - date.getTime();

        this.setState({
            date : date,
            days : Math.floor(dt / dayInMilli),
            hours : Math.floor((dt % dayInMilli) / hourInMilli),
            minutes : Math.floor((dt % hourInMilli) / minuteInMilli),
            seconds : Math.floor((dt % minuteInMilli) / secondInMilli)
        });
    }

    render() {
        return (
            <div>
                <h1>{this.state.date.toString()} </h1>
                <h1>{this.state.target.toString()} </h1>
                <h1> {this.state.days} days : {this.state.hours} hours :&nbsp;
                {this.state.minutes} minutes : {this.state.seconds} seconds </h1>
            </div>    
        );
    }

}

function App() {
    return (
        <Countdown />
    );
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
);