import React, { Component } from "react";


class AddSiteForm extends Component {
    render() {
        return (
            <form className="adding-form" id="adding-form" method="POST"
                  onSubmit={(e) => {this.props.onAdd(); e.preventDefault();}}>
                <label>Название: <input type="text" name="name"/></label>
                <br />
                <label>Адрес сайта: <input type="text" name="site" /></label>
                <br />
                <label>Уведомления: <input type="checkbox" name="notification"/></label>
                <button>Добавить</button>
            </form>
        )
    }
}


export default AddSiteForm;