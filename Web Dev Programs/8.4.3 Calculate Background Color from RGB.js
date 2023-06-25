import React from 'react';
import ReactDOM from 'react-dom';

class BackgroundButton extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            newR : 255,
            newG : 255,
            newB : 255,
            currentR : 255, 
            currentG : 255,
            currentB : 255
        }
    }

    handleSubmit(event) {
        
        var tempR = this.state.newR;
        var tempG = this.state.newG;
        var tempB = this.state.newB;

        event.preventDefault(); /* use this to stop the form from clearing */
        this.setState({
            newR : 0,
            newG : 0,
            newB : 0,
            currentR : tempR, 
            currentG : tempG,
            currentB : tempB
        });
    }

    handleRvalueChange(event) {
        this.setState({
            newR : event.target.value
        });
    }

    handleGvalueChange(event) {
        this.setState({
            newG : event.target.value
        });
    }

    handleBvalueChange(event) {
        this.setState({
            newB : event.target.value
        });
    }

    render() {
        return(
            <div style={{backgroundColor : `rgb(` + this.state.currentR + `,` + this.state.currentG + `,` + this.state.currentB + `)`}}>
                <form onSubmit={(e)=>this.handleSubmit(e)}>
                    <label>
                        Enter 3 RGB Values. &nbsp;
                    </label>
                    <input type="text" value={this.state.newR} onChange={(e)=>this.handleRvalueChange(e)}/>
                    <input type="text" value={this.state.newG} onChange={(e)=>this.handleGvalueChange(e)}/>
                    <input type="text" value={this.state.newB} onChange={(e)=>this.handleBvalueChange(e)}/>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        );
    }
}

function App() {
    return (
        <BackgroundButton />
    );
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
);