import React from 'react';
import ReactDOM from 'react-dom';

var months = {
    0 : "January",
    1 : "February",
    2 : "March",
    3 : "April",
    4 : "May",
    5 : "June",
    6 : "July",
    7 : "August",
    8 : "September",
    9 : "October",
    10 : "November",
    11 : "December"
};

class Calendar extends React.Component {
    
    constructor (props) {
        super(props);

        var date = new Date();
        var firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
        var lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
        
        this.state = {
            date : date,
            year : date.getFullYear(),
            month : date.getMonth(),
            startOfMonth : (firstDay.getDay() + 6) % 7,
            days : lastDay.getDate()
        }
    }

    nextMonth() {
        var firstDay = new Date(this.state.date.getFullYear(), this.state.date.getMonth() + 1, 1);
        var lastDay = new Date(this.state.date.getFullYear(), this.state.date.getMonth() + 2, 0);
        this.setState({
            date : firstDay,
            year : firstDay.getFullYear(),
            month : firstDay.getMonth(),
            startOfMonth : (firstDay.getDay() + 6) % 7,
            days : lastDay.getDate()
        })
    }

    prevMonth() {
        var firstDay = new Date(this.state.date.getFullYear(), this.state.date.getMonth() - 1, 1);
        var lastDay = new Date(this.state.date.getFullYear(), this.state.date.getMonth(), 0);
        this.setState({
            date : firstDay,
            year : firstDay.getFullYear(),
            month : firstDay.getMonth(),
            startOfMonth : (firstDay.getDay() + 6) % 7,
            days : lastDay.getDate()
        })
    }

    getRowValues(row) {
        var currRow = -1;
        var days = 1;
        var values = [];
        for (var i = 0; i < 35; i++) {

            if (i % 7 === 0) {
                currRow = currRow + 1;
            }

            if (i < this.state.startOfMonth || days > this.state.days) {
                if (currRow === row) values.push(null);
            }
            else if (currRow === row) {
                values.push(days);
                days = days + 1;
            }
            else {
                days = days + 1;
            }
        }
        return values;
    }

    render() {
        return (
            <div>
                <h1> {months[this.state.month]} </h1>
                <table>
                    <Heading />
                    <Row values={this.getRowValues(0)} />
                    <Row values={this.getRowValues(1)} />
                    <Row values={this.getRowValues(2)} />
                    <Row values={this.getRowValues(3)} />
                    <Row values={this.getRowValues(4)} />
                    <Row values={this.getRowValues(5)} />

                    <button onClick={ () => this.nextMonth() }> 
                        Next
                    </button>
                    <button onClick={() => this.prevMonth()}> 
                        Previous 
                    </button>
                </table>
            </div>
        );
    }

}

class Heading extends React.Component {
    
    render() {
        return (
            <tr> 
                <th> Monday </th>
                <th> Tuesday </th>
                <th> Wednesday </th>
                <th> Thursday </th>
                <th> Friday </th> 
                <th> Saturday </th>
                <th> Sunday </th>
            </tr>
        );
    }
}

class Row extends React.Component {
    
    render() {
        return (
            <tr>
                <td>{this.props.values[0]}</td>
                <td>{this.props.values[1]}</td>
                <td>{this.props.values[2]}</td>
                <td>{this.props.values[3]}</td>
                <td>{this.props.values[4]}</td>
                <td>{this.props.values[5]}</td>
                <td>{this.props.values[6]}</td>
            </tr>
        );
    }
}

function App() {
    return (
        <Calendar />
    );
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
);
