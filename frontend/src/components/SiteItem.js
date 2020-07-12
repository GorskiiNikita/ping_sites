import React, { Component } from "react";


class SiteItem extends Component {
    constructor(props) {
        super(props);
        this.state = {
            siteId: this.props.siteId,
            formId: 'siteForm' + this.props.siteItem.id
        };
    }

    render() {
        return (
            <li>
                <p>{this.props.siteItem.name}</p>
                <button className="settings-btn" onClick={() => this.handleClickHiddenForm(this.state.formId)}>Параметры</button>
                <button className="delete-btn" onClick={this.props.onDelete}>Удалить</button>
                <form className="settings-form" hidden id={this.state.formId} method="POST"
                      onSubmit={(e) => {this.props.onUpdate(); e.preventDefault();}}>
                    <label>Название: <input type="text" defaultValue={this.props.siteItem.name} name="name" size="35"/></label>
                    <br />
                    <label>Адрес сайта: <input type="url" defaultValue={this.props.siteItem.site} name="site" size="35" /></label>
                    <br />
                    <label>Уведомления: <input type="checkbox" defaultChecked={this.props.siteItem.notification} name="notification"/></label>
                    <button>Сохранить</button>
                </form>
            </li>
        );
    }

    handleClickHiddenForm(formId) {
        let form = document.getElementById(formId);
        form.hidden = !form.hidden;
    }
}


export default SiteItem;