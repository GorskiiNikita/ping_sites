import {render} from "react-dom";
import React, {Component} from "react";
import ListSites from "./ListSites";


class App extends Component {
    render() {
        return (
            <ListSites />
        );
    }
}



const container = document.getElementById("app");
render(<App />, container);