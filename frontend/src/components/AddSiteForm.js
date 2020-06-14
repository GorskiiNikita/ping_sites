import React, { Component } from "react";


class AddSiteForm extends Component {
    render() {
        return (
            <form className="adding-form" id="adding-form" method="POST"
                  onSubmit={(e) => {
                      this.props.onAdd();
                      this.clearAddingForm()
                      e.preventDefault();
                  }}>
                <label>Название: <input type="text" name="name" size="25" required id="add-site-name"/></label>
                <br />
                <label>Адрес сайта: <input type="text" name="site" size="25" required id="add-site-url"/></label>
                <br />
                <label>Уведомления: <input type="checkbox" name="notification" id="add-site-notification"/></label>
                <button>Добавить</button>
            </form>
        )
    }

    clearAddingForm() {
        document.getElementById('add-site-name').value = '';
        document.getElementById('add-site-url').value = '';
        document.getElementById('add-site-notification').checked = true;
    }
}


export default AddSiteForm;