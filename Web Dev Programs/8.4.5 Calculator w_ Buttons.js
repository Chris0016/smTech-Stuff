import React from 'react';
import ReactDOM from 'react-dom';

function isOperator(x) {
    if (x === "+" || x === "-" || x === "*" || x === "/") {
        return true;
    }
    else {
        return false;
    }
}

class Calculator extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            newEntry : true,
            answer: 0,
            current: 0
        };

        this.handleInput = this.handleInput.bind(this)
    }

    handleInput(x) {

        var current = this.state.current;
        var answer = this.state.answer;
        var operator = this.state.operator;

        if (isOperator(x)) {

           this.setState({
                operator : x,
                newEntry : true,
                answer : current
           })

           return
        }

        if (x === "=") {
             
             current = Number(current);
             answer = Number(answer);

             if (operator === "+") {
                 current = answer + current;
             } else if (operator === "-") {
                 current = answer - current;
             } else if (operator === "*") {
                 current = answer * current;
             } else if (operator === "/") {
                 current = answer / current;
             }

            this.setState({
                operator : "",
                newEntry : true,
                answer : current,
                current : current
            });

            return 
        }

        if (this.state.newEntry) {
            this.setState({
                newEntry : false,
            });
            current = "";
        }

        var result = current + x

        this.setState({
            current: result
        })
    }

    render() {
        return (
            <div>
                <h1> {this.state.current} </h1>
                <table>
                    <tr>
                        <Button value="1" callback={this.handleInput}/>
                        <Button value="2" callback={this.handleInput}/>
                        <Button value="3" callback={this.handleInput}/>
                        <Button value="+" callback={this.handleInput}/>
                    </tr>
                    <tr>
                        <Button value="4" callback={this.handleInput}/>
                        <Button value="5" callback={this.handleInput}/>
                        <Button value="6" callback={this.handleInput}/>
                        <Button value="-" callback={this.handleInput}/>
                    </tr>
                    <tr>
                        <Button value="7" callback={this.handleInput}/>
                        <Button value="8" callback={this.handleInput}/>
                        <Button value="9" callback={this.handleInput}/>
                        <Button value="*" callback={this.handleInput}/>
                    </tr>
                    <tr>
                        <Button value="0" callback={this.handleInput}/>
                        <Button value="=" callback={this.handleInput}/>
                        <Button value="." callback={this.handleInput}/>
                        <Button value="/" callback={this.handleInput}/>
                    </tr>
                </table>
            </div>
        );
    }

}

class Button extends React.Component {

    constructor(props) {
        super(props);

        this.value = props.value;
        this.callback = props.callback;
    }

    handleClick(e) {
        e.preventDefault();

        this.callback(this.value);
    }

    render() {
        return (
            <td onClick={(e) => this.handleClick(e) } style={{width : `50px`, height : `50px`, border : `1px solid black`}}> 
            {this.value} </td>
        );
    }
}

function App() {
    return (
        <Calculator />
    );
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
);