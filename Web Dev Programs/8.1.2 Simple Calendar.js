import React from 'react';
import ReactDOM from 'react-dom';

class Calendar extends React.Component {
    
    render() {
        return (
            <div>
                <h1> January </h1>
                <table>
                    <Heading />
                    <Row />
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
                <td> 1 </td>
                <td> 2 </td>
                <td> 3 </td>
                <td> 4 </td>
                <td> 5 </td>
                <td> 6 </td>
                <td> 7 </td>
            </tr>
        );
    }
}

ReactDOM.render(
    <Calendar />,
    document.getElementById("root")
);
